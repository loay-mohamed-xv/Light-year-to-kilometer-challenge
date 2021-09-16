import time

print("----------------------------------------\n")
time.sleep(1)


def light_year_to_kilometer_def():
    token = int(input("how many light year?\n>>"))
    light_year_to_kilometer = int(9460730472580)
    calc = token * light_year_to_kilometer
    print(f"{calc} kilometer")
    print('\n')
    time.sleep(0.6)


while True:
    print("{**MENU**}")
    time.sleep(1)
    print("1-* convert light year to kilometer")
    time.sleep(1)
    print("the rest of the program coming soon....\n")
    choice = input('>>')
    if choice == "1":
        light_year_to_kilometer_def()
    else:
        print('coming soon...')
