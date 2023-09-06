
# AI_Lab1a_q2_stu
# Ques: Given that nums = [1, 2, 3, 4, 5, 6], 
#       Design an algorithm to print them into line1=[1, 3, 5]; and line2=[2, 4, 6]
# Student Name:Xu Xiaochi
# Student ID:12556828
nums = [1, 2, 3, 4, 5, 6]
line1 = []
line2 = []
for i in range(len(nums)):
    if i % 2 == 0:
        line1.append(nums[i])
    else:
        line2.append(nums[i])
print(line1)
print(line2)
