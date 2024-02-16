replace_list = {"…":"...","—":"-","«":"\"","»":"\"","’":"'","–":"-"," ":" "}
remove_list = {"<strong>":"","</strong>":"","<emphasis>":"","</emphasis>":""}

def filter_text(text):
    for key in replace_list:
        text = text.replace(key, replace_list[key])
    for key in remove_list:
        text = text.replace(key, "")
    return text
    


def get_text(search_index=0):
    #load fb2 file
    #parse it
    #return text

    path = "./books/example.fb2"
    with open(path, "r", encoding="utf-8") as file:
        text = file.read()

    index_start = text[search_index:].find("<p>")+search_index
    index_end = index_start+text[index_start+3:].find("</p>")+6
    print(index_start)
    print(index_end)
    text = filter_text(text[index_start+3:index_end-3])
    return text , index_start,index_end

def max_length_of_line():
    max_length = 0
    with open("./books/example.fb2", "r", encoding="utf-8") as file:
        text = file.read()
        index_start = 0
        index_end = 0
        end = text.find("</body>")
        while index_start < end and index_end < end:
            index_start = text[index_end:].find("<p>")+index_end
            index_end = index_start+text[index_start+3:].find("</p>")+6
            if index_end - index_start > max_length:
                max_length = index_end - index_start
    return max_length



if __name__ == "__main__":
    print(max_length_of_line())
    