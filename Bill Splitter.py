import random
def list_of_member(number):
    if number > 0:
        member = {}
        lucky = []
        print("Enter the name of every friend (including you), each on a new line:")
        for i in range(number):
            name = input()
            member[name] = 0
            lucky.append(name)
        bill = float(input("Enter the total bill value:\n"))
        Who_is_lucky = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
        if Who_is_lucky == "Yes":
            person = random.choice(lucky)
            print(f'{person} is the lucky one!')
            new = dict.fromkeys(member, round(bill / (number - 1), 2))
            new[person] = 0
            print(new)
        else:
            print("No one is going to be lucky")
            new1 = dict.fromkeys(member, round(bill / number, 2))
            print(new1)
    else:
        print("No one is joining for the party")
    return
number = int(input("Enter the number of friends joining (including you):\n"))
list_of_member(number)