a = int(input("Please enter your age"))
if a >= 18:
    print('you can watch the movie')
elif 18 > a >= 16:
    print('you can watch the movie with an adult')
    c = input('an adult with you? Y or N').upper()
    if c== "Y":
        print( 'enjoy')
    else:
        print('get out of here!')
else:
    print('no movie for you')   
print('Done')
