import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import PIL
from PIL import Image, ImageTk
import msvcrt

#Tabs
class Tabs:
    def __init__(self, window, text_tab):
        self.window = window
        self.tabs = ttk.Notebook(window)
        self.tabs.pack(expand = 1, fill = "both")
        
        self.tab_sen = ttk.Frame(self.tabs)
        self.tabs.add(self.tab_sen, text = text_tab)

    def add_tab(self, text_tab):
        new_tab = ttk.Frame(self.tabs)
        self.tabs.add(new_tab, text = text_tab)
class EntrY:
    def __init__(self, window, entry_width, entry_string, entry_index, entry_x, entry_y):
        self.window = window
        self.entry = tk.Entry(window, width=entry_width)
        self.entry.insert(index=entry_index, string=entry_string)
        self.entry.place(x=entry_x, y=entry_y)
    
    def set_value(self, value):
        self.entry.delete(0, tk.END)  # Mevcut değeri temizle
        self.entry.insert(0, str(value))  # Yeni değeri ekle
#Photo oop
class Photo:
    def __init__(self, window, width_photo, height_photo, bg_photo, photo_cordx, photo_cordy,
                 uzanti, width_bi, height_bi, number1, number2):

        self.image = tk.PhotoImage(file=uzanti, width=width_bi, height=height_bi)
        self.canvas = tk.Canvas(window, width=width_photo, height=height_photo, bg=bg_photo, highlightthickness=0)
        self.canvas.place(relx=photo_cordx, rely=photo_cordy)
        self.canvas.create_image(number1, number2, anchor=tk.NW, image=self.image)


# Button oop
class Button:
    def __init__(self, window, text, ab, bg, fg, af, height, width, font, cordx, cordy):
        self.window = window
        self.button = tk.Button(self.window, text=text, activebackground=ab,
                                bg=bg, fg=fg, activeforeground=af,
                                font=font, height=height, width=width, command=self.buttonFunction)
        self.button.place(relx=cordx, rely=cordy)

    def buttonFunction(self):
        if self.button == but1.button:
            Anapencere()

        elif self.button == but2.button:
            dosya_yolu = filedialog.askopenfilename(defaultextension=".asm", filetypes=[
                                                    ("Assembly Files", ".asm"), ("All Files", ".*")])
            if dosya_yolu:
                with open(dosya_yolu, "r") as dosya:
                    icerik = dosya.read()
                    Anapencere(icerik)
            

#Label oop
class Label:
    def __init__(self,window,text_label,font_label,fg_label,bg_label,label_wrap,label_cordx,label_cordy):
        self.window=window
        self.label=tk.Label(window,text=text_label,font = font_label, fg = fg_label, bg=bg_label,
                            wraplength = label_wrap)
        self.label.place(relx=label_cordx,rely=label_cordy)
#Frame oop
class Frame:
    def __init__(self,window,width_frame,height_frame,bg_frame,frame_cordx,frame_cordy):
        self.window=window
        self.frame=tk.Frame(window, width=width_frame, height=height_frame, bg=bg_frame)
        self.frame.place(relx=frame_cordx, rely=frame_cordy)
#Menubar oop
class MenuBarr:
    def __init__(self, window, menuitems):
        self.window = window
        self.menubar = tk.Menu(window)
        window.config(menu=self.menubar)
        
        for menuitem, submenuitems in menuitems.items():
            self.menulabels = tk.Menu(self.menubar, tearoff=0)
            self.menubar.add_cascade(label=menuitem, menu=self.menulabels)

            for item in submenuitems:
                if item == "-":
                    self.menulabels.add_separator()
                else:
                    self.menulabels.add_command(label=item, command=lambda item=item: self.fileFunction(item))

    def fileFunction(self, menuitem):
        if menuitem == "Exit":
            result = messagebox.askyesno("Exit", "Are you sure you want to exit?")
            if result:
                self.window.destroy()  # Pencereyi kapat
                
        else:
            # Diğer file menü komutlarını buraya ekleyebilirsiniz.
            pass
        



     
        
window = tk.Tk()
window.geometry("1300x900")
window.title("EmuPent")
window.configure(bg="white")
window.resizable(width=False, height=False) 
#Photo
foto = Photo(window, 1000, 1000, "white", 0.30, 0.19, r"C:/Program Files (x86)/Emupent/mcu.jpg", 900, 700, 0, 0)
foto1 = Photo(window, 40, 40, "white", 0.05, 0.399, r"C:/Program Files (x86)/Emupent/open.jpg", 900, 700, 0, 0)
foto2 = Photo(window, 40, 40, "white", 0.05, 0.45, r"C:/Program Files (x86)/Emupent/yeni.jpg", 900, 700, 0, 0)
foto3 = Photo(window, 40, 40, "white", 0.05, 0.503, r"C:/Program Files (x86)/Emupent/last.jpg", 900, 700, 0, 0)
foto4 = Photo(window, 40, 40, "white", 0.05, 0.555, r"C:/Program Files (x86)/Emupent/ex.jpg", 900, 700, 0, 0)
foto5 = Photo(window, 65, 65, "white", 0.909, 0.342, r"C:/Program Files (x86)/Emupent/flow.jpg", 900, 700, 0, 0)
foto6 = Photo(window, 65, 65, "white", 0.904, 0.395, r"C:/Program Files (x86)/Emupent/docu.jpg", 900, 700, 0, 0)
foto7 = Photo(window, 65, 65, "white", 0.904, 0.437, r"C:/Program Files (x86)/Emupent/mc.jpg", 900, 700, 0, 0)
foto8 = Photo(window, 65, 65, "white", 0.912, 0.503, r"C:/Program Files (x86)/Emupent/about.jpg", 900, 700, 0, 0)
#foto1 ve foto8 arasındaki tüm resimler pngegg.com
but1 = Button(window, "New File", "white", "black", "white", "blue", 1, 21, "Courier 13", 0.09, 0.398) 
but2 = Button(window,"Open File","white","black","white","blue",1,21,"Courier 13",0.09, 0.450)
but3 = Button(window,"Open Last","white","black","white","blue",1,21,"Courier 13",0.09, 0.502)
but4 = Button(window,"Examples","white","black","white","blue",1,21,"Courier 13",0.09, 0.555)



but11 = Button(window,"Create a Flowchart","white","black","white","blue",1,21,"Courier 13",0.685,0.346)
but22 = Button(window,"Documentation","white","black","white","blue",1,21,"Courier 13",0.685,0.398)
but33 = Button(window,"About Pentium","white","black","white","blue",1,21,"Courier 13",0.685,0.450)
but44 = Button(window,"About Us","white","black","white","blue",1,21,"Courier 13",0.685,0.502)
#Frame
fra1 = Frame(window,350,120,"black",0.37,0.09)
#labels
lab1 = Label(window,"EmuPent","Courier 30","white","black",300,0.42,0.12)
lab1 = Label(window,"Microprocessor Emulator With Integrated Assembler",
             "Courier 19","black","white",400,0.35,0.735)
#Menubar
oop = MenuBarr(window, {"File": ["New"+" " * 50, "Open", "-", "Save", "Save As...","-","Print","Print As...","-","Example","-","Exit"], 
                        "Edit": ["Undo"+" " * 50, "Redo","-","Cut","Copy","Paste","-",
                                 "Select All","-","Find","Find Next...","Replace...","Go To Line","-","Indent","Outdent","-",
                                 "Comment Block","Uncomment Block","-","Advanced Editor Macros","Advanced"],
                        "Bookmarks": ["Toggle Bookmark"+" " * 50,"-","Previous Bookmark","Next Bookmark","-","Jump To First",
                                      "Jump To Last","-","Clear All Bookmark"],
                        "Assembler": ["Compile"+" " * 50,"Compile And Load In The Emulator","Fasm","-","Set Output Directory"],
                        "Emulator": ["Show Emulator"+" " * 50,"Assemble And Load In The Emulator"],
                        "Math": ["Multi Base Calculator","Base Converter"+" " * 50],
                        "Help": ["Documentation And Tutorials","About"+" " * 50],
                        "ASCII": ["Show Ascii Codes"+" " * 30],
                        })



#######################################################################################################################################################3
#Ana Pancere

