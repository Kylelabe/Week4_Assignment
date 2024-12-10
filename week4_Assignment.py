try:
    filename = input("Enter the name of the file to read: ")

    # Opens the input_file for reading
    input_file = open(filename,"r")

    # Reads the content of input_file
    content = input_file.read()

    # Closes the input_file
    input_file.close()

    # Modifies the content by changing to uppercase
    modified_content = content.upper()

    # Opens the output.txt file for writing
    updatedFile = open("output.txt", "w")

    # Writes the modified content to the updated file
    updatedFile.write(modified_content)

    # Closes thw updated file
    updatedFile.close()

    print("The modified content has been written to 'output.txt'.")
except FileNotFoundError:

    print("Error: The file does not exist. Please check the filename and try again.")

except IOError:
    print("Error: The file could not be read or written. Please check the file and try again.")

