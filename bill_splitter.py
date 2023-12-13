"""Hyperskill Bill-Splitter project implementation"""


def main():
    """Main program."""
    friends_count = int(input("Enter the number of friends joining (including you):"))
    if friends_count <= 0:
        print("No one is joining for the party")
    else:
        friends = {}
        print("Enter the name of every friend (including you), each on a new line:")
        for i in range(0, friends_count):
            friends[input()] = 0
        print(friends)


if __name__ == "__main__":
    main()