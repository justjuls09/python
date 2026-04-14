"""
-----------------------------------------------------------------------
ASSIGNMENT 11A REVISED: THE BUG TRACKING LOG
-----------------------------------------------------------------------
[x] 1. Program uses a while loop to keep asking for bugs.
[x] 2. Uses the datetime module to get a timestamp format.
[x] 3. Stores the timestamp, file name, description, and priority in a dictionary.
[x] 4. Uses `with open("bug_log.txt", "a")` to append to the file safely.
[x] 5. The bug_log.txt file is formatted neatly with newlines.
-----------------------------------------------------------------------
"""

"""
Author: Julie Gavas
Program: Uses a while loop to keep asking for bugs.
Description: Keeps track of bugs reported by users, stores the timestamp, file name,
description, and priority in a dictionary, and appends entries to bug_log.txt.
"""

import datetime # for timestamp generation


def get_bug_inputs():
    """Asks the user for the three required bug fields."""
    file_name = input("File name: ").strip()
    description = input("Description of error: ").strip()
    priority = input("Priority (High, Medium, Low): ").strip()
    return file_name, description, priority


def make_timestamp():
    """Creates a timestamp string after user input is gathered."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def append_bug_to_file(timestamp, file_name, description, priority):
    """Appends one formatted bug record to bug_log.txt using append mode."""
    with open("bug_log.txt", "a") as f:
        f.write("[" + timestamp + "]\n")
        f.write("File: " + file_name + "\n")
        f.write("Status: " + description + "\n")
        f.write("Priority: " + priority + "\n")
        f.write("--------------------------------------------------\n")


def main():
    # this timestamp will be the key, value will be [file_name, description, priority]
    bugs = {}

    while True:
        choice = input("Enter 'log' to record a bug, or 'quit' to stop: ").strip().lower()

        if choice == "quit":
            break

        elif choice == "log":
            file_name, description, priority = get_bug_inputs()

            # timestamp created after gathering inputs
            timestamp = make_timestamp()

            # dictionary storage (key = timestamp, value = list)
            bugs[timestamp] = [file_name, description, priority]

            # ensures each entry is saved to the file immediately
            append_bug_to_file(timestamp, file_name, description, priority)

        else:
            print("Please type 'log' or 'quit'.")

    print("Bug log updated!")


main()
