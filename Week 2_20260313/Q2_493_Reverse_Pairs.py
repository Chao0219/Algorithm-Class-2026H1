class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # 找到前面一個就去搜後面小的
        def merge_sort(array):
            if len(array) <= 1 :return array, 0

            # divide
            mid = len(array) // 2
            left, left_count = merge_sort(array[:mid])
            right, right_count = merge_sort(array [mid:])
            result =[]

            
            count = 0
            j = 0
            for i in range(len(left)):
                while j < len(right) and left[i] > 2 * right[j]:
                    j += 1
                count += j

            count += left_count + right_count

            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] > right[j] :
                    result.append(right[j])
                    j += 1
                else : 
                    result.append(left[i])
                    i += 1

            result += (left[i:])
            result += (right[j:])

            return result, count
        _, count = merge_sort(nums)
        return count
