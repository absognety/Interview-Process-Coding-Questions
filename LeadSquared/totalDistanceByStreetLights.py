"""
Given N street lights, and an array of tuples which signify the start and 
end distances of street covered by that street light.

Find the total distance covered by all the street lights

Ex:1
    N = 1
    arr = [(5,10)]
    Number of street lights = 1
    and distance covered by street light i is 5m to 10m which is 10-5 = 5m
    
Ex:2  
    N = 2
    arr = [(5,10),(8,12)]
    Number of street lights = 2
    street light 0 = 10 - 5 = 5
    street light 1 = 12 - 8 = 4
    common region = 10 - 8 = 2
    total distance = (5 + 4 - 2) = 7
    
"""