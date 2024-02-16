from tkinter import filedialog
from tkinter import Tk

replace_list = {"…":"...","—":"-","«":"\"","»":"\"","’":"'","–":"-"," ":" "}
remove_list = {"<strong>":"","</strong>":"","<emphasis>":"","</emphasis>":""}

def filter_text(text):
    for key in replace_list:
        text = text.replace(key, replace_list[key])
    for key in remove_list:
        text = text.replace(key, "")
    return text
    

def get_text(search_index=0, path=""):
    #open file picker and get the path to the file
    if path == "":
        Tk().withdraw()
        path = filedialog.askopenfilename()
    




    with open(path, "r", encoding="utf-8") as file:
        text = file.read()

    index_start = text[search_index:].find("<p>")+search_index
    index_end = index_start+text[index_start+3:].find("</p>")+6
    print(index_start)
    print(index_end)
    text = filter_text(text[index_start+3:index_end-3])
    return text , index_start,index_end