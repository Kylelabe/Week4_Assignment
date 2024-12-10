# Opens the input_file for reading
input_file = open("Week3_Assignment.py","r")

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

