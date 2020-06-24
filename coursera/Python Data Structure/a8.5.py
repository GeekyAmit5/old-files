fh = open("coursera/Python Data Structure/mbox-short.txt")
count = 0
for line in fh:
    if line.startswith("From "):
        words = line.split()
        print(words[1])
        count += 1
print("There were", count, "lines in the file with From as the first word")
