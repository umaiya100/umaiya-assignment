filename = input("enter the name of the file:")

words =open(filename).read().split()
counts ={}

    
for w in words:
     counts[w]=counts.get(w,0)+1

     most = max(counts, key=counts.get)

     print("most frequent word:", most)
     print("occurrences:", counts[most])

