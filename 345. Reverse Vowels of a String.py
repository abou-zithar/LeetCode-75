class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        new_word= []
        word_vowels= []
        for letter in s:
            if letter in vowels:
                word_vowels.append(letter)
                new_word.append("_")
            else:
                new_word.append(letter)

        word_vowels.reverse()
        output = []
        i=0
        for letter in new_word:
            if letter == "_":
                output.append(word_vowels[i])
                i+=1
            else:
                output.append(letter)
        
        return "".join(output)


                
                

        



        