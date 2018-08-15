from textwrap import dedent
import sys
import uuid


'''totals at the top as global variables for easier access. helps with scoping'''
SUBTOTAL = float(0)
TAX = float(SUBTOTAL * 0.101)
TOTAL = float(SUBTOTAL + TAX)
CATEGORIES = ['entrees', 'appetizers', 'desserts', 'sides', 'drinks']

WIDTH = 96
BANK = [
    {
        'question' : 'What would you like to order?\n',
        'answer': 'hamburger',
        'status': False
    }
    {
    'category': 'entrees',
    'name': 'Hamburger',
    'item': 'hamburger',
    'amount': 1,
    'price': 9.00,
    'quantity': 0,
    },
    {
    'category': 'entrees',
    'name': 'Cheese burger',
    'item': 'cheeseburger',
    'amount': 1,
    'price': 10.00,
    'quantity': 0,
    },
    {
    'category': 'entrees',
    'name': 'Salmon Burger',
    'item': 'salmonburger',
    'amount': 1,
    'price': 20.00,
    'quantity': 0,
    },
    {
    'category': 'entrees',
    'name': 'Lamb Burger',
    'item': 'lambburger',
    'amount': 1,
    'price': 10.00,
    'quantity': 0,
    },
    {
    'category': 'entrees',
    'name': 'Garden Burger',
    'item': 'gardenburger',
    'amount': 1,
    'price': 8.00,
    'quantity': 0,
    },
    {
    'category': 'entrees',
    'name': 'Burger burger',
    'item': 'burgerburger',
    'amount': 1,
    'price': 18.00,
    'quantity': 0,
    },
    {
    'category': 'entrees',
    'name': 'Nasty Patty',
    'item': 'nastypatty',
    'amount': 1,
    'price': 5.00,
    'quantity': 0,
    },
    {
    'category': 'entrees',
    'name': 'Krabby Patty',
    'item': 'krabbypatty',
    'amount': 1,
    'price': 10.00,
    'quantity': 0,
    },
    {
    'category': 'entrees',
    'name': 'Ratty Patty',
    'item': 'rattypatty',
    'amount': 1,
    'price': 7.00,
    'quantity': 0,
    },
    {
    'category': 'appetizers',
    'name': 'Mozzarella Sticks',
    'item': 'mozzarellasticks',
    'amount': 1,
    'price': 4.00,
    'quantity': 0,
    },
    {
    'category': 'appetizers',
    'name': 'Spinach Artichoke Dip',
    'item': 'spinachartichokedip',
    'amount': 1,
    'price': 7.00,
    'quantity': 0,
    },
    {
    'category': 'appetizers',
    'name': 'Fries',
    'item': 'fries',
    'amount': 1,
    'price': 3.00,
    'quantity': 0,
    },
    {
    'category': 'appetizers',
    'name': 'Poutine',
    'item': 'poutine',
    'amount': 1,
    'price': 5.00,
    'quantity': 0,
    },
    {
    'category': 'appetizers',
    'name': 'Nachos',
    'item': 'nachos',
    'amount': 1,
    'price': 9.00,
    'quantity': 0,
    },
    {
    'category': 'appetizers',
    'name': 'Wontons',
    'item': 'wontons',
    'amount': 1,
    'price': 5.00,
    'quantity': 0,
    },
    {
    'category': 'appetizers',
    'name': 'Fried Egg',
    'item': 'friedegg',
    'amount': 1,
    'price': 3.00,
    'quantity': 0,
    },
    {
    'category': 'appetizers',
    'name': 'Circular Pancake',
    'item': 'circularpancake',
    'amount': 1,
    'price': 2.00,
    'quantity': 0,
    },
    {
    'category': 'appetizers',
    'name': 'PanCupcakes',
    'item': 'pancupcakes',
    'amount': 1,
    'price': 3.00,
    'quantity': 0,
    },
    {
    'category': 'desserts',
    'name': 'Cheesecake'
    'item': 'cheesecake',
    'amount': 1,
    'price': 6.00,
    'quantity': 0,
    },
    {
    'category': 'desserts',
    'name': 'Apple Pie',
    'item': 'applepie',
    'amount': 1,
    'price': 5.00,
    'quantity': 0,
    },
    {
    'category': 'desserts',
    'name': 'Taffy',
    'item': 'taffy',
    'amount': 1,
    'price': 3.00,
    'quantity': 0,
    },
    {
    'category': 'desserts',
    'name': 'Laffy Taffy',
    'item': 'laffytaffy',
    'amount': 1,
    'price': 4.00,
    'quantity': 0,
    },
    {
    'category': 'desserts',
    'name': 'Craapy Taffy',
    'item': 'Crappy Taffy',
    'amount': 1,
    'price': 2.00,
    'quantity': 0,
    },
    {
    'category': 'desserts',
    'name': 'Loopy Taffy',
    'item': 'loopytaffy',
    'amount': 1,
    'price': 4.00,
    'quantity': 0,
    },
    {
    'category': 'desserts',
    'name': 'Droopy Taffy',
    'item': 'droopytaffy',
    'amount': 1,
    'price': 4.00,
    'quantity': 0,
    },
    {
    'category': 'desserts',
    'name': 'Sappy Taffy',
    'item': 'sappytaffy',
    'amount': 1,
    'price': 5.00,
    'quantity': 0,
    },
    {
    'category': 'desserts',
    'name': 'Bananas Foster',
    'item': 'bananasfoster',
    'amount': 1,
    'price': 5.00,
    'quantity': 0,
    },
    {
    'category': 'sides',
    'name': 'Side Salad',
    'item': 'sidesalad',
    'amount': 1,
    'price': 3.00,
    'quantity': 0,
    },
    {
    'category': 'sides',
    'name': 'Side Fries',
    'item': 'sidefries',
    'amount': 1,
    'price': 5.00,
    'quantity': 0,
    },
    {
    'category': 'sides',
    'name': 'Baked Potato',
    'item': 'bakedpotato',
    'amount': 1,
    'price': 3.00,
    'quantity': 0,
    },
    {
    'category': 'sides',
    'name': 'Snaked Potato',
    'item': 'snakedpotato',
    'amount': 1,
    'price': 3.00,
    'quantity': 0,
    },
    {
    'category': 'sides',
    'name': 'Jacked Potato',
    'item': 'jackedpotato',
    'amount': 1,
    'price': 3.00,
    'quantity': 0,
    },
    {
    'category': 'sides',
    'name': 'Troubled Potato',
    'item': 'troubledpotato',
    'amount': 1,
    'price': 2.00,
    'quantity': 0,
    },
    {
    'category': 'sides',
    'name': 'Uncooked Potato',
    'item': 'uncookedpotato',
    'amount': 1,
    'price': 3.00,
    'quantity': 0,
    },
    {
    'category': 'sides',
    'name': 'Buffalo Potato'
    'item': 'buffalopotato',
    'amount': 1,
    'price': 3.00,
    'quantity': 0,
    },
    {
    'category': 'sides',
    'name': 'Billed Potato'
    'item': 'billedpotato',
    'amount': 1,
    'price': 3.00,
    'quantity': 0,
    },
    {
    'category': 'drinks',
    'name': 'Moscow Mule'
    'item': 'moscowmule',
    'amount': 1,
    'price': 6.00,
    'quantity': 0,
    },
    {
    'category': 'drinks',
    'name': 'Under Mule'
    'item': 'undermule',
    'amount': 1,
    'price': 3.00,
    'quantity': 0,
    },
    {
    'category': 'drinks',
    'name': 'Double Mule'
    'item': 'doublemule',
    'amount': 1,
    'price': 12.00,
    'quantity': 0,
    },
    {
    'category': 'drinks',
    'name': 'Mulled Mule'
    'item': 'mulledmule',
    'amount': 1,
    'price': 5.00,
    'quantity': 0,
    },
    {
    'category': 'drinks',
    'name': 'Some Mule'
    'item': 'somemule',
    'amount': 1,
    'price': 5.00,
    'quantity': 0,
    },
    {
    'category': 'drinks',
    'name': 'Muddled Mule'
    'item': 'muddledmule',
    'amount': 1,
    'price': 5.00,
    'quantity': 0,
    },
    {
    'category': 'drinks',
    'name': 'Appletini'
    'item': 'appletini',
    'amount': 1,
    'price': 6.00,
    'quantity': 0,
    },
    {
    'category': 'drinks',
    'name': 'Martini'
    'item': 'martini',
    'amount': 1,
    'price': 5.00,
    'quantity': 0,
    },
    {
    'category': 'drinks',
    'name': 'Gin And Tonic'
    'item': 'ginandtonic',
    'amount': 1,
    'price': 5.00,
    'quantity': 0,
    }
        ]


