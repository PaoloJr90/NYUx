n = int(input("Please enter a positive integer:"))

# printing continuous rows:
for row in range(1, n+1):
# printing each line:
    for i in range(1,n+1):
        print(row * i, end='\t')
    print('')