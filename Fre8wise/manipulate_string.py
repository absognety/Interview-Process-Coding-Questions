"""
Solve the following algorithm problem:
    Given a string, develop a solution that removes only 1's
    in the beginning
    
    Examples:
        1198fgh098nm -> 98fgh098nm
        a1198fgh098nm -> a1198fgh098nm
        a1198fgh098nm11 -> a1198fgh098nm11
"""

s = "1198fgh098nm"


def changeString(s):
    try:
        while (s.index("1") == 0):
            slist = list(s)
            temp = slist.pop(0)
            s = "".join(slist)
    except:
        pass
    return s

if __name__ == '__main__':
    s = input()
    print (changeString(s))