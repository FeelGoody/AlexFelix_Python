import re

string_1 = 'Hello, Felix'
pattern = r'Hello, F'
result = re.match(pattern, string_1)
# print("result:", result.group())
# print("Start index:", result.start())
# print("End index:", result.end())

string_2 = 'Felix Hello HelloAlex Hello'
pattern_2 = r'Hello'
result_2 = re.search(pattern_2, string_2)
# print("result2:", result_2.group())
# print("Start index:", result_2.start())
# print("End index:", result_2.end())

result_3 = re.findall(pattern_2, string_2)
# print('Findall result:', result_3)

split_pattern = r'll'
split_r = re.split(split_pattern, string_2, 1)
# print("Split patt:", split_r)


sub_r = re.sub(pattern_2, 'GoodMorning', string_2)
# print("Substitution:", sub_r)

our_pattern = re.compile(r"Hello")
# print(our_pattern.findall(string_2))
# print(our_pattern.split(string_2))

our_pattern = re.compile(r"and")
myText = '''
RegExr was created by gskinner.com, and is proudly hosted by Media Temple.
Edit the Expression & Text to see matches. Roll over matches or the expression for details. PCRE & JavaScript flavors of RegEx are supported. Validate your expression with Tests mode.
The side bar includes a Cheatsheet, full Reference, and Help. You can also Save & Share with the Community, and view patterns you create or favorite in My Patterns.
Explore results with the Tools below. Replace & List output custom results. Details lists capture groups. Explain describes your expression in plain English.
'''
fromMyText = our_pattern.findall(string=myText, pos=5, endpos=10)
print(fromMyText)