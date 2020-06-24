fname = input("Enter file name: ")
fh = open(fname)
# fh = open("coursera/Python Data Structure/romeo.txt")
lst = list()
for line in fh:
    words = line.split()
    for word in words:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)
