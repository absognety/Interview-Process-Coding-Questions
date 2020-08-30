"""
Given a dictionary of elements:
    mydict = {'one':1,
              'two':2,
              'three':3,
              'four':4,
              'five':5}
    print the sequence of elements in the following fashion:
        {'n':1,'w':2,'r':3,'ou':4,'iv':5}
        
"""

mydict = {'one':1,
              'two':2,
              'three':3,
              'four':4,
              'five':5}

def doop(mydict):
    if len(mydict) == 0:
        return "no data"
    for k,v in mydict.items():
        res = {}
        leng = len(k)
        if leng%2 != 0:
            res.update({k[(leng-1)//2]:v})
        else:
            key = ''.join([k[(leng-1)//2],k[(leng+1)//2]])
            res.update({key:v})
    return res

print (doop(mydict))