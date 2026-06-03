import csv
import os


TODO_FILE = "todos.csv"
todos = []


def load_todos():
	"""Load tasks from CSV into the in-memory list."""
	todos.clear()

	if not os.path.exists(TODO_FILE):
		return

	with open(TODO_FILE, "r", newline="", encoding="utf-8") as file:
		reader = csv.reader(file)
		for row in reader:
			if row:
				todos.append(row[0])


def save_todos():
	"""Persist in-memory tasks to CSV."""
	with open(TODO_FILE, "w", newline="", encoding="utf-8") as file:
		writer = csv.writer(file)
		for task in todos:
			writer.writerow([task])


def add_one_task(title):
	"""Add one task to memory and save changes."""
	cleaned_title = title.strip()
	if not cleaned_title:
		print("Task title cannot be empty.")
		return

	todos.append(cleaned_title)
	save_todos()
	print(f"Added task: {cleaned_title}")


def print_list():
	"""Print all tasks with their 1-based positions."""
	if not todos:
		print("No tasks yet.")
		return

	print("Current tasks:")
	for index, task in enumerate(todos, start=1):
		print(f"{index}. {task}")


def delete_task(number_to_delete):
	"""Delete one task by its 1-based list position."""
	try:
		position = int(number_to_delete)
	except ValueError:
		print("Please enter a valid task number.")
		return

	if position < 1 or position > len(todos):
		print(f"Task number is out of range. Enter a number from 1 to {len(todos)}.")
		return

	removed_task = todos.pop(position - 1)
	save_todos()
	print(f"Removed task: {removed_task}")


def prompt_text(message):
	"""Read text input and return None on Ctrl+C/Ctrl+D to exit cleanly."""
	try:
		return input(message)
	except (KeyboardInterrupt, EOFError):
		return None


def main():
	load_todos()

	while True:
		print("\nTodo CLI")
		print("1. Add task")
		print("2. Show tasks")
		print("3. Delete task")
		print("4. Exit")

		choice = prompt_text("Choose an option (1-4): ")
		if choice is None:
			print("\nGoodbye.")
			break
		choice = choice.strip()

		if choice == "1":
			title = prompt_text("Task title: ")
			if title is None:
				print("\nGoodbye.")
				break
			add_one_task(title)
		elif choice == "2":
			print_list()
		elif choice == "3":
			print_list()
			if todos:
				number_to_delete = prompt_text("Task number to delete: ")
				if number_to_delete is None:
					print("\nGoodbye.")
					break
				number_to_delete = number_to_delete.strip()
				delete_task(number_to_delete)
		elif choice == "4":
			print("Goodbye.")
			break
		else:
			print("Invalid option. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
	main()