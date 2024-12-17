class Solution:
    def removeStars(self, s: str) -> str:
        answer = []
        for letter in s:
            if letter == '*':
                answer.pop()
            else:
                answer.append(letter)
        return "".join(answer)