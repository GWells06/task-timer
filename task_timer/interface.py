"""
interface.py
Grant Wells <gswells0206@gmail.com>
<The date in 2025-01-30 format>
 
<The file holds all the different interfaces that are used in this program. Interfaces like the main
 program title and the other headers used throughout the program.>
"""

# Imports Here:
import os
import time
import click

@click.command

def formatted_header(header_message):
    """ Create a formatted header function that is able to be used dynamically based on use case. """

    try:
        # Get the current terminal width using os module.
        term_width = os.get_terminal_size().columns

    # Running into error with terminal, this seems to help. 
    except OSError:
        term_width = 80 

    # Get the padding of the left and right sides. Subtract for borders.
    bord_padding = (term_width - len(header_message) - 2) // 2

    # Header Build
    border = "=" * term_width
    complete_header = " " * bord_padding + header_message + " " * bord_padding

    # Maintaining symmetry if the padding is odd.
    if len(complete_header) < term_width:
        complete_header += " " # Add extra space if needed. 

    click.echo(border)
    click.echo(complete_header)
    click.echo(border)

def task_interface():
    """ Formatted interface to show the user what the program can do. """

    formatted_header("CLI Task Timer")

    print(f"1. Start Task\n2. End Task\n3. Current Tasks\n4. View Timesheet\n5. Exit")
    
    ## This will call the user_task_choice() funtion.
    user_task_choice()


# Main Project/Title Header

# Task Selection Header/UI

# Timesheet UI (In timesheet?)

