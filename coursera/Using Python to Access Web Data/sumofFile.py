# this program find all integers from a text file and sums it

import re
fh = open("coursera/Using Python to Access Web Data/regex_sum_706990.txt")
# fh = open("coursera/Using Python to Access Web Data/regex_sum_42.txt")
# fh = open("coursera/Using Python to Access Web Data/sample.txt")


# the below four lines does same job as this one line does
print(sum([int(x) for x in re.findall('[0-9]+', fh.read())]))

# s = 0
# for line in fh:
#     l = [int(x) for x in re.findall("[0-9]+", line)]
#     s += sum(l)
# print(s)
