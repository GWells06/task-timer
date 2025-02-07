"""
interface.py
Grant Wells <gswells0206@gmail.com>
<The date in 2025-01-30 format>
 
<The file holds all the different interfaces that are used in this program. Interfaces like the main
 program title and the other headers used throughout the program.>
"""

# Imports Here:

from utils import formatted_header
import click
#from user_input import user_task_choice
from colorama import init, Fore, Style

init(autoreset=True)

def task_interface():
    """ Formatted interface to show the user what the program can do. """

    formatted_header(Fore.YELLOW + " TASK OPTIONS ")

    click.echo(Fore.CYAN + Style.BRIGHT + f"\n1. Start Task\n2. End Task\n3. Current Tasks\n4. View Timesheet\n5. Exit")

