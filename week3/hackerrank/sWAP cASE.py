def swap_case(s):
    result = ""

    for char in s:
        if char.islower():
            result += char.upper()
        else:
            result += char.lower()
    return result


s = input('enter:')
result = swap_case(s)
print(result)

# sample input
# HackerRank.com presents "Pythonist 2".

# Sample Output
# hACKERrANK.COM PRESENTS "pYTHONIST 2".