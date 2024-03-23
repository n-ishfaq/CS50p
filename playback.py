inn = input("Enter a line that you want to be at 0.75x speed: ")
dot="."*3
for i, char in enumerate(inn):
    if char == ' ':
        print(dot, end='')  
    else:
        print(char, end='')
