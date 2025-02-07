"""
user_input.py
Grant Wells <gswells0206@gmail.com>
<The date in 2025-01-30 format>
 
< This file handles the user input logic for this CLI Task Timer program. It will mostly handle the logic that deals 
  with the what the user wants to do given their options from the task interface.>
"""

# Imports Here:
import time
from datetime import datetime
import click 
from utils import formatted_header
from colorama import init, Fore, Style

# initialize colorama.
init(autoreset=True)

active_tasks = {}
completed_tasks = []

def welcome_to_task_timer():
    """ Display a welcome message for end-user and explain how program works. """
    click.echo(Fore.CYAN + Style.BRIGHT + "\n// Welcome to Task Timer! // \n")
    time.sleep(1)
    click.echo(Fore.CYAN + Style.BRIGHT + "// This program will help you keep track of the time you spend on tasks. //\n")
    click.echo(Fore.CYAN + Style.BRIGHT + "// You will be able to start a task, end a task, and view a timesheet. //\n")
    time.sleep(5)
    continue_response = click.prompt(Fore.YELLOW+ "Would you like to proceed? (Press Enter to continue, or 'No' to exit)",default='',show_default=False)

    # Exit program if the user does not want to continue.
    if continue_response == 'no':
        click.echo(Fore.CYAN + Style.BRIGHT + "\n// Exiting Task Timer... //")
        exit()
    elif continue_response == '':
        time.sleep(3)
        click.echo(Fore.CYAN + Style.BRIGHT + "\n// Ok. Here's how it works. //")
    else:
        click.echo(Fore.MAGENTA + "\nInvalid Input, Try Again.\n")
    
    # Continue if the user wants to proceed. 
    #if continue_response == '':
        #time.sleep(1)
        #click.echo("\n// Ok. Here's how it works. //\n")

    time.sleep(2)
    click.echo(Fore.CYAN + Style.BRIGHT + "\n// You will, depending on what you would like, will enter what option via a number, like '1'. // \n")
    time.sleep(3)
    click.echo(Fore.CYAN + Style.BRIGHT + "// When you choose to add a task, you will be prompted to enter a name for the task. //\n")
    time.sleep(2)
    click.echo(Fore.CYAN + Style.BRIGHT + "// When you decide you are done with your task, you will enter the number associated with that, so '2' and //\n")
    click.echo(Fore.CYAN + Style.BRIGHT + "// then the program will ask for the name and then end your task. //\n")
    time.sleep(3)
    click.echo(Fore.CYAN + Style.BRIGHT + "// You also have the ability to add multiple tasks, just enter '1' and you will be able to enter another. //\n")
    time.sleep(2)

    continue_response = click.prompt(Fore.YELLOW + "Would you like to proceed? (Press Enter to continue, or 'No' to exit)",default='',show_default=False)

    # Exit program if the user does not want to continue.
    if continue_response == 'no':
        click.echo("Fore.CYAN + Style.BRIGHT + \n// Exiting Task Timer... //")
        exit()
    
    if continue_response == '':
        time.sleep(1)
        click.echo(Fore.CYAN + Style.BRIGHT + "\n// Ok. One Second. // \n")
        time.sleep(2)
    
def add_task():
    """ Start a new task and record its starting time. """

    get_task_name = click.prompt(Fore.YELLOW + "\nEnter a name for your task")
    click.echo(Fore.CYAN + Style.BRIGHT + "\n// Starting Task... //")
    time.sleep(2)
    click.echo(Fore.CYAN + Style.BRIGHT + "\n// Task Started //")
    time.sleep(1)

    # Rename to make it easier to use later.
    task_name = get_task_name

    if task_name in active_tasks:
        click.echo(Fore.MAGENTA + "\n// Whoops. Looks like you already have a task running with that name. ")
    else:
        active_tasks[task_name] = datetime.now()
        ## echo out name and time?? 

    return active_tasks

def end_task():
    """ End a current running task and record its time. """

    if not active_tasks:
        click.echo(Fore.CYAN + Style.BRIGHT + "// There are no current running tasks. //")
        return
    
    task_name = click.prompt(Fore.YELLOW + "\nEnter the task you would like to end")
    time.sleep(1)
    click.echo(Fore.CYAN + Style.BRIGHT + "\n// One moment. //")
    time.sleep(1.2)
    click.echo(Fore.CYAN + Style.BRIGHT + "\n// Task Ended. \n")

    # Pop the task out of the active tasks.
    starting_time = active_tasks.pop(task_name)

    ending_time = datetime.now()

    total_time = ending_time - starting_time
    completed_tasks.append((task_name, starting_time, ending_time, total_time))

    return completed_tasks

    ## Format the output here

def show_timesheet():
    """ Print the completed tasks with their total time. """

    if not completed_tasks:
        click.echo(Fore.CYAN + Style.BRIGHT + "\n// There are no tasks that have been completed yet. //\n")
    else:
        formatted_header(Fore.YELLOW + "Task Timesheet")
        for task in completed_tasks:
            click.echo(Fore.RED + f"\n{task[0]}: {task[1].strftime('%H:%M:%S')} - {task[2].strftime('%H:%M:%S')} (Duration: {task[3]})")

def show_current_task():
    """ Show the end-user the current running tasks. """

    if not active_tasks:
        click.echo(Fore.CYAN + Style.BRIGHT + "// There are no active tasks running. //")
    else:
        formatted_header(Fore.YELLOW + "Current Running Tasks")
        for task, start_time, in active_tasks.items():
            click.echo(Fore.RED + f"\n{task} started at {start_time.strftime('%H:%M:%S')}")

def user_task_choice():
    """ Handle user input logic for receiving Task Timer option from task_interface. """

    while True:
        user_choice = click.prompt(Fore.YELLOW + "\nChoose an option (1-5)", type=int)

        if user_choice == 1:
            add_task()
        elif user_choice == 2:
            end_task()
        elif user_choice == 3:
            show_current_task()
        elif user_choice == 4:
            show_timesheet()
        elif user_choice == 5:
            click.echo(Fore.CYAN + Style.BRIGHT + "\nExiting Task Timer...")
            time.sleep(2)
            exit()

        else:
            click.echo(Fore.RED + "\nInvalid Input, Try Again.")