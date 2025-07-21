import csv
users=[
    {'name':'bhargav','age':20,'city':'warangal'},
    {'name':'sahil','age':23,'city':'hyderabad'}

]

try:
    with open("users.csv","w",newline="") as csvfile:
        fieldnames=['name','age','city']
        writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(users)
    print("Successfully wrote to users")
except IOError as e:
    print("csv not found")
except Exception:
    print("Some error occured")
