import pandas as pd

df =pd.read_csv("dataset.csv")

# print(df)

print(df.head(10))
# print(df.tail(10))
# df.info()
# print(df.shape)

# print(df.describe())
# print(df["SR"].describe())
print(df["Opposition"].describe())

# run_frequency = df["Runs"].value_counts()
run_frequency = df["Opposition"].value_counts()
print(run_frequency)

new_df = df[["Runs","SR","Opposition"]]
print(new_df)

print(df["Opposition"] == "v Australia")
vs_aussies = df[df["Opposition"]== "v Australia"]
print(vs_aussies)

#Question  
# find al the matches where virat scored a century 
# find all the matches where virat's strike rate was > 100
# find all the matches where viarat played with srilanka and scored a century
print("find al the matches where virat scored a century ")

tons = df[df["Runs"] >=100]
print(tons)

print("find all the matches where virat's strike rate was > 100")

tons_sr = df[df["SR"] > 100]
print(tons_sr)

print("find all the matches where viarat played with srilanka and scored a century")

sril_cent = df[(df["Opposition"]== "v Sri Lanka") & (df["Runs"]>=100)
]

print(sril_cent)




def find_centuries(x):
    if x>=100:
        return "OG"
    else:
        return "NOOB"

df["Centuries"] = df["Runs"].apply(find_centuries)
print(df.tail(10))

