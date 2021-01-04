# demo of dictionary

# Create dictionary
d = {'Aa': 1, 'Bbb': 22, 'Ccc': 333, 'Dddd': 4444, 'Eeeee': 55555}

# Print without alignment
for k, v in d.items():
    print('{}:{}'.format(k, v))
'''
>>> Aa:1
    Bbb:22 
    Ccc:333
    Dddd:4444
    Eeeee:55555 
'''

# Print with alignment
for k, v in d.items():
    print('{:<7}:{:>6}'.format(k, v))
    # :<7 - left alignment till 7th char
    # :>6 - right alignment till 6th char
'''
>>> Aa     :     1
    Bbb    :    22
    Ccc    :   333
    Dddd   :  4444
    Eeeee  : 55555
'''