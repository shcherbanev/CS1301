import re
input = str(input("camelCase: " )).strip()
pattern = re.compile(r'(?<!^)(?=[A-Z])')

input = pattern.sub('_', input).lower()

print("snake_case: " + input)