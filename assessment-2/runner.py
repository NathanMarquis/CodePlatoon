from classes.store import Store

store = Store('Code Platoon Video') 

while True:
    selection = input("\n== Welcome to Code Platoon Video! ==\n1. View store video inventory\n2. View customer rented videos\n3. Add new customer\n4. Rent video\n5. Return video\n6. Exit\n")
    if selection == '1':
        store.view_inventory()

    elif selection == '2':
        customer_id = input('Please enter your ID number: ')
        if store.valid_id_check(customer_id) == True:
            store.view_customer_rentals(customer_id)
        else:
            print('\nNot a valid ID.\n')
    elif selection == '3':  
        #A new customer does not have any rented movies
        new_customer_data = {'current_video_rentals': ''}
        new_customer_data['id'] = str(input('Please choose an ID number: '))
        #Checks to see if that ID is already taken by another customer
        while store.valid_id_check(new_customer_data['id']) == True:
            new_customer_data['id'] = str(input('Sorry, that ID is taken. Please choose a different user ID.\n'))
        
        new_customer_data['account_type'] = input('\nPlease enter your account type:\n\t-sx\n\t-px\n\t-sf\n\t-pf\n')
        #Verifies customer is inputting a valid account type
        while new_customer_data['account_type'] not in ['sx', 'px', 'sf', 'pf']:
            new_customer_data['account_type'] = input('Sorry, that type does not exist. Please enter appropriate account type.\n')
        
        new_customer_data['first_name'] = input('Please enter first name.')
        new_customer_data['last_name'] = input('Please enter last name.')

        store.add_customer(new_customer_data)

    elif selection == '4':
        customer_id = input('Please enter your ID number: ')
        if store.valid_id_check(customer_id) == True:
            movie = input('Please enter desired movie: ')
            while
        else:
            print('\nNot a valid ID.\n')
        


    elif selection == '5':
        pass

    #Exits program
    elif selection == '6':
        break

    #If user input not valid
    else:
        print('Please enter a valid input.')

    input('Use any key to return to menu')

print(store.customers)