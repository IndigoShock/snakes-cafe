from textwrap import dedent
import sys

SUBTOTAL = 0
TAX = SUBTOTAL * 0.101
TOTAL = (SUBTOTAL + TAX)

WIDTH = 96
BANK = [
    {
        'question' : 'What food would you like to order?\n',
        'answer': 'hamburger',
        'status': False
    }
        ]


ENTREES = {
    'Hamburger' : 6.00,
    'Cheeseburger' : 9.00,
    'Lamb Burger' : 10.00,
    'Garden Burger' : 10.00,
    'Salmon burger' : 20.00,
    'Burger burger' : 10.00
}


APPETIZERS = {
    'Mozzarella Sticks' : 4.00,
    'Spinach Artichoke Dip' : 5.00,
    'Fries' : 5.00,
    'Poutine' : 5.00,
    'Nachos' : 5.00,
    'Wontons' : 3.00
}


DESSERTS = {
    'Cheesecake' : 5.00,
    'Apple Pie' : 5.00,
    'Taffy' : 3.00,
    'LaffyTaffy' : 3.00,
    'CrappyTaffy' : 3.00,
    'DroopyTaffy' : 3.00
}


SIDES = {
    'Side Salad' : 3.00,
    'Side Fries' : 3.00,
    'Baked Potato' : 3.00,
    'Snaked Potato' : 3.00,
    'Troubled Potato' : 2.00,
    'Uncooked Potato' : 3.00
}

DRINKS = {
    'Moscow Mule' : 6.00,
    'Double Mule' : 12.00,
    'Under Mule' : 3.00,
    'Mulled Mule' : 7.00,
    'Some Mule' : 5.00,
    'Muddled Mule' : 5.00
}


def menu():
    for x in DRINKS:
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


def greeting():
    print(dedent(f'''
    {'*'*36}\n
    Welcome to the Snakes Cafe!\n To leave this restaurant at any time, type quit.\n Easy as that...unfortunately\n Here is the menu for tonight:\n
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

    if user_in == 'order':
        order_total()
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


# def customer_order(user_in):
#     user_in


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

        Order #{uuid4()}
        {'='*36}

        # {customer_order[x]}           {customer_order[y]}

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


def run():
    greeting()
    menu()
    ordering_process()


if __name__ == '__main__':
    run()
