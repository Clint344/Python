# File Read & Write Challenge 🖋️
try:
    # Ask user for the filename to read
    filename = input("Enter the name of the file to read: ")

    # Open the file and read its content
    with open(filename, "r") as file:
        content = file.read()

    # Modify the content (for example, make it all uppercase)
    modified_content = content.upper()

    # Write the modified content to a new file
    new_filename = "modified_" + filename
    with open(new_filename, "w") as new_file:
        new_file.write(modified_content)

    print(f"Modified content has been written to {new_filename}")

except FileNotFoundError:
    print("Error 🛑: The file you entered does not exist.")
except IOError:
    print("Error 🛑: There was a problem reading or writing the file.")
