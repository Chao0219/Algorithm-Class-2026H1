class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # 按照 lastDay (也就是課程的截止日期) 排序
        courses.sort(key=lambda x: x[1])
        total_day = 0 # Check if the courses are overlapping by comparing it with last day
        amount = 0
        selected_duration = []
        for i in range(len(courses)):
            
            duration_est = total_day + courses[i][0]
            if duration_est <= courses[i][1]:
                # the courses aren't overlapping, take it
                total_day += courses[i][0]
                heapq.heappush(selected_duration, -courses[i][0]) # 存負數
                amount += 1
            elif selected_duration and -selected_duration[0] > courses[i][0]:
                # courses are overlapping, drop longest
                longest = -heapq.heappop(selected_duration)
                total_day -= longest
                # amount -= 1             
                # add new class
                total_day += courses[i][0]
                heapq.heappush(selected_duration, -courses[i][0])
                # amount += 1 抵銷
                
        return amount
            
