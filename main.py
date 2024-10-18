import random
import string
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)


def generate_promo():
    # Generates a random promo code with the given format
    characters = string.ascii_letters + string.digits  # a-z, A-Z, 0-9
    random_code = ''.join(random.choices(characters, k=22))
    return f"https://promos.discord.gg/7T{random_code}"


def save_promos_to_file(promos):
    # Save promo links to promos.txt
    with open('promos.txt', 'a') as file:
        for promo in promos:
            file.write(promo + '\n')


def promo_gen():
    print(f"{Fore.CYAN}Promo Gen by mekambesik__{Style.RESET_ALL}")

    while True:
        try:
            # Asking the user how many promo links to generate
            num_promos = int(
                input(
                    f"{Fore.MAGENTA}How many promos do you want to generate? {Style.RESET_ALL}"
                ))

            # Generating the requested number of promo links
            promos = [generate_promo() for _ in range(num_promos)]
            save_promos_to_file(promos)

            # Success message
            print(
                f"{Fore.GREEN}Successfully saved {num_promos} promo(s) to promos.txt{Style.RESET_ALL}"
            )

            # Asking if the user wants to generate more
            another_round = input(
                f"{Fore.YELLOW}Do you want to generate more promos? (yes/no): {Style.RESET_ALL}"
            ).strip().lower()

            if another_round != 'yes':
                print(
                    f"{Fore.CYAN}Thank you for using Promo Gen!{Style.RESET_ALL}"
                )
                break  # Exit if the user doesn't want to continue
        except ValueError:
            print(
                f"{Fore.RED}Invalid input, please enter a valid number.{Style.RESET_ALL}"
            )


# Running the promo generator function
promo_gen()
