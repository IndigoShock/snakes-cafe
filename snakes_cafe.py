from textwrap import dedent
import sys


WIDTH = 96
BANK = [
    { 
        'question' : 'What appetizer would you like to order?\n',
        'answer': 'hamburger' or 'cheeseburger' or 'lambburger' or 'cheesecake' or 'applepie' or 'taffy' or 'mozzarellasticks' or 'spinachartichokedip' or 'fries' or 'moscowmule' or 'doublemule' or 'undermule'
    }
        ]


def greeting():  
    print(dedent(f'''
    {'*'*36}\n 
    Welcome to the Snakes Cafe!\n To leave this restaurant at any time, type quit.\n Easy as that...unfortunately\n Here is the menu for tonight:\n
    {'*'*36}\n
    '''))


def ask_question(question):
    return input(question)


def check_input(user_in, item):
    if user_in.lower() == 'quit':
        exit()
        return

    if user_in.lower() == item['answer'].lower().replace(" ",""):
        return


def menu():
    print(dedent(f'''
    Appetizers:\n {'-'*10}\n Mozzarella Sticks\n Spinach Artichoke Dip\n Fries\n {'-'*10}\n
    Entrees:\n {'-'*10}\n Hamburger\n Cheeseburger\n Lamb Burger\n {'-'*10}\n
    Desserts:\n {'-'*10}\n Cheesecake\n Apple Pie\n Taffy\n {' '*10}
    Drinks:\n {'-'*10}\n Moscow Mule\n Double Mule\n Under Mule\n {' '*10}
    '''))


def run():
    greeting()
    menu()
    for item in BANK:
        while item != 0:
        user_in = ask_question(item['question'])


def exit():
    print(dedent('''
        Thanks for visiting the snakeriffic Snakes Cafe!
    '''))
    sys.exit()


if __name__ == '__main__':
    run()
    