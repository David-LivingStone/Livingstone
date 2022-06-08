# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    
     
    # the sorted strings are checked
    if(sorted(word)== sorted(anagram)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")        
         
# driver code 
s1 ="listen"
s2 ="silent"
find_anagram(s1, s2)

    #return True