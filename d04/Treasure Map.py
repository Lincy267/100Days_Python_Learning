# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
x_axis = int(position[0])
y_axis = int(position[1])

row_number = map[y_axis - 1]
row_number[x_axis - 1] = 'X'



#(3,1)-->map[0][2]
#(2,2)-->map[1][1]
#(1,3)-->map[2][0]



#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

