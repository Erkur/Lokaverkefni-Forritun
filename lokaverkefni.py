from tkinter import *
import tkinter as tk
import random
import time



def main():
    global root
    root=Tk()
    root.title("Typeracer")
    root.geometry("400x400")   
    typeracer()
    root.mainloop()

def typeracer():
    global wordsCount
    global wordsCorrect
    global wordsIncorrect
    global keyCount
    global keyCorrect
    global keyIncorrect
    global keyWordCount
    #talninga breytur
    wordsCount = 0
    wordsCorrect = 0
    wordsIncorrect = 0
    keyCount = 0
    keyCorrect = 0
    keyIncorrect = 0
    keyWordCount = 0

    def before():
        #gerir random listann af orðum
        wordsList = []
        for i in range(0,9):
            liner = [line.strip() for line in open('betterWords.txt')]
            wordsList.append(random.choice(liner))
        
        var = tk.StringVar()
        max_len = 0
        
        #sýnir listann sem label
        w = tk.Label(root, text=wordsList)
        w.pack()
        
        def on_write(*args):
            s = var.get()
            if len(s) > max_len:
                var.set(s[:max_len])

        var.trace_variable("w", on_write)
        entry = tk.Entry(root, textvariable=var, background='#FF9999')
        entry.pack()

        label = tk.Label(root)
        label.place(x=35, y=15)
        def countdown(count):
            label['text'] = count
            if count > 0:
                # call countdown again after 1000ms (1s)
                root.after(1000, countdown, count-1)
            elif count == 0:
                typeracer()
                entry.configure(background="white")
                label['text'] = "GO!"
        b = Button(root, text="Start", command=lambda: countdown(3))
        b.pack()
    before()
    #birtir nýtt orð
    def newWord():
        wordsList.pop(0)
        liner = [line.strip() for line in open('betterWords.txt')]
        wordsList.insert(9,random.choice(liner))
        entry.delete(0, END)
        w.config(text=wordsList)

    #ef orðið er rétt skrifað
    def correctWord(event=None):
        global wordsCount
        global wordsCorrect
        global keyWordCount
        keyWordCount = 0
        wordsCount += 1
        wordsCorrect += 1
        newWord() 
        print ("Correct")

    #ef orðið er rangt skrifað
    def incorrectWord(event=None):
        global wordsCount
        global wordsIncorrect
        global keyWordCount
        keyWordCount = 0
        wordsCount += 1
        wordsIncorrect += 1
        newWord()
        print ("Incorrect")

    #ef ýtt er á space þá fer það í gegnum checkið
    def spacePressed(event=None):
        if entry.get() == wordsList[0]:
            correctWord()
        else:
            incorrectWord()
            
    def click(key):
        global keyCount
        global keyCorrect
        global keyIncorrect
        global keyWordCount
        keyCount += 1
        print (key.char)
        if key.char == ' ':
                keyWordCount = 0
        else:
            if key.char == wordsList[0][keyWordCount]:
                keyCorrect += 1
                keyWordCount += 1
            else:
                keyIncorrect += 1
                keyWordCount += 1
        print ("Total key:",keyCount)
        print ("Correct keys:",keyCorrect)
        print ("Incorrect keys",keyIncorrect)
        print (keyWordCount)
        
    entry.bind("<Key>", click)
    root.bind("<space>", spacePressed)  
    count_flag = True   

if __name__ == "__main__":
    main()
