from python_learn.python_module_learn import python_module_learn

money=200

def add_money():
    global money
    money = money + 1
    print(money)

if __name__ == '__main__':
    add_money()
    python_module_learn.print_func("test")