class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        
        double = 0
        movement = 0
        while target > 1 :
            if double < maxDoubles :
                if target % 2 == 0 :
                    target = target / 2
                    movement += 1
                    double += 1
                else :
                    target -= 1
                    movement +=1
            else:
                return int(movement + (target - 1))

        
        return int(movement)
