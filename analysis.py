import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")
print(df.head())

# Total no of runs kohli has scored
print("Total no of runs kohli has scored")
print("total runs :" ,  df["Runs"].sum())

#  Find out the total no balls he has faced

print("Find out the total no balls he has faced")
print("total ball faced:", df["BF"].sum())

# find out the average strke rate of kohli
print("find out the average strke rate of kohli")
print("avg strick rate :", df["SR"].mean())



# number of matches he has played at different position
print(df["Pos"].head(10))


position = df["Pos"].unique()
print(position)

df["Pos"]= df["Pos"].map({
    3.0: "Batting at 3",
    4.0: "Batting at 4",
    2.0: "Batting at 2",
    1.0: "Batting at 1",
    7.0: "Batting at 7",
    5.0: "Batting at 5",
    6.0: "Batting at 6"
})

print(df.head(10))

pos_counts = df["Pos"].value_counts()
print(pos_counts)
print(type(pos_counts))
# print(df[["Runs", "Pos"]])

#  total run scored in different position
pos_counts_value = pos_counts.values
pos_counts_labels = pos_counts.index

fig = plt.figure(figsize=(10,7))
plt.pie(pos_counts_value, labels=pos_counts_labels)
plt.show()

#  total 6 scored in different posisiton
def show_pie_plots(df,key):
    counts = df[key].value_counts()
    print(counts)
    count_value = counts.values
    count_labels = counts.index
    
    fig = plt.figure(figsize=(10,7))
    plt.pie(count_value,labels=count_labels)
    plt.show()

# number of matches has played with different opposition
show_pie_plots(df, "Opposition")

# numbre of matches he has played at ground
show_pie_plots(df, "Ground")

# total sixrs scored in different position
runs_at_pos = df.groupby("Pos")["6s"].sum()
print(runs_at_pos, type(runs_at_pos))
runs_at_pos_values = runs_at_pos.values
runs_at_pos_labels = runs_at_pos.index

fig = plt.figure(figsize=(10,7))
plt.bar(
    runs_at_pos_labels,
    runs_at_pos_values,
    color = "Green",
    width=0.3
)
plt.show()

# total run scored with different countries
# runs_with_countries = df.groupby("Opposition")["Runs"].sum
# runs_with_countries



#  number of centurires scored by him in 1st and 2nd inings
centuries = df.query("Runs >= 100")
print(centuries)

innings = centuries["Inns"].value_counts()
print(centuries)
plt.pie(innings.values, labels=innings.index)
plt.show()
# tons = centuries["Runs"]

# plt.bar(innings,tons, width=0.3,color="red")
# plt.show()


# calculate the dismissals of kohli

# against wich teams he has scored

# against 




































# x = np.arange(0, 3*np.pi, 0.1)
# y = np.sin(x)

# print(x)
# print(y)
# plt.plot(x, y)
# plt.show()