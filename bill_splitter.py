import random
"""Hyperskill Bill-Splitter project implementation"""


def get_friends_list():
    """Constructs a dictionaries with friends present at the party.

    If the number of friends is lower or equal to zero, returns
    an empty list
    """
    friends = {}
    friends_count = int(input("Enter the number of friends joining (including you):"))
    if friends_count > 0:
        print("Enter the name of every friend (including you), each on a new line:")
        for i in range(0, friends_count):
            friends[input()] = 0
    return friends


def who_s_lucky(friends):
    """Get the name of the lucky friend."""
    lucky_one = None
    enable_lucky = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    if enable_lucky == "Yes":
        lucky_one = random.choice(list(friends.keys()))
        print(f"{lucky_one} is the lucky one!")
    else:
        print("No one is going to be lucky")
    return lucky_one


def split_bill(friends, total, shares_count):
    """Split the bill and assign the corresponding amount to each friend"""
    split_amount = round(total / shares_count, 2)
    for name, amount in friends.items():
        friends[name] = split_amount


def main():
    """Main program."""
    friends = get_friends_list()
    if len(friends) <= 0:
        print("No one is joining for the party")
    else:
        bill = float(input("Enter the total bill value:"))
        lucky_one = who_s_lucky(friends)
        if lucky_one is None:
            split_bill(friends, bill, len(friends))
        else:
            split_bill(friends, bill, len(friends) - 1)
            friends[lucky_one] = 0

        print(friends)

if __name__ == "__main__":
    main()
