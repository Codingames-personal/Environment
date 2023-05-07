##
#%%
import os

command_list = ['merge']

main_folder_path = __file__[:-16]
src_path = os.path.join(main_folder_path, "/src")

class merge:

    def script_in_order():
        scripts = []
        for file_path in os.listdir(src_path):
            if file_path[-3:] == ".py":
                with open(os.path.join(src_path, file_path), "r") as script:
                    first_line = script.readline()
                    number_index = first_line.index("order :") + len("order :")
                    number = ""
                    while first_line[number_index].isdigit():
                        number+=first_line[number_index]
                        number_index +=1
                
                scripts.append({'file_path' :file_path, 'order' : number})

        return list(map(
            lambda script : script[file_path],
            sorted(
                scripts,
                key=lambda script : script['order'])
                )
            )
            
    def copy_files(path_to_copy, path_to_paste):
        with open(path_to_copy, "r") as copy_,  open(path_to_paste, "a") as past_:
            for line in copy_.readlines():
                past_.write(line)
        


    def merge_scripts(scripts):
        main_path = os.path.join(main_folder_path, "main.py"):
        for script_path in scripts:
            merge.copy_files(script_path, main_path)

    def execute():
        merge.merge_scripts(
            merge.script_in_order()
        )


    

        
# %%
