# Cambridge University PDF PAGE 88 challenges.

print(''' 
    1) Create a new file.
    2) Display the file.
    3) Add a new item to the file.
\__________________________
>>Make a selection 1, 2, 3.
      
      ''')

choices = [1, 2, 3]

user_selection = int(input("Choose a selection: "))

while user_selection not in choices:
        print("Please fill the field!")
        user_selection = int(input("Choose a selection: "))

        
if user_selection == choices[0]:
    with open('subjects.txt', 'w') as subjectsText:
        subjectsText.write(input("type your favorite subject: "))

elif user_selection == choices[1]:
    with open('subjects.txt', 'r') as subjectsText:
        content = subjectsText.read()
        print(content)

elif user_selection == choices[2]:
    with open('subjects.txt', 'a') as subjectsText:
        subjectsText.write(f'\n{input("add one more subjects and see the whole list: ")}')
    with open('subjects.txt', 'r') as subjectsText:
        content = subjectsText.read()
        print(content)
        
        
        
