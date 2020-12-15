import matplotlib.pyplot as plt


data = []
with open("data", "r", encoding="UTF-8") as f:
    for line in f:
        data.append(line.lstrip())


c1 = []
c2 = []
c3 = []
for x in data:
    s = x.split(",")
    c1.append(float(s[0]))
    c2.append(float(s[1]))
    c3.append(float(s[2]))


plt.plot(c1, c2)
plt.xlabel("c1")
plt.ylabel("c2")
plt.savefig("c1c2.png")


plt.clf()


plt.plot(c1, c3)
plt.xlabel("c1")
plt.ylabel("c3")
plt.savefig("c1c3.png")

plt.clf()

c1 = range(0, 10, 1)
c2 = range(0, 10, 1)

plt.xlim(left=-2)
# plt.xlim(right=5)
plt.plot(c1, c2)
plt.xlabel("c1")
plt.ylabel("c2")
plt.savefig("c1c2-1.png")

plt.clf()

# plt.xlim(left=-2)
# plt.xlim(right=5)
plt.plot(c1, c2)
plt.xlabel("c1")
plt.ylabel("c2")
plt.savefig("c1c2-2.png")
