import math
def count_a(wordd, char='a'):
    count = 0
    for c in wordd:
        if c == char:
            count += 1
    return count

def count_e(wordd, char='e'):
    count = 0
    for c in wordd:
        if c == char:
            count += 1
    return count

def count_i(wordd, char='i'):
    count = 0
    for c in wordd:
        if c == char:
            count += 1
    return count

def count_o(wordd, char='o'):
    count = 0
    for c in wordd:
        if c == char:
            count += 1
    return count
    
def count_u(wordd, char='u'):
    count = 0
    for c in wordd:
        if c == char:
            count += 1
    return count
    
def count_comma(wordd, char=','):
    count = 0
    for c in wordd:
        if c == char:
            count += 1
    return count

txt_input = "This, is, a, sentence,"
txt_list = txt_input.split()
amt_vowel = 0
sec = 0
for word in txt_list:
  current_amt = count_a(word) + count_e(word) + count_i(word) + count_o(word) + count_u(word)
  amt_vowel = amt_vowel + current_amt
  sec = sec + count_comma(word)
  print("Amount of vowels",amt_vowel)

print(math.ceil(amt_vowel/3.8)+sec)
print (txt_list)

