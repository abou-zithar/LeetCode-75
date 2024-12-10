class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        heap = {}
        for n in arr:
            if n in heap:
                heap[n] +=1
            else:
                heap[n] =1
        
        s = set(heap.values()) 
        if len(s) == len(heap.values()):
            return True
        else:
            return False
        