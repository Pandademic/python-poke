import tkinter as tk

root = tk.Tk()
root.geometry("400x400")
root.title("poke game!")
root.configure(bg="light blue")

p1_label = tk.Label(root,text="player 1")
p2_label = tk.Label(root,text="player 2")

p1_tscore = tk.Label(root,text="7")
p2_tscore = tk.Label(root,text="8")

the_middle_label = tk.Label(root,text="center!")



p1_label.place(relx=0.3,rely=0.3)
p2_label.place(relx=0.6,rely=0.3)

p1_tscore.place(relx=0.3,rely=0.4)
p2_tscore.place(relx=0.6,rely=0.4)

the_middle_label.place(relx=0.5,rely=0.6,anchor=tk.CENTER)

root.mainloop()
