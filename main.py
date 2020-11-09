from raw import retrieve_data_by_code, search_by_code, get_pid


data = search_by_code("12509324")

print(data)
pid_val=get_pid(data)


data = retrieve_data_by_code("", str(pid_val))

print(data)
