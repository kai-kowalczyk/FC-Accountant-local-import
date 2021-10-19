import pprint


def saldo(filename, amount, comment):
    
    with open(filename) as store:
        acc_balance = store.readline()
        products = store.readlines()
        acc_balance = float(acc_balance) + float(amount)     
    with open(filename, 'w') as store:
        store.write(str(acc_balance) + '\n')
        for product in products:
            store.write(product)
    with open('logs.txt', 'a') as logs:
        logs.write(f'Stan konta zmienił się o {amount}. Komentarz: {comment}. Saldo bieżące: {acc_balance}' + '\n')


def sprzedaz(filename, item_id, price, amount):

    with open(filename) as store:
        acc_balance = store.readline()
        products = store.readlines()
        sale = False
        for line in products:
            if item_id in line:
                product_data = line.split(';')
                product_id = product_data[0]
                product_price = float(product_data[1])
                product_amount = int(product_data[2])
                if product_amount >= int(amount):
                    updated_amount = product_amount - int(amount)
                    updated_data = f'{item_id};{float(price)};{updated_amount}'
                    i = products.index(line)
                    products[i] = updated_data + '\n'
                    acc_balance = float(acc_balance) + (float(amount) * float(price))
                    sale = True
                else:
                    print(f'W magazynie jest za mało towaru! Stan: {product_amount} szt.')
                break
            else:
                continue
    if not sale:
        print('Brak produktu w magazynie!')  
    else:
        with open(filename, 'w') as store:
            store.write(str(acc_balance) + '\n') 
            for line in products:
                store.write(line)    
        with open('logs.txt', 'a') as logs:
            logs.write(f'Sprzedano {amount} szt. towaru: {item_id}. Saldo bieżące: {acc_balance} '+ '\n')
    



def zakup(filename, item_id, price, amount):
    

    with open(filename) as store:
        acc_balance = float(store.readline())
        products = store.readlines()
        purchase = False
        whole_price = float(price) * float(amount)
        item_found = False
        for line in products:
            if item_id in line:
                item_found = True
                product_data = line.split(';')
                product_id = product_data[0]
                product_price = float(product_data[1])
                product_amount = int(product_data[2])
                if acc_balance >= whole_price:
                    updated_amount = product_amount + int(amount)
                    updated_data = f'{item_id};{product_price};{updated_amount}'
                    i = products.index(line)
                    products[i] = updated_data + '\n'
                    acc_balance = float(acc_balance) - (float(amount) * float(price))
                    purchase = True
                else:
                    print(f'Za mało środków na koncie! Saldo bieżące: {acc_balance} zł.')
                break
            else:
                pass
        if not item_found :
            if acc_balance >= whole_price:
                    products.append('\n' + f'{item_id};{float(price)};{amount}')
                    acc_balance = float(acc_balance) - (float(amount) * float(price))
                    purchase = True
            else:
                print(f'Za mało środków na koncie! Saldo bieżące: {acc_balance} zł.')        
    if purchase:
        with open(filename, 'w') as store:
            store.write(str(acc_balance) + '\n') 
            for line in products:
                store.write(line)
        with open('logs.txt', 'a') as logs:
            logs.write(f'Zakupiono {amount} szt. towaru: {item_id}. Saldo bieżące: {acc_balance} '+ '\n')


def konto(filename):

    with open(filename) as store:
        acc_balance = float(store.readline())
        print(f'Saldo bieżące: {acc_balance} zł.')


def magazyn(filename, *items):

    with open(filename) as store:
        acc_balance = store.readline()
        products = store.readlines()
        for item in items:
            item_found = False
            for line in products:
                if item in line:
                    item_found = True 
                    product_data = line.split(';')
                    product_id = product_data[0]
                    product_price = float(product_data[1])
                    product_amount = int(product_data[2])
                    print(f'{product_id}:{product_amount}' + '\n')
                    break
                else:
                    continue
            if not item_found:
                print(f'Brak produktu: {item} w magazynie.' + '\n')


def przeglad(filename):

    with open(filename) as logs:
        history = logs.readlines()
        for line in history:
            print(line)