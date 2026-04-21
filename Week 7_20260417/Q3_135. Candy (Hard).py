class Solution:
    def candy(self, ratings: List[int]) -> int:
        # Give each person a candy first
        candy = [1] * len(ratings)

        for i in range(1,len(ratings)):
            # from left
            if ratings[i] > ratings[i-1]:
                candy[i] = candy[i-1] + 1
            # from right
        for  i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candy[i] = max(candy[i], candy[i+1] + 1)
        return sum(candy)
        
