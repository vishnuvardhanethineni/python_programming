list1=[]
def add_to_list(item):
    list1.append(item)
while True:
    item = input("Enter an item to add to the list (or 'q' to quit): ")
    if item == 'q':
        break
    add_to_list(item)
print("Current list:", list1)