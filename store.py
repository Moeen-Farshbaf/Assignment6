def showmenu():
    print('1. Add product')
    print('2. Edit product')
    print('3. Delete Product')
    print('4. Search')
    print('5. Show list')
    print('6. Buy')
    print('7. Exit')

products = []


def deleter():
    user_choice = input("Please enter the serial of the product you'd like to delete:")
    for i in range(len(products)):
        if products[i]['serial'] == user_choice:
            print(products[i]['name']+' is removed.')
            del products[i]
            break



def edit_prod():
    user_choice = input("Please enter the serial of the product you'd like to edit:")
    for i in range(len(products)):
        if products[i]['serial'] == user_choice:
            products[i]['name']=input('please enter the new name')
            products[i]['price']=input('please enter the new price')
            products[i]['quantity']=input('please enter the new amount')
            




def add_prod():
    Active = True
    while Active:
        new_prod_dict = {}
        new_product_name = input('Please enter the name of the new product')
        new_id = input('please enter the id of the new product')
        new_price = input('please enter the price of the new product')
        new_quantity = input('please enter the quantity of the new product')
        new_prod_dict['name'] = new_product_name 
        new_prod_dict['serial'] = new_id
        new_prod_dict['price'] = new_price
        new_prod_dict['quantity'] = new_quantity
        products.append(new_prod_dict)
        print(new_prod_dict['name']+'added succesfully')
        more = input("do you want to add more stuff?(yes/no)")
        if more == 'yes':
            pass
        else:
            Active = False

def load():
    fi = open('D:\Python online class\Assignment6\storefiles\database1.txt', 'r')
    big_text = fi.read()
    product_list = big_text.split('\n')
    
    for i in range(len(product_list)):
        product_info=product_list[i].split(',')
        mydict = {'name':product_info[0], 'serial':product_info[1] , 'price':product_info[2] , 'quantity':product_info[3]}
        products.append(mydict)

5
load()


from pyfiglet import Figlet
f = Figlet(font='standard')
print (f.renderText('WALLMART'))


active = True
while active:
    showmenu()
    print()
    choice = int(input('Please choose an option: '))

    if choice == 1:
        add_prod()
    elif choice == 2:
        edit_prod()
    elif choice == 3:
        deleter()
    elif choice == 4:
        pass
    elif choice == 5:
            
        for product in products:
            for key,value in product.items():
                
                print(key+": "+value)
            print()
           
    elif choice == 6:
        pass
    elif choice == 7:
        exit()


