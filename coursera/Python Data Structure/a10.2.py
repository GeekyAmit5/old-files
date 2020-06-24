fh = open("coursera/Python Data Structure/mbox-short.txt")
# fh = open("mbox-short.txt")

counts = dict()
for line in fh:
    if line.startswith("From "):
        pos = line.find(":")
        hour = line[pos-2:pos]
        counts[hour] = counts.get(hour, 0) + 1

for i, j in sorted(counts.items()):
    print(i, j)
