def notes(amount):
    notes_dict={2000:0,500:0,50:0,20:0,10:0,5:0,2:0,1:0}
    for i in notes_dict:
        notes_dict[i]=amount//i
        amount=amount%i
    return notes_dict
amount=int(input("Enter the amount: "))
print("Number of notes:")
print(notes(amount))
print("Thank you!")