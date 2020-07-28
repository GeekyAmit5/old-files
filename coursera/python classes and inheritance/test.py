# class fruit:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def __str__(self):
#         return '{} {}'.format(self.name, self.price)

#     def sort_priority(self):
#         return self.price


# l = [fruit("apple", 20), fruit("mango", 10)]

# # for i in sorted(l, key=fruit.sort_priority):
# for i in sorted(l, key=lambda x: x.sort_priority()):
#     print(i)


a = 10
print(f"a = {a}")
