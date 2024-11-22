FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """
    Read the text file and
    returns a list of all the items stored already in that text file.
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """
    Note: The parameter with a fixed argument always follows the parameter with a not fixed argument
    filepath is fixed argument and todos_arg is not a fixed argument
    Function: Write/stores the content of the list into the text file mentioned as a filepath
    """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello!")