# this is comment

# elements = []
# for i in range(10): #array
#     elements.append(i)

# print(elements)

# first_name = int(input("enter ur first name in number")) #type casting
# last_name = int(input("enter ur second name in number"))
# print(first_name + last_name)
# print(type(first_name))
# print(type(last_name))


#string

# val = "Hunter"
# print(type(val)) #string

# for i in range(len(val)):
#     print(val[i], type(val[i]))


#list
# elem = [8, 9, "Altaf", "Raja"]
# print(len(elem))
# print(elem[0])
# print(elem[-1])


# studentList = ["Altaf", "Raja", "Aryan", "Adnan", "Thor", "Hunt"]
# ratingList = [10, 9, 8, 6, 7, 8]
# ratedStudent = []

# for i in range(len(studentList)):
#     ratedStudent.append(studentList[i])
#     ratedStudent.append(ratingList[i])
# print(ratedStudent)
# print(type(ratedStudent))

#rateStudentList = ["Altaf", 10, "Raja", 9, "Aryan", 8, "Adnan", 6, "Thor", 7, "Hunt", 8]
#print(rateStudentList)

#tuple

#Dictonary in python

# avengerDict = {
#     "Ironman": 10,
#     "captain america": 9,
#     "Thor": 8

# }
# print(avengerDict)
# print(type(avengerDict))

# print("Rating of ironman :", avengerDict["Ironman"])
# print(type(avengerDict.keys()))
# print(type(list(avengerDict.keys())))


avengerDict = {
    "Ironman": [       #key of the dictnory
        {"Spiderman": 8},
        {"Black panther": 7}
    ],
    "Captain America": [
        {"Winter Solider": 7},
        {"Hawkey: 10"}
    ],
    "Thor": [
        {"Hulk": 8},
        {"Groot: 7"}
    ]

}
print(len(avengerDict))
print("Spiderman score :", avengerDict["Ironman"][0]["Spiderman"])
print("Winter Solider score :", avengerDict["Captain America"][0]["Winter Solider"])

# avengersDict = {
# 		"Ironman": 10,
# 		"Captain America": 9,
# 		"Thor": 8
# }

# unlike lists and tuples you can actually represent avenger-rating relation using key-value pair. It is a great way of retreiving data points
# from a complex dataset.

avengersDict = {
		"Ironman": [
				{"Spiderman": 8},
				{"Black Panther": 7}
		],
		"Captain America": [
				{"Winter Soldier": 7},
				{"Hawkeye": 6}
		],
		"Thor": [
				{"Hulk": 8},
				{"Groot": 7}
		]
}

# teamIronman = avengersDict["Ironman"]
# print("TEAM IRON MAN: ", teamIronman)

# teamCaptain = avengersDict["Captain America"]
# print("TEAM CAPTAIN AMERICA: ", teamCaptain)

# teamThor = avengersDict["Thor"]
# print("TEAM THOR: ", teamThor)

"""
Output
TEAM IRON MAN: [{"Spiderman": 8}, {"Black Panther": 7}]
TEAM CAPTAIN: [{"Winter Soldier": 7}, {"Hawkeye": 6}]
TEAM THOR: [{"Hulk": 8}, {"Groot": 7}]  
"""

# firstname = input("enter the first name")  # how can input from the user (using the input function we take the input form the user)
# lastname = input("enter te second name ")
# print("full name ",firstname+lastname)

# var_x = int(input("enter the number of ms dhoni"))
# player = str(input("enter your fav crickter name :"))


# acces the individual character in a string by accesing the index value 
# value = "Hunter"
# print("value of 0th index is ", value[0])
# print("value of first index is ", value[1])
# print("character form 0th to 4 index is ", value[0:4])
# print("character form 1 to 4th index", value[1:4])


# list in the python it is similar to array in c/c++ except it can simultaneouslyhold different types of data.
# avengerList = ["Ironman", "CaptainAmerica", "Doctor Strange", "Hult", "Spiderman", "Thor", "Batman"]
# #print(avengerList)
# rateList = [10, 9, 8, 6, 7, 8, 4]
# #ratedAvengerList = ["Ironman", 10, "Captain America", 9, "Doctor Strange", 8, "Hulk", 6, "Spiderman", 7, "Thor", 8]
# ratedStudent = []

# for i in range(len(avengerList)):
#     ratedStudent.append(avengerList[i])
#     ratedStudent.append(rateList[i])
# print(ratedStudent)
# print(type(ratedStudent))

#rateStudentList = ["Altaf", 10, "Raja", 9, "Aryan", 8, "Adnan", 6, "Thor", 7, "Hunt", 8]
#print(rateStudentList)

# avengersDict = {
# 	"Ironman": 10,
# 	"Captain America": 9,
# 	"Thor": 8
# }
# print(type(avengersDict))


# teamIronman = avengersDict["Ironman"]
# print("TEAM IRON MAN: ", teamIronman)

# teamCaptain = avengersDict["Captain America"]
# print("Team of Captain America",teamCaptain)

# teamThor = avengersDict["Thor"]
# print("Team of Thor :", teamThor)

