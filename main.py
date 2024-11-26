import sys
from wc import WC

def main():
    # Get filename from command-line arguments
    if len(sys.argv) < 2:
        print("Error: No filename provided. Usage: main.py <filename> [-c -l -w -m]")
        sys.exit(1)

    filename = sys.argv[1]

    # Try to open the file
    try:
        with open(filename, 'rb') as file:  # Open the file here
            # Initialize WC object and pass the file object to it
            wc = WC(file)
            wc.calculate_stats()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except IOError:
        print(f"Error: Could not read file '{filename}'.")
        sys.exit(1)

    # Handle options based on command-line arguments
    options = sys.argv[2:]  # Options are any additional arguments after filename
    if not options:
        options = ["-c", "-l", "-w"]  # Default options if none specified

    # Print the results based on options
    if "-c" in options:
        print(f"Bytes: {wc.bytes}")
    if "-l" in options:
        print(f"Lines: {wc.lines}")
    if "-w" in options:
        print(f"Words: {wc.words}")
    if "-m" in options:
        print(f"Characters: {wc.characters}")

if __name__ == "__main__":
    main()
