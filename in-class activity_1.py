string = input("Please enter your team name: ")
S = []
for char in string:
    S.append(char)
reversed_string = ""
while S:
    reversed_string += S.pop()
print(reversed_string)
