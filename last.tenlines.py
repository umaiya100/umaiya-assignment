filename = input("enter a file:")
try:
    with open(filename) as f:
        lines =f.readline()

        for line in lines[-10:]:
            print(line,end="")

except:
    print("file not found:")