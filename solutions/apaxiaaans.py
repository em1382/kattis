import re
name = str(input())
name = re.sub(r'([a-z])\1+', r'\1', name)
print(name)
