""" 
1
1 3
1 3 5
1 3 5 7 
1 3 5 7 9
n...
"""
count = 1
for l in range (1, 20, 2):
    print(f'{count}: ', end = ' ')
    soma = 0
    for c in range (l+1):
        if (c % 2 == 1):
            soma = count**2
            print(c, end = ' ')
    print(f' - {count}^2')
    count+=1
print('n...')

"""
run with:
python main.py
"""
