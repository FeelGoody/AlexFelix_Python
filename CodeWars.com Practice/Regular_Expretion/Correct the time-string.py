''' # https://www.codewars.com/kata/57873ab5e55533a2890000c7/train/python
  # test.describe("Basic Tests")
  # test.it("None or empty")
  # test.assert_equals(time_correct(None), None)
  # test.assert_equals(time_correct(""), "")
  # test.it("Invalid Format")
  # test.assert_equals(time_correct("001122"), None)
  # test.assert_equals(time_correct("00;11;22"), None)
  # test.assert_equals(time_correct("0a:1c:22"), None)
  # test.it("Correction Tests")
  # test.assert_equals(time_correct("09:10:01"), "09:10:01")
  # test.assert_equals(time_correct("11:70:10"), "12:10:10")
  # test.assert_equals(time_correct("19:99:99"), "20:40:39")
  # test.assert_equals(time_correct("24:01:01"), "00:01:01")
  # test.assert_equals(time_correct("52:01:01"), "04:01:01")
  # -----------
  # You have to create a method, that corrects a given time string.
  # There was a problem in addition, so many of the time strings are broken.
  # Time is formatted using the 24-hour clock, so from 00:00:00 to 23:59:59.
'''

# 1. making reg Exception between
# 2. re will return 3 values(if valid) or NONE (if invalid)
# 3. HH - if above 23 -> subsctruct 24
# 4. MM - if above 60 -> subsctruct 60 and remaining add to HH
# 5. SS - if above 60 -> subsctruct 60 and remaining add to MM

import re


def time_correct(t):
    if t == "":
        return ""
    res = re.match(r'(\d\d):(\d\d):(\d\d)', str(t))

    if not res:
        return None

    h = int(res.group(1))
    m = int(res.group(2))
    s = int(res.group(3))

    if s > 59:
        s -= 60
        m += 1
    if s <= 9:
        s = f'0{s}'

    if m > 59:
        m -= 60
        h += 1
    if m <= 9:
        m = f'0{m}'

    if h > 23:
        h = h % 24
    if h <= 9:
        h = f'0{h}'

    return f'{h}:{m}:{s}'


res1 = time_correct('2), None)"00;11;2288:12:01""), No"52:01:01"ne)')
res2 = time_correct('25:62:99')
print(res1, res2)