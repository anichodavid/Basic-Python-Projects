def reverse_stack(stack):
     
    if len(stack) == 0:
        return []
    return reverse_stack (stack[1:]) + [stack[0]]

print(reverse_stack ([1, 2, 3, 4, 5]))
print(reverse_stack([]))

















#def reverse_stack(stack):
#
#    lost = []
#    if stack == "" :
#        return ""
#    else: 
#        lost.append(stack)
#        return reverse_stack(stack[1:]) + stack[0]
#
#print(reverse_stack ("12345"))










