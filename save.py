import os
def save(text,text_to_type, index_start, index_end):
    with open("save\save.ttsf", "a", encoding="utf-8") as file:
        file.write(f"{text}\n{text_to_type}\n\n{index_start},{index_end}\n")

def load():
    if not os.path.exists("save\save.ttsf"):
        return 0
    with open("save\save.ttsf", "r", encoding="utf-8") as file:
        #return last line
        lines = file.readlines()
        line=lines[-1]
        print(line)
        index_start, index_end = line.split(",")
        return int(index_end)
    
