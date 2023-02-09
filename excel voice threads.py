import openpyxl

# Load the workbook and select the active sheet
workbook = openpyxl.load_workbook("data.xlsx")
sheet = workbook.active

# Define the data entry function
def enter_data(row, col, data):
    # Write the data to the specified cell
    sheet.cell(row=row, column=col).value = data
    print("Data entered at cell ({}, {}): {}".format(row, col, data))

# Start a chatbot loop to enter data
row = 1
col = 1
while True:
    # Get the data from the user
    data = input("Enter the data for cell ({}, {}):".format(row, col))

    # Check if the user wants to quit
    if data.lower() == "quit":
        break

    # Call the data entry function
    enter_data(row, col, data)

    # Update the row and column numbers
    col += 1
    if col > 5:
        col = 1
        row += 1

# Save the changes to the workbook
workbook.save("data.xlsx")
