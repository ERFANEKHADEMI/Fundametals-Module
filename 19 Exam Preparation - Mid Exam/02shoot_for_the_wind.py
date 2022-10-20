def increase_decrease(target_list, target):
    for idx in range(len(target_list)):
        if target_list[idx] == -1:
            continue
        if target_list[idx] > target:
            target_list[idx] -= target
        else:
            target_list[idx] += target

    return target_list


targets = list(map(int, input().split()))

while True:
    command = input()
    if command == 'End':
        break
    index = int(command)
    current_number = 0
    if index in range(len(targets)):
        current_number = targets[index]
        targets[index] = -1
        targets = increase_decrease(targets, current_number)

shooted = int(targets.count(-1))

print(f"Shot targets: {shooted} -> {' '.join(str(num) for num in targets)}")



#################################### TASK CONDITION ############################
"""
                             2.	Shoot for the Win
Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2305#1.

Write a program that helps you keep track of your shot targets. 
You will receive a sequence with integers, separated by a single space, 
representing targets and their value. Afterward, you will be receiving 
indices until the "End" command is given, and you need to print the 
targets and the count of shot targets. Every time you receive an index, 
you need to shoot the target on that index, if it is possible. 
Every time you shoot a target, its value becomes -1, and it is considered shot. 
Along with that, you also need to:
•	Reduce all the other targets, which have greater values 
than your current target, with its value. 
•	Increase all the other targets, which have less than or 
equal value to the shot target, with its value.
Keep in mind that you can't shoot a target, which is already shot. 
You also can't increase or reduce a target, which is considered shot.
When you receive the "End" command, print the targets in their current 
state and the count of shot targets in the following format:
"Shot targets: {count} -> {target1} {target2}… {targetn}"
Input / Constraints
•	On the first line of input, you will receive a sequence of integers, 
separated by a single space – the targets sequence.
•	On the following lines, until the "End" command, you be receiving 
integers each on a single line – the index of the target to be shot.
Output
•	The format of the output is described above in the problem description.


____________________________________________________________________________________________
Example_01

Input
24 50 36 70
0
4
3
1
End

Output
Shot targets 3 -> -1 -1 130 -1


Explanation
First, we shoot the target on index 0. It becomes equal to -1, 
and we start going through the rest of the targets. 
Since 50 is more than 24, we reduce it to 26 and 36 to 12 and 70 to 46. 
The sequence looks like that:
-1 26 12 46
The following index is invalid, so we don't do anything. Index 3 is valid, 
and after the operations, our sequence should look like that:
-1 72 58 -1
Then we take the first index with value 72, and our sequence looks like that:
-1 -1 130 -1
Then we print the result after the "End" command.


____________________________________________________________________________________________
Example_02

Input
30 30 12 60 54 66
5
2
4
0
End

Output
Shot targets: 4 -> -1 120 -1 66 -1 -1

"""
