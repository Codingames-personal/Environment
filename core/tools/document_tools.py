import os

def del_last_line(file_path : str) -> None:
    with open(file_path, 'r') as file:
        file_list = list(file.readlines())
    
    with open(file_path, 'w') as file:
        for file_line in file_list[:-1]:
            file.write(file_line)

def write_after(file_path : str, line : str) -> None:
    with open(file_path, 'a') as file:
        file.write(line)

def is_empty(file_path):
    """
    If file_path is the path of a folder, verify if there is something inside
    if it is a script verify if it is empty
    """
    if os.path.isdir(file_path):
        return list(os.listdir(file_path)) == []
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            return list(file.readlines()) == []
    
def find_import(file_path):
    """
    Find all the file that have been imported on a script
    """
    
    
    with open(file_path, 'r') as file:
        import_list = list()
        state = 0
        for line in file.readlines():
            split_line = line.split(" ")
            if not split_line: continue
            if state == 0:
                if split_line[0] in ("import", "from"):
                    import_list.append(split_line[1] if not '\n' in split_line[1] else split_line[1][:-1])
                    state = 1
            if state == 1:
                if not split_line[0] in ("import", "from", '"""') or not line[0] == "#":
                    break

    return import_list

##
#%%
def insert_text(text, insert, index):
    return text[:index] + insert + text[index:]

def python_to_sys_path(python_path):
    sys_path = ""
    double_point = False
    for character in python_path:
        if character == ".":
            if double_point:
                sys_path = sys_path[:-1] + ".." + sys_path[-1]
                double_point = False
            else:
                sys_path += "/"
                double_point = True
        else:
            sys_path += character
            double_point = False
    sys_path += ".py"
    if not os.path.exists(sys_path):
        return "not exist " + sys_path
    return sys_path


python_to_sys_path("..src.blabla")

#%%