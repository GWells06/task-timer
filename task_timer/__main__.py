"""
__main__.py
Grant Wells <gswells0206@gmail.com>
<The date in 2025-01-30 format>
 
<Short Description>
""" 

# Imports Here: 
import click
from interface import formatted_header
from user_input import welcome_to_task_timer
from user_input import user_task_choice
from user_input import task_interface


#from interface import welcome_to_task_timer()

@click.command()

def main():
    """This is my main cli."""

    # Top Header of Program
    formatted_header(header_message=" CLI TASK TIMER ")
    welcome_to_task_timer()
    task_interface()
    user_task_choice()
    # Welcome Section of the Program.
    

    click.echo("Hello World")
 
if __name__ == '__main__':
    main()