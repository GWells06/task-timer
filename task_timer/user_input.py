"""
user_input.py
Grant Wells <gswells0206@gmail.com>
<The date in 2025-01-30 format>
 
< This file handles the user input logic for this CLI Task Timer program. It will mostly handle the logic that deals 
  with the what the user wants to do given their options from the task interface.>
"""

# Imports Here:
from timesheet import show_timesheet
from timesheet import show_current_task
import time
from datetime import datetime
import click 

def welcome_to_task_timer():
    """ Display a welcome message for end-user and explain how program works. """
    click.echo("\n// Welcome to Task Timer! // \n")
    time.sleep(1)
    click.echo("// This program will help you keep track of the time you spend on tasks. //\n")
    click.echo("// You will be able to start a task, end a task, and view a timesheet. //\n")
    time.sleep(3)
    continue_response = click.prompt("Would you like to proceed? (Press Enter to continue, or 'No' to exit)")

    # Exit program if the user does not want to continue.
    if continue_response == 'no':
        click.echo("\n// Exiting Task Timer... //")
        exit()
    
    # Continue if the user wants to proceed. 
    if continue_response == '':
        time.sleep(1)
        click.echo("\n// Ok. Here's how it works. //\n")

    time.sleep(1)
    click.echo("// You will, depending on what you would like, will enter what option via a string, or phrase, like 'Add Task'. // \n")
    time.sleep(0.7)
    click.echo("// You then will be prompted to enter a name for your task. //\n")
    time.sleep(0.5)
    click.echo("// When you decide you are done with your task, you will say 'End' in //\n")
    click.echo("// which the program will ask for the name and then end your task.    //\n")
    time.sleep(0.5)

    continue_response = click.prompt("Would you like to proceed? (Press Enter to continue, or 'No' to exit)",default='',show_default=False)

    # Exit program if the user does not want to continue.
    if continue_response == 'no':
        click.echo("\n// Exiting Task Timer... //")
        exit()
    
    if continue_response == '':
        time.sleep(1)
        click.echo("\nOk.\n")
    
def add_task():
    """ Start a new task and record its starting time. """

    ### Add User Experience Here

    get_task_name = click.prompt("Enter a name for your task")

    # Rename to make it easier to use later.
    task_name = get_task_name

    if task_name in active_tasks:
        click.echo("// You already have a task running with that name. //")
    else:
        active_tasks[task_name] = datetime.now()
        ## echo out name and time?? 

    return add_task

#add_task()

def end_task():
    """ End a current running task and record its time. """

    if not active_tasks:
        click.echo("// There are no current running tasks. //")
        return
    
    task_name = click.prompt("Enter the task you would like to end")

    # Pop the task out of the active tasks.
    starting_time = active_tasks.pop(task_name)

    ending_time = datetime.now()

    total_time = ending_time - starting_time
    completed_tasks.append((task_name, starting_time, ending_time, total_time))

    ## Format the output here

def user_task_choice():
    """ Handle user input logic for receiving Task Timer option from task_interface. """

    while True:
        user_choice = click.prompt("Choose an option (1-5)", type=int)

        if user_choice == 1:
            add_task()
        elif user_choice == 2:
            end_task()
        elif user_choice == 3:
            show_timesheet()
        elif user_choice == 4:
            show_current_task()
        elif user_choice == 5:
            break

        else:
            click.echo("Invalid Input, Try Again.")

        return user_choice
