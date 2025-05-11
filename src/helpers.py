import os

# This function checks if a directory exists. If not, then it creates the directory
def check_directory(path:str) -> None:
    if not os.path.exists(path):
        os.makedir(path)
    return None