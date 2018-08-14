from tkinter import *
from tkinter import messagebox
class tctcto(Frame):
    i = 1
    winx= False
    wino = False
    size = 100
    size2 = 5
    winsr = 0
    winsb = 0
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.crt()
    def crt(self):
        self.rset = Button(self, text = "Reset", command = self.reset_game, font = ("New Times Roman", 16)).grid(row = 1, column = 4, padx = 8, ipadx = 14, ipady = 5)
        Label(self, text = "Scoreboard: ", font = ("Helvetica", 16)).grid(row = 0, column = 3)
        self.txt = Text(self, width = 15, height = 1, wrap = WORD, font = ("Helvetica", 16))
        self.txt.grid(row = 0, column = 4, padx = 5)
        self.txt2 = Text(self, width = 15, height = 1, wrap = WORD, font = ("Helvetica", 16))
        self.txt2.grid(row = 0, column = 5, padx = 5)
        self.txt.delete(0.0, END)
        self.txt2.delete(0.0, END)
        self.txt.insert(0.0, "RED: 0")
        self.txt2.insert(0.0, "BLUE: 0")
        self.btt1 = Button(self)
        self.btt1["command"] = self.ckd1
        self.btt1["bg"] = "white"
        self.btt1.grid(row = 0, column = 0, ipadx = self.size, ipady = self.size, padx = self.size2+10, pady = self.size2)

        self.btt2 = Button(self)
        self.btt2["command"] = self.ckd2
        self.btt2["bg"] = "white"
        self.btt2.grid(row = 0, column = 1, ipadx = self.size, ipady = self.size, padx = self.size2+40, pady = self.size2)

        self.btt3 = Button(self)
        self.btt3["command"] = self.ckd3
        self.btt3["bg"] = "white"
        self.btt3.grid(row = 0, column = 2, ipadx = self.size, ipady = self.size, padx = self.size2+15, pady = self.size2)

        self.btt4 = Button(self)
        self.btt4["command"] = self.ckd4
        self.btt4["bg"] = "white"
        self.btt4.grid(row = 1, column = 0, ipadx = self.size, ipady = self.size, padx = self.size2, pady = self.size2)

        self.btt5 = Button(self)
        self.btt5["command"] = self.ckd5
        self.btt5["bg"] = "white"
        self.btt5.grid(row = 1, column = 1, ipadx = self.size, ipady = self.size, padx = self.size2, pady = self.size2)

        self.btt6 = Button(self)
        self.btt6["command"] = self.ckd6
        self.btt6["bg"] = "white"
        self.btt6.grid(row = 1, column = 2, ipadx = self.size, ipady = self.size, padx = self.size2, pady = self.size2)

        self.btt7 = Button(self)
        self.btt7["command"] = self.ckd7
        self.btt7["bg"] = "white"
        self.btt7.grid(row = 2, column = 0, ipadx = self.size, ipady = self.size, padx = self.size2, pady = self.size2)

        self.btt8 = Button(self)
        self.btt8["bg"] = "white"
        self.btt8["command"] = self.ckd8
        self.btt8.grid(row = 2, column = 1, ipadx = self.size, ipady = self.size, padx = self.size2, pady = self.size2,)

        self.btt9 = Button(self)
        self.btt9["bg"] = "white"
        self.btt9["command"] = self.ckd9
        self.btt9.grid(row = 2, column = 2, ipadx = self.size, ipady = self.size, padx = self.size2, pady = self.size2)
    def reset_game(self):
        self.btt1["bg"] = "white"
        self.btt2["bg"] = "white"
        self.btt3["bg"] = "white"
        self.btt4["bg"] = "white"
        self.btt5["bg"] = "white"
        self.btt6["bg"] = "white"
        self.btt7["bg"] = "white"
        self.btt8["bg"] = "white"
        self.btt9["bg"] = "white"
        self.winx = False
        self.wino = False
        self.i = 0
        #Label(self, text = "Scoreboard", width = 10, height = 6).grid(row = 0, column = 4)
    def ckd1(self):
        if self.btt1["bg"] == "white":
            if self.i%2==0:
                self.btt1["bg"] = "red"
                self.check_win()
                self.i = self.i+1
                self.check_draw()
            else:
                self.btt1["bg"] = "blue"
                self.check_win()
                self.i += 1
                self.check_draw()
        else:
            messagebox.showinfo(title = "Invalid move", message = "You have made an invalid move")
    def ckd2(self):
         if self.btt2["bg"] == "white":
                if self.i%2==0:
                    self.btt2["bg"] = "red"
                    self.check_win()
                    self.i = self.i+1
                    self.check_draw()
                else:
                    self.btt2["bg"] = "blue"
                    self.check_win()
                    self.i += 1
                    self.check_draw()
         else:
            messagebox.showinfo(title = "Invalid move", message = "You have made an invalid move")
    def ckd3(self):
          if self.btt3["bg"] == "white":
                if self.i%2==0:
                    self.btt3["bg"] = "red"
                    self.check_win()
                    self.i = self.i+1
                    self.check_draw()
                else:
                    self.btt3["bg"] = "blue"
                    self.check_win()
                    self.i += 1
                    self.check_draw()
          else:
            messagebox.showinfo(title = "Invalid move", message = "You have made an invalid move")
    def ckd4(self):
        if self.btt4["bg"] == "white":
            if self.i%2==0:
                self.btt4["bg"] = "red"
                self.check_win()
                self.i = self.i+1
                self.check_draw()
            else:
                self.btt4["bg"] = "blue"
                self.check_win()
                self.i += 1
                self.check_draw()
        else:
            messagebox.showinfo(title = "Invalid move", message = "You have made an invalid move")
    def ckd5(self):
        if self.btt5["bg"] == "white":
            if self.i%2==0:
                self.btt5["bg"] = "red"
                self.check_win()
                self.i = self.i+1
                self.check_draw()
            else:
                self.btt5["bg"] = "blue"
                self.check_win()
                self.i += 1
                self.check_draw()
        else:
            messagebox.showinfo(title = "Invalid move", message = "You have made an invalid move")
    def ckd6(self):
        if self.btt6["bg"] == "white":
            if self.i%2==0:
                self.btt6["bg"] = "red"
                self.check_win()
                self.i = self.i+1
                self.check_draw()
            else:
                self.btt6["bg"] = "blue"
                self.check_win()
                self.i += 1
                self.check_draw()
        else:
            messagebox.showinfo(title = "Invalid move", message = "You have made an invalid move")
    def ckd7(self):
        if self.btt7["bg"] == "white":
            if self.i%2==0:
                self.btt7["bg"] = "red"
                self.check_win()
                self.i = self.i+1
                self.check_draw()
            else:
                self.btt7["bg"] = "blue"
                self.check_win()
                self.i += 1
                self.check_draw()
        else:
            messagebox.showinfo(title = "Invalid move", message = "You have made an invalid move")
    def ckd8(self):
        if self.btt8["bg"] == "white":
            if self.i%2==0:
                self.btt8["bg"] = "red"
                self.check_win()
                self.i = self.i+1
                self.check_draw()
            else:
                self.btt8["bg"] = "blue"
                self.check_win()
                self.i += 1
                self.check_draw()
        else:
            messagebox.showinfo(title = "Invalid move", message = "You have made an invalid move")
    def ckd9(self):
        if self.btt9["bg"] == "white":
            if self.i%2==0:
                self.btt9["bg"] = "red"
                self.check_win()
                self.i = self.i+1
                self.check_draw()
            else:
                self.btt9["bg"] = "blue"
                self.check_win()
                self.i += 1
                self.check_draw()
        else:
            messagebox.showinfo(title = "Invalid move", message = "You have made an invalid move")
    def check_win(self):
        #messagebox.showinfo(title = "Check Win", message = "For debugging purposes")
        if self.btt1["bg"] == "red" and self.btt2["bg"] == "red" and self.btt3["bg"] == "red":
            self.winx = True
        elif self.btt4["bg"] == "red" and self.btt5["bg"] == "red" and self.btt6["bg"] == "red":
            self.winx = True
        elif self.btt7["bg"] == "red" and self.btt8["bg"] == "red" and self.btt9["bg"] == "red":
            self.winx = True
        elif self.btt1["bg"] == "red" and self.btt4["bg"] == "red" and self.btt7["bg"] == "red":
            self.winx = True
        elif self.btt2["bg"] == "red" and self.btt5["bg"] == "red" and self.btt8["bg"] == "red":
            self.winx = True
        elif self.btt3["bg"] == "red" and self.btt6["bg"] == "red" and self.btt9["bg"] == "red":
            self.winx = True
        elif self.btt1["bg"] == "red" and self.btt5["bg"] == "red" and self.btt9["bg"] == "red":
            self.winx = True
        elif self.btt3["bg"] == "red" and self.btt5["bg"] == "red" and self.btt7["bg"] == "red":
            self.winx = True

        elif self.btt1["bg"] == "blue" and self.btt2["bg"] == "blue" and self.btt3["bg"] == "blue":
            self.wino = True
        elif self.btt4["bg"] == "blue" and self.btt5["bg"] == "blue" and self.btt6["bg"] == "blue":
            self.wino = True
        elif self.btt7["bg"] == "blue" and self.btt8["bg"] == "blue" and self.btt9["bg"] == "blue":
            self.wino = True
        elif self.btt1["bg"] == "blue" and self.btt4["bg"] == "blue" and self.btt7["bg"] == "blue":
            self.wino = True
        elif self.btt2["bg"] == "blue" and self.btt5["bg"] == "blue" and self.btt8["bg"] == "blue":
            self.wino = True
        elif self.btt3["bg"] == "blue" and self.btt6["bg"] == "blue" and self.btt9["bg"] == "blue":
            self.wino = True
        elif self.btt1["bg"] == "blue" and self.btt5["bg"] == "blue" and self.btt9["bg"] == "blue":
            self.wino = True
        elif self.btt3["bg"] == "blue" and self.btt5["bg"] == "blue" and self.btt7["bg"] == "blue":
            self.wino = True
        if self.winx == True:
            messagebox.showinfo(title = "Victory", message = "Player RED wins this game")
            self.winsr += 1
            self.txt.delete(0.0, END)
            self.txt.insert(0.0, "RED: " + str(self.winsr))
            self.reset_game()
        elif self.wino == True:
            messagebox.showinfo(title = "Victory", message = "Player BLUE wins this game")
            self.winsb += 1
            self.txt2.delete(0.0, END)
            self.txt2.insert(0.0, "BLUE: " + str(self.winsb))
            self.reset_game()
    def check_draw(self):
        if self.btt1["bg"] != "white" and self.btt2["bg"] != "white" and self.btt3["bg"] != "white" and self.btt4["bg"] != "white" and self.btt5["bg"] != "white" and self.btt6["bg"] != "white" and self.btt7["bg"] != "white" and self.btt8["bg"] != "white" and self.btt9["bg"] != "white" and self.winx==False and self.wino==False:
            messagebox.showinfo(title = "Draw", message = "Match drawn! No one wins")
            self.reset_game()
root = Tk()
root.title("Tic Tac Toe")
root.geometry("1366x760")
app = tctcto(root)
root.mainloop()