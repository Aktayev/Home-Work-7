str = input ('whazzaap? ')
str = str.lower ()
if str[0:5] != 'hello' and str[0] == 'h':
    print('0$')
elif str[0:5] =='hello':
    print ('20$')
elif str[0:5] != 'h':
    print('100$')