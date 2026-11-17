def digit_sum(n):
    if n < 10:
        return n
    return (n % 10) + digit_sum(n // 10)  
#digit_sum(1234)
#= 4 + digit_sum(123)
#= 4 + (3 + digit_sum(12))
#= 4 + (3 + (2 + digit_sum(1)))
#= 4 + (3 + (2 + 1))
#= 10 ✅



def reverse_text(text):
    if text == "":
        return ""
    return reverse_text(text[1:]) + text[0]
#reverse_text("abc")
#= reverse_text("bc") + "a"
#= (reverse_text("c") + "b") + "a"
#= ((reverse_text("") + "c") + "b") + "a"
#= (("" + "c") + "b") + "a"
#= "cba" ✅


def count_char(text, ch):
    if text == "":
        return 0
    if text[0] == ch:
        return 1 + count_char(text[1:], ch)
    return count_char(text[1:], ch)
#count_char("banana", "a")
#= count_char("anana", "a")            # 'b' ≠ 'a'
#= 1 + count_char("nana", "a")         # 'a' == 'a'
#= 1 + count_char("ana", "a")          # 'n' ≠ 'a'
#= 1 + 1 + count_char("na", "a")       # 'a' == 'a'
#= 1 + 1 + count_char("a", "a")        # 'n' ≠ 'a'
#= 1 + 1 + 1 + count_char("", "a")     # 'a' == 'a'
#= 1 + 1 + 1 + 0
#= 3 ✅


def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)
#power(2, 10)
#= 2 * power(2, 9)
#= 2 * 2 * power(2, 8)
#= ...
#= 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * power(2, 0)
#= 2^10 * 1
#= 1024 ✅


print(digit_sum(1234))
print(digit_sum(0))
print(reverse_text("abc"))
print(reverse_text(""))
print(count_char("banana", "a"))
print(power(2, 10))
print(power(5, 0))
   

