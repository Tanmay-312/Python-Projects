mean, median, mode = 0, 0, 0

# mean
list1 = [12, 69, 14, 2, 5, 3, 6, 66, 8, 8, 7, 55, 22, 3, 4, 9]
mean = sum(list1) / len(list1)
print("mean", mean)

# median
list1.sort()
if len(list1) % 2 == 0:
    m1 = list1[len(list1) // 2]
    m2 = list1[len(list1) // 2 - 1]
    median = (m1 + m2) / 2
else:
    median = list1[len(list1) // 2]
print("median", median)

# mode
freq = {}
for i in list1:
    freq.setdefault(i, 0)
    freq[i] += 1
frequent = max(freq.values())
for i, j in freq.items():
    if j == frequent:
        mode = i
print("mode", mode)
