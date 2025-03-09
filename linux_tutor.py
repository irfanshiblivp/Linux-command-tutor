import json
import random
import os
import sys
from termcolor import colored

# Load Linux commands from JSON
def load_commands():
    try:
        with open("commands.json", "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(colored("Error: commands.json not found.  Make sure it's in the same directory.", "red"))
        sys.exit(1)  # Exit the program if the file isn't found
    except json.JSONDecodeError:
        print(colored("Error: commands.json is not a valid JSON file.", "red"))
        sys.exit(1) # Exit if the JSON is invalid
    except Exception as e:
        print(colored(f"An unexpected error occurred: {e}", "red")) # Generic error
        sys.exit(1)

COMMANDS = load_commands()

# Display command details
def show_command_info(command):
    if command in COMMANDS:
        info = COMMANDS[command]
        print(colored(f"\n🔹 Command: {command}", "green", attrs=["bold"]))
        print(colored(f"📌 Description: {info.get('description', 'No description available')}", "cyan"))
        print(colored(f"📜 Usage: {info.get('usage', 'No usage information available')}", "yellow"))
        print(colored(f"💡 Example: {info.get('example', 'No example available')}", "magenta"))
    else:
        print(colored(f"❌ Command '{command}' not found!", "red"))

# Search for commands
def search_commands(keyword):
    print(colored(f"\n🔎 Searching for '{keyword}'...\n", "blue"))
    results = [cmd for cmd in COMMANDS if keyword in cmd.lower()]  # Lowercase for case-insensitive search
    if results:
        for cmd in results:
            info = COMMANDS[cmd]  # Access the dictionary using the command name
            print(colored(f"👉 {cmd}: {info.get('description', 'No description available')}", "green"))  # Use .get() for safety
    else:
        print(colored("❌ No matching commands found!", "red"))

# Quiz mode
def quiz_mode():
    print(colored("\n🧠 QUIZ MODE: Identify the Command!", "yellow", attrs=["bold"]))
    if not COMMANDS:
        print(colored("❌ No commands loaded. Please check commands.json.", "red"))
        return

    command = random.choice(list(COMMANDS.keys())) # Get a random *key* (command name)
    details = COMMANDS[command] # Access the details using the command name

    print(colored(f"📌 Description: {details.get('description', 'No description available')}", "cyan")) # Safely access 'description'
    answer = input(colored("🔹 Your Answer: ", "yellow")).strip()

    if answer.lower() == command.lower():  # Compare in lowercase
        print(colored("✅ Correct!", "green"))
    else:
        print(colored(f"❌ Incorrect! The correct command is: {command}", "red"))


# Practice mode
def practice_mode():
    print(colored("\n🎯 PRACTICE MODE: Try the Command!", "yellow", attrs=["bold"]))
    if not COMMANDS:
        print(colored("❌ No commands loaded. Please check commands.json.", "red"))
        return

    command = random.choice(list(COMMANDS.keys()))  # Get a random command name
    details = COMMANDS[command]

    print(colored(f"📌 Description: {details.get('description', 'No description available')}", "cyan"))  # Safe access
    print(colored(f"💡 Example: {details.get('example', 'No example available')}", "magenta"))  # Safe access

    user_input = input(colored("\n🔹 Type the command as shown: ", "yellow")).strip()

    if user_input == details.get('example', ''): # Compare with example, or empty string if no example
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
