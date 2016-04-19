from tkinter import *
import tkinter as tk
import random
import time



def main():
    global root
    root=Tk()
    root.title("Typeracer")
    root.geometry("400x400")  
    wordInput()
    root.mainloop()
    
def wordInput():
    global wordsCount
    global wordsCorrect
    global wordsIncorrect
    #gerir random listann af orðum
    wordsList = []
    wordsCount = 0
    wordsCorrect = 0
    wordsIncorrect = 0
    for i in range(0,9):
        liner = [line.strip() for line in open('betterWords.txt')]
        wordsList.append(random.choice(liner))
    #sýnir listann sem label
    w = tk.Label(root, text="\n".join(map(str, wordsList)))
    w.pack()
    #takmarkar input á entry í lengdina á fyrsta orðinu í listanum
    var = tk.StringVar()
    def on_write(*args):
        max_len = len(wordsList[0])
        s = var.get()
        if len(s) > max_len:
            var.set(s[:max_len])
    var.trace_variable("w", on_write)
    entry = tk.Entry(root, textvariable=var)
    entry.pack()

    def newWord():
        wordsList.pop(0)
        liner = [line.strip() for line in open('words.txt')]
        wordsList.insert(9,random.choice(liner))
        on_write()
        entry.delete(0, END)
        w.config(text="\n".join(map(str, wordsList)))

    def correctWord(event=None):
        global wordsCount
        global wordsCorrect
        wordsCount += 1
        wordsCorrect += 1
        newWord() 
        print ("Correct")
        
    def incorrectWord(event=None):
        global wordsCount
        global wordsIncorrect
        wordsCount += 1
        wordsIncorrect += 1
        newWord()
        print ("Incorrect")
    
    def onclick(event=None):
        if entry.get() == wordsList[0]:
            correctWord()
        else:
            incorrectWord()
    def play():
        def countdown(count):    
            label['text'] = count
            if count > 0:
                root.after(1000, countdown, count-1)
            else:
                w = Label(root, text="GO!")
                w.place(x=35, y=15)
                w.pack()
        label = tk.Label(root)
        label.place(x=35, y=15)  
        countdown(3)
            
    root.bind("<space>", onclick)  
            
    button = tk.Button(root, text="click me", command=play)
    button.pack()
    
main()
