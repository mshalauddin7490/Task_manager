import datetime
from uuid import uuid4

class Task():
    tasks = []

    def __init__(self, str):
        self.task = str
        self.create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.updated_time = 'NA'
        self.completed_time = 'NA'
        self.task_done = False
        self.id = uuid4()
        self.tasks.append(self)

    def update_task(self, x, str):
        i = 0
        for tsk in self.tasks:
            i += 1
            if (i == x):
                tsk.task = str
                tsk.updated_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            break

    def complete_task(self, x):
        i = 0
        for tsk in self.tasks:
            i += 1
            if (i == x):
                tsk.completed_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                tsk.task_done = True
            break

while (True):
    print('\n1. Add New Task')
    print('2. Show All Tasks')
    print('3. Show Incomplete Tasks')
    print('4. Show Completed Tasks')
    print('5. Update Task')
    print('6. Mark a Task Completed')
    try:
        a = int(input('\nEnter Option: '))

        if a == 1:
            str = input('\nEnter New Task: ')
            # code create new task
            myTask = Task(str)
            print('\nTask Created Successfully')

        elif a == 2:
            # code
            for task in myTask.tasks:
                print(f'\nID - {task.id}')
                print(f'Task - {task.task}')
                print(f'Created Time - {task.create_time}')
                print(f'Updated Time - {task.updated_time}')
                print(f'Completed - {task.task_done}')
                print(f'Completed Time- {task.completed_time}\n')
        elif a == 3:
            # show incomplete task
            inc_task = False
            for task in myTask.tasks:
                if task.task_done == False:
                    inc_task = True
                    print(f'\nID - {task.id}')
                    print(f'Task - {task.task}')
                    print(f'Created Time - {task.create_time}')
                    print(f'Updated Time - {task.updated_time}')
                    print(f'Completed - {task.task_done}')
                    print(f'Completed Time- {task.completed_time}\n')
            if not (inc_task):
                print('No Incomplete Task')
            # if all task completed print('No Incomplete Task')

        elif a == 4:
            for task in myTask.tasks:
                if task.task_done == True:
                    print(f'\nID - {task.id}')
                    print(f'Task - {task.task}')
                    print(f'Created Time - {task.create_time}')
                    print(f'Updated Time - {task.updated_time}')
                    print(f'Completed - {task.task_done}')
                    print(f'Completed Time- {task.completed_time}\n')

        elif a == 5:
            # check if there is any uncompleted task
            print('Select Which Task To Update')
            # code
            task_no = 1
            for task in myTask.tasks:
                if task.task_done == False:
                    print(f'\nTask No- {task_no}')
                    print(f'ID - {task.id}')
                    print(f'Task - {task.task}')
                    print(f'Created Time - {task.create_time}')
                    print(f'Updated Time - {task.updated_time}')
                    print(f'Completed - {task.task_done}')
                    print(f'Completed Time- {task.completed_time}\n')
                    task_no += 1
            x = int(input('Enter Task Number: '))
            str = input('Enter New Task: ')
            # code show all uncompleted task
            myTask.update_task(x, str)
            print('Task Updated Successfully')
        elif a == 6:
            print('Select Which Task To Complete')
            task_no = 1
            for task in myTask.tasks:
                if task.task_done == False:
                    print(f'\nTask No- {task_no}')
                    print(f'ID - {task.id}')
                    print(f'Task - {task.task}')
                    print(f'Created Time - {task.create_time}')
                    print(f'Updated Time - {task.updated_time}')
                    print(f'Completed - {task.task_done}')
                    print(f'Completed Time- {task.completed_time}\n')
                    task_no += 1
            # code show all uncomplited task

            y = int(input('Enter Task No: '))
            # code complete the task and delete it from list
            myTask.complete_task(y)
            print('\nTask Completed Successfully\n')

    except:
        print("Please enter a numeric value")
