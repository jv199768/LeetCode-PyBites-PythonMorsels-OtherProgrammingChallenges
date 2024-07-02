''' Bite 373. Reverse only Letters
Given a string, reverse only the English letters (lowercase or uppercase) in the string, leaving all non-English letters and other characters (e.g. numbers) in their original position.'''
# Online Python - IDE, Editor, Compiler, Interpreter
def reverse_only_letters(input):
    ans = list(input)
    i = 0
    j = len(input) - 1

    while i < j:
        while i < j and not input[i].isalpha():
            i += 1
        while i < j and not input[j].isalpha():
            j -= 1
        ans[i], ans[j] = ans[j], ans[i]
        i += 1
        j -= 1
    ans = ''.join(ans)
    return ans

print(reverse_only_letters("ab-cd"))
print(reverse_only_letters("ab5DEf"))
print(reverse_only_letters("a-bC-dEf-ghIj"))
