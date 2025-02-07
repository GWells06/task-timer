"""
__main__.py
Grant Wells <gswells0206@gmail.com>
<The date in 2025-01-30 format>
 
<Main file for the CLI Task Timer. Imports needed files and runs the program.>
""" 

# Imports Here: 
import click
from utils import formatted_header
from user_input import welcome_to_task_timer
from user_input import user_task_choice
from interface import task_interface

@click.command()

def main():
    """This is my main cli."""

    # Top Header of Program
    formatted_header(" 2077 CLI TASK TIMER ")

    # Tell the End-User How It Works
    welcome_to_task_timer()
    
    # Interface Housing Tasks
    task_interface()

    # Operate Based On User Choice
    user_task_choice()
 
if __name__ == '__main__':
    main()
