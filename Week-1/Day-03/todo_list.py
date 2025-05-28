'''
File Based

Design a simple to-do list app where users can add, remove, and view tasks.
Tasks are saved to a text file, allowing persistence between sessions.
'''

def create_todo_list():
    user_input =  input("Name of the todos: ")

    file_path = user_input + '.txt'
    open(file_path, 'a').close()
    return file_path


def add_todo_list(file_path):
    user_input = input("Enter todo: ")

    with open(file_path, 'r+') as file:
        lines = file.readlines()
        file.write(str(len(lines) + 1) + '.' + ' ' + user_input + '\n')

def remove_todo_list(file_path):
    view_todo_list(file_path)
    remove_todo = input("Enter the number of the todo that you want to remove: ")

    with open(file_path, 'r') as file:
        lines = file.readlines()

    update_lines = []
    removed = False

    for line in lines:
        if not line.startswith(f"{remove_todo}."):
            update_lines.append(line)
        else:
            removed = True

    renumbered_lines = []
    for i, line in enumerate(update_lines):
        parts = line.split('. ',  1)
        if len(parts) > 1:
            renumbered_lines.append(f"{i + 1}. {parts[1]}")
        else:
            renumbered_lines.append(line)

    with open(file_path, 'w') as file:
        file.writelines(renumbered_lines)

    if removed:
        print(f"Todo #{remove_todo} has been removed.")
    else:
        pritn(f"No todo with number {remove_todo} found.")

def view_todo_list(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            if content.strip():
                print("\nYour TODOs:")
                print(content)
            else:
                print("\nYUour todo list is empty.")
    except FileNotFoundError:
        print(f'Todo list file not found.')

def main():
    print('Welcome to a simple TODO List App!!!\n')
    file_path = create_todo_list()

    while True:
        print("\nWhat would you like to do?")
        print("1. Add a todo")
        print("2. Remove a todo")
        print("3. View todos")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_todo_list(file_path)
        elif choice == '2':
            remove_todo_list(file_path)
        elif choice == '3':
            view_todo_list(file_path)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
