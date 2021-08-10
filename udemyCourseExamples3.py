l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

while True:
    a = input('guess a number or type q to quit')
    if a == "q":
        break
    elif int(a) in l:
        print('Correct Guess!')
    else:
        print('Wrong Guess!')
