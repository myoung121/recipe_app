"""
RECIPE PAGE
"""


from PIL import Image, ImageTk
import tkinter as tk
from tkinter import scrolledtext
import  io
from Pages import ScrollBox as sBox
import application as app
class Recipe(tk.Toplevel):

    def closePage(self,name):
        #print(app.open_recipes)
        del app.open_recipes[name]
        #print(app.open_recipes)
        self.destroy()



    def __init__(self, recipe_info:dict, recipe_image_blob:bytes):
        super().__init__()
        self.recipe_name = recipe_info['name']
        self.recipe_ingreds = recipe_info['ingredients']
        self.recipe_instrs = recipe_info['instr'].split('. ')
        self.recipe_comment = recipe_info['comment']
        if not self.recipe_comment:
            self.recipe_comment = ''
        pic = Image.open(io.BytesIO(recipe_image_blob))  # convert image bytes to PIL image format(jpeg)
        recipe_pic = ImageTk.PhotoImage(pic)
        app.open_recipes[self.recipe_name] = recipe_pic
        length = '900'
        width = '700'
        self.geometry(f'{length}x{width}')
        self.title(self.recipe_name.upper())
        # FRAME
        frame_navigation = tk.LabelFrame(self, text='navigation', padx=0, pady=0)
        frame_navigation.grid(row=0, column=1)
        frame_image_note = tk.LabelFrame(self,text='image/note')
        frame_image_note.grid(row=1, column=1,rowspan=3)
        frame_ingreds_instrs = tk.LabelFrame(self, text='Ingreds/Instrs',height=int(width)-100,width=int(int(length)/2))
        frame_ingreds_instrs.grid(row=1, rowspan=2,column=0)
        frame_ingreds = tk.LabelFrame(frame_ingreds_instrs,text='ingreds')
        frame_ingreds.grid(row=0,column=0,sticky='n',pady=20)
        frame_instrs = tk.LabelFrame(frame_ingreds_instrs,text='instrs')
        frame_instrs.grid(row=1,column=0,sticky='s',pady=25)
        frame_note = tk.LabelFrame(frame_image_note, text='notes')
        frame_note.grid(row=2, column=0,columnspan=3)
        # CHECKBOX
        favorite_toggle = tk.IntVar()
        chk_box_fav = tk.Checkbutton(frame_navigation, text='fav', variable=favorite_toggle)
        chk_box_fav.grid(row=0, column=0)
        # BUTTON
        btn_close = tk.Button(frame_navigation,text='close',command=lambda:self.closePage(self.recipe_name))
        btn_close.grid(row=0,column=1)
        btn_save_note = tk.Button(frame_note, text='save')
        btn_save_note.grid(row=1, column=2)
        # LABEL
        lbl_blank = tk.Label(frame_ingreds_instrs)
        lbl_blank.grid(row=1, column=0, pady=5)
        # SCROLLTEXT
        scroll_text_ingreds= sBox.ScrollTextBox(frame_ingreds,self.recipe_ingreds)
        scroll_text_istrs = sBox.ScrollTextBox(frame_instrs,self.recipe_instrs)
        # IMAGE
        lbl_pic = tk.Label(frame_image_note, image=recipe_pic)
        lbl_pic.grid(row=0, column=0)
        # ENTRY
        entry_recipe_note = tk.Entry(frame_note,
                                     borderwidth=4)
        entry_recipe_note.grid(row=0, column=0, pady=0)
        # SCROLLED TEXT
        # Creating scrolled text area
        recipe_note = scrolledtext.ScrolledText(frame_note,
                                    width=30,
                                    height=8,
                                    font=("Times New Roman",
                                          15))
        recipe_note.grid(column=0,row=0, pady=0, padx=0,columnspan=3)
        # Inserting Text which is read only
        recipe_note.insert(tk.INSERT,self.recipe_comment)
        # Making the text read only
        recipe_note.configure(state='disabled')
