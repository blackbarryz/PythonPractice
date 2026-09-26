# Named Constants
# The maximum rows to print starting from 7 down to 1
START_ROWS = 7
END_ROWS = 0
STEP_DOWN = -1

# Outer loop handles the rows, stepping downward from 7 to 1
for row_length in range(START_ROWS, END_ROWS, STEP_DOWN):
    
    # Inner loop handles individual character columns inside the row
    for column in range(row_length):
        # Print asterisk and override newline with a blank string
        print("*", end="")
        
    # Move cursor to the next line at the end of each outer loop row iteration
    print()