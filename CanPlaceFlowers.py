class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n ==0:
            return True
        Num_of_flowers = len(flowerbed)
        for i in range(Num_of_flowers):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1]== 0) and (i == Num_of_flowers-1 or flowerbed[i+1]== 0):
                flowerbed[i] = 1
                n -=1
            if n == 0 :
                return True
        
        return False

    


        