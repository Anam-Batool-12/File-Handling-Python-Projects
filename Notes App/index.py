# Project Name: Notes App
import os

def file_creation():
    file_name = input("Enter the name of the file (with .txt extension): ")
    if os.path.exists(file_name):
        print(f"File {file_name} already exists")
    else:
        with open(file_name, "w") as file:
            file_content = input("Enter the content of the file: ")
            file.write(file_content + "\n")
            print(f"File {file_name} created successfully.")

def file_opening():
    file_name = input("Enter the name of the file (with .txt extension): ")
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            print("\nFile Content:\n" + "-" * 30)
            print(file.read())
            print("-" * 30)
    else:
        print(f"File {file_name} does not exist.")

def file_editing():
    file_name = input("Enter the name of the file (with .txt extension): ")
    if os.path.exists(file_name):
        with open(file_name, "a") as file:
            file_content = input("Enter the content to append: ")
            file.write("\n" + file_content)
            print(f"File {file_name} edited successfully.")
    else:
        print(f"File {file_name} does not exist.")

def file_deleting():
    file_name = input("Enter the name of the file (with .txt extension): ")
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"File {file_name} deleted successfully.")
    else:
        print(f"File {file_name} does not exist.")

def main():
    while True:
        print("\nNotes App - File Manager")
        print("1. Create a new file")
        print("2. Open a file")
        print("3. Edit a file")
        print("4. Delete a file")
        print("5. Exit")
        
        try:
            user_choice = int(input("Enter your choice: "))
            if user_choice == 1:
                file_creation()
            elif user_choice == 2:
                file_opening()
            elif user_choice == 3:
                file_editing()
            elif user_choice == 4:
                file_deleting()
            elif user_choice == 5:
                print("Exiting...")
                break
            else:
                print("Invalid choice! Please enter a valid option.")
        except ValueError:
            print("Please enter a number (1-5).")

main()
