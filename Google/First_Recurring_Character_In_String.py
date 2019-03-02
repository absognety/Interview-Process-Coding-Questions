from collections import Counter
input_string = input()

def firstRecurringChar(input_string):
    recurring_chars= []
    count_dict = Counter(input_string)
    for x, y in count_dict.items():
        if y > 1:
            recurring_chars.append(x)
    if recurring_chars:
        return recurring_chars[0]
    else:
        return (-1)
    
if __name__ == '__main__':
    print (firstRecurringChar(input_string))