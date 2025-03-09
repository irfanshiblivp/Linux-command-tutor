import json
import random
import os
import sys
import time
from termcolor import colored

# Load Linux commands from JSON
def load_commands():
    with open("commands.json", "r") as file:
        return json.load(file)

COMMANDS = load_commands()

# Fancy loading effect
def loading_animation(text="Loading", dots=3, duration=0.5):
    for _ in range(dots):
        print(colored(f"\r{text}{'.' * (_+1)}", "cyan"), end="")
        time.sleep(duration)
    print("\n")

# Beautified title
def print_title():
    os.system("clear")
    print(colored("════════════════════════════════════════", "green"))
    print(colored("🚀 WELCOME TO LINUX COMMAND TUTOR CLI 🚀", "yellow", attrs=["bold"]))
    print(colored("════════════════════════════════════════", "green"))

# Beautified footer (Watermark)
def print_footer():
    print(colored("\n════════════════════════════════════════", "green"))
    print(colored("🔥 Made with ❤️ by @irfanshiblivp 🔥", "blue", attrs=["bold"]))
    print(colored("════════════════════════════════════════", "green"))

# List all commands with numbering
def list_all_commands():
    print(colored("\n📜 AVAILABLE LINUX COMMANDS:", "blue", attrs=["bold"]))
    for index, cmd in enumerate(COMMANDS, start=1):
        print(colored(f"{index}. {cmd['name']} - {cmd['description']}", "green"))

# Show command details
def show_command_info(command_name):
    found = False
    for cmd in COMMANDS:
        if cmd["name"] == command_name:
            print(colored("\n════════════════════════════", "yellow"))
            print(colored(f"🔹 COMMAND: {cmd['name']}", "green", attrs=["bold"]))
            print(colored(f"📌 CATEGORY: {cmd['category']}", "blue"))
            print(colored(f"📜 DESCRIPTION: {cmd['description']}", "cyan"))
            print(colored("════════════════════════════", "yellow"))
            found = True
            break

    if not found:
        print(colored(f"❌ Command '{command_name}' not found!", "red"))

# Search for commands
def search_commands(keyword):
    print(colored(f"\n🔎 SEARCHING FOR '{keyword}'...\n", "blue"))
    results = [cmd for cmd in COMMANDS if keyword.lower() in cmd["name"]]

    if results:
        for index, cmd in enumerate(results, start=1):
            print(colored(f"{index}. {cmd['name']} - {cmd['description']}", "green"))
    else:
        print(colored("❌ No matching commands found!", "red"))

# Quiz mode
def quiz_mode():
    print(colored("\n🧠 QUIZ MODE: Identify the Command!", "yellow", attrs=["bold"]))
    
    command_info = random.choice(COMMANDS)  # Pick a random command
    command_name = command_info["name"]
    
    print(colored(f"📌 DESCRIPTION: {command_info['description']}", "cyan"))
    answer = input(colored("🔹 Your Answer: ", "yellow")).strip()

    if answer.lower() == command_name:
        print(colored("✅ Correct!", "green"))
    else:
        print(colored(f"❌ Incorrect! The correct command is: {command_name}", "red"))

# Practice mode
def practice_mode():
    print(colored("\n🎯 PRACTICE MODE: Try the Command!", "yellow", attrs=["bold"]))
    
    command_info = random.choice(COMMANDS)
    
    print(colored(f"📌 DESCRIPTION: {command_info['description']}", "cyan"))
    print(colored(f"💡 EXAMPLE: {command_info['name']}", "magenta"))
    
    user_input = input(colored("\n🔹 Type the command: ", "yellow")).strip()

    if user_input == command_info["name"]:
        print(colored("✅ Correct!", "green"))
    else:
        print(colored("❌ Incorrect! Try again.", "red"))

# Interactive CLI
def main():
    print_title()
    loading_animation("Starting up")

    while True:
        user_input = input(colored("\n🔹 Enter a Linux command (or 'exit'/'list'/'search [keyword]'/'quiz'/'practice'): ", "yellow")).strip()

        if user_input.lower() == "exit":
            print(colored("👋 Exiting... Happy Learning!", "cyan"))
            print_footer()
            sys.exit()
        elif user_input.lower() == "list":
            list_all_commands()
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
