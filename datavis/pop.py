import matplotlib.pyplot as plt

years = [1, 1000, 1500, 1600, 1700, 1750, 1800, 1850, 1900, 1950]
for i in range(0, 13):
    last = years[-1]
    years.append(last + 5)

pops = [
    200,
    400,
    458,
    580,
    682,
    791,
    1000,
    1262,
    1650,
    2525,
    2758,
    3018,
    3322,
    3682,
    4061,
    4440,
    4853,
    5310,
    5375,
    6127,
    6520,
    6930,
    7349,
]
print(len(pops))
print(len(years))

plt.plot(years, pops)
plt.show()
