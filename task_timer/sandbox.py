import os
import click
import time
from datetime import datetime
# Task-Timer Project UI + Welcome Messages


# List of what user may want to do


# Use dictionary to hold the users active tasks and a list to hold the completed tasks.
active_tasks = {}
completed_tasks = []
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

    print(border)
    print(complete_header)
    print(border)


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

#welcome_to_task_timer()

def task_interface(do_add_task):
    """ Formatted interface to show the user what the program can do. """

    formatted_header("CLI Task Timer")

    print(f"1. Start Task\n2. End Task\n3. Current Tasks\n4. View Timesheet\n5. Exit")
    
    ## This will call the user_task_choice() funtion.
    user_task_choice()
    return task_interface

task_interface()
    

### Adding A Task:

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

add_task()

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

end_task()
  

def show_timesheet():
    """ Print the completed tasks with their total time. """

    if not completed_tasks:
        click.echo("// There are no tasks that have been completed yet. //")
    else:
        formatted_header("Task Timesheet")
        for task in completed_tasks:
            print(f"{task[0]}: {task[1].strfttime('%H:%M:%S')} - {task[2].strfttime('%H:%M:%S')} (Duration: {task[3]})")

show_timesheet()

def show_current_task():
    """ Show the end-user the current running tasks. """

    if not active_tasks:
        click.echo("There are no active tasks running.")
    else:
        formatted_header("Current Running Tasks")
        for task, start_time, in active_tasks.items():
            print(f"{task} started at {start_time.strftime('%H:%M:%S')}")

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
