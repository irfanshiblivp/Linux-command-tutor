import json
import random
import os
import sys
from termcolor import colored

# Load Linux commands from JSON
def load_commands():
    with open("commands.json", "r") as file:
        return json.load(file)

COMMANDS = load_commands()

# Display command details
def show_command_info(command):
    if command in COMMANDS:
        info = COMMANDS[command]
        print(colored(f"\n🔹 Command: {command}", "green", attrs=["bold"]))
        print(colored(f"📌 Description: {info['description']}", "cyan"))
        print(colored(f"📜 Usage: {info['usage']}", "yellow"))
        print(colored(f"💡 Example: {info['example']}", "magenta"))
    else:
        print(colored(f"❌ Command '{command}' not found!", "red"))

# Search for commands
def search_commands(keyword):
    print(colored(f"\n🔎 Searching for '{keyword}'...\n", "blue"))
    results = [cmd for cmd in COMMANDS if keyword in cmd]
    
    if results:
        for cmd in results:
            print(colored(f"👉 {cmd}: {COMMANDS[cmd]['description']}", "green"))
    else:
        print(colored("❌ No matching commands found!", "red"))

# Quiz mode
def quiz_mode():
    print(colored("\n🧠 QUIZ MODE: Identify the Command!", "yellow", attrs=["bold"]))
    command, details = random.choice(list(COMMANDS.items()))
    print(colored(f"📌 Description: {details['description']}", "cyan"))
    answer = input(colored("🔹 Your Answer: ", "yellow")).strip()

    if answer.lower() == command:
        print(colored("✅ Correct!", "green"))
    else:
        print(colored(f"❌ Incorrect! The correct command is: {command}", "red"))

# Practice mode
def practice_mode():
    print(colored("\n🎯 PRACTICE MODE: Try the Command!", "yellow", attrs=["bold"]))
    command, details = random.choice(list(COMMANDS.items()))
    print(colored(f"📌 Description: {details['description']}", "cyan"))
    print(colored(f"💡 Example: {details['example']}", "magenta"))
    
    user_input = input(colored("\n🔹 Type the command as shown: ", "yellow")).strip()

    if user_input == details['example']:
        print(colored("✅ Correct!", "green"))
    else:
        print(colored("❌ Incorrect! Try again.", "red"))

# Interactive CLI
def main():
    os.system("clear")
    print(colored("🚀 Linux Command Tutor CLI", "green", attrs=["bold", "underline"]))

    while True:
        user_input = input(colored("\n🔹 Enter a Linux command (or type 'exit'/'search [keyword]'/'quiz'/'practice'): ", "yellow")).strip()

        if user_input.lower() == "exit":
            print(colored("👋 Exiting... Happy Learning!", "cyan"))
            sys.exit()
        elif user_input.startswith("search "):
            keyword = user_input.split(" ", 1)[1]
            search_commands(keyword)
        elif user_input.lower() == "quiz":
            quiz_mode()
        elif user_input.lower() == "practice":
            practice_mode()
        else:
            show_command_info(user_input)

# Run the CLI
if __name__ == "__main__":
    main()
