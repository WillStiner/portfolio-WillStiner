class StringUtility:
    
    def __init__(self, string):
        self.string = string
        
    def __str__(self):
        '''
        returns the original string, unchanged
        args: none
        return: self.string - str - original string
        '''
        return self.string
    
    def vowels(self):
        '''
        counts the vowels in the string and returns it as a string
        args: none
        return: 
        - count - int - number of vowels in the string
        - "many" - str- the word "many" if there are more than 5 vowels
        '''
        ind = 0
        count = 0
        vowels = 'aeiou'
        for _ in self.string:
            letter = self.string[ind]
            ind = ind + 1
            print(letter)
            if letter in vowels:
                count = count + 1
        if count < 5:
            return str(count)
        else:
            return "many"
              
    def bothEnds(self):
        '''
        return a string with the first and last two characters of the original string, return empty string if length of original < 2
        args: none
        return: both_ends_string - str - either an empty string or a string with the first and last two characters of the original string
        - 
        '''
        both_ends_string = ""
        if len(self.string) < 2:
            return both_ends_string
        else:
            both_ends_string = (self.string[0] + self.string[1] + self.string[-2] + self.string[-1])
            return both_ends_string
        
    def fixStart(self):
        '''
        return a string where all occurances of first character are replaced with *, except for the first occurance
        args: none
        return: 
        - self.string - str - originak string
        - new_string - str - new string with all occurances of first character replaced with *
        '''
        if len(self.string) < 1:
            return self.string
        else:
            start = self.string[0]
            ind = 1
            length = len(self.string) - 1
            end_of_string = []
            i = 1
            for _ in range(length):
                end_of_string.append(self.string[i])
                i = i + 1
                rest_of_string = "".join(end_of_string) # .join method from https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/
            for _ in range (length):
                letter = self.string[ind]
                if letter == start:
                    rest_of_string = rest_of_string.replace(letter, "*", )
                ind = ind + 1
            new_string = start + rest_of_string
            return new_string
        
    def asciiSum(self):
        '''
        return an int that contains sum of all ascii values in the string
        args: none
        return: sum - int - sum of all ascii values in string
        '''
        sum = 0
        ind = 0
        length = len(self.string) 
        for _ in range(length):
            sum = sum + ord(self.string[ind]) # ord() function from https://www.toppr.com/guides/python-guide/questions/how-do-i-get-the-ascii-value-of-a-character-in-python-and-python-3/
            ind = ind + 1
        return sum
            
    def cipher(self):
        '''
        return an encoded string that incrememnts all letters by length of the string
        args: none
        return: result - str - encoded string, all letters shifted by length of string, other characters unchanged
        '''
        result = ""
        length = len(self.string) 
        ind = 0
        for _ in range(length):
            if self.string[ind].isalpha(): # isalpha() method from https://www.w3schools.com/python/ref_string_isalpha.asp
                char_ascii = ord(self.string[ind])
                if self.string[ind].isupper(): # isupper() method from https://www.w3schools.com/python/ref_string_isupper.asp
                    base_char_code = ord('A')
                else:
                    base_char_code = ord('a')
                shifted_char_code = (char_ascii - base_char_code + length) % 26 + base_char_code
                result = result + chr(shifted_char_code) # chr function from https://www.pythoncheatsheet.org/builtin/chr
            else:
                result = result + self.string[ind]
            ind = ind + 1
            print(result)
        return result