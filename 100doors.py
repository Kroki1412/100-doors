# You have 100 doors in a hallway in a row that are all initially closed. You make 100 passes by the doors.
# The first time through, you visit every door and toggle the door (if the door is closed, you open it;
# if it is open, you close it). The second time you only visit every 2nd door (door #2, #4, #6, ...).
# The third time, every 3rd door (door #3, #6, #9, ...), etc, until you only visit the 100th door.

# this part of the script is creating the 100 doors in a list as 0 (closed).
door_list = []
door_number = []
i = 0
while (i <= 99):
    door_list.append('0')
    i += 1


# this function will change the numbers from 0 to 1 and from 1 to 0 for open or closed state of the door.
def door_changer(number):
    global door_list
    a = number
    while (number <= 100):
#        print(number)
        b = number - 1
        if door_list[b] == '1':
            door_list[b] = '0'
        elif door_list[b] == '0':
            door_list[b] = '1'
        number += a
    return


# this loop will run the script for all 100 numbers. incrementing it by 1.
m = 1
while (m <= 100):
#    print(door_list)
    door_changer(m)
    m += 1

# the following lines are printing the door numbers which are open.
print("The following doors are open:")
k = 0
while (k <= 99):
    if door_list[k] == '1':
        print(k + 1,' ', end="")
        k += 1
    else:
        k += 1