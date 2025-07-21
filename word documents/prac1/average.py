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
                average = sum(values)/len(values)
                return average
            else:
                return None
    except FileNotFoundError:
        print("csv not found")
    except KeyError:
        print("Column not found")
csv_path=r"C:\Users\289244\Desktop\prac1\examples.csv"
column='salary'
average=calculate_average(csv_path,column)

if average is not None:
    print(f"the average of column '{column}' is {average:.2f}")
else:
    print("some error occured")