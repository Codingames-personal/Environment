##
#%%
import os
import sys

command_list = ['merge']

main_folder_path = __file__[:-16]
src_path = os.path.join(main_folder_path, "src")

class merge:

    def script_in_order():
        scripts = []
        for file_path in os.listdir(src_path):
            if file_path[-3:] == ".py":
                with open(os.path.join(src_path, file_path), "r") as script:
                    first_line = script.readline()
                    number_index = first_line.index("order :") + len("order :")
                    number = ""
                    while not first_line[number_index].isdigit(): number_index+=1
                    while number_index < len(first_line) and first_line[number_index].isdigit():
                        number+=first_line[number_index]
                        number_index +=1
                    if not number : 
                        raise Exception("Not okay")
                    
                scripts.append({'file_path' :os.path.join(src_path, file_path), 'order' : number})
        print("Order the scripts : ok", file=sys.stderr)
        return list(map(
            lambda script : script['file_path'],
            sorted(
                scripts,
                key=lambda script : script['order'])
                )
            )
            
    def copy_files(path_to_copy, path_to_paste):
        with open(path_to_copy, "r") as copy_,  open(path_to_paste, "a") as past_:
            for line in copy_.readlines():
                past_.write(line)
            past_.write('\n')
            print("copy {} : ok".format(path_to_copy.split("/")[-1]), file=sys.stderr)


    def merge_scripts(scripts):
        main_path = os.path.join(main_folder_path, "main.py")
        open(main_path, "w").close()
        print("main.py recreated : ok", file=sys.stderr)
        for script_path in scripts:
            merge.copy_files(script_path, main_path)

    def execute():
        print("Starting merge", file=sys.stderr)
        merge.merge_scripts(
            merge.script_in_order()
        )
        print("Scripts have been merged", file=sys.stderr)


    

        
# %%
