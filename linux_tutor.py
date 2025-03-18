import json
import random
import os
import sys
import time
import shutil
from termcolor import colored
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.align import Align

console = Console()

# Load Linux commands from JSON
def load_commands():
    with open("commands.json", "r") as file:
        return json.load(file)

COMMANDS = load_commands()

# Get terminal width for centering
def get_terminal_width():
    return shutil.get_terminal_size().columns

# Centered print function
def print_centered(text, color="white", bold=False):
    width = get_terminal_width()
    styled_text = colored(text, color, attrs=["bold"] if bold else [])
    print(styled_text.center(width))

# Fancy loading effect
def loading_animation(text="Loading"):
    width = get_terminal_width()
    for _ in range(3):
        for dots in [".  ", ".. ", "..."]:
            print(colored(f"\r{text}{dots}".center(width), "cyan"), end="")
            time.sleep(0.3)
    print("\n")

# Floating watermark
def show_watermark():
    width = get_terminal_width()
    watermark = colored("🔥 github @irfanshiblivp 🔥", "blue", attrs=["bold"])
    print("\n" + watermark.center(width) + "\n")

# Beautiful title screen
def print_title():
    os.system("clear")
    print_centered("════════════════════════════════════════", "green", True)
    print_centered("🚀 WELCOME TO LINUX COMMAND TUTOR CLI 🚀", "yellow", True)
    print_centered("════════════════════════════════════════", "green", True)
    show_watermark()

# List all commands with numbering
def list_all_commands():
    console.print(Panel("📜 [bold cyan]AVAILABLE LINUX COMMANDS:[/bold cyan]", expand=False))
    for index, cmd in enumerate(COMMANDS, start=1):
        console.print(f"[bold green]{index}. {cmd['name']}[/bold green] - {cmd['description']}")

# Show command details in a beautiful box
def show_command_info(command_name):
    found = False
    for cmd in COMMANDS:
        if cmd["name"] == command_name:
            command_panel = Panel(
                f"[bold green]🔹 COMMAND:[/bold green] {cmd['name']}\n"
                f"[bold blue]📌 CATEGORY:[/bold blue] {cmd['category']}\n"
                f"[bold cyan]📜 DESCRIPTION:[/bold cyan] {cmd['description']}",
                title="💻 Command Details",
                border_style="yellow"
            )
            console.print(command_panel)
            found = True
            break

    if not found:
        console.print(Panel(f"[red]❌ Command '{command_name}' not found![/red]", border_style="red"))

# Search for commands
def search_commands(keyword):
    console.print(Panel(f"🔎 [bold blue]SEARCHING FOR '{keyword}'...[/bold blue]", expand=False))
    results = [cmd for cmd in COMMANDS if keyword.lower() in cmd["name"]]

    if results:
        for index, cmd in enumerate(results, start=1):
            console.print(f"[bold green]{index}. {cmd['name']}[/bold green] - {cmd['description']}")
    else:
        console.print(Panel("[red]❌ No matching commands found![/red]", border_style="red"))

# Quiz mode
def quiz_mode():
    console.print(Panel("[bold yellow]🧠 QUIZ MODE: Identify the Command![/bold yellow]", expand=False))
    
    command_info = random.choice(COMMANDS)  # Pick a random command
    command_name = command_info["name"]
    
    console.print(f"[cyan]📌 DESCRIPTION:[/cyan] {command_info['description']}")
    answer = input(colored("🔹 Your Answer: ", "yellow")).strip()

    if answer.lower() == command_name:
        console.print(Panel("[green]✅ Correct![/green]", border_style="green"))
    else:
        console.print(Panel(f"[red]❌ Incorrect! The correct command is: {command_name}[/red]", border_style="red"))

# Practice mode
def practice_mode():
    console.print(Panel("[bold yellow]🎯 PRACTICE MODE: Try the Command![/bold yellow]", expand=False))
    
    command_info = random.choice(COMMANDS)
    
    console.print(f"[cyan]📌 DESCRIPTION:[/cyan] {command_info['description']}")
    console.print(f"[magenta]💡 EXAMPLE:[/magenta] {command_info['name']}")
    
    user_input = input(colored("\n🔹 Type the command: ", "yellow")).strip()

    if user_input == command_info["name"]:
        console.print(Panel("[green]✅ Correct![/green]", border_style="green"))
    else:
        console.print(Panel("[red]❌ Incorrect! Try again.[/red]", border_style="red"))

# Interactive CLI
def main():
    print_title()
    loading_animation("🚀 Starting up")

    while True:
        user_input = input(colored("\n🔹 Enter a Linux command (or 'exit'/'list'/'search [keyword]'/'quiz'/'practice'): ", "yellow")).strip()

        if user_input.lower() == "exit":
            console.print(Panel("[cyan]👋 Exiting... Happy Learning![/cyan]", border_style="cyan"))
            show_watermark()
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
