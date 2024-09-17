import os

current_directory = os.getcwd()
print(f"Current directory: {current_directory}")

os.mkdir("new_folder")

os.chdir("new_folder")
print(f"Changed to: {os.getcwd()}")

os.chdir("..")  
os.rmdir("new_folder")
