"""
Refer below link for the question:
    https://www.geeksforgeeks.org/search-a-word-in-a-2d-grid-of-characters/

Solution:
    Algorithm for this is already present, but expected solution should 
    have lowest time complexity (the algorithm should only traverse once unlike the 
    solution above which traverses whole matrix for each word given)

Enhancement: 
    if the word is not present in the grid, print word along with row 
    and col as (-1,-1) like word,-1,-1

Hint: 
    Use DP approach

Solution that I have gone with is below:

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
class word_seek: 
      
    def __init__(self): 
        self.R = None
        self.C = None
        self.dir = [[-1, 0], [1, 0], [1, 1],  
                    [1, -1], [-1, -1], [-1, 1], 
                    [0, 1], [0, -1]] 
    def search_grid(self, grid, row, col, word): 
        if grid[row][col] != word[0]: 
            return False
        for x, y in self.dir: 
            rd, cd = row + x, col + y 
            flag = True
            for k in range(1, len(word)): 
                if (0 <= rd <self.R and 
                    0 <= cd < self.C and 
                    word[k] == grid[rd][cd]):  
                    rd += x 
                    cd += y 
                else: 
                    flag = False
                    break       
            if flag: 
                return True
        return False  
    def patternSearch(self, grid, word): 
        self.R = len(grid) 
        self.C = len(grid[0])
        tracker = []
        for row in range(self.R): 
            for col in range(self.C): 
                if self.search_grid(grid, row, col, word): 
                    tracker.append((word,row,col))
                else:
                    tracker.append((word,-1,-1))
        if len(set(tracker)) > 1:
            tracker = sorted(tracker,key=lambda x: x[1],reverse=True)
            print (tracker[0][0],tracker[0][1],tracker[0][2])
            return
        else:
            assert (tracker[0][1] == -1) and (tracker[0][2] == -1),"failed"
            print (tracker[0][0],tracker[0][1],tracker[0][2])
            return

if __name__ == '__main__':
    grid = sys.stdin.readlines()
    grid = [i.strip() for i in grid]
    ind = grid.index('')
    #grid = grid[:(ind)]
    #finders = grid[(ind+1):]
    #print (grid)
    #print (finders)
    wordSeek = word_seek()
    for w in grid[(ind+1):]:
        wordSeek.patternSearch(grid[:(ind)],w)