# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, list):
        result = []
        for word in list:
            string1 = [letter for letter in self.word]
            string2 = [letter for letter in word]
            if sorted(string1) == sorted(string2):
                result.append(word)
        return result


#compare word with each word in list
#if any letter in word matches with a word in the list
# -make them cancel out
# continue comparing until all letters of word are used OR
# no letter match

#if letters match, push word in list to new list
# -continue to next word
# repeat steps

# return new list