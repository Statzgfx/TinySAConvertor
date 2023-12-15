import csv
import math
import tkinter as tk
from tkinter import filedialog
def round_to_nearest_whole_number(num):
    if num >= 0:
        return int(num + 0.5)
    else:
        return math.ceil(num - 0.5)

def modify_csv():
    # Open a file dialog to select the CSV file
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

    # Read the CSV file and modify the data
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        data = [row for row in reader]
        for row in data:
            # Modify the first column
            row[0] = row[0][:-2]
            # Add a dot before the last three digits in the first column
            row[0] = row[0][:-3] + "." + row[0][-3:]
            # Modify the second column
            row[1] = round_to_nearest_whole_number(float(row[1]))

    # Write the updated data back to the CSV file
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

        # Show success message
        tk.messagebox.showinfo("Success", "CSV file has been modified successfully!")

        # Close the program
        root.destroy()

if __name__ == "__main__":
    modify_csv()
