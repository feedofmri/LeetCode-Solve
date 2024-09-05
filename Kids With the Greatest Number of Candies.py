class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        
        result = []
        largest = candies[0]
        for i in candies:
            if i > largest:
                largest = i

        for j in candies:
            if j+extraCandies >= largest:
                result.append(True)
            else:
                result.append(False)

        return result