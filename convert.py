import os

def convert_tbldata_to_csvformat(filename, path="."):
    # Open the .csv file for writing
    csv_filename = os.path.join(path, filename + ".csv")
    with open(csv_filename, "w+") as csv_file:
        # Open the .tbl file for reading
        tbl_filename = os.path.join(path, filename + ".tbl")
        with open(tbl_filename, "r") as tbl_file:
            # Read the first line of the .tbl file to determine the number of columns
            first_line = tbl_file.readline().strip()
            
            # Write the first line to the .csv file
            first_line = first_line.replace("|", ",")
            first_line = first_line.rstrip(",")
            csv_file.write(first_line + "\n")
            
            # Read each subsequent line of the .tbl file
            lines = tbl_file.readlines()
            for line in lines:
                # Remove the trailing newline character
                line = line.strip()
                
                # Replace commas with "N" and pipes with commas
                line = line.replace(",", "N")
                line = line.replace("|", ",")
                line = line.rstrip(",")

                # Write the modified line to the .csv file
                csv_file.write(line + "\n")

    print(f"Successfully converted {filename}.tbl to {filename}.csv")


my_files = ["customer", "lineitem", "nation", "orders", "part", "partsupp", "region", "supplier"]

for item in my_files:
    convert_tbldata_to_csvformat("partsupp", "C:/Users/user/Desktop/CZ4031/Project 2/TPC-H V3.0.1/dbgen")
