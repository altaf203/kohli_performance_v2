import pandas as pd

data = {
    "apples" : [4,3,6,1],
    "oranges": [3,7,4,1]
}

index_titles = [
    "Altaf", "Raja", "Adnan", "MdAltaf"
]
df = pd.DataFrame(data,index=index_titles)
print(df)
# print(df.loc["Altaf"])
# print(df.loc["Altaf"]["apples"]) # rows
# print(df ["oranges"].iloc[0:])   #column
# print(df ["oranges"].iloc[1]) 
print(df ["oranges"].iloc[1:]) 
# print(df ["oranges"].iloc[0:3])
print(type(df))
