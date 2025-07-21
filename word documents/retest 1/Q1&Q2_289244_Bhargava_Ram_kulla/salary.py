import csv

def calculate_average(csv_file, column_name):
    try:
        with open(csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            values = []
            for row in reader:
                try:
                    values.append(float(row[column_name]))
                except ValueError:
                    pass  
            if values:
                average = sum(values) / len(values)
                return average
            else:
                return None
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
    except KeyError:
        print(f"Error: Column '{column_name}' not found in the CSV file.")

# Example usage
csv_file_path = r"C:\Users\289244\Desktop\retest 1\Q1&Q2_289244_Bhargava_Ram_kulla\example.csv"  
column_to_average = 'salary'  
average = calculate_average(csv_file_path, column_to_average)

if average is not None:
    print(f"The average value for column '{column_to_average}' is {average:.2f}")
else:
    print(f"Could not calculate the average for column '{column_to_average}'.")
