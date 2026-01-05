import json
import os
import utils
from colorama import Fore

USERS_PATH = "users.json"

if os.path.exists(USERS_PATH):
    with open(USERS_PATH, "r") as f:
        try:
            users = json.load(f)
        except json.JSONDecodeError:
            users = {}
else:
    users = {}

def auth_sign_up():
    os.system("clear")
    utils.show_title()
    signed_up = False
    print(Fore.CYAN + "\n" + "="*50)
    print(Fore.YELLOW + "           CREATE NEW ACCOUNT")
    print(Fore.CYAN + "="*50)
    while not signed_up:
        print(Fore.BLUE + "\n" + "-"*50)
        name = input(Fore.WHITE + "👤 Please enter your name: ").strip()
        email = input(Fore.WHITE + "📧 Please enter your email: ").lower().strip()
        if "@" not in email or "." not in email:
            print(Fore.RED + "\n❌ Invalid email format. Please try again.")
            continue
        if email in users:
            print(Fore.RED + "\n❌ This email already exists. Please use a different email.")
            return False
        print(Fore.BLUE + "-"*50)
        password = input(Fore.WHITE + "🔑 Enter your password: ").strip()
        confirm_pass = input(Fore.WHITE + "🔐 Confirm your password: ").strip()
        if password != confirm_pass:
            print(Fore.RED + "\n❌ Passwords do not match. Please try again.")
            continue
        users[email] = {"name": name, "password": password}
        with open(USERS_PATH, "w") as f:
            json.dump(users, f, indent=4)
        print(Fore.MAGENTA + "\n" + "☆"*50)
        print(Fore.GREEN + f"      Hello {name.capitalize()}, Welcome to")
        print(Fore.YELLOW + "             FIN-TRACK PLUS!")
        print(Fore.CYAN + "        Where Financial Clarity Begins")
        print(Fore.MAGENTA + "☆"*50)
        signed_up = True
    return signed_up

def auth_sign_in():
    os.system("clear")
    utils.show_title()
    print(Fore.CYAN + "\n" + "="*50)
    print(Fore.YELLOW + "               SIGN IN")
    print(Fore.CYAN + "="*50)
    email = input(Fore.WHITE + "📧 Please enter your email: ").lower().strip()
    password = input(Fore.WHITE + "🔑 Please enter your password: ").strip()
    if email in users and password == users[email]["password"]:
        print(Fore.GREEN + "\n" + "✓"*50)
        print(Fore.YELLOW + f"     Success! Welcome back, {users[email]['name'].capitalize()}!")
        print(Fore.GREEN + "✓"*50)

        user = users[email]          
        user["email"] = email  
        return user             
    else:
        print(Fore.RED + "\n" + "✗"*50)
        print(Fore.YELLOW + "     Wrong email or password. Please try again.")
        print(Fore.RED + "✗"*50)
        return None