# random package
import random

# fridge = ['Rice', 'Curry', 'Fried Chicken', 'Noodles', 'Burger', 'Chips']
class Food():
        fridge = input('Do you have food in your fridge? ')
        if fridge == "yes":
            # list of items in fridge
                print('List items that you have in your fridge, maximum of 5 items.')
                fridge_itm_1 = input('Item one: ').lower()
                fridge_itm_2 = input('Item two: ').lower()
                fridge_itm_3 = input('Item three: ').lower()
                fridge_itm_4 = input('Item four: ').lower()
                fridge_itm_5 = input('Item five: ').lower()
                # adding all of them up
                fridge = [fridge_itm_1, fridge_itm_2, fridge_itm_3, fridge_itm_4, fridge_itm_5]
                # creating a variable to randomize the items in your fridge
                random_fridge = random.choice(fridge)
                # result 
                print(f'Your reccomendation today: {random_fridge} ')
                       
        else:
            print('Come back next time! :)')

# remember to use random.choice instead of random.randrange