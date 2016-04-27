from tkinter import *
import tkinter as tk
from time import *
import random
import string


#breytur sem halda mikilvægar upplýsingar
wordsCount = 0
wordsCorrect = 0
wordsIncorrect = 0
keyCount = 0
timeMin = 1
char = 0
allowKeyPress = False

#glugginn sem heldur forritinu
def main():
    global root
    root=Tk()
    root.title("WPM")
    root.geometry("560x400")
    root.resizable(0,0)
    root.configure(background='#e8fbff')
    typeracer()
    root.mainloop()

#forritið
def typeracer():
    #gerir random listann af orðum
    wordsList = []
    for i in range(0,9):
        liner = [line.strip() for line in open('betterWords.txt')]
        wordsList.append(random.choice(liner))
        
    #sýnir listann sem label
    wordListLabel = tk.Label(root, text=wordsList, relief=GROOVE, width=55, height=2, font=('Verdana', 8), state=DISABLED)
    wordListLabel.pack()
    wordListLabel.place(x=5, y=50)

    #entry boxið fyrir orðinn
    textbox = tk.Entry(root, width=50)
    textbox.insert(0, 'Type the above text here')
    textbox.configure(disabledbackground='#ffe0e0', state=DISABLED)
    textbox.pack()
    textbox.place(x=5, y=105)

    #countdown til byrjunar (3 sec)
    timerLabel = tk.Label(root, bg='#e8fbff', font=('Arial', 72))
    timerLabel.place(x=280, y=150)

    #Listbox fyrir wpm
    global listbox
    listbox = Listbox(root,width=24, height=22)
    listbox.pack()
    listbox.place(y=20,x=400)

    #Label fyrir ofan listbox
    listboxLabelDT = tk.Label(root, text="Date and time", background="#e8fbff")
    listboxLabelDT.pack()
    listboxLabelDT.place(x=415,y=0)
    listboxLabelWPM = tk.Label(root, text="WPM", background="#e8fbff")
    listboxLabelWPM.pack()
    listboxLabelWPM.place(x=510,y=0)

    #byrjar á prófinu
    def toggle():
        global started
        global wordsCount
        global wordsCorrect
        global wordsIncorrect
        global keyCount
        root.bind("<Key>", keyPress) 
        wordsCount = 0
        wordsCorrect = 0
        wordsIncorrect = 0
        keyCount = 0
        started = True
        countdownToStart(3)
        
    #telur niður 3
    def countdownToStart(count):
        global started
        if started:
            global max_len
            startButton.configure(state=DISABLED)
            timerLabel['text'] = count
            if count > 0:
                # call countdown again after 1000ms (1s)
                root.after(1000, countdownToStart, count-1)
            elif count == 0:
                textbox.configure(background="white", state=NORMAL)
                textbox.delete(0, END)
                textbox.focus()
                timer(60)

    #núllar allar breytur til að byrja upp á nýtt
    def restart():
        global wordsCount
        global wordsCorrect
        global wordsIncorrect
        global allowKeyPress
        global keyCount
        global started
        allowKeyPress = False
        timerLabel['text'] = " "
        started = False
        sec = 0
        wordsCount = 0
        wordsCorrect = 0
        wordsIncorrect = 0
        keyCount = 0
        startButton.configure(state=NORMAL)
        textbox.configure(disabledbackground='#ffe0e0', state=DISABLED)
        wordListLabel.configure(state=DISABLED)

    #telur niður 60 sec
    def timer(sec):
        global started
        global allowKeyPress
        global listbox
        global rounded
        allowKeyPress = True
        if started:
            wordListLabel.configure(state=NORMAL)
            timerLabel['text'] = sec
            if sec > 0:
                # call countdown again after 1000ms (1s)
                root.after(1000, timer, sec-1)
            elif sec == 0:
                timerLabel['text'] = " "
                calculateWPM(keyCount, wordsIncorrect, timeMin)
                textbox.delete(0, END)
                startButton.configure(state=NORMAL)
                textbox.configure(background="#FF9999", state=DISABLED)
                wordListLabel.configure(state=DISABLED)
                listbox.insert(END, strftime("%Y-%m-%d %H:%M:%S", gmtime()) + " | " + rounded)
                
    #reiknar út skrif hraðann
    def calculateWPM(entries, errors, t):
        global rounded
        calculate = (((entries/5) - errors) / t)
        rounded = "%.0f" % calculate
    
    #birtir nýtt orð
    def newWord():
        global char
        char = 0
        wordsList.pop(0)
        liner = [line.strip() for line in open('betterWords.txt')]
        wordsList.insert(9,random.choice(liner))
        textbox.delete(0, END)
        wordListLabel.config(text=wordsList, underline=char)

    #ef ýtt er á space þá fer það í gegnum checkið
    def spacePressed(event=None):
        global started
        global wordsCount
        global wordsIncorrect
        global wordsCorrect
        global keyCount
        if allowKeyPress:
            if textbox.get()[:-1] == wordsList[0]: #ef orðið er rétt
                keyCount += len(wordsList[0]) + 1
                wordsCount += 1
                wordsCorrect += 1
                newWord()
            else: #ef orðið er vitlaus
                keyCount += len(textbox.get())
                wordsCount += 1
                wordsIncorrect += 1
                newWord()

    def keyPress(event):
        global char
        if allowKeyPress:
            if char < len(wordsList[0]):             
                if event.keysym == wordsList[0][char]:
                    wordListLabel.configure(underline=char)
                    char = char + 1
    #radio takkar (FLOATING IDEA)
##    v = StringVar()
##    v.set("1")
##    oneMin = Radiobutton(root, text="One Minute", variable=v, value=1, background='#e8fbff', activebackground='#e8fbff').place(x= 5, y= 250)
##    twoMin = Radiobutton(root, text="Two Minutes", variable=v, value=2, background='#e8fbff', activebackground='#e8fbff').place(x= 5, y= 270)
##    threeMin = Radiobutton(root, text="Three Minutes", variable=v, value=3, background='#e8fbff', activebackground='#e8fbff').place(x= 5, y= 290)
##    fourMin = Radiobutton(root, text="Four Minutes", variable=v, value=4, background='#e8fbff', activebackground='#e8fbff').place(x= 5, y= 310)
##    fiveMin = Radiobutton(root, text="Five Minutes", variable=v, value=5, background='#e8fbff', activebackground='#e8fbff').place(x= 5, y= 330)

    #about gluggi
    def aboutWindow():
        aboutNewWindow = tk.Toplevel(root)
        aboutNewWindow.title("About this application")
        aboutNewWindow.grab_set()
        aboutButton.configure(state=DISABLED)
        msg = tk.Label(aboutNewWindow, text="Lokaverkefni í FORR2MY05 \n Eiríkur Jóhannsson")
        msg.pack()

        def back():
            aboutNewWindow.destroy()
            aboutButton.configure(state=NORMAL)
            
        backButton = tk.Button(aboutNewWindow, text='Back', command=back)
        backButton.pack()
        
        aboutNewWindow.protocol("WM_DELETE_WINDOW", back) 

    #about takki
    aboutButton = Button(root, text="About", command=aboutWindow)
    aboutButton.pack()
    
    #start takkinn
    startButton = Button(root, text="Start", command=toggle, height= 1, width=10)
    startButton.pack()
    startButton.place(x=150, y=250)

    #restart takkinn
    restartButton = Button(root, text="Restart", command=restart, height= 1, width=10)
    restartButton.pack()
    restartButton.place(x=315, y=100)

    
    #festir takka við föll
    root.bind("<space>", spacePressed) 

if __name__ == "__main__":
    main()
