import json
import random
import os
import sys
import time
from termcolor import colored
from rich.console import Console
from rich.progress import track

console = Console()

# Load Linux commands from JSON
def load_commands():
    with open("commands.json", "r") as file:
        return json.load(file)

COMMANDS = load_commands()

# Animated loading effect
def loading_animation(text="🔄 Loading", duration=2):
    console.print(f"[cyan]{text}[/cyan]", end="")
    for _ in range(5):
        time.sleep(duration / 5)
        console.print("[cyan]•[/cyan]", end="", flush=True)
    print("\n")

# Fancy ASCII Title
def print_title():
    os.system("clear")
    console.print("[bold green]════════════════════════════════════════[/bold green]")
    console.print("[bold yellow]🚀 WELCOME TO LINUX COMMAND TUTOR CLI 🚀[/bold yellow]")
    console.print("[bold green]════════════════════════════════════════[/bold green]")
    console.print("[bold cyan]🔥 Made with ❤️ by @irfanshiblivp 🔥[/bold cyan]")

# List all commands with numbering (Scrollable)
def list_all_commands():
    console.print("\n📜 [bold blue]AVAILABLE LINUX COMMANDS:[/bold blue]")
    for index, cmd in enumerate(COMMANDS, start=1):
        time.sleep(0.05)  # Smooth scrolling effect
        console.print(f"[bold green]{index}. {cmd['name']}[/bold green] - {cmd['description']}")

# Show command details (Fancy Box)
def show_command_info(command_name):
    found = False
    for cmd in COMMANDS:
        if cmd["name"] == command_name:
            console.print("\n[bold yellow]════════════════════════════[/bold yellow]")
            console.print(f"[bold green]🔹 COMMAND:[/bold green] {cmd['name']}")
            console.print(f"[bold blue]📌 CATEGORY:[/bold blue] {cmd['category']}")
            console.print(f"[bold cyan]📜 DESCRIPTION:[/bold cyan] {cmd['description']}")
            console.print("[bold yellow]════════════════════════════[/bold yellow]")
            found = True
            break

    if not found:
        console.print(f"❌ [red]Command '{command_name}' not found![/red]")

# Search for commands
def search_commands(keyword):
    console.print(f"\n🔎 [bold blue]SEARCHING FOR '{keyword}'...[/bold blue]\n")
    results = [cmd for cmd in COMMANDS if keyword.lower() in cmd["name"]]

    if results:
        for index, cmd in enumerate(results, start=1):
            console.print(f"[bold green]{index}. {cmd['name']}[/bold green] - {cmd['description']}")
    else:
        console.print("[red]❌ No matching commands found![/red]")

# Quiz mode (With progress bar)
def quiz_mode():
    console.print("\n🧠 [bold yellow]QUIZ MODE: Identify the Command![/bold yellow]")

    command_info = random.choice(COMMANDS)
    command_name = command_info["name"]
    
    console.print(f"📌 [cyan]DESCRIPTION:[/cyan] {command_info['description']}")
    answer = console.input("[bold yellow]🔹 Your Answer: [/bold yellow]").strip()

    for step in track(range(10), description="[green]Checking your answer...[/green]"):
        time.sleep(0.1)  # Fake processing delay

    if answer.lower() == command_name:
        console.print("[bold green]✅ Correct![/bold green]")
    else:
        console.print(f"[bold red]❌ Incorrect! The correct command is: {command_name}[/bold red]")

# Practice mode (Typing effect)
def practice_mode():
    console.print("\n🎯 [bold yellow]PRACTICE MODE: Try the Command![/bold yellow]")

    command_info = random.choice(COMMANDS)
    
    console.print(f"📌 [cyan]DESCRIPTION:[/cyan] {command_info['description']}")
    console.print(f"💡 [magenta]EXAMPLE:[/magenta] {command_info['name']}")
    
    user_input = console.input("\n[bold yellow]🔹 Type the command: [/bold yellow]").strip()

    loading_animation("Checking input")

    if user_input == command_info["name"]:
        console.print("[bold green]✅ Correct![/bold green]")
    else:
        console.print("[bold red]❌ Incorrect! Try again.[/bold red]")

# Interactive CLI
def main():
    print_title()
    loading_animation("Starting up")

    while True:
        user_input = console.input("\n[bold yellow]🔹 Enter a Linux command (or 'exit'/'list'/'search [keyword]'/'quiz'/'practice'): [/bold yellow]").strip()

        if user_input.lower() == "exit":
            console.print("[bold cyan]👋 Exiting... Happy Learning![/bold cyan]")
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
