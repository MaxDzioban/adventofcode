# first part
# It contains at least three vowels (aeiou only), 
# like aei, xazegov, or aeiouaeiouaeiou.
# It contains at least one letter that appears 
# twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
# It does not contain the strings ab, 
# має аб- погана
# немає аб добра
# cd, pq, or xy, even if they are part of one of the other requirements.

ok_strings=0

def at_least_three_vowels(stringa):
    count_of_vowels = 0
    vowels = ["a","e","i","o","u"]
    for elem in vowels:
        count_of_vowels += stringa.count(elem)
    if count_of_vowels>=3:
        return True
    return False

def letter_that_appears_twice(stringa):
    for i in range(len(stringa)-1):
        if stringa[i] == stringa[i+1]:
            return True
    return False

def contain_the_strings_ab(stringa):
    blocked =["ab","cd", "pq", "xy"]
    for block in blocked:
        if block in stringa:
            return False
    return True

with open("day_5_year_2015.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        # print(line)
        if at_least_three_vowels(str(line)) and letter_that_appears_twice(str(line)) and contain_the_strings_ab(str(line)):
            ok_strings+=1
        else:
            continue
print(ok_strings)


#part 2
# two letters that appears at least twice

# at least one letter which repeats with 
# exactly one letter between them, 
# like xyx, abcdefeghi (efe), or even aaa.
ok_strings=0

def has_repeated_pair(s):
    pairs = {}
    for i in range(len(s) - 1):
        pair = s[i:i+2]
        if pair in pairs:
            if i - pairs[pair] >= 2:
                return True
        else:
            pairs[pair] = i
    return False


def has_repeating_letter_with_gap(s):
    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            return True
    return False

with open("day_5_year_2015.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if has_repeating_letter_with_gap(str(line)) and has_repeated_pair(str(line)):
            ok_strings+=1
        else:
            continue
print(ok_strings)
