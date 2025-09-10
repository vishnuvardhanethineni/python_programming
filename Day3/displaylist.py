def display_negative_values(input_list):
    negative_values = [num for num in input_list if num < 0]
    print("Negative values in the list:", negative_values)
print("Enter a list of integers separated by spaces:")
list1=list(map(int,input().split()))
display_negative_values(list1)