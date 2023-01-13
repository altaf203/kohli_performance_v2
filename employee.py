mployee_list = [
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
def get_employee_pin_list(employee_list,addresskey):
    emp_pin_list = []
    for emp in employee_list:
    # print("name: ", emp["name"])
    # print("ID:", emp["emp_id"])
        emp_pin_list.append({"name": emp["name"]})
    # print(emp_pin_list)
        emp_pin_list[employee_list.index(emp)]["addresskey"] = []
        for address in emp["address"]:
        # print(employee_list.index(emp))
            emp_pin_list[employee_list.index(emp)]["addresskey"].append(address["addresskey"])
        # print("pincode :", address["pincode"])
    return emp_pin_list
    # return get_employee_pin_list
    func_list = get_employee_pin_list(employee_list,addresskey="state")
    print(func_list)