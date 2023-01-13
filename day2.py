
# ratedAvegenerList2D = [
#     ["Spiderman", 81],
#     ["Groot", 7],
#     ["Black Widow", 8]
# ]

# for i in range(0, len(ratedAvegenerList2D)):
#     print(ratedAvegenerList2D[i])
#     # for j in range(0, len(ratedAvegenerList2D[i])):
#     #     print(ratedAvegenerList2D[i][j])

# for elem in ratedAvegenerList2D:
#     for innerElem in elem:
#         print(innerElem)
    

employee = {
    "name": "Tony Stark",
    "emp_id": 3,
    "address": [
        {
            "line1": "mehsi",
            "line2": "east champaran",
            "state": "Bihar",
            "pincode": "845426"
        },
        {
            "line1": "haldia",
            "line2": "purba mednipur",
            "line3": "WB",
            "pincode": "700107"
        }

    ]
}

# for i in range(len(employee["address"])):
#     print(employee["address"][i]["pincode"])

employee_list = [
    {
        "name": "Tonay Stark",
        "emp_id": 3,
        "address": [
            {
                "line1": "mehsi",
                "line2": "east champaran",
                "state": "Bihar",
                "pincode": "845426"
            },
            {
                "line1": "mehsi",
                "line2": "east champaran",
                "state": "Bihar",
                "pincode": "845426"   
            }
        ]
    },
    {
        "name": "steve Rogers",
        "emp_id": 6,
        "address": [
            {
                "line1": "mehsi",
                "line2": "east champaran",
                "state": "Bihar",
                "pincode": "845426"
            },
            {
                "line1": "mehsi",
                "line2": "east champaran",
                "state": "Bihar",
                "pincode": "845425"
            }
        ]
    }
]
emp_pin_list = []
for emp in employee_list:
    # print("name: ", emp["name"])
    # print("ID:", emp["emp_id"])
    emp_pin_list.append({"name": emp["name"]})
    # print(emp_pin_list)
    emp_pin_list[employee_list.index(emp)]["pincode"] = []
    for address in emp["address"]:
        # print(employee_list.index(emp))
        emp_pin_list[employee_list.index(emp)]["pincode"].append(address["pincode"])
        # print("pincode :", address["pincode"])

def get_employee_pin_list(employee_list):
    emp_pin_list = []
    for emp in employee_list:
    # print("name: ", emp["name"])
    # print("ID:", emp["emp_id"])
        emp_pin_list.append({"name": emp["name"]})
    # print(emp_pin_list)
        emp_pin_list[employee_list.index(emp)]["pincode"] = []
        for address in emp["address"]:
        # print(employee_list.index(emp))
            emp_pin_list[employee_list.index(emp)]["pincode"].append(address["pincode"])
        # print("pincode :", address["pincode"])
    return get_employee_pin_list
    func_list = get_employee_pin_list(employee_list)
    print(func_list)

print(emp_pin_list)

# # emp_pin = {}

# def multiply(a,b):
#     z=a+b
#     return z
# c = multiply(5,4)
# print(c)


# a=5
# b=6
# result=a*b
# print(result)

# def multiplier(a,b):

#     #body of the function
#     result=a*b
#     return result

# res = multiplier(4,5)
# print(res)

