count = 0
total = 0
# fname = input("Enter file name: ")
# fh = open(fname)
fh = open("coursera/Python Data Structure/mbox-short.txt")
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    pos = line.find(":")
    count += 1
    total += float(line[pos+1:].strip())
print("Average spam confidence:", total/count)
