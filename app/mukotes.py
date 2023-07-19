#!/usr/bin/env python3

# Copyright (C) 2023 MuKonqi (Muhammed Abdurrahman)

# Mukotes is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Mukotes is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Mukotes.  If not, see <https://www.gnu.org/licenses/>.

from tkinter import *
from tkinter import messagebox
from subprocess import *
import subprocess
import os
import getpass
username=getpass.getuser()

en="/home/"+username+"/.by-mukonqi/mukotes/en.txt"
tr="/home/"+username+"/.by-mukonqi/mukotes/tr.txt"

def settings():
    if not os.path.isfile("/home/"+username+"/.by-mukonqi/mukotes/dark.txt") and not os.path.isfile("/home/"+username+"/.by-mukonqi/mukotes/light.txt"):
        bg="#000000"
        fg="#FFFFFF"
        button_bg="#FFFFFF"
        button_fg="#000000"
        a_button_bg="#000000"
        a_button_fg="#FFFFFF"
    if os.path.isfile("/home/"+username+"/.by-mukonqi/mukotes/dark.txt"):
        bg="#000000"
        fg="#FFFFFF"
        button_bg="#FFFFFF"
        button_fg="#000000"
        a_button_bg="#000000"
        a_button_fg="#FFFFFF"
    elif os.path.isfile("/home/"+username+"/.by-mukonqi/mukotes/light.txt"):
        bg="#FFFFFF"
        fg="#000000"
        button_bg="#000000"
        button_fg="#FFFFFF"
        a_button_bg="#FFFFFF"
        a_button_fg="#000000"
    def dark():
        os.system("cd /home/"+username+"/.by-mukonqi/mukotes/ ; rm light.txt ; touch dark.txt")
        if os.path.isfile(en):
            messagebox.showinfo("Information","Successful! Dark theme applied.")
        if os.path.isfile(tr):
            messagebox.showinfo("Bilgilendirme","Başarılı! Koyu tema uygulandı.")
        swindow.destroy()
        os.system("python3 /usr/local/bin/mukotes/mukotes.py")
    def light():
        os.system("cd /home/"+username+"/.by-mukonqi/mukotes/ ; rm dark.txt ; touch light.txt")
        if os.path.isfile(en):
            messagebox.showinfo("Information","Successful! Light theme applied.")
        if os.path.isfile(tr):
            messagebox.showinfo("Bilgilendirme","Başarılı! Açık tema uygulandı.")
        swindow.destroy()
        os.system("python3 /usr/local/bin/mukotes/mukotes.py")
    def langen():
        os.system("cd /home/"+username+"/.by-mukonqi/mukotes/ ; rm tr.txt ; touch en.txt")
        messagebox.showinfo("Information","Successful! English language applied.")
        swindow.destroy()
        os.system("python3 /usr/local/bin/mukotes/mukotes.py")
    def langtr():
        os.system("cd /home/"+username+"/.by-mukonqi/mukotes/ ; rm en.txt ; touch tr.txt")
        messagebox.showinfo("Bilgilendirme","Başarılı! Türkçe dili uygulandı.") 
        swindow.destroy()
        os.system("python3 /usr/local/bin/mukotes/mukotes.py")
    swindow=Tk()
    swindow.config(background=bg)
    swindow.resizable(0, 0)
    if os.path.isfile(en):
        swindow.title("Settings | Mukotes")
        stext1=Label(swindow, background=bg, foreground=fg, font="arial 10 bold", text="Please select the theme you want to apply.")
        sspace1=Label(swindow, background=bg, foreground=fg, font="arial 3", text="\n")
        sbutton1=Button(swindow, text="Dark", command=dark, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font=",arial 10", cursor="hand2", borderwidth="3 ")
        sbutton2=Button(swindow, text="Light", command=light, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3" )
        sspace2=Label(swindow, background=bg, foreground=fg, font="arial 3", text="\n\n")
        stext2=Label(swindow, background=bg, foreground=fg, font="arial 10 bold", text="You can change your language preferences below.")
        sspace2=Label(swindow, background=bg, foreground=fg, font="arial 3", text="\n")
        sbutton3=Button(swindow, text="English (English)", command=langen, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font=",arial 10", cursor="hand2", borderwidth ="3")
        sbutton4=Button(swindow, text="Turkish (Turkish)", command=langtr, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth= "3")
    if os.path.isfile(tr):
        swindow.title("Ayarlar | Mukotes")
        stext1=Label(swindow, background=bg, foreground=fg, font="arial 10 bold", text="Lütfen uygulamak istediğiniz temayı seçiniz.")
        sspace1=Label(swindow, background=bg, foreground=fg, font="arial 3", text="\n")
        sbutton1=Button(swindow, text="Koyu", command=dark, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg,  font=",arial 10", cursor="hand2", borderwidth="3")
        sbutton2=Button(swindow, text="Açık", command=light, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
        sspace2=Label(swindow, background=bg, foreground=fg, font="arial 3", text="\n\n")
        stext2=Label(swindow, background=bg, foreground=fg, font="arial 10 bold", text="Aşağıdan dil tercihlerinizi değiştirebilirsiniz.")
        sspace2=Label(swindow, background=bg, foreground=fg, font="arial 3", text="\n")
        sbutton3=Button(swindow, text="English (İngilizce)", command=langen, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg,  font=",arial 10", cursor="hand2", borderwidth="3")
        sbutton4=Button(swindow, text="Türkçe (Turkish)", command=langtr, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
    stext1.pack()
    sspace1.pack()
    sbutton1.pack()
    sbutton2.pack()
    sspace2.pack()
    stext2.pack()
    sspace2.pack()
    sbutton3.pack()
    sbutton4.pack()
    mainloop()
    exit()
    
def first_start():
    bg="#000000"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#000000"
    a_button_bg="#000000"
    a_button_fg="#FFFFFF"
    def llangen():
        os.system("cd /home/"+username+"/.by-mukonqi/mukotes ; touch en.txt")
        messagebox.showinfo("Information","English language applied! When you click 'OK', Mukotes settings will open.")
        lwindow.destroy()
        settings()
    def llangtr():
        os.system("cd /home/"+username+"/.by-mukonqi/mukotes ; touch tr.txt")
        messagebox.showinfo("Bilgilendirme","İstenilen dil uygulandı! 'OK' tuşuna bastığınızda Mukotes ayarları açılacak.")
        lwindow.destroy()
        settings()
    lwindow=Tk()
    lwindow.title("Choose a language for Mukotes")
    lwindow.config(background=bg)
    lwindow.resizable(0, 0)
    ltext1=Label(lwindow, background=bg, foreground=fg, font="arial 10 bold", text="Please choose a language.\nLütfen bir dil seçin.")
    ltext1.pack()
    lspace1=Label(lwindow, background=bg, foreground=fg, font="arial 3", text="\n")
    lspace1.pack()
    lbutton1=Button(lwindow, text="English (İngilizce)", command=llangen, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg,  font=",arial 10", cursor="hand2", borderwidth="3")
    lbutton1.pack()
    lbutton2=Button(lwindow, text="Türkçe (Turkish)", command=llangtr, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
    lbutton2.pack()
    mainloop()

if not os.path.isdir("/home/"+username+"/.by-mukonqi/"):
    os.system("cd /home/"+username+" ; mkdir .by-mukonqi")
    os.system("cd /home/"+username+"/.by-mukonqi ; mkdir mukotes")
    first_start()
if not os.path.isdir("/home/"+username+"/.by-mukonqi/mukotes"):
    os.system("cd /home/"+username+"/.by-mukonqi ; mkdir mukotes")
    first_start()
    
bg=""
fg=""
button_bg=""
button_fg=""
a_button_bg=""
a_button_fg=""
if os.path.isfile("/home/"+username+"/.by-mukonqi/mukotes/dark.txt"):
    bg="#000000"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#000000"
    a_button_bg="#000000"
    a_button_fg="#FFFFFF"
elif os.path.isfile("/home/"+username+"/.by-mukonqi/mukotes/light.txt"):
    bg="#FFFFFF"
    fg="#000000"
    button_bg="#000000"
    button_fg="#FFFFFF"
    a_button_bg="#FFFFFF"
    a_button_fg="#000000"
else:
    if os.path.isfile(en):
        messagebox.showwarning("Warning","Can't found theme config. When you click 'OK' settings will open.")
    elif os.path.isfile(tr):
        messagebox.showwarning("Uyarı","Tema yapılandırması bulunamadı, ayarlar 'OK' tuşuna bastığınızda açılacaktır.")
    settings()
    exit()

def module_exit():
    exit("\nThis module is shutting down...\nModül kapatılıyor...")

window=Tk()
window.config(background=bg)
window.resizable(0, 0)
name=Entry()

nf=1
fs=1
nf2=1

def s():
    if os.path.isfile(en):
        messagebox.showinfo("Succesfull!","Operation successfully completed.")
    elif os.path.isfile(tr):
        messagebox.showinfo("Başarılı!","Operasyon başarıyla tamamlandı.")
def e():
    if os.path.isfile(en):
        messagebox.showerror("Error","You did not enter any name!")
    elif os.path.isfile(tr):
        messagebox.showerror("Hata","Herhangi bir ad girmediniz!")    
def e2():
    if os.path.isfile(en):
        messagebox.showerror("Error","Can't find "+name.get()+" file.")
    elif os.path.isfile(tr):
        messagebox.showerror("Hata",name.get()+" bulunamadı.")

def file():
            
    def save():
        global nf2
        if fs != 0 and nf2 != 0:
            if name.get() == "":
                e()
                file()
            os.system("cd /home/"+username+"/Notes ; rm "+name.get()+" ; touch "+name.get())
            output_file=open("/home/"+username+"/Notes/"+name.get(), "a")
        else:
            if fentry.get() == "":
                e()
                file()
            os.system("cd /home/"+username+"/Notes ; touch "+fentry.get())
            output_file=open("/home/"+username+"/Notes/"+fentry.get(), "a")
            if fs != 0:
                if nf2 == 0:
                   nf2=1
        output_file.write(ftext1.get(1.0, END))
        output_file.close()
        fwindow.destroy()
        s()
        if fs == 0:
            os.system("python3 /usr/local/bin/mukotes/mukotes.py")
            exit()
            global text1
        else:
            text1.config(state=NORMAL)
            text1.delete(1.0, END)
            mynotes_update = subprocess.Popen("cd /home/"+username+"/Notes ; ls", shell=TRUE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE,universal_newlines=True)
            (out, err)=mynotes_update.communicate() 
            text1.insert(END, out)
            text1.insert(END, err)  
            text1.config(state=DISABLED)     

    fwindow=Tk()
    fwindow.config(background=bg)
    fwindow.resizable(0, 0)
    fspace1=Label(fwindow, background=bg, foreground=fg, text="\n", font="arial 3")
    fspace2=Label(fwindow, background=bg, foreground=fg, text="\n", font="arial 3")
    fspace3=Label(fwindow, background=bg, foreground=fg, text="\n", font="arial 3")
    fscroll=Scrollbar(fwindow)
    ftext1=Text(fwindow, yscrollcommand=fscroll.set)
    fscroll.config(command=ftext1.yview)
    if name.get() == "":
        if fs == 0:
            window.destroy()
        global nf
        nf=0
        global nf2
        nf2=0
        if os.path.isfile(en):
            flabel1=Label(fwindow, background=bg, foreground=fg, font="arial 14 bold", text="You can start taking your note.\n\nBefore save this file you should type file name.")
        elif os.path.isfile(tr):
            flabel1=Label(fwindow, background=bg, foreground=fg, font="arial 14 bold", text="Notunuzu almaya başlayabilirsiniz.\n\nBu dosyayı kaydetmeden önce dosya adı girmelisiniz.")
        fentry=Entry(fwindow)
    else:
        ftext1.delete(1.0, END)
        try:
            input_file=open("/home/"+username+"/Notes/"+name.get())
        except:
            fwindow.destroy()
            e2()
            return
        data = input_file.read()
        ftext1.insert(END, data)
        input_file.close()
        if os.path.isfile(en):
            flabel1=Label(fwindow, background=bg, foreground=fg, font="arial 14 bold", text="You can start editing your note.")
        elif os.path.isfile(tr):
            flabel1=Label(fwindow, background=bg, foreground=fg, font="arial 14 bold", text="Notunuzu düzenlemeye başlayabilirsiniz.")
    if os.path.isfile(en):
        if  nf == 0:
            window.title("New Note - Notes | Mukotes")
        else:
            window.title(name.get()+" - Notes | Mukotes")
        fbutton1=Button(fwindow, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Save", command=save)    
    elif os.path.isfile(tr):
        if  nf == 0:
            fwindow.title("Yeni Not - Notlar | Mukotes")
        else:
            fwindow.title(name.get()+" - Notlar | Mukotes")
        fbutton1=Button(fwindow, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Kaydet", command=save)           
    fscroll.pack(side=RIGHT, fill=Y)    
    fspace1.pack()
    flabel1.pack()
    fspace2.pack()
    ftext1.pack()
    fspace3.pack()
    if nf == 0:
        fentry.pack()
        nf=1
    fbutton1.pack()
    fwindow.mainloop()

def delete():
    if name.get() != "" and os.path.isfile("/home/"+username+"/Notes/"+name.get()):
        os.system("cd /home/"+username+"/Notes ; rm "+name.get())
        s()
        text1.config(state=NORMAL)
        text1.delete(1.0, END)
        mynotes_update = subprocess.Popen("cd /home/"+username+"/Notes ; ls", shell=TRUE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE,universal_newlines=True)
        (out, err)=mynotes_update.communicate() 
        text1.insert(END, out)
        text1.insert(END, err)
        text1.config(state=DISABLED)
    else:
        if name.get() == "": 
            e()
        elif not os.path.isfile("cd /home/"+username+"/Notes/"+name.get()):
            e2()

if os.path.isdir("/home/"+username+"/Notes"):
    space1=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")
    space2=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")
    space3=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")
    mynotes = subprocess.Popen("cd /home/"+username+"/Notes ; ls", shell=TRUE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE,universal_newlines=True)
    (out, err)=mynotes.communicate()
    scroll=Scrollbar(window)
    text1=Text(window, yscrollcommand=scroll.set)
    text1.insert(END, out)
    text1.insert(END, err)
    scroll.config(command=text1.yview)
    text1.config(state=DISABLED)
    if os.path.isfile(en):
        window.title("Notes | Mukotes")
        label1=Label(window, background=bg, foreground=fg, font="arial 14 bold", text="The notes taken are listed below.")
        label2=Label(window, background=bg, foreground=fg, font="arial 14 bold", text="Please type a file name below.\nIf you want open existing file type file name AND click 'Open' button, if you want new file do NOT type anything and ONLY click 'Open' button.\nIf you want delete existing file type file name AND click 'Delete' button.")        
        button1=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="3", background=button_bg, text="Open",command=file)
        button2=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="3", background=button_bg, text="Delete",command=delete)
    elif os.path.isfile(tr):
        window.title("Notlar | Mukotes")
        label1=Label(window, background=bg, foreground=fg, font="arial 14 bold", text="Aşağıda alınan notlar listelenmiştir.")
        label2=Label(window, background=bg, foreground=fg, font="arial 14 bold", text="Aşağıya lütfen bir dosya adı yazın.\nVar olan dosya açmak istiyorsanız dosya adı girin VE 'Aç' butonuna, yeni bir dosya açmak istiyorsanız bir şey yazMAyın ve SADECE 'Aç' butonuna tıklayınız.\nVar olan dosyayı silmek istiyorsanız dosya adı girin VE 'Sil' butonuna tıklayınız.")  
        button1=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="3", background=button_bg, text="Aç",command=file)        
        button2=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="3", background=button_bg, text="Sil",command=delete)        
    scroll.pack(side=RIGHT, fill=Y)
    space1.pack()
    label1.pack()
    space2.pack()
    text1.pack()
    space3.pack()
    label2.pack()
    name.pack()
    button1.pack()
    button2.pack()
    mainloop()
else:
    os.system("cd /home/"+username+"/ ; mkdir Notes")
    fs=0
    file()