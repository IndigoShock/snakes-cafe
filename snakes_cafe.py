from textwrap import dedent
import sys


WIDTH = 96
BANK = [
    { 
        'question' : 'What food would you like to order?\n',
        'answer': 'hamburger' or 'cheeseburger' or 'lambburger' or 'cheesecake' or 'applepie' or 'taffy' or 'mozzarellasticks' or 'spinachartichokedip' or 'fries' or 'moscowmule' or 'doublemule' or 'undermule',
        'status': False
    }
        ]


def menu():
    print(dedent(f'''
    Appetizers:\n {'-'*10}\n Mozzarella Sticks\n Spinach Artichoke Dip\n Fries\n {'-'*10}\n
    Entrees:\n {'-'*10}\n Hamburger\n Cheeseburger\n Lamb Burger\n {'-'*10}\n
    Desserts:\n {'-'*10}\n Cheesecake\n Apple Pie\n Taffy\n {' '*10}
    Drinks:\n {'-'*10}\n Moscow Mule\n Double Mule\n Under Mule\n {' '*10}
    '''))


def greeting():  
    print(dedent(f'''
    {'*'*36}\n 
    Welcome to the Snakes Cafe!\n To leave this restaurant at any time, type quit.\n Easy as that...unfortunately\n Here is the menu for tonight:\n
    {'*'*36}\n
    '''))


def ask_question(question):
    return input(question)


def check_input(user_in, item):
    if user_in.lower().replace(" ", "") == 'quit':
        exit()
        return

    if user_in.lower().replace(" ","") == item['answer'].lower().replace(" ",""):
        item['status'] = True
        return True


def feedback(status):
    if status is True:
        print(dedent(f'''
            You ordered a food item! I'll bring it out right away.\n
        '''))
        ordering_process()

    else: 
        print(dedent('''
            Sorry, I do not understand. Do you mind repeating your order?\n
        '''))


def exit():
    print(dedent('''
        Thanks for visiting the snakeriffic Snakes Cafe!
    '''))
    sys.exit()


def run():
    greeting()
    menu()
    ordering_process()


def ordering_process():
    for item in BANK:
        while item['status'] is False:
            user_in = ask_question(item['question'])
            status = check_input(user_in, item)
            feedback(status)


if __name__ == '__main__':
    run()