def menu():
    for x in DRINKS:
        '''this round() is not changing to the 2nd or 3rd decimals place. not sure why'''
        print (x,':',round(DRINKS[x],3))
    print('-'*10)
    for x in ENTREES:
        print (x,':',ENTREES[x])
    print('-'*10)
    for x in APPETIZERS:
        print (x,':',APPETIZERS[x])
    print('-'*10)
    for x in DESSERTS:
        print (x,':',DESSERTS[x])
    print('-'*10)
    for x in SIDES:
        print (x,':',SIDES[x])
    print('-'*10)
    ordering_process()


def greeting():
    print(dedent(f'''
    {'*'*36}\n
    Welcome to the Snakes Cafe!\n To leave this restaurant at any time, type quit.\n Easy as that...unfortunately\n Here is the menu for tonight. You can type in 'menu' again if you would like to see the menu. Or type in any of the categories if you would like to see those specific items:\n
    {'*'*36}\n
    '''))


def ask_question(question):
    return input(question)


def check_input(user_in, item):
    if user_in.lower().replace(' ', '') == 'quit':
        exit()
        return

    if user_in.lower().replace(' ','') == item['answer'].lower().replace(' ',''):
        item['status'] is True
        feedback(status)
        ordering_process()

    if user_in.lower() == 'quantity':
        order_total()
        ordering_process()

    if user_in.lower() == 'menu':
        menu()
        ordering_process()

    if user_in.lower() == 'drinks':
        for x in DRINKS:
            print(x,':',DRINKS[x])
        ordering_process()

    if user_in.lower() == 'entrees':
        for x in ENTREES:
            print (x,':',ENTREES[x])
        ordering_process()

    if user_in.lower() == 'appetizers':
        for x in APPETIZERS:
            print (x,':',APPETIZERS[x])
        ordering_process()

    if user_in.lower() == 'entrees':
        for x in ENTREES:
            print (x,':',ENTREES[x])
        ordering_process()

    if user_in.lower() == 'desserts':
        for x in DESSERTS:
            print (x,':',DESSERTS[x])
        ordering_process()

    if user_in.lower() == 'sides':
        for x in SIDES:
            print (x,':',SIDES[x])
        ordering_process()


def feedback(status):
    if status is True:
        print(dedent(f'''
            You ordered a {user_in}!\n
        '''))
        ordering_process()

    else:
        print(dedent('''
            Sorry, I do not understand. Do you mind repeating your order?\n
        '''))


# def customer_order(user_in, items, price):
    # user_in
    # items
    # price


def exit():
    print(dedent('''
        Thanks for visiting the snakeriffic Snakes Cafe!
    '''))
    sys.exit()


def order_total():
    print(dedent(f'''
    {'*' * 36}
        The Snakes Cafe
        "Eatability Counts"

        Order #{uuid.uuid4()}
        {'='*36}

        # {customer_order.items}           {customer_order.price}

    {'-'*18}

        {SUBTOTAL}
        {TAX}
        {'-'*12}
        {TOTAL}
    {'*' * 36}
    '''))
    ordering_process()


def ordering_process():
    for item in BANK:
        while item['status'] is False:
            user_in = ask_question(item['question'])
            status = check_input(user_in, item)
            feedback(status)
            item['status'] is False


def run():
    greeting()
    menu()


if __name__ == '__main__':
    run()
