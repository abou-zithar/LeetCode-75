class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        output= [0]
        for n in gain:  
            output.append(n+output[-1])

        return max(output)
      