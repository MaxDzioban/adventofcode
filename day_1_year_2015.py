# part1 
stack=[]
with open("day_1_year_2015.txt", "r", encoding="utf-8") as file:
    for line in file:
        for elem in line:
            if len(stack)==0:
                stack.append(elem)
            elif stack[-1] == elem:
                stack.append(elem)
            else:
                stack.pop()
if len(stack)!=0:
    print(len(stack)*-1 if stack[0]==")" else len(stack)*1)

#part 2 
found = False
floor = 0
with open("day_1_year_2015.txt", "r", encoding="utf-8") as file:
    for line in file:
        for index, char in enumerate(line):
            if char == "(":
                floor += 1
            elif char == ")":
                floor -= 1
            if floor == -1:
                print(index + 1)
                found = True
                break
        if found:
            break
