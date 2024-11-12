# with open("products.txt", 'r') as file:
#     for line in file:
#         # Split the line into ID, Name, and Number
#         parts = line.strip().split('=')
#         current_id = parts[0]
#         name = parts[1]
#     print(current_id)
#

def print_specific_line(line_number, filename='products.txt'):
    with open(filename, 'r') as file:
        lines = file.readlines()
        total_lines = len(lines)

        # Check if the specified line number is within the valid range
        if 1 <= line_number <= total_lines:
            # Print the specified line
            print(lines[line_number - 1])
        else:
            print(f"Line number {line_number} is out of range (1-{total_lines}).")


line_number = int(input("Enter the line number to print: "))

print_specific_line(line_number)
