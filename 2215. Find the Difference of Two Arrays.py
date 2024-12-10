class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer1= set()
        answer2 = set()
        answer= []
        for element in nums1:
            if element not in nums2:
                answer1.add(element)
        answer.append(list(answer1))
        for element in nums2:
            if element not in nums1:
                answer2.add(element)

        answer.append(list(answer2))

        return answer

class Solution2:
    def findDifference2(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        h1 = set(nums1)
        h2 =set(nums2)
        for n in nums2:
            if n in h1:
                h1.remove(n)
                h2.discard(n)


        return [list(h1),list(h2)]
