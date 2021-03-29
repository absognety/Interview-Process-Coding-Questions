"""
Given a text and a word, find the count of occurrences of anagrams
of word in given text

"""

def countAnagrams(text,word):
    count=0
    b = text
    a = word
    for i in range(len(b)-len(a)+1):
        if(sorted(a)==sorted(b[i:i+len(a)])):
            count=count+1
    return count 


if __name__ == '__main__':
    text = str(input())
    word = str(input())
    print (countAnagrams(text, word))