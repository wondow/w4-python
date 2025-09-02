"""
File Processing Script
----------------------
This script reads a text file, modifies its content (converts to uppercase),
and saves the modified content to a new file with proper error handling.

Features:
- User input for filename
- File existence and read permission validation
- Content modification (uppercase conversion)
- Safe file writing with error handling
- Success/failure feedback messages
"""

def main():
    """
    Main function that orchestrates the file processing workflow.
    Handles user input, file operations, and error management.
    """
    # Prompt user for the filename to process
    filename = input("Enter the filename to read: ")

    # Attempt to read the file with proper error handling
    try:
        # Using 'with' statement ensures proper file closure even if errors occur
        with open(filename, 'r') as file:
            # Read the entire content of the file into a string
            content = file.read()
    except FileNotFoundError:
        # Handle case where the specified file doesn't exist
        print(f"Error: The file '{filename}' does not exist.")
        return  # Exit the function early since file doesn't exist
    except IOError:
        # Handle case where file exists but cannot be read (permission issues, etc.)
        print(f"Error: The file '{filename}' cannot be read.")
        return  # Exit the function early due to read error

    # Modify the content - in this example, convert all text to uppercase
    # This demonstrates a simple content transformation that could be customized
    modified_content = content.upper()

    # Create a new filename by prefixing the original filename with 'modified_'
    # This preserves the original file while creating a new modified version
    new_filename = f"modified_{filename}"

    # Attempt to write the modified content to the new file
    try:
        # Using 'with' statement ensures proper file closure
        with open(new_filename, 'w') as new_file:
            # Write the modified content to the new file
            new_file.write(modified_content)
    except IOError:
        # Handle case where the file cannot be written (permission issues, disk full, etc.)
        print(f"Error: Could not write to file '{new_filename}'.")
        return  # Exit the function early due to write error

    # Success message indicating the modified file was created successfully
    print(f"Modified file has been created successfully as '{new_filename}'.")

# Standard Python idiom to check if this script is being run directly
# (as opposed to being imported as a module)
if __name__ == "__main__":
    # If run directly, execute the main function
    main()
