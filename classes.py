
def saldo(filename, amount, comment):
    '''Aktualizuje stan konta i zapisuje akcję w pliku historii operacji'''
    with open(filename) as saldo:
        acc_balance = saldo.readline()
        #print(acc_balance)
        acc_balance = float(acc_balance) + float(amount)
        #acc_balance = str(acc_balance)
        #print(acc_balance)
        with open(filename, 'w') as saldo:
            saldo.write(str(acc_balance))
    #print(saldo)


    with open('logs.txt', 'a') as logs:
        new_line = '/n'
        logs.write(f'Stan konta zmienił się o {amount}. Komentarz: {comment}.{new_line}')



