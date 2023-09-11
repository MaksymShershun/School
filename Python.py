# # print((95+229)/3)
# # print(3*(215-133/6))
# # print(21**2-5**3)

# # print('Hello, Max!')
# # print('\nHello, Max!\n')

# # print((2+5+17+134+10)/5)

# # number = [2, 5, 17, 134, 10]
# # sum = 0
# # for n in number:
# #     sum += n
# # ser_arrif=sum / len(number)
# # print(ser_arrif)

# # name = input('What is your name? \n')
# # # print('Hello, ', name)
# # print(f'Hello, {name}')

# name = input('What is your name? \n')
# print(f'Hello, {name}')
# while True:
#     command=input('How can I help you? ')
#     if command.startswith('add'):
#         print('Ok, I will help you.')
#     else:
#         print("I don't understand, what do you want from me?")
#         break


i = 0
while True:
    text = input('Enter the text.')
    text1 = text.split()
    print('\n', text1, '\n')
    
    for e in text1:
        if 'is' in e:
            i += 1
            print(e)
    print(i)