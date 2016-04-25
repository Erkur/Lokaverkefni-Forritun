from tkinter import *
import tkinter as tk
import random
import string
import time

#talninga breytur
wordsCount = 0
wordsCorrect = 0
wordsIncorrect = 0
keyCount = 0
timeMin = 1

def main():
    global root
    root=Tk()
    root.title("Typeracer")
    root.geometry("400x400")
    root.configure(background='#f1ffff')
    typeracer()
    root.mainloop()

def typeracer():
    #gerir random listann af orðum
    wordsList = []
    for i in range(0,9):
        liner = [line.strip() for line in open('betterWords.txt')]
        wordsList.append(random.choice(liner))
        
    #sýnir listann sem label
    wordListLabel = tk.Label(root, text=wordsList,borderwidth=1, bd=3, relief=GROOVE)
    wordListLabel.pack()
    wordListLabel.place(x=80, y=5)

    #entry boxið fyrir orðinn
    textbox = tk.Entry(root, background='#FF9999', state=DISABLED)
    textbox.pack()
    textbox.place(x=145, y=30)

    #countdown til byrjunar (3 sec)
    countdownLabel = tk.Label(root)
    countdownLabel.place(x=200, y=200)

    def toggle():
        global started
        started = True
        countdownToStart(3)
        
    
    def countdownToStart(count):
        global started
        if started:
            global max_len
            startButton.configure(state=DISABLED)
            countdownLabel['text'] = count
            if count > 0:
                # call countdown again after 1000ms (1s)
                root.after(1000, countdownToStart, count-1)
            elif count == 0:
                textbox.configure(background="white", state=NORMAL)
                textbox.focus()
                countdownLabel['text'] = "GO!"
                timer(60)

    startButton = Button(root, text="Start", command=toggle)
    startButton.pack()
    startButton.place(x=185, y=50)

    timerLabel = tk.Label(root)
    timerLabel.place(x=200, y=100)

    def restart():
        global wordsCount
        global wordsCorrect
        global wordsIncorrect
        global keyCount
        global started
        countdownLabel['text'] = " "
        timerLabel['text'] = " "
        
        started = False
        sec = 0
        wordsCount = 0
        wordsCorrect = 0
        wordsIncorrect = 0
        keyCount = 0
        startButton.configure(state=NORMAL)
            
    restartButton = Button(root, text="Restart", command=restart)
    restartButton.pack()
    restartButton.place(x=250, y=50)

    #telur niður 60 sec
    
    def timer(sec):
        global started
        if started:
            timerLabel['text'] = sec
            if sec > 0:
                # call countdown again after 1000ms (1s)
                root.after(1000, timer, sec-1)
                showWPM(keyCount, wordsIncorrect, timeMin)
            elif sec == 0:
                textbox.delete(0, END)
                startButton.configure(state=NORMAL)
                textbox.configure(background="#FF9999", state=DISABLED)
                timerLabel['text'] = "TIMER OVER!"
                

    def showWPM(entries, errors, t):
        calculate = (((entries/5) - errors) / t)
        rounded = "%.2f" % calculate
        timerLabel = tk.Label(root)
        timerLabel.configure(text=rounded)
        timerLabel.pack()
        timerLabel.place(x=300, y=30)
    
    #birtir nýtt orð
    def newWord():
        wordsList.pop(0)
        liner = [line.strip() for line in open('betterWords.txt')]
        wordsList.insert(9,random.choice(liner))
        textbox.delete(0, END)
        wordListLabel.config(text=wordsList)

    #ef orðið er rétt skrifað
    def correctWord(event=None):
        global wordsCount
        global wordsCorrect
        global keyCount
        keyCount += len(wordsList[0]) + 1
        wordsCount += 1
        wordsCorrect += 1
        newWord() 
        print ("Correct")
        print (keyCount)

    #ef orðið er rangt skrifað
    def incorrectWord(event=None):
        global wordsCount
        global wordsIncorrect
        global keyCount
        keyCount += len(textbox.get())
        wordsCount += 1
        wordsIncorrect += 1
        newWord()
        print ("Incorrect")
        print (keyCount)

    #ef ýtt er á space þá fer það í gegnum checkið
    def spacePressed(event=None):
        global keyCount
        if textbox.get()[:-1] == wordsList[0]:
            correctWord()
        else:
            print (wordsList[0])
            print (textbox.get())
            incorrectWord()
            
    root.bind("<space>", spacePressed)  
    count_flag = True   

if __name__ == "__main__":
    main()
