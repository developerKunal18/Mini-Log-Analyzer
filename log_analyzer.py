filename = input("Enter log file name: ")

error_count = 0
warning_count = 0
info_count = 0
total_lines = 0

try:
    with open(filename, "r") as file:
        for line in file:
            total_lines += 1
            if "ERROR" in line:
                error_count += 1
            elif "WARNING" in line:
                warning_count += 1
            elif "INFO" in line:
                info_count += 1

    print("\nLog Analysis:")
    print("Total Lines:", total_lines)
    print("ERROR:", error_count)
    print("WARNING:", warning_count)
    print("INFO:", info_count)

except FileNotFoundError:
    print("File not found.")
