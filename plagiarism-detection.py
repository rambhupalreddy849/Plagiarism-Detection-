from tkinter import *
import math
import re
from collections import Counter
WORD = re.compile(r"\w+")

TITLE = "PLAG CHECK"
PLAG_OUTPUT_LAYOUT = "   Plag checking value is "
ENTRY_LABLE_WIDTH = 20
TEXT_LABLE_HEIGTH = 5
TEXT_LABLE_WIDTH = 25
window_width = 400
window_height = 150

def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in list(vec1.keys())])
    sum2 = sum([vec2[x] ** 2 for x in list(vec2.keys())])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)

def submitpressed():
    text1 = t1.get().lower()
    text2 = t2.get().lower()
    reference = ref.get().lower()
    vector1 = text_to_vector(text1)
    vector2 = text_to_vector(text2)
    vector3= text_to_vector(reference)
    cosine = get_cosine(vector1,vector3)
    cosine1= get_cosine(vector2,vector3)
    #printing
    value = PLAG_OUTPUT_LAYOUT + str(cosine)+'\n'+PLAG_OUTPUT_LAYOUT + str(cosine1)
    lab.config(text=value)

root = Tk()
root.title(TITLE)
t1 = Entry(master=root,width=ENTRY_LABLE_WIDTH)
t2 = Entry(master=root,width=ENTRY_LABLE_WIDTH)
ref = Entry(master=root,width=ENTRY_LABLE_WIDTH)
lab = Label(master=root, text="palg check is 0%", height=TEXT_LABLE_HEIGTH, width=TEXT_LABLE_WIDTH)

Label(master=root,text="text 1").grid(row=0,column=0)
Label(master=root,text="text 2").grid(row=1,column=0)
Label(master=root,text="reference").grid(row=2,column=0)
Button(master=root,command=submitpressed,text="check").grid(row=3,column=0)

t1.grid(row=0,column=1)
t2.grid(row=1,column=1)
ref.grid(row=2,column=1)
lab.grid(row=4,column=0)

# TESTING
#t1.insert(0,"This is an apple.")
#t2.insert(0,"This is a check")

def getsizeandpos():
    screenheight = root.winfo_screenheight()
    screenwidth = root.winfo_screenwidth()
    posy = int(screenheight / 2 - window_height / 2)
    posx = int(screenwidth / 2 - window_width / 2)
    return str(window_width) + "x" + str(window_height) + "+" + str(posx) + "+" + str(posy)

root.geometry(getsizeandpos())
root.mainloop()