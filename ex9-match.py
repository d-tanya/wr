import re

print('enter text:')
text =  input()
print('enter pattern:')
pat = input()
try:
    match = re.search(pat, text)
    print(match.group(0))
except AttributeError:
    print("no matches with pattern in this text")
