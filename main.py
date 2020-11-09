from raw import retrieve_data_by_code, search_by_code


data = search_by_code("12509324")
print(data)
data = retrieve_data_by_code("", "5212")
print(data)
