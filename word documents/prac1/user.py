import csv
data=[
    {'name':'bhargav','age':23,'city':'warangal'},
    {'name':'sahil','age':22,'city':'hyderabad'}
]

try:
    with open("users.csv","w",newline="") as csvfile:
        fieldnames=['name','age','city']
        writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(users)
    print("succcessfully wrote to users.csv")
except IOError as e:
    print("csv not found")
except Exception:
    print('some error occured')