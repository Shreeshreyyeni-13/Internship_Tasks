# Problem: Find a String
# Link: https://www.hackerrank.com/challenges/find-a-string/problem

string = input()
substring = input()

count = 0

for i in range(len(string) - len(substring) + 1):
    if string[i:i + len(substring)] == substring:
        count += 1

print(count)