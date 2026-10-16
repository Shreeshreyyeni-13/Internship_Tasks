# Problem: Mutations
# Link: https://www.hackerrank.com/challenges/python-mutations/problem

string = input()
position, character = input().split()

string = (
    string[:int(position)]
    + character
    + string[int(position) + 1:]
)

print(string)