class RegisterOperations:
    deneme=""
    value2 = 0   
    
    @classmethod
    def operation_command(cls,operation, command, register_degerleri, flag, process, pointer, stringx):
        try:

            operands = command.split(' ')[1].strip().split(',')  # Komutu boşluklara göre bölelim ve operandları alalım
            operand1 = operands[0].strip()
            operand2 = operands[1].strip()
            operandss = ['EAX', 'EBX','ECX', 'EDX','ESI','EDI']
            operandsH = ['AH', 'BH', 'CH', 'DH']
            operandsL = ['AL', 'BL', 'CL', 'DL']
            operandsX = ['AX', 'BX', 'CX', 'DX','SI']

            value1 = int(register_degerleri.get(operand1, 0), 16)
            if process == 'two_operand':
               
                if operand2 in pointer.keys():   
                    cls.value2 = int(pointer.get(operand2, 0), 16)
                elif operand2 in register_degerleri.keys():   
                    cls.value2 = int(register_degerleri.get(operand2, 0), 16)
            elif process == 'one_operand':
                cls.value2 = int(operand2)
            
            if operation == 'ADD':
                result = hex(value1 + cls.value2)[2:]
            elif operation == 'SUB':
                result = hex(value1 - cls.value2)[2:]
            elif operation == 'XOR':
                result = hex(value1 ^ cls.value2)[2:]
            elif operation == 'OR':
                result = hex(value1 | cls.value2)[2:]
            elif operation == 'AND':
                result = hex(value1 & cls.value2)[2:]
            
            elif operation == 'CMP':
                if value1 > cls.value2:
                    cls.deneme = 'buyuk'
                    loop.EQ(cls.deneme)
                    loop.GEL(cls.deneme)
                elif value1 < cls.value2:
                    cls.deneme = 'kucuk'
                    loop.EQ(cls.deneme)
                    loop.GEL(cls.deneme)
                elif value1 == cls.value2:
                    cls.deneme = 'esit'
                    loop.EQ(cls.deneme)
                    loop.GEL(cls.deneme)
                return cls.deneme

            
            binary_result = bin(int(result, 16))[2:]  #converting binary
            x = len(result)
            number_of_ones = binary_result.count('1')
            
            #SIGN FLAG
            if len(binary_result) == 32 and binary_result[0] == "1":
                flag['SF'] = 1
                if operation == 'CMP' and flag['SF'] == 1:
                    deneme = 'JNS'
                    loop.CMP(deneme)
        
                    
            else:
                flag['SF'] = 0
                if operation == 'CMP' and flag['SF'] == 0:
                   deneme = 'JS'
                   loop.CMP(cls.deneme)
            
                
            #PARITY FLAG    
            if number_of_ones % 2 == 1:   
                flag['PF'] = 0 
            else: 
                flag['PF'] = 1
            #ZERO FLAG
            if result == "0":
                flag['ZF'] = 1
                for operand in operandss:
                    if operand1 == operand:
                        result = result.zfill(8)
                for operand in operandsX:
                    if operand1 in operand:
                        result = result.zfill(4)
                for operand in operandsH:
                    if operand1 in operand:
                        result = result.zfill(2)                        
                for operand in operandsL:
                    if operand1 in operand:
                        result = result.zfill(2)                      
            else:
                flag['ZF'] = 0
            
            binary_value1 = bin(value1)[2:]
            binary_value2 = bin(cls.value2)[2:]            
            bin_value1_32bit = binary_value1.zfill(32)
            bin_value2_32bit = binary_value2.zfill(32)
            bin_result_32bit = binary_result.zfill(32)
            # Overflow
            if (bin_value1_32bit[0] == '1' or bin_value2_32bit[0] == '1') and bin_result_32bit[0] == '0':
                flag['OF'] = 1
                if operation == 'CMP' and flag['OF'] == 1:
                    cls.deneme = 'JNO'
                    loop.CMP(cls.deneme)
               
            elif (bin_value1_32bit[0] == '0' and bin_value2_32bit[0] == '0') and bin_result_32bit[0] == '1':
                flag['OF'] = 1
                if operation == 'CMP' and flag['OF'] == 1:
                    cls.deneme = 'JNO'
                    loop.CMP(cls.deneme)
          
            else:
                flag['OF'] = 0
                if operation == 'CMP' and flag['OF'] == 0:
                    cls.deneme = 'JO'
                    loop.CMP(cls.deneme)
        
            #AUXILIARY CARRY FLAG
            lowbinval1 = bin_value1_32bit[28:]
            lowbinval2 = bin_value2_32bit[28:]
            Low_value1 = int(lowbinval1, 2)
            Low_value2 = int(lowbinval2,2)
            if operation == 'ADD':
                aux_value = Low_value1 + Low_value2
                bin_aux_value = bin(aux_value)[2:]
                if len(bin_aux_value) > 4:
                    flag['AF'] = 1           
            elif operation == 'SUB' and Low_value1 < Low_value2 :
                flag['AF'] = 1
            else:
                flag['AF'] = 0
                  
             
            if x == 9:
                flag['CF'] = 1
                            
            for operand in operandss:
                if operand1 == operand:
                    resulty = result.zfill(8)
                    if operand == 'EAX':
                        register_degerleri['EAX'] =  resulty
                        register_degerleri['AX'] =  resulty[4:]
                        register_degerleri['AH'] =  resulty[4:6]
                        register_degerleri['AL'] =  resulty[6:]
                    if operand == 'EBX':
                        register_degerleri['EBX'] =  resulty
                        register_degerleri['BX'] =  resulty[4:]
                        register_degerleri['BH'] =  resulty[4:6]
                        register_degerleri['BL'] =  resulty[6:]
                    if operand == 'ECX':
                        register_degerleri['ECX'] =  resulty
                        register_degerleri['CX'] =  resulty[4:]
                        register_degerleri['CH'] =  resulty[4:6]
                        register_degerleri['CL'] =  resulty[6:]
                    if operand == 'EDX':
                        register_degerleri['EDX'] =  resulty
                        register_degerleri['DX'] =  resulty[4:]
                        register_degerleri['DH'] =  resulty[4:6]
                        register_degerleri['DL'] =  resulty[6:]    
                    if operand == 'ESI':
                        register_degerleri['ESI'] =  resulty
                        register_degerleri['SI'] = resulty[4:]               
                        if stringx != "":                        
                            point = pointer["[ESI]"] = stringx.get_value(int(register_degerleri['ESI'],16))
                            pointer["[ESI]"] = str(point)
                    if operand == 'EDI':                       
                        register_degerleri['EDI'] =  resulty
                        register_degerleri['DI'] = resulty[4:]
                        if stringx != "":
                            point2 = stringx.get_value(int(register_degerleri['EDI'],16))
                            pointer["[EDI]"] = str(point2)
                    flag['CF'] = 0
            if x > 4:
                for operand in operandsX:
                    if operand1 == operand:
                        resultx = result[1:]
                        if operand == 'AX':
                            register_degerleri['EAX'] =  register_degerleri['EAX'][:4] + resultx 
                            register_degerleri['AX'] =  resultx
                            register_degerleri['AH'] =  resultx[:2]
                            register_degerleri['AL'] =  resultx[2:]
                        if operand == 'BX':
                            register_degerleri['EBX'] =  register_degerleri['EBX'][:4] + resultx 
                            register_degerleri['BX'] =  resultx
                            register_degerleri['BH'] =  resultx[:2]
                            register_degerleri['BL'] =  resultx[2:]
                        if operand == 'CX':
                            register_degerleri['ECX'] =  register_degerleri['ECX'][:4] + resultx 
                            register_degerleri['CX'] =  resultx
                            register_degerleri['CH'] =  resultx[:2]
                            register_degerleri['CL'] =  resultx[2:]
                        if operand == 'DX':
                            register_degerleri['EDX'] =  resultx['EDX'][:4] + resultx 
                            register_degerleri['DX'] =  resultx
                            register_degerleri['DH'] =  resultx[:2]
                            register_degerleri['DL'] =  resultx[2:]
                        if operand == 'SI':
                            register_degerleri['ESI'] =  resultx['ESI'][:4] + resultx 
                            register_degerleri['SI'] = resultx
                        flag['CF'] = 1
            else:        
                for operand in operandsX:
                    if operand1 in operand:
                        resultx = result.zfill(4)
                        if operand == 'AX':
                            register_degerleri['EAX'] =  register_degerleri['EAX'][:4] + resultx 
                            register_degerleri['AX'] =  resultx
                            register_degerleri['AH'] =  resultx[:2]
                            register_degerleri['AL'] =  resultx[2:]
                        if operand == 'BX':
                            register_degerleri['EBX'] =  register_degerleri['EBX'][:4] + resultx 
                            register_degerleri['BX'] =  resultx
                            register_degerleri['BH'] =  resultx[:2]
                            register_degerleri['BL'] =  resultx[2:]
                        if operand == 'CX':
                            register_degerleri['ECX'] =  register_degerleri['ECX'][:4] + resultx 
                            register_degerleri['CX'] =  resultx
                            register_degerleri['CH'] =  resultx[:2]
                            register_degerleri['CL'] =  resultx[2:]
                        if operand == 'DX':
                            register_degerleri['EDX'] =  resultx['EDX'][:4] + resultx 
                            register_degerleri['DX'] =  result
                            register_degerleri['DH'] =  resultx[:2]
                            register_degerleri['DL'] =  resultx[2:]
                        flag['CF'] = 0
            if x>2:
                for operand in operandsH:
                    if operand1 in operand:
                        resultz = result[1:]
                        if operand == 'AH':
                            register_degerleri['EAX'] =  register_degerleri['EAX'][:4] + resultz + register_degerleri['EAX'][6:]
                            register_degerleri['AX'] =  resultz + register_degerleri['EAX'][6:]
                            register_degerleri['AH'] =  resultz
                            register_degerleri['AL'] =  register_degerleri['EAX'][6:]
                        if operand == 'BH':
                            register_degerleri['EBX'] =  register_degerleri['EBX'][:4] + resultz + register_degerleri['EBX'][6:]
                            register_degerleri['BX'] =  resultz + register_degerleri['EBX'][6:]
                            register_degerleri['BH'] =  resultz
                            register_degerleri['BL'] =  register_degerleri['EBX'][6:]
                        if operand == 'CH':
                            register_degerleri['ECX'] =  register_degerleri['ECX'][:4] + resultz + register_degerleri['EDX'][6:]
                            register_degerleri['CX'] =  resultz + register_degerleri['ECX'][6:]
                            register_degerleri['CH'] =  resultz
                            register_degerleri['CL'] =  register_degerleri['ECX'][6:]
     
                        if operand == 'DH':
                            register_degerleri['EDX'] =  register_degerleri['EDX'][:4] + resultz + register_degerleri['EDX'][6:]
                            register_degerleri['DX'] =  resultz + register_degerleri['EDX'][6:]
                            register_degerleri['DH'] =  resultz
                            register_degerleri['DL'] =  register_degerleri['EDX'][6:]
                        flag['CF'] = 1
                for operand in operandsL:
                    if operand1 in operand:
                        resultw = result[1:]
                        if operand == 'AL':
                            register_degerleri['EAX'] =  register_degerleri['EAX'][:6] + resultw 
                            register_degerleri['AX'] =  register_degerleri['EAX'][4:6] + resultw
                            register_degerleri['AH'] =  register_degerleri['EAX'][4:6]
                            register_degerleri['AL'] =  resultw
                        if operand == 'BL':
                            register_degerleri['EBX'] =  register_degerleri['EBX'][:6] + resultw
                            register_degerleri['BX'] =  register_degerleri['EBX'][4:6] + resultw
                            register_degerleri['BH'] =  register_degerleri['EBX'][4:6]
                            register_degerleri['BL'] =  resultw
                        if operand == 'CL':
                            register_degerleri['ECX'] =  register_degerleri['ECX'][:6] + resultw 
                            register_degerleri['CX'] =  register_degerleri['ECX'][4:6] + resultw
                            register_degerleri['CH'] =  register_degerleri['ECX'][4:6]
                            register_degerleri['CL'] =  resultw
                        if operand == 'DL':
                            register_degerleri['EDX'] =  register_degerleri['EDX'][:6] + resultw 
                            register_degerleri['DX'] =  register_degerleri['EDX'][4:6] + resultw
                            register_degerleri['DH'] =  register_degerleri['EDX'][4:6]
                            register_degerleri['DL'] =  resultw
                        flag['CF'] = 1
            else: 
                for operand in operandsH:
                    if operand1 in operand:
                        resultz = result.zfill(2)
                        if operand == 'AH':
                            register_degerleri['EAX'] =  register_degerleri['EAX'][:4] + resultz + register_degerleri['EAX'][6:]
                            register_degerleri['AX'] =  resultz + register_degerleri['EAX'][6:]
                            register_degerleri['AH'] =  resultz
                            register_degerleri['AL'] =  register_degerleri['EAX'][6:]
                        if operand == 'BH':
                            register_degerleri['EBX'] =  register_degerleri['EBX'][:4] + resultz + register_degerleri['EBX'][6:]
                            register_degerleri['BX'] =  resultz + register_degerleri['EBX'][6:]
                            register_degerleri['BH'] =  resultz
                            register_degerleri['BL'] =  register_degerleri['EBX'][6:]
                        if operand == 'CH':
                            register_degerleri['ECX'] =  register_degerleri['ECX'][:4] + resultz + register_degerleri['EDX'][6:]
                            register_degerleri['CX'] =  resultz + register_degerleri['ECX'][6:]
                            register_degerleri['CH'] =  resultz
                            register_degerleri['CL'] =  register_degerleri['ECX'][6:]
     
                        if operand == 'DH':
                            register_degerleri['EDX'] =  register_degerleri['EDX'][:4] + resultz + register_degerleri['EDX'][6:]
                            register_degerleri['DX'] =  resultz + register_degerleri['EDX'][6:]
                            register_degerleri['DH'] =  resultz
                            register_degerleri['DL'] =  register_degerleri['EDX'][6:]
          
                for operand in operandsL:
                    if operand1 in operand:
                        resultw = result.zfill(2)
                        if operand == 'AL':
                            register_degerleri['EAX'] =  register_degerleri['EAX'][:6] + resultw 
                            register_degerleri['AX'] =  register_degerleri['EAX'][4:6] + resultw
                            register_degerleri['AH'] =  register_degerleri['EAX'][4:6]
                            register_degerleri['AL'] =  resultw
                        if operand == 'BL':
                            register_degerleri['EBX'] =  register_degerleri['EBX'][:6] + resultw
                            register_degerleri['BX'] =  register_degerleri['EBX'][4:6] + resultw
                            register_degerleri['BH'] =  register_degerleri['EBX'][4:6]
                            register_degerleri['BL'] =  resultw
                        if operand == 'CL':
                            register_degerleri['ECX'] =  register_degerleri['ECX'][:6] + resultw 
                            register_degerleri['CX'] =  register_degerleri['ECX'][4:6] + resultw
                            register_degerleri['CH'] =  register_degerleri['ECX'][4:6]
                            register_degerleri['CL'] =  resultw
                        if operand == 'DL':
                            register_degerleri['EDX'] =  register_degerleri['EDX'][:6] + resultw 
                            register_degerleri['DX'] =  register_degerleri['EDX'][4:6] + resultw
                            register_degerleri['DH'] =  register_degerleri['EDX'][4:6]
                            register_degerleri['DL'] =  resultw
                                
        except IndexError:
            print("Error: Not enough operands")
        except ValueError as e:
            print(f"Error: {e}")

