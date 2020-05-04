def find_min_pos(my_list):
    for i in range(min(my_list), max(my_list)):
        if i not in my_list:
            return i 
        else:
            continue
