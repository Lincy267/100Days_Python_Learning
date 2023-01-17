# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
x = 0
sum_height = 0
for h in student_heights:
    x += 1
    sum_height += h

print(round(sum_height/x))
