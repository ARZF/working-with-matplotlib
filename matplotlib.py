import matplotlib.pyplot as plt 

year = [1950,
        1955,1960,1965,1970,1975,1980,1985,1990,1995,2000,2005,2010,2015]

pop = [2.5,2.7,3.0,3.3,3.6,4.0,4.4,4.8,5.3,5.7,6.1,6.5,6.9,7.3]

lines = plt.plot(year, pop)
plt.grid(True)

plt.setp(lines,color=(0.4,0.4,1), marker="o")

plt.xlabel("population growth by year")
plt.ylabel("population in billions")
plt.title("Population growth")
plt.show()