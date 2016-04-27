from tkinter import *
import tkinter as tk
from time import *
import random
import string
import math


#breytur sem halda mikilvægar upplýsingar
wordsCount = 0
wordsCorrect = 0
wordsIncorrect = 0
wpmTotal = 0
keyCount = 0
fintests = 0
restartTotal = 0
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
    root.configure(background="#e8fbff")
    typeracer()
    root.mainloop()

#forritið
def typeracer():
    v = IntVar()
    v.set(1)
    #gerir random listann af orðum
    wordsList = []
    for i in range(0,9):
        liner = [line.strip() for line in open("betterWords.txt")]
        wordsList.append(random.choice(liner))
    #title
    titleLabel = tk.Label(root, text="Test your typing speed", bg="#e8fbff", font=("Helvetica", 30, "bold"))
    titleLabel.place(x=50, y=0)
    #sýnir listann sem label
    wordListLabel = tk.Label(root, text=wordsList, relief=GROOVE, width=55, height=2, font=("Verdana", 8), state=DISABLED)
    wordListLabel.pack()
    wordListLabel.place(x=5, y=65)

    #entry boxið fyrir orðinn
    textbox = tk.Entry(root, width=48)
    textbox.insert(0, 'Type the above text here')
    textbox.configure(disabledbackground="#ffe0e0", state=DISABLED)
    textbox.pack()
    textbox.place(x=5, y=120)

    #countdown til byrjunar (3 sec)
    timerLabel = tk.Label(root, bg="#e8fbff", relief=SOLID, font=("Arial", 23), width=5, height= 1)
    timerLabel.place(x=300, y=110)

    #Listbox fyrir wpm
    global listbox
    listbox = Listbox(root,width=24, height=20)
    listbox.pack()
    listbox.place(y=65,x=400)

    #Label fyrir ofan listbox
    listboxLabelDT = tk.Label(root, text='Date and time', background="#e8fbff")
    listboxLabelDT.pack()
    listboxLabelDT.place(x=415,y=44)
    listboxLabelWPM = tk.Label(root, text='WPM', background="#e8fbff")
    listboxLabelWPM.pack()
    listboxLabelWPM.place(x=510,y=44)

    #Ef orðið er rétt birtir þennan label
    booleanLabel = tk.Label(root, background="#e8fbff")
    booleanLabel.pack()
    booleanLabel.place(x=100, y=150)

    #labels fyrir próf í gangi
    totalTitleLabel = tk.Label(root, text="Total Statistics", font=("Helvetica",10, "bold"), background="#e8fbff")
    totalTitleLabel.pack()
    totalTitleLabel.place(x=20, y=180)
    
    wordsLabel = tk.Label(root,text=("Total words: " + str(wordsCount)), background="#e8fbff")
    wordsLabel.pack()
    wordsLabel.place(x=20, y=210)

    correctWordsLabel = tk.Label(root,text=("Correct words: " + str(wordsCorrect)), background="#e8fbff")
    correctWordsLabel.pack()
    correctWordsLabel.place(x=20, y=230)

    incorrectWordsLabel = tk.Label(root,text=("Incorrect words: " + str(wordsIncorrect)), background="#e8fbff")
    incorrectWordsLabel.pack()
    incorrectWordsLabel.place(x=20, y=250)

    totalGames = tk.Label(root,text=("Total finished games: " + str(fintests)), background="#e8fbff")
    totalGames.pack()
    totalGames.place(x=20, y=270)

    totalrestartGames = tk.Label(root,text=("Total restarts: " + str(restartTotal)), background="#e8fbff")
    totalrestartGames.pack()
    totalrestartGames.place(x=20, y=290)
    
    #labels fyrir meðaltal úr öllum prófum
    
    avgTitleLabel = tk.Label(root, text="Average Statistics", font=("Helvetica",10, "bold"), background="#e8fbff")
    avgTitleLabel.pack()
    avgTitleLabel.place(x=150, y=180)
    
    avgWordsLabel = tk.Label(root,text=("Average words: 0"), background="#e8fbff")
    avgWordsLabel.pack()
    avgWordsLabel.place(x=150, y=210)

    avgCorrectWordsLabel = tk.Label(root,text=("Average correct words: 0"), background="#e8fbff")
    avgCorrectWordsLabel.pack()
    avgCorrectWordsLabel.place(x=150, y=230)

    avgIncorrectWordsLabel = tk.Label(root,text=("Average Incorrect words: 0"), background="#e8fbff")
    avgIncorrectWordsLabel.pack()
    avgIncorrectWordsLabel.place(x=150, y=250)

    avgWPM = tk.Label(root,text=("Average WPM: 0"), background="#e8fbff")
    avgWPM.pack()
    avgWPM.place(x=150, y=270)
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
                if v.get() == 1:
                    timer(60)
                elif v.get() == 2:
                    timer(120)
                elif v.get() == 3:
                    timer(180)
                elif v.get() == 4:
                    timer(240)
                elif v.get() == 5:
                    timer(300)

    #núllar allar breytur til að byrja upp á nýtt
    def restart():
        global wordsCount
        global wordsCorrect
        global wordsIncorrect
        global allowKeyPress
        global keyCount
        global started
        global sf
        global restartTotal
        restartTotal += 1
        allowKeyPress = False
        timerLabel['text'] = " "
        sf = 0
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
        global sf
        global fintests
        allowKeyPress = True
        minutes = sec / 60
        seconds = sec % 60
        if started:
            sf = "{:02d}:{:02d}".format(*divmod(sec, 60))
            wordListLabel.configure(state=NORMAL)
            timerLabel['text'] = sf
            if sec > 0:
                # call countdown again after 1000ms (1s)
                root.after(1000, timer, sec-1)
            elif sec == 0:
                fintests += 1
                timerLabel['text'] = " "
                avgWordsLabel['text'] = "Average words:" + (str(wordsCount / fintests))
                avgCorrectWordsLabel['text'] = "Average correct words:" + (str(wordsCorrect / fintests))
                avgIncorrectWordsLabel['text'] = "Average incorrect words:" + (str(wordsIncorrect / fintests))
                avgWPM['text'] = "Average WPM:" + (str(wpmTotal / fintests))
                calculateWPM(keyCount, wordsIncorrect, timeMin)
                textbox.delete(0, END)
                startButton.configure(state=NORMAL)
                textbox.configure(background="#FF9999", state=DISABLED)
                wordListLabel.configure(state=DISABLED)
                listbox.insert(END, strftime("%Y-%m-%d %H:%M:%S", gmtime()) + " | " + rounded)
                
    #reiknar út skrif hraðann
    def calculateWPM(entries, errors, t):
        global rounded
        global wpmTotal
        calculate = (((entries/5) - errors) / t)
        rounded = "%.0f" % calculate
        wpmTotal += rounded
    
    #birtir nýtt orð
    def newWord():
        global char
        char = 0
        wordsList.pop(0)
        liner = [line.strip() for line in open("betterWords.txt")]
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
            wordsCount += 1
            wordsLabel.configure(text=("Total words: " + str(wordsCount)))
            if textbox.get()[:-1] == wordsList[0]: #ef orðið er rétt
                keyCount += len(wordsList[0]) + 1
                wordsCorrect += 1
                booleanLabel.configure(text="Correct", fg="green", font=("Arial", 16))
                correctWordsLabel['text'] = "Correct words: " + str(wordsCorrect)
                newWord()
            else: #ef orðið er vitlaus
                keyCount += len(textbox.get())
                wordsIncorrect += 1
                booleanLabel.configure(text="Incorrect", fg="red")
                incorrectWordsLabel['text'] = "Incorrect words: " + str(wordsIncorrect)
                newWord()

    #fall sem kíkir ef notandinn ýtir á takka
    def keyPress(event):
        global char
        if allowKeyPress:
            if char < len(wordsList[0]):             
                if event.keysym == wordsList[0][char]:
                    wordListLabel.configure(underline=char)
                    char = char + 1

    #Lokar glugganum
    def quit():
        root.destroy()

    #settings gluggi
    def settingsWindow():
        settingsNewWindow = tk.Toplevel(root)
        settingsNewWindow.title("Settings")
        settingsNewWindow.geometry("100x160")
        settingsNewWindow.configure(background="#e8fbff")
        settingsNewWindow.grab_set()
        settingsButton.configure(state=DISABLED)
        #radio takkar (FLOATING IDEA)
        timeDiffLabel = tk.Label(settingsNewWindow, text="Time Length", background='#e8fbff', font=("Arial",10,"bold"))
        timeDiffLabel.pack()
        timeDiffLabel.place(x=15, y=0)
        timeDiff = Radiobutton(settingsNewWindow, text="One Minute", variable=v, value=1, background='#e8fbff', activebackground='#e8fbff').place(x= 5, y= 20)
        timeDiff = Radiobutton(settingsNewWindow, text="Two Minutes", variable=v, value=2, background='#e8fbff', activebackground='#e8fbff').place(x= 5, y= 40)
        timeDiff = Radiobutton(settingsNewWindow, text="Three Minutes", variable=v, value=3, background='#e8fbff', activebackground='#e8fbff').place(x= 5, y= 60)
        timeDiff = Radiobutton(settingsNewWindow, text="Four Minutes", variable=v, value=4, background='#e8fbff', activebackground='#e8fbff').place(x= 5, y= 80)
        timeDiff = Radiobutton(settingsNewWindow, text="Five Minutes", variable=v, value=5, background='#e8fbff', activebackground='#e8fbff').place(x= 5, y= 100)

        def back():
            settingsNewWindow.destroy()
            settingsButton.configure(state=NORMAL)
    
        backButton = tk.Button(settingsNewWindow, text='Apply', command=back)
        backButton.pack()
        backButton.place(x=38, y=130)
        
        settingsNewWindow.protocol("WM_DELETE_WINDOW", back)

    #about gluggi
    def aboutWindow():
        aboutNewWindow = tk.Toplevel(root)
        aboutNewWindow.title("About this application")
        aboutNewWindow.configure(background="#e8fbff")
        aboutNewWindow.grab_set()
        aboutButton.configure(state=DISABLED)
        msg = tk.Label(aboutNewWindow, text="Lokaverkefni í FORR2MY05 \n Eiríkur Jóhannsson", background='#e8fbff')
        msg.pack()

        def back():
            aboutNewWindow.destroy()
            aboutButton.configure(state=NORMAL)
            
        backButton = tk.Button(aboutNewWindow, text='Back', command=back)
        backButton.pack()
        
        aboutNewWindow.protocol("WM_DELETE_WINDOW", back)

    #about takkinn
    aboutButton = Button(root, text="About", command=aboutWindow, height=1, width=10)
    aboutButton.pack()
    aboutButton.place(x=310, y= 250)
    
    #settings takkinn
    settingsButton = Button(root, text="Settings", command=settingsWindow, height=1, width=10)
    settingsButton.pack()
    settingsButton.place(x=310, y= 220)
    
    #start takkinn
    startButton = Button(root, text="Start", command=toggle, height=1, width=10)
    startButton.pack()
    startButton.place(x=310, y=160)

    #restart takkinn
    restartButton = Button(root, text="Restart", command=restart, height=1, width=10)
    restartButton.pack()
    restartButton.place(x=310, y=190)

    #quit takkinn
    quitButton = Button(root, text="Exit", command=quit, height=1,width=10)
    quitButton.pack()
    quitButton.place(x=310,y=280)
    
    #festir takka við föll
    root.bind("<space>", spacePressed) 

if __name__ == "__main__":
    main()
