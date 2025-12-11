import pandas

data = {
    id: [1, 2, 3],
    "name": ['Divya', 'Tushar', 'Pariya'],
    "city": ['Surat', 'Ahmedabad', 'Vadodara']
}

print(data)
df = pandas.DataFrame(data)
print(df)