class divide:
    def dividex(self, operation, command, register_degerleri):
        try:
            operand = command.split(' ')[1].strip()
            divisor = int(register_degerleri.get(operand, 0), 16)
            if divisor == 0:
                raise ValueError("Error: Division by zero")
            
            value1 = int(register_degerleri.get('EAX', 0), 16)
            register_degerleri['EAX'] ='{:08x}'.format(value1 // divisor)
            register_degerleri['EDX'] ='{:08x}'.format(value1 % divisor)
            


        except IndexError:
            print("Error: Not enough operands")
        except ValueError as e:
            print(f"Error: {e}")
            
            
class mul:
    def mulx(self, operation, command, register_degerleri):
        try:
            operand = command.split(' ')[1].strip()
            multiplier = int(register_degerleri.get(operand, 0), 16) 
            value1 = int(register_degerleri.get('EAX', 0), 16)
            register_degerleri['EAX'] ='{:08x}'.format(value1 * multiplier)
        except IndexError:
            print("Error: Not enough operands")
        except ValueError as e:
            print(f"Error: {e}")            
  
            
class bitwise_not:
    def notx(self, operation, command, register_degerleri):
        try:
            operand = command.split(' ')[1].strip()
            value = int(register_degerleri.get(operand, 0), 16)

            result = format((~value & 0xFFFFFFFF), '08x')
            result = result.lstrip('f')
            register_degerleri[operand] = result

        except IndexError:
            print("Error: Not enough operands")
        except ValueError as e:
            print(f"Error: {e}")


multiplier = mul()        
register_operations = RegisterOperations()
divider = divide()
bitwise = bitwise_not()
            
class entryregister:
    def registerlists(register_degerlerix,name1,name2,name3):
        register_str = str(register_degerlerix)
        register_list11 = list(register_str)
        register_list1 = [letter.upper() for letter in register_list11]
        while len(register_list1) < 8:
            register_list1.insert(0, '0')
        register_list = ''.join(register_list1)
        a = len(register_list)
        if a < 9:
            if a<3:
                name1.set_value(register_list[(a+4):(a+6)])
                name2.set_value(register_list[(a+2):(a+4)])
                name3.set_value(register_list[:(a+2)]) 
            elif a<5:
                name1.set_value(register_list[(a-2):a]) 
                name2.set_value(register_list[a:(a+2)])
                name3.set_value(register_list[:(a)]) 
            else:
                name1.set_value(register_list[(a-2):a])
                name2.set_value(register_list[(a-4):(a-2)])
                name3.set_value(register_list[:(a-4)])     
        else:
            print("Value of register can not be greater than 32 bits")
class entryrindex:
    def registerlists(register_degerlerix,name1,name2):
        register_str = str(register_degerlerix)
        register_list11 = list(register_str)
        register_list1 = [letter.upper() for letter in register_list11]
        while len(register_list1) < 8:
            register_list1.insert(0, '0')
        register_list = ''.join(register_list1)
        a = len(register_list)
        if a < 9:
            if a<5:
                name1.set_value(register_list[(a-4):a]) 
                name2.set_value(register_list[a:(a+4)])

            else:
                name1.set_value(register_list[(a-4):a])
                name2.set_value(register_list[(a-8):(a-4)]) 
        else:
            print("Value of register can not be greater than 32 bits")
            
class entryflag:
    def flag(self, flag, name):
        name.set_value(flag)
        
entryflag_instance = entryflag()         

def easyforregistersavinglist(line_upper): 
    try:
        pass
    except (ValueError, IndexError) as e:
        print(f"Error: {e}")
        print("No valid number value entered or invalid format t")
        return None


def easyforregistersavingAdress(registernameInd,EX,X,line_upper, register_degerleri): 
    try:
        stringofregister = line_upper.split(registernameInd)[1].strip()  # get the EAX    
        deger = int(stringofregister)  # get the EAX    
        b = '{:08x}'.format(deger)
        c=b[2:]
        return c
    except (ValueError, IndexError) as e:
        print(f"Error: {e}")
        print("No valid number value entered or invalid format t")

def easyforregistersavingIndex(registernameInd,EX,X,line_upper, register_degerleri, pointer): 
    try:
        stringofregister = line_upper.split(registernameInd)[1].strip()  # get the EX    
        if stringofregister in register_degerleri:  # check if the value is another register
            deger = int(register_degerleri[stringofregister], 16)  # get the value from the other register
        elif stringofregister.endswith("H"):
            deger = int(stringofregister[:-1], 16)
        elif stringofregister.endswith("B"):
            deger = int(stringofregister[:-1], 2)
        else:
            deger = int(stringofregister)  # get the EX         
        b = '{:08x}'.format(deger)
        register_degerleri[EX] = b
        register_degerleri[X] = b[4:]
        if EX == "EDI" and stringofregister == "ESI":
            pointer['[EDI]'] = pointer['[ESI]']
       
        return b
        
            
    except (ValueError, IndexError) as e:
        print(f"Error: {e}")
        print("No valid number value entered or invalid format t")
        
def easyforregistersavingEX(registernameEX, EX, X, H, L, line_upper, register_degerleri, pointer): 
    try:  
        stringofregister = line_upper.split(registernameEX)[1].strip()  # get the EX    
        if stringofregister == "[ESI]":    
            deger = int(pointer["[ESI]"],16)
        elif stringofregister == "[EDI]":
            deger = int(pointer["[EDI]"],16)
        elif stringofregister == "[SI]":    
            deger = int(pointer["[SI]"],16)
        elif stringofregister == "[DI]":
            deger = int(pointer["[DI]"],16)
        elif stringofregister.endswith("H"):
            deger = int(stringofregister[:-1], 16)
        elif stringofregister.endswith("B"):
            deger = int(stringofregister[:-1], 2)
        else:
            deger = int(stringofregister)  # get the EX         
        b = '{:08x}'.format(deger)
        register_degerleri[EX] = b
        register_degerleri[X] = b[4:]
        register_degerleri[L] = b[6:]
        register_degerleri[H] = b[4:6]              
    except (ValueError, IndexError) as e:
        print(f"Error: {e}")
        print("No valid number value entered or invalid format to be assigned to 16 bit register.")

def easyforregistersavingX(registernameX, EX, X, H, L, line_upper, register_degerleri, pointer):
    try:
      
       stringofregister = line_upper.split(registernameX)[1].strip()  # get the EAX    
 
       if stringofregister == "[ESI]":    
           deger = int(pointer["[ESI]"],16)
       elif stringofregister == "[EDI]":
           deger = int(pointer["[EDI]"],16)
       elif stringofregister == "[SI]":    
           deger = int(pointer["[SI]"],16)
       elif stringofregister == "[DI]":
           deger = int(pointer["[DI]"],16)
       elif stringofregister.endswith("H"):
           deger = int(stringofregister[:-1], 16)
       elif stringofregister.endswith("B"):
           deger = int(stringofregister[:-1], 2)
       else:
           deger = int(stringofregister)  # get the EX  
       a = '{:04x}'.format(deger) 
       if register_degerleri[EX] is None or register_degerleri[EX] == '00000000':
           register_degerleri[EX] = '00000000'
       c = register_degerleri[EX][:4]              
       register_degerleri[EX] = c+a
       register_degerleri[X] = a
       register_degerleri[L] = a[2:]
       register_degerleri[H] = a[:2]
    except (ValueError, IndexError) as e:
        print(f"Error: {e}")
        print("No valid number value entered or invalid format to be assigned to 16 bit register.")

def easyforregistersavingL(registernameL, EX, X, H, L, line_upper, register_degerleri, pointer):
    try:
       stringofregister = line_upper.split(registernameL)[1].strip()  # get the EAX    
       if stringofregister == "[ESI]":    
           deger = int(pointer["[ESI]"],16)
       elif stringofregister == "[EDI]":
           deger = int(pointer["[EDI]"],16)
       elif stringofregister == "[SI]":    
           deger = int(pointer["[SI]"],16)
       elif stringofregister == "[DI]":
           deger = int(pointer["[DI]"],16)
       elif stringofregister.endswith("H"):
           deger = int(stringofregister[:-1], 16)
       elif stringofregister.endswith("B"):
           deger = int(stringofregister[:-1], 2)
       else:
           deger = int(stringofregister)  # get the EX                    
       e = '{:02x}'.format(deger)
       if register_degerleri[EX] is None or register_degerleri[EX] == '00000000':
           register_degerleri[EX] = '00000000'
       if register_degerleri[X] is None or register_degerleri[EX] == '0000':
           register_degerleri[X] = '0000'
       c = register_degerleri[EX][:4]
       d = register_degerleri[X][:2]
       register_degerleri[EX] = c+d+e
       register_degerleri[X] = d+e
       register_degerleri[L] = e
    except (ValueError, IndexError) as e:
        print(f"Error: {e}")
        print("No valid number value entered or invalid format to be assigned to 16 bit register.")
 
        
def easyforregistersavingH(registernameH, EX, X, H, L, line_upper, register_degerleri, pointer):
    try:
       stringofregister = line_upper.split(registernameH)[1].strip()  # get the EAX    
       if stringofregister == "[ESI]":    
           deger = int(pointer["[ESI]"],16)
       elif stringofregister == "[EDI]":
           deger = int(pointer["[EDI]"],16)
       elif stringofregister == "[SI]":    
           deger = int(pointer["[SI]"],16)
       elif stringofregister == "[DI]":
           deger = int(pointer["[DI]"],16)
       elif stringofregister.endswith("H"):
           deger = int(stringofregister[:-1], 16)
       elif stringofregister.endswith("B"):
           deger = int(stringofregister[:-1], 2)
       else:
           deger = int(stringofregister)  # get the EX   
       f = '{:02x}'.format(deger)
       if register_degerleri[EX] is None or register_degerleri[EX] == '00000000':
           register_degerleri[EX] = '00000000'
       if register_degerleri[X] is None or register_degerleri[EX] == '0000':
           register_degerleri[X] = '0000'
       c = register_degerleri[EX][:4]
       d = register_degerleri[X][2:]
       register_degerleri[EX] = c+f+d
       register_degerleri[X] = f+d
       register_degerleri[H] = f
    except (ValueError, IndexError) as e:
        print(f"Error: {e}")
        print("No valid number value entered or invalid format to be assigned to 16 bit register.") 

class string:
    data = []
    data2 = ""
    y = []
    string = ""
    string_dict = {}  # Define a class attribute to store the dictionary
    numberofindex = ""
    memory_val1 = 0
    memory_val2 = 0
    memory_val3 = 0
    digit= ""
    kara=""
    x = 0
    result = ""

    
    
    @classmethod
    def op_string(cls, process, entry_list, i, values_of_registers, line, line_upper, texteditor, custom_console, window2, pointer,variable):
        if process == 'set_string':
            if line_upper[-1] == "'" and line_upper[-2] == "$":                
                ilk_tırnak_index = line.find("'")  # İlk tek tırnak işaretinin indeksini bul
                if ilk_tırnak_index != -1:  # İlk tek tırnak işareti bulunduysa
                    dolar_index = line.find("$", ilk_tırnak_index + 1)  # İkinci tek tırnak işaretinin indeksini bul
                cls.data.append(line_upper.split()[0])  # msg ifadesi                   
                cls.y.append(line[ilk_tırnak_index + 1:dolar_index])
                cls.string_dict = {"data": cls.y}  # Assign the dictionary to the class attribute
                cls.memory_val1 = memory.saving_memory('DB1', texteditor, cls.data, cls.y)  #DB1 for setstring
            else:
                print("Syntax of string is wrong")
        elif process == 'propertiesofstring':           
            cls.string = line_upper.split()[0]
            a = line_upper.index("DB") + 3  
            b = line.find(",",a)
            cls.numberofindex = line[a:b].strip()
        
            c = line.find(",",b+1)
            cls.question = line[b+1:c].strip()
        
            
            dup_index = line_upper.find("DUP")

            # Eğer "dup" bulunduysa
            if dup_index != -1:
                # "dup"tan sonraki ifadeyi al
                nextofdup = line_upper[dup_index + len("DUP"):].strip()

                # Eğer sonraki ifade "$" ile bitiyorsa veya boş ise
                if nextofdup == "('$')":
                   
                    parcalar = line_upper.split()
         
                    for parca in parcalar:     
                        if parca == "DUP": 
                            break
                        elif parca.isdigit():     # "dup" kelimesinden önceki ilk ifadeyi bul
                            cls.digit = parca
                    if cls.digit:
                        cls.memory_val2 = memory.saving_memory('DB2', texteditor, cls.data, cls.y)    #DB2 for prop of string
                
                    
            elif line_upper.endswith("'$'"):
                cls.dollar = line[c+2].strip()
                cls.memory_val3 = memory.saving_memory('DB3', texteditor, cls.data, cls.y)    #DB3 for prop of string
                
        elif process == 'EDX':
            offset = "OFFSET"
            index = line_upper.find(offset)
            if index != -1:  # Eğer 'OFFSET' bulunduysa
                a = index + len(offset)
                while a < len(line_upper) and line_upper[a].isspace():
                    a += 1
                cls.result = line_upper[a:].split()[0]  # 'OFFSET' sonrasındaki ilk kelimeyi al
           
            else:
                print("OFFSET not found in line")

            if cls.result == cls.data:                
                values_of_registers["EDX"] = hex(cls.memory_val1)[2:]
            elif cls.result == cls.string and cls.digit == ""    :
                values_of_registers["EDX"] = hex(cls.memory_val3)[2:]
            elif cls.result == cls.string:
                values_of_registers["EDX"] = hex(cls.memory_val2)[2:]
                
        elif process == 'print': 
            a=0
            var = cls.data.index(cls.result) + 1
            while a < var:
               a+=1
            
            print(cls.y[a-1])     
     
            
        elif process == 'scanf':
            a=input()
            kara=a
            cls.y.append(a)
            if values_of_registers['ESI'] == None:
                values_of_registers['ESI'] = "9"
                ad = int(values_of_registers['ESI'],16)
            else:
                ad = int(values_of_registers['ESI'],16)
                        
            q = MetinSinifi(kara,ad)
            cls.x = q.get_value(ad)
       
            pointer["[ESI]"] = cls.x
            return q
            

class MetinSinifi():
    def __init__(self, metin, bas):
        self.metin = metin
        self.bas = bas
        self.liste = [0] * (2**20)
        
        # Eğer metin bir string ise ASCII kodlarına dönüştürerek listeye ekleyin
        if isinstance(self.metin, str):
            for j in range(len(metin)):
                self.liste[bas + j] = hex(ord(metin[j]))[2:]  # ord() fonksiyonu karakteri ASCII koduna dönüştürür
            
        # Eğer metin bir integer ise ASCII koduna dönüştürerek listeye ekleyin
        elif isinstance(self.metin, int):
            self.liste[bas] = hex(self.metin)[2:]
            
            
    def get_value(self, index):
        # Belirli bir indeksteki değeri döndürür
        if index < len(self.liste):
            return self.liste[index]
        else:
            print("Unvalid index!")

  

            
class memory:
    @staticmethod
    def saving_memory(operation, texteditor, data, y):
        metin = texteditor.get("1.0", tk.END).strip()  # get metin from the text widget, clean the spaces at first and end
        lines = metin.split('\n')  # seperate rows
        counter = 4096
        if operation == 'DB1':
            memory_val = counter
            return memory_val
        elif operation == 'DB2':
            memory_val = counter + 16
            return memory_val
        elif operation == 'DB3':
            memory_val = counter + 256
            return memory_val
        
       
        # registerlar için de buraya yazarız
class loop:
    dt=""
    et=""
    
    
    @classmethod
    def op_loop(cls, process, index_i, line, line_upper, text_editor, window2, start_index, x):
        lines = text_editor.get("1.0", "end").split('\n')
        index_i = lines.index(line) + 1
        
        if process == 'C2' and  loop.dt == "GE"  :
                offset = "JGE"
                index = line_upper.find(offset)
                return for_loops.forloops(index, offset, line_upper, lines)  
    
        if process == 'C3' and loop.dt == "L":
                offset = "JL" 
                index = line_upper.find(offset)
                return for_loops.forloops(index, offset, line_upper, lines)
            
        if process == 'C6' and loop.et == "NE":
            offset = "JNE" 
            index = line_upper.find(offset)
            return for_loops.forloops(index, offset, line_upper, lines)
        
        if process == 'C5' and loop.dt == "MP":
                offset = "JMP" 
                index = line_upper.find(offset)
                return for_loops.forloops(index, offset, line_upper, lines)  
        else:
            return index_i-1
    @classmethod
    def GEL(cls,wht):
        if wht == 'kucuk':  # wht değeri "buyuk" veya "esit" değilse
            cls.dt = "L"
        else:
            cls.dt = "GE"
        return cls.dt
    @classmethod    
    def EQ(cls,wht):
        if wht == 'esit':
            cls.et = "E"
        else:
            cls.et = "NE"
        return cls.et
    @classmethod  
    def JMP(cls,wht):
        if wht == "JMP":
            cls.dt = "MP"
            return cls.dt
     
            
     
        
class for_loops:
    def forloops(index, offset, line_upper, lines):
        if index != -1:
            i = index + len(offset)
            while i < len(line_upper) and line_upper[i].isspace():
                i += 1
            result = line_upper[i:].split()[0]
        
            found = False
            index_i = 0
            for lines[0] in lines:
                if found:
                    break
                if (result + ":").lower() in lines[index_i]:
                        found = True
                index_i += 1
                
            if not found:
                print(f"{result}: not found in the text editor") 
            return index_i-1
        else:
            print("OFFSET not found in line")                               
            return index_i       
        
    

class registersaving:

    def save_register(entry_list, text_editor, custom_console, window2, start_index = 0):
        metin = text_editor.get("1.0", tk.END).strip()  # get metin from the text widget, clean the spaces at first and end
        lines = metin.split('\n')  # seperate rows
        register_degerleri = {"EAX": None, "EBX": None, "ECX": None, "EDX": None, "AX": None, "BX": None, "CX": None, "DX": None, "AH": None, "BH": None, "CH": None, "DH": None, "AL": None, "BL": None, "CL": None, "DL": None, "ESI" : None, "EDI" : None}
        pointers = { "[ESI]" : None, "[EDI]" : None}
        a = ""
        flags = {"CF" : 0, "PF": 0, "AF": 0, "ZF": 0, "SF": 0, "OF": 0, "TF": 0, "IF": 0}  #EKLENECEKLER VAR
        i = 0
        variable =0 
        
        while i < len(lines):
         
            line = lines[i]
          
            line_upper = line.upper()
            found_code = False
            linex = line
            line_upperx = linex.upper()
          
            if ".DATA" in line_upperx:
                for linex in lines:
                    line_upperx = linex.upper()
                    if "DB" in line_upperx and line_upperx.count("'") == 2 and line_upperx.count(",") == 2  :                                                                
                            string.op_string('propertiesofstring', entry_list, i, register_degerleri, linex, line_upperx, text_editor, custom_console, window2, pointers,variable)
                    elif "DB" in line_upperx and line_upperx.count("'") == 2:                             
                            string.op_string('set_string', entry_list, i, register_degerleri, linex, line_upperx, text_editor, custom_console, window2, pointers,variable)
                    if ".CODE" in line_upperx:
                        found_code = False
                        break
                    else:
                        found_code = True
                    i += 1                  
                if found_code:
                    break
                    
            elif "MOV EDX,OFFSET" in line_upper:           
                string.op_string('EDX', entry_list, i, register_degerleri,line, line_upper, text_editor, custom_console, window2, pointers,variable)
        
            elif "MOV EAX," in line_upper:
                easyforregistersavingEX("MOV EAX,", "EAX", "AX", "AH", "AL", line_upper, register_degerleri, pointers)
            elif "MOV AX," in line_upper:
                easyforregistersavingX("MOV AX,", "EAX", "AX", "AH", "AL", line_upper, register_degerleri, pointers)
            elif "MOV AH," in line_upper:
                easyforregistersavingH("MOV AH,", "EAX", "AX", "AH", "AL", line_upper, register_degerleri, pointers) 
            elif "MOV AL," in line_upper:
                easyforregistersavingL("MOV AL,", "EAX", "AX", "AH", "AL", line_upper, register_degerleri, pointers)     
            elif "MOV EBX," in line_upper:
                easyforregistersavingEX("MOV EBX,", "EBX", "BX", "BH", "BL", line_upper, register_degerleri, pointers)
            elif "MOV BX," in line_upper:
                easyforregistersavingX("MOV BX,","EBX", "BX", "BH", "BL", line_upper, register_degerleri, pointers)
            elif "MOV BH," in line_upper:
                easyforregistersavingH("MOV BH,", "EBX", "BX", "BH", "BL", line_upper, register_degerleri, pointers)    
            elif "MOV BL," in line_upper:
                easyforregistersavingL("MOV BL,","EBX", "BX", "BH", "BL", line_upper, register_degerleri, pointers) 
            elif "MOV ECX," in line_upper:
                easyforregistersavingEX("MOV ECX,", "ECX", "CX", "CH", "CL", line_upper, register_degerleri, pointers)
            elif "MOV CX," in line_upper:
                easyforregistersavingX("MOV CX,", "ECX", "CX", "CH", "CL", line_upper, register_degerleri, pointers)
            elif "MOV CH," in line_upper:
                easyforregistersavingH("MOV CH,", "ECX", "CX", "CH", "CL", line_upper, register_degerleri, pointers)
            elif "MOV CL," in line_upper:
                easyforregistersavingL("MOV CL,", "ECX", "CX", "CH", "CL", line_upper, register_degerleri, pointers) 
            elif "MOV EDX," in line_upper:
                easyforregistersavingEX("MOV EDX,", "EDX", "DX", "DH", "DL", line_upper, register_degerleri, pointers)
            elif "MOV DX," in line_upper:
                easyforregistersavingX("MOV DX,", "EDX", "DX", "DH", "DL", line_upper, register_degerleri, pointers)
            elif "MOV DH," in line_upper:
                easyforregistersavingH("MOV DH,", "EDX", "DX", "DH", "DL", line_upper, register_degerleri, pointers)
            elif "MOV DL," in line_upper:
                easyforregistersavingL("MOV DL,", "EDX", "DX", "DH", "DL", line_upper, register_degerleri, pointers) 
            elif "MOV ESI," in line_upper:
                cagir=int(easyforregistersavingIndex("MOV ESI,", "ESI", "SI",line_upper, register_degerleri, pointers),16)
                string.x = cagir
          
            
            

                
             

                
            elif "MOV EDI," in line_upper:
                    cagir1=int(easyforregistersavingIndex("MOV EDI,", "EDI", "DI",line_upper, register_degerleri, pointers),16)
                    string.x = cagir1
            elif "MOV [EDI]," in line_upper:
                    bagir1=easyforregistersavingAdress("MOV [EDI],", "[EDI]", "[DI]",line_upper, register_degerleri)
                    MetinSinifi(bagir1,cagir1)

        


                
            
     



            elif "CMP" in line_upper:
                x = register_operations.operation_command('CMP', line_upper, register_degerleri,flags, 'two_operand',pointers, a)
            
             
            elif "JGE" in line_upper:
                i = loop.op_loop('C2',i, line, line_upper, text_editor, window2, start_index,x) 
            elif "JG" in line_upper:
                i = loop.op_loop('C1',i, line, line_upper, text_editor, window2, start_index, x)
            elif "JL" in line_upper:
                i = loop.op_loop('C3',i, line, line_upper, text_editor, window2, start_index, x)
            elif "JLE" in line_upper:
                i = loop.op_loop('C4',i, line, line_upper, text_editor, window2, start_index, x) 
            elif "JNG" in line_upper:
                i = loop.op_loop('C4',i, line, line_upper, text_editor, window2, start_index, x) 
            elif "JNGE" in line_upper:
                i = loop.op_loop('C3',i, line, line_upper, text_editor, window2, start_index, x) 
            elif "JNL" in line_upper:
                i = loop.op_loop('C2',i, line, line_upper, text_editor, window2, start_index, x) 
            elif "JNLE" in line_upper:
                i = loop.op_loop('C1',i, line, line_upper, text_editor, window2, start_index, x)
            elif "JNE" in line_upper:
                i = loop.op_loop('C6',i, line, line_upper, text_editor, window2, start_index, x) 
            elif "JO" in line_upper:
                i = loop.op_loop("O",i, line, line_upper, text_editor, window2, start_index, x) 
            elif "JNO" in line_upper:
                i = loop.op_loop("NO",i, line, line_upper, text_editor, window2, start_index, x) 
            elif "JS" in line_upper:
                i = loop.op_loop("S",i, line, line_upper, text_editor, window2, start_index, x) 
            elif "JNS" in line_upper:
                i = loop.op_loop("NS",i, line, line_upper, text_editor, window2, start_index, x) 
            elif "JMP" in line_upper:
                x = loop.JMP('JMP')
                i = loop.op_loop('C5',i, line, line_upper, text_editor, window2, start_index, 'JMP')
            
                
                
            #loop
            elif "ADD" in line_upper:
                register_operations.operation_command('ADD', line_upper, register_degerleri,flags, 'two_operand', pointers, a)
            elif "SUB" in line_upper:
                register_operations.operation_command('SUB', line_upper, register_degerleri,flags, 'two_operand', pointers, a)
            elif "AND" in line_upper:
                register_operations.operation_command('AND', line_upper, register_degerleri,flags, 'two_operand', pointers, a)
            elif "XOR" in line_upper:
                register_operations.operation_command('XOR', line_upper, register_degerleri,flags, 'two_operand', pointers, a)
            elif "OR" in line_upper:
                register_operations.operation_command('OR', line_upper, register_degerleri,flags, 'two_operand', pointers, a)
            elif "MUL" in line_upper:
                multiplier.mulx('MUL', line_upper, register_degerleri)
            elif "NOT" in line_upper:
                bitwise.notx('NOT', line_upper, register_degerleri)
            elif "DIV" in line_upper:
                divider.dividex('DIV', line_upper, register_degerleri)
            elif "INC" in line_upper:
                line_upperx = line_upper.rstrip() + ",1"
                register_operations.operation_command('ADD', line_upperx, register_degerleri,flags, 'one_operand', pointers, a) 
            elif "DEC" in line_upper:
                line_upperx = line_upper.rstrip() + ",1"
                register_operations.operation_command('SUB', line_upperx, register_degerleri,flags, 'one_operand', pointers, a)
            
            
                

            elif 'INT 33H' in line_upper and int(register_degerleri["EAX"]) == 0:
                print('MOUSE interrupt active')
                for j in range(i+1, len(lines)):
                    next_line_upper = lines[j].upper()
                    if 'INT 33H' in next_line_upper:
                        if int(register_degerleri["EAX"]) == 1:
                            print('MOUSE cursor active')
                            tk.canvas.config(cursor="arrow")
                        elif int(register_degerleri["EAX"]) == 2:
                            print('MOUSE cursor inactive')
                        break
            elif 'INT 21H' in line_upper and (register_degerleri["AH"]) == '09':                
                string.op_string('print', entry_list, i, register_degerleri, line, line_upper, text_editor, custom_console, window2, pointers,variable)
                variable += 1
            elif 'INT 21H' in line_upper and (register_degerleri["AH"]) == '0a':                                
                a = string.op_string('scanf', entry_list, i, register_degerleri, line, line_upper, text_editor, custom_console, window2, pointers,variable)
                variable += 1
                 
            i += 1
                
                
        entryregister.registerlists(register_degerleri["EAX"],entry_list[2],entry_list[1],entry_list[0])
        entryregister.registerlists(register_degerleri["EBX"],entry_list[5],entry_list[4],entry_list[3])
        entryregister.registerlists(register_degerleri["ECX"],entry_list[8],entry_list[7],entry_list[6])
        entryregister.registerlists(register_degerleri["EDX"],entry_list[11],entry_list[10],entry_list[9]) 
        entryrindex.registerlists(register_degerleri["ESI"],entry_list[13],entry_list[12])
        entryrindex.registerlists(register_degerleri["EDI"],entry_list[15],entry_list[14])
        
        entryflag_instance.flag(flags["CF"], entry_list[28])
        entryflag_instance.flag(flags["PF"], entry_list[29])
        entryflag_instance.flag(flags["AF"], entry_list[30])
        entryflag_instance.flag(flags["ZF"], entry_list[31])
        entryflag_instance.flag(flags["SF"], entry_list[32])
        entryflag_instance.flag(flags["OF"], entry_list[33])
                           
        
class txt():
    def __init__(self,icerik1,textEditor1):
        self.textEditor1 = textEditor1
        if icerik1:

            self.textEditor1.insert("1.0", icerik1)
        else:
            pass

class CustomConsole:
    def __init__(self, console_text_widget):
        self.console_text = console_text_widget

    def write(self, text):
        self.console_text.insert(tk.END, text)
        self.console_text.see(tk.END)  # shift to left

class CodeRunner:
    def __init__(self, oopEntryList, textEditor, console_text, window):
        self.oopEntryList = oopEntryList
        self.textEditor = textEditor
        self.console_text = console_text
        self.window = window

    def run_code(self, index=0):
        registersaving.save_register(self.oopEntryList, self.textEditor, self.console_text, self.window, index)



        
def Anapencere(icerik=None):
    window2 = tk.Toplevel() 
    window2.geometry("1440x960")
    window2.title("New File Window")
    #Menubar
    oop2 = MenuBarr(window2, {"File": ["New"+" " * 50, "Open", "-", "Save", "Save As...","-","Print","Print As...","-","Example","-","Exit"], 
                              "Edit": ["Undo"+" " * 50, "Redo","-","Cut","Copy","Paste","-",
                                       "Select All","-","Find","Find Next...","Replace...","Go To Line","-","Indent","Outdent","-",
                                       "Comment Block","Uncomment Block","-","Advanced Editor Macros","Advanced"],
                              "Bookmarks": ["Toggle Bookmark"+" " * 50,"-","Previous Bookmark","Next Bookmark","-","Jump To First",
                                            "Jump To Last","-","Clear All Bookmark"],
                              "Assembler": ["Compile"+" " * 50,"Compile And Load In The Emulator","Fasm","-","Set Output Directory"],
                              "Emulator": ["Show Emulator"+" " * 50,"Assemble And Load In The Emulator"],
                              "Math": ["Multi Base Calculator","Base Converter"+" " * 50],
                              "Help": ["Documentation And Tutorials","About"+" " * 50],
                              "ASCII": ["Show Ascii Codes"+" " * 30],
                              })
    upper_frame = tk.Frame(window2, height=100, bg="white")
    upper_frame.pack(side="top", fill="x")

    pw = ttk.Panedwindow(window2, orient = tk.HORIZONTAL)
    pw.pack(fill = tk.BOTH, expand = True)

    m2 = ttk.Panedwindow(pw, orient = tk. VERTICAL)            
               
    frame2 = ttk.Frame(pw, width = 720, height = 400, relief = tk.RIDGE)
    frame2.pack(fill = tk.BOTH, expand = False)
    frame3 = ttk.Frame(pw, width = 720, height = 400, relief = tk.RAISED)
    m2.add(frame2)
    m2.add(frame3)
            
    #console
    console_text = tk.Text(frame3, wrap=tk.WORD, bg="gray", fg="beige", font=("Courier", 12))
    console_text.pack(expand=True, fill="both")

    frame1 = ttk.Frame(pw, width = 360, height = 640, relief = tk.GROOVE)
    pw.add(m2)
    pw.add(frame1)
    # text editor
    textEditor = tk.Text(frame1, wrap = tk.WORD)
    textEditor.place(relheight = 1, relwidth = 1)

    
    # Tab
    tabs = ttk.Notebook(frame2)
    tabs.pack(expand = 1, fill ="both")

    tab_sen = ttk.Frame(tabs)
    tab_ben = ttk.Frame(tabs)
    
    tabs.add(tab_sen, text = "REGISTER")
    tabs.add(tab_ben, text = "EFLAGS")            
    #Register Labels
    tk.Label(tab_sen, text = "H",).place(x=163,y=14)
    tk.Label(tab_sen, text = "L",).place(x=183,y=14)
    tk.Label(tab_sen, text = "EAX:").place(x=50,y=35)
    tk.Label(tab_sen, text = "AX:").place(x=130,y=35)
    tk.Label(tab_sen, text = "EBX:").place(x=50,y=60)
    tk.Label(tab_sen, text = "BX:").place(x=130,y=60)
    tk.Label(tab_sen, text = "ECX:").place(x=50,y=85)
    tk.Label(tab_sen, text = "CX:").place(x=130,y=85)
    tk.Label(tab_sen, text = "EDX:").place(x=50,y=110)
    tk.Label(tab_sen, text = "DX:").place(x=130,y=110)
    tk.Label(tab_sen, text = "ESI:").place(x=50,y=135)
    tk.Label(tab_sen, text = "SI:").place(x=130,y=135)
    tk.Label(tab_sen, text = "EDI:").place(x=50,y=160)
    tk.Label(tab_sen, text = "DI:").place(x=130,y=160)
    tk.Label(tab_sen, text = "ESP:").place(x=50,y=185)
    tk.Label(tab_sen, text = "SP:").place(x=130,y=185)
    tk.Label(tab_sen, text = "EBP:").place(x=50,y=210),
    tk.Label(tab_sen, text = "BP:").place(x=130,y=210)
    tk.Label(tab_sen, text = "CS").place(x=50,y=235)
    tk.Label(tab_sen, text = "DS").place(x=50,y=260)
    tk.Label(tab_sen, text = "SS").place(x=50,y=285)
    tk.Label(tab_sen, text = "ES").place(x=50,y=310)
    tk.Label(tab_sen, text = "FS").place(x=50,y=335)
    tk.Label(tab_sen, text = "GS").place(x=50,y=360)
    tk.Label(tab_sen, text = "EAFLAG").place(x=50,y=385)
    tk.Label(tab_sen, text = "EIP").place(x=50,y=410)
    #EFLAGS
    tk.Label(tab_ben, text = "CF:").place(x=50,y=35)
    tk.Label(tab_ben, text = "PF:").place(x=50,y=60)
    tk.Label(tab_ben, text = "AF:").place(x=50,y=85)
    tk.Label(tab_ben, text = "ZF:").place(x=50,y=110)
    tk.Label(tab_ben, text = "SF:").place(x=50,y=135)
    tk.Label(tab_ben, text = "OF:").place(x=50,y=160)
    tk.Label(tab_ben, text = "TF:").place(x=50,y=185)
    tk.Label(tab_ben, text = "IF:").place(x=50,y=210)
    tk.Label(tab_ben, text = "IOPL").place(x=50,y=235)
    tk.Label(tab_ben, text = "NT").place(x=50,y=260)
    tk.Label(tab_ben, text = "RF").place(x=50,y=285)
    tk.Label(tab_ben, text = "VM").place(x=50,y=310)
    tk.Label(tab_ben, text = "AC").place(x=50,y=335)
    tk.Label(tab_ben, text = "VIF").place(x=50,y=360)
    tk.Label(tab_ben, text = "VIP").place(x=50,y=385)
    tk.Label(tab_ben, text = "ID").place(x=50,y=410)
    #EntrY
    oopEntry1  = EntrY(tab_sen, 4, "", 0, 90, 35)
    oopEntry2  = EntrY(tab_sen, 2, "", 0, 160, 35)
    oopEntry3  = EntrY(tab_sen, 2, "", 0, 180, 35)
    
    oopEntry4  = EntrY(tab_sen, 4, "", 0, 90, 60)
    oopEntry5  = EntrY(tab_sen, 2, "", 0, 160, 60)
    oopEntry6  = EntrY(tab_sen, 2, "", 0, 180, 60)
    
    oopEntry7  = EntrY(tab_sen, 4, "", 0, 90, 85)
    oopEntry8  = EntrY(tab_sen, 2, "", 0, 160, 85)
    oopEntry9  = EntrY(tab_sen, 2, "", 0, 180, 85)
    
    oopEntry10 = EntrY(tab_sen, 4, "", 0, 90, 110)
    oopEntry11 = EntrY(tab_sen, 2, "", 0, 160, 110)
    oopEntry12 = EntrY(tab_sen, 2, "", 0, 180, 110)
            
    oopEntry13 = EntrY(tab_sen, 4, "", 0, 90, 135)
    oopEntry14 = EntrY(tab_sen, 4, "", 0, 160, 135)
    
    oopEntry15 = EntrY(tab_sen, 4, "", 0, 90, 160)
    oopEntry16 = EntrY(tab_sen, 4, "", 0, 160, 160)
            
    oopEntry17 = EntrY(tab_sen, 4, "", 0, 90, 185)
    oopEntry18 = EntrY(tab_sen, 4, "", 0, 160, 185)
            
    oopEntry19 = EntrY(tab_sen, 4, "", 0, 90, 210)
    oopEntry20 = EntrY(tab_sen, 4, "", 0, 160, 210)
            
    oopEntry21 = EntrY(tab_sen, 4, "", 0, 160, 235)
    oopEntry22 = EntrY(tab_sen, 4, "", 0, 160, 260)
    oopEntry23 = EntrY(tab_sen, 4, "", 0, 160, 285)
    oopEntry24 = EntrY(tab_sen, 4, "", 0, 160, 310)
    oopEntry25 = EntrY(tab_sen, 4, "", 0, 160, 335)
    oopEntry26 = EntrY(tab_sen, 4, "", 0, 160, 360)
    oopEntry27 = EntrY(tab_sen, 4, "", 0, 160, 385)
    oopEntry28 = EntrY(tab_sen, 4, "", 0, 160, 410)

    #ENTRYEFLAGS        
    oopEntry29 = EntrY(tab_ben, 2, "", 0, 90, 35)    
    oopEntry30 = EntrY(tab_ben, 2, "", 0, 90, 60)    
    oopEntry31 = EntrY(tab_ben, 2, "", 0, 90, 85)    
    oopEntry32 = EntrY(tab_ben, 2, "", 0, 90, 110)
    oopEntry33 = EntrY(tab_ben, 2, "", 0, 90, 135)
    oopEntry34 = EntrY(tab_ben, 2, "", 0, 90, 160)
    oopEntry35 = EntrY(tab_ben, 2, "", 0, 90, 185)
    oopEntry36 = EntrY(tab_ben, 2, "", 0, 90, 210)
    oopEntry37 = EntrY(tab_ben, 2, "", 0, 90, 210)
    
    oopEntry38 = EntrY(tab_ben, 2, "", 0, 90, 235)
    oopEntry39 = EntrY(tab_ben, 2, "", 0, 90, 260)
    oopEntry40 = EntrY(tab_ben, 2, "", 0, 90, 285)
    oopEntry41 = EntrY(tab_ben, 2, "", 0, 90, 310)
    oopEntry42 = EntrY(tab_ben, 2, "", 0, 90, 335)
    oopEntry43 = EntrY(tab_ben, 2, "", 0, 90, 360)
    oopEntry44 = EntrY(tab_ben, 2, "", 0, 90, 385)
    oopEntry45 = EntrY(tab_ben, 2, "", 0, 90, 410)
    
    oopEntryList = [oopEntry1, oopEntry2, oopEntry3, oopEntry4, oopEntry5, oopEntry6, oopEntry7, oopEntry8, oopEntry9, 
                    oopEntry10, oopEntry11, oopEntry12, oopEntry13, oopEntry14, oopEntry15, oopEntry16, oopEntry17, 
                    oopEntry18, oopEntry19, oopEntry20, oopEntry21, oopEntry22, oopEntry23, oopEntry24, oopEntry25, 
                    oopEntry26, oopEntry27, oopEntry28, oopEntry29, oopEntry30, oopEntry31, oopEntry32, oopEntry33, 
                    oopEntry34, oopEntry35, oopEntry36, oopEntry37, oopEntry38, oopEntry39, oopEntry40, oopEntry41, 
                    oopEntry42, oopEntry43, oopEntry44, oopEntry45]


                

                
    
        
    # creat special console
    custom_console = CustomConsole(console_text)
                



    def set_value(self, value):
        self.entry.delete(0, tk.END)  # clean the present value
        self.entry.insert(0, str(value))  # add new value

    registersaving.save_register(oopEntryList, textEditor, custom_console, window2, 0) #register kaydeden fonksiyonu çağur
    

    code_runner = CodeRunner(oopEntryList, textEditor, console_text, window2)
                             

    image1 = Image.open(r"C:/Program Files (x86)/Emupent/yeni.jpg")  
    photo1 = ImageTk.PhotoImage(image1)

    image2 = Image.open(r"C:/Program Files (x86)/Emupent/mcu.jpg")
    photo2 = ImageTk.PhotoImage(image2)
    
    button31 = tk.Button(upper_frame, text="RUN", compound=tk.TOP, image=photo1, command=code_runner.run_code, width=50, height=50)
    button31.pack(side=tk.LEFT)
   

    txt(icerik,textEditor)
    
    # scroll
    scroll = tk.Scrollbar(textEditor)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)
    scroll.config(command=textEditor.yview)
    textEditor.config(yscrollcommand=scroll.set)
    


    # Klavye olaylarını dinle
    def on_key_press(event):
        if event.keysym == "F5":
            code_runner.run_code()

    window2.bind("<KeyPress>", on_key_press)
            
    window2.protocol("WM_DELETE_WINDOW", lambda: restore_stdout(window2))
    window2.mainloop()

def restore_stdout(window):
    window.destroy()  #close window 
    
window.mainloop() 

