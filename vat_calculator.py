list = []
print('> Welcome to the VAT Calculator! \n')
print('> To enter the program, type Y \n > To exit the program, type N \n > To calculate, type C: \n ')
while True:
    choice = input('> ')
    if choice == 'Y':
        num = int(input('Add your integer prices: \n > '))
        list.append(num)
        print('This are the prices added: \n', *list)
        print(' ')
    elif choice == 'C':
        no_vat = int(sum(list)) #sums without the VAT
        only_vat = no_vat/100 * 20
        total = no_vat + only_vat
        print('> Total without the VAT: ', no_vat, '\n'
            '> Only the VAT: ', only_vat, '\n'
            '> Total price with VAT of 20%: ', total)
        print(' ')
    else:
        print('Thank you!')
        break
