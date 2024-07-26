# Program to find max & min item in a list

ls = [45, -6, 67, -15, 61, 25, 43, 85]

max = ls[0]
min = ls[0]
for i in ls :
    if i<=min :
        min = i
    if i>=max :
        max = i
    
print('max item:', max, 'present at index:', ls.index(max))
print('min item:', min, 'present at index:', ls.index(min))
