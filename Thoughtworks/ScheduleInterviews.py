from typing import List,Tuple
import datetime

def divideWorkingHours(start_time:datetime.datetime,
                       end_time:datetime.datetime,
                       interval:datetime.timedelta) -> List[Tuple]:
    periods = []
    period_start = start_time
    while period_start < end_time:
        period_end = min(period_start + interval, end_time)
        if (period_end - period_start == interval):
            periods.append((period_start, period_end))
        period_start = period_end
    return periods


def removeOverlaps(slots:List[Tuple],break_hour:Tuple) -> List[Tuple]:
    refined_slots = []
    for slot in slots:
        latest_start = max(slot[0], break_hour[0])
        earliest_end = min(slot[1], break_hour[1])
        delta = (earliest_end - latest_start).days
        if (delta < 0) or (earliest_end == latest_start):
            refined_slots.append(slot)
    return refined_slots


def scheduleInterviews(attendees:dict,
                       interviewers:dict,
                       rooms:dict,
                       slots:List[Tuple]) -> List[Tuple]:
    available_attendees = attendees.get("entity").copy()
    available_interviewers = interviewers.get("entity").copy()
    available_rooms = rooms.get("entity").copy()
    available_slots = slots[::-1].copy()
    attendees_done_with_interview = set()
    interviews_scheduled = list()
    while len(available_slots) > 0:
        while ((len(available_interviewers) > 0) & (len(available_rooms) > 0) & 
               (len(available_attendees) > 0)):
             attendee = available_attendees[-1]
             interviewer = available_interviewers[-1]
             room = available_rooms[-1]
             slot = available_slots[-1]
             interviews_scheduled.append((slot,attendee,interviewer,room))
             attendees_done_with_interview.add(attendee)
             print (interviews_scheduled)
             available_attendees.pop()
             available_rooms.pop()
             available_interviewers.pop()
        available_slots.pop()
        available_interviewers = interviewers.get("entity").copy()
        available_rooms = rooms.get("entity").copy()
        available_attendees = list(set(attendees.get("entity").copy()) - attendees_done_with_interview)
    return interviews_scheduled


if __name__ == '__main__':
    #Attendees
    n_attendees = int(input())
    attendees = list(map(int, input().strip().split(",")))
    assert len(attendees) == n_attendees, "length of attendees list does not match with declared total"
    #Interviewers
    n_interviewers = int(input())
    interviewers = list(map(str, input().strip().split(",")))
    assert len(interviewers) == n_interviewers, "length of interviewers list does not match with declared total"
    #Rooms
    n_rooms = int(input())
    rooms = list(map(str, input().strip().split(",")))
    assert len(rooms) == n_rooms, "length of rooms list does not match with declared total"

    attendees_dict = {"entity":attendees,"count":n_attendees}
    interviewers_dict = {"entity":interviewers,"count":n_interviewers}
    rooms_dict = {"entity":rooms,"count":n_rooms}
    #Give all Inputs required
    year = 2024
    month = 1
    day = 22
    break_hour_start = 14
    break_hour_end = 15
    work_hours_start = 9
    work_hours_end = 18
    slot_duration_in_min = 120
    break_hour = (datetime.datetime(year,month,day,break_hour_start,0,0),
                  datetime.datetime(year,month,day,break_hour_end,0,0))
    start_time = datetime.datetime(year,month,day,work_hours_start,0,0)
    end_time = datetime.datetime(year,month,day,work_hours_end,0,0)
    interval = datetime.timedelta(minutes=slot_duration_in_min)
    #Run the Algorithm
    slots = divideWorkingHours(start_time,end_time,interval)
    refined_slots = removeOverlaps(slots=slots,break_hour=break_hour)
    result = scheduleInterviews(attendees=attendees_dict,
                                interviewers=interviewers_dict,
                                rooms=rooms_dict,
                                slots=refined_slots)
    print (result)