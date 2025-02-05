"""
timesheet.py
Grant Wells <gswells0206@gmail.com>
<The date in 2025-01-30 format>
 
<This file holds the timesheet logic. This involves the final timesheet and the current running tasks.>
"""

def show_timesheet():
    """ Print the completed tasks with their total time. """

    if not completed_tasks:
        click.echo("// There are no tasks that have been completed yet. //")
    else:
        formatted_header("Task Timesheet")
        for task in completed_tasks:
            print(f"{task[0]}: {task[1].strfttime('%H:%M:%S')} - {task[2].strfttime('%H:%M:%S')} (Duration: {task[3]})")

##show_timesheet()

def show_current_task():
    """ Show the end-user the current running tasks. """

    if not active_tasks:
        click.echo("There are no active tasks running.")
    else:
        formatted_header("Current Running Tasks")
        for task, start_time, in active_tasks.items():
            print(f"{task} started at {start_time.strftime('%H:%M:%S')}")