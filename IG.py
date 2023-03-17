from instagrapi import Client
from colorama import Fore, init

import argparse
import time as T
import random

init(autoreset=True)

# GLOBAL VARS
bot = Client()
parser = argparse.ArgumentParser(description='Collect username, password and target to scrape all followers and follow them')
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
cyan = Fore.CYAN
reset = Fore.RESET
class cli:
    def banner():
        print(f"""{cyan}
            ──▄█████████████████████████▄──
            ▄█▀░█░█░█░░░░░░░░░░░░░░░░░░░▀█▄
            █░░░█░█░█░░░░░░░░░░░░░░█████░░█
            █░░░█░█░█░░░░░░░░░░░░░░█████░░█
            █░░░█░█░█░░░░░░░░░░░░░░█████░░█
            █░░░░░░░░░▄▄▄█████▄▄▄░░░░░░░░░█
            ███████████▀▀░░░░░▀▀███████████
            █░░░░░░░██░░▄█████▄░░██░░░░░░░█
            █░░░░░░░██░██▀░░░▀██░██░░░░░░░█
            █░░░░░░░██░██░░░░░██░██░░░░░░░█
            █░░░░░░░██░██▄░░░▄██░██░░░░░░░█
            █░░░░░░░██▄░▀█████▀░▄██░░░░░░░█
            █░░░░░░░░▀██▄▄░░░▄▄██▀░░░░░░░░█
            █░░░░░░░░░░▀▀█████▀▀░░░░░░░░░░█
            █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
            █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
            █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
            ▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀
            ──▀█████████████████████████▀──
""")
        print(f"\n\n{red} +---------- written by the best on earth ----------+ \n")

    def args():
        global args

        parser.add_argument('-u', '--user', type=str, required=True, help="Your username")
        parser.add_argument('-p', '--password', type=str, required=True, help="Your password")
        parser.add_argument('-t', '--target', type=str, required=True, help="User to scrape all followers")

        args = parser.parse_args()


class instaop:

    def follow():

        try:

            bot.login(username = args.user, password=args.password)
            print(f'{green}[+] Logged in')
            print(f'{green}[~] Fetching followers of target {red}@{args.target}{green}. This may take a while')
            id = bot.user_id_from_username(args.target)
            followers = bot.user_followers(id, amount= 0)
            follow_count = 0
            for follower in followers:
                for random_delay in random.sample(range(15, 60), 1):
                    user = bot.username_from_user_id(follower)
                    if user == args.user:
                        pass
                    else:
                        print(f'{cyan}[*] Delaying for: {random_delay}')
                        T.sleep(random_delay)
                        bot.user_follow(follower)
                        print(f'{green}[+] {user} followed')
                        follow_count += 1
                print(f'{green}[*] Done. {red}{follow_count}{RES} users have been followed')
        except Exception:
            print(f'{red}[!] Error')

if __name__ == "__main__":
    try:
        cli.banner()
        cli.args()
        instaop.follow()
    except KeyboardInterrupt:
        print(f"{red}\n[!] Pressed CTRL+C. Quitting\n")
