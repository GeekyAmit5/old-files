fh = open("coursera/Python Data Structure/mbox-short.txt")
# fh = open("mbox-short.txt")
counts = dict()
for line in fh:
    if line.startswith("From "):
        words = line.split()
        counts[words[1]] = counts.get(words[1], 0) + 1


max = 0
email = None
for i in counts:
    if counts[i] > max:
        max = counts[i]
        email = i

print(email, max)
