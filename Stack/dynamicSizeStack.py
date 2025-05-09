s = []

# Push elements
s.append(10)
s.append(20)
s.append(30)

# Pop and print the top element
print(f'{s[-1]} popped from stack')
s.pop()

# Peek at the top element
print(f'Top element is: {s[-1]}')

# Print all elements in the stack
print('Elements present in stack: ', end='')
while s:
    print(s.pop(), end=' ')

'''
Output:
30 popped from stack
Top element is: 20
Elements present in stack: 20 10 
'''