import csv

def calculate_average(csv_file,column_name):
    try:
        with open(csv_file,mode='r') as file:
            reader=csv.DictReader(file)
            values=[]
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
        print("csv file not found")
    except KeyError:
        print("column_name not found")
csv_path=r"C:\Users\289244\Desktop\prac\example.csv"
csv_average='salary'
average=calculate_average(csv_path,csv_average)

if average is not None:
    print(f"the average of column '{csv_average}' is {average:.2f}")
else:
    print("csv file not found")
