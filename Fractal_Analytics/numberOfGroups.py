"""
A pole of the magnet is represented as "01" or "10"
1 = North pole and 0 = South pole
we know the like poles of magnet repel each other but unlike poles
attract.
Suppose a magnet has pole "10" and adjacent magnet also has "10" 
they attract 
if a magnet "01" is located adjacent to magnet "10" they repel.

Given a list of poles of different magnets, find the number of the
separate groups that magnets form into

example:
    number of magnets = 3
    01
    01
    10
    
    number of groups = 2 because first 2 magnets attract each other
    so will be in the same group where as the third one repels
    second one so will be in different group
"""


def numGroups(poles):
    groups = [poles[0]]
    for i in range(1,len(poles)):
        if poles[i][0] == groups[-1][0]:
            groups.append(poles[i])
        else:
            groups.append(' ')
            groups.append(poles[i])
    concat_groups = ''.join(groups)
    print (concat_groups)
    return len(concat_groups.split(' '))
    
if __name__ == '__main__':
    n = int(input())
    poles = []
    for tc in range(n):
        pole = input()
        poles.append(pole)
    print (numGroups(poles))