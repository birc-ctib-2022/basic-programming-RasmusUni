
# Print the pattern
list2 = []

for x in range(9):
    if x <=4:
        list2.append("*")
        y=" ".join(list2)
        print(y)
    elif x>0:
        list2.pop(0)
        y=" ".join(list2)
        print(y)

