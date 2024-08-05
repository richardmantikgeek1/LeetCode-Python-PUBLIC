from collections import deque
class Solution:
    def countStudents(self, students, sandwiches):
        students = deque(students)
        sandwiches = deque(sandwiches)
        last_students = None
        while (len(students) > 0):
            if (students[0] == sandwiches[0]):
                front_student = students.popleft()
                front_sandwich = sandwiches.popleft()
            else:
                front_student = students.popleft()
                students.append(front_student)

            if (students == last_students):
                return len(students)
            
            last_students = students.copy()

        return 0

students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]
sol = Solution()
result = sol.countStudents(students, sandwiches)
print(result)