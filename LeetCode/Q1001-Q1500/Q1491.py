# 1491. Average Salary Excluding the Minimum and Maximum Salary
class Solution:
    def average(self, salary) -> float:
        minimum, maximum, length = salary[0], salary[0], len(salary)
        total = salary[0]
        for i in range(1,length):
            s = salary[i]
            total += s
            if s < minimum : minimum = s
            elif s > maximum : maximum = s
        return (total - maximum - minimum) / (length-2)