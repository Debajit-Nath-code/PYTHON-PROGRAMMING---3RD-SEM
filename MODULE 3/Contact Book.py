phonebook = {}
entry_count = int(input("Enter number of contacts: "))

for _ in range(entry_count):
    person = input("Enter name: ")
    mobile = input("Enter phone number: ")
    phonebook[person] = mobile

print("\nContact Book")
for person, mobile in phonebook.items():
    print(person, ":", mobile)
