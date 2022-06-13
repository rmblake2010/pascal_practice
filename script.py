#print lines
def print_line():
    print('------------------------')

# Using max()
def max_num(num1, num2):
    print('using max()')
    return max([num1, num2])

print('Testing Functions')
print_line()
print(max_num(4,24))
print_line()

# Multiplying a list
def mult_list(lst):
    prod = lst[0]

    for i in lst[1:]:
        prod = prod * i

    print('multiplying elements in a list')
    return prod

print(mult_list([1,5,5]))
print_line()

# Reversing a string
def rev_string(x):
    print('reversing a string')
    return x[::-1]

print(rev_string('bill'))
print_line()

# Function to check if number falls within a given range
def num_within(range_check, num1, num2):
    print("Checking numbers within a range")
    print(f"checking if {num1} & {num2+1} is in the range of {range_check}")
    return range_check in range(num1, num2+1)
print(num_within(3, 1, 3))
print_line()


#Pascal triangle Function

def pascal(x):
    pascal_triangle = [[1], [1, 1]]
    if(x) < 1:
        print('no rows/invalid rows')
    elif x == 1:
        print(pascal_triangle[0])
    else:
        #Row is atleast 2 because x is greater than 1
        row_number = 2
        while len(pascal_triangle) < x:
            row = []
            row_prev = pascal_triangle[row_number - 1]

            length = len(row_prev) + 1
            for i in range(length):
                if i == 0:
                    row.append(1)
                elif i > 0 and i < length-1:
                    row.append(pascal_triangle[row_number - 1][i-1]+pascal_triangle[row_number - 1][i])
                else:
                    row.append(1)
            pascal_triangle.append(row)
            row_number += 1
        for row in pascal_triangle:
            print(row)



print("Pascal Triangle")
print_line()
pascal(5)