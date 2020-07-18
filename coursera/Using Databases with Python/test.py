fh = open('coursera/Using Databases with Python/mbox.txt')
count = dict()
for line in fh:
    if line.startswith("From:"):
        email = line.split()[1].split("@")[1]
        count[email] = count.get(email, 0)+1
print(count)

h = 0
v = None
for key in count.keys():
    if count[key] > h:
        h = count[key]
        v = key
print(h, v)
