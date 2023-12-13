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


def split_bill(friends):
    """Compute de bill's fraction for each friend and update the dictionary."""
    bill = float(input("Enter the total bill value:"))
    split_amount = round(bill / len(friends), 2)
    for name, amount in friends.items():
        friends[name] = split_amount


def main():
    """Main program."""
    friends = get_friends_list()
    if len(friends) <= 0:
        print("No one is joining for the party")
    else:
        split_bill(friends)
        print(friends)


if __name__ == "__main__":
    main()
