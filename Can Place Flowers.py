class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):

        if n < 1:
            return True
        size = len(flowerbed)

        for i in range(size):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == size - 1 or flowerbed[i+1] == 0) :
                n -= 1
                flowerbed[i] = 1
        
        return n <= 0
        
        