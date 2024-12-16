import os

# Cross-platform screen clear
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Print a separator with an optional title
def print_separator(title=""):
    print("\n" + 50 * "-")
    if title:
        print(f"--{title}--")
    print(50 * "-")

# Initialize file if it doesn't exist
if not os.path.exists("data.txt"):
    print("Creating data.txt file")
    open("data.txt", "w").close()

# Add tasks
def add_tasks():
    print_separator("Add tasks")
    with open("data.txt", "r") as f:
        task_count = len([line for line in f if line.strip()])
    
    with open("data.txt", "a") as f:
        while True:
            task = input(f"{task_count + 1}. ")
            if not task.strip():
                break
            f.write(task + "\n")
            task_count += 1

# Read tasks
def read_task():
    print_separator("Reading tasks")
    with open("data.txt", "r") as f:
        tasks = [line.strip() for line in f if line.strip()]
        if not tasks:
            print("\n--Empty--\n")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

# Delete tasks
def delete_task():
    read_task()
    print_separator("Deleting task")
    with open("data.txt", "r") as f:
        data = [line for line in f if line.strip()]

    try:
        task_no = int(input("Enter task number to delete or '0' to delete all: "))
        if task_no == 0:
            open("data.txt", "w").close()
        elif 1 <= task_no <= len(data):
            del data[task_no - 1]
            with open("data.txt", "w") as f:
                f.writelines(line + "\n" for line in data)
        else:
            print("Invalid task number!")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

# Main loop
def main():
    while True:
        clear_screen()
        read_task()
        action = input("\nPress 'a' to add, 'd' to delete, or 'q' to quit: ").lower()
        if action == 'a':
            add_tasks()
        elif action == 'd':
            delete_task()
        elif action == 'q':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
