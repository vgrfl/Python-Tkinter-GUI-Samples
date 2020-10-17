import tkinter as tk

def benin_flag():    
    flagC.create_rectangle(120,0,300,90, fill="yellow", width=0)
    flagC.create_rectangle(120,90,300,180, fill="red", width=0)
    flagC.create_rectangle(0,0,120,180, fill="green", width=0)

def estonia_flag():
    flagC.create_rectangle(0, 0,300, 60, fill="blue", width=0)
    flagC.create_rectangle(0,60, 300, 120, fill="black", width=0)
    flagC.create_rectangle(0, 120, 300, 180, fill="white", width=0)

def france_flag():
    flagC.create_rectangle(0,0,100,180, fill="blue", width=0)
    flagC.create_rectangle(100,0,200, 180, fill= "white", width=0)        
    flagC.create_rectangle(200,0,300,180, fill="red", width=0)

window = tk.Tk()
window.title("Flags") 
flagC=tk.Canvas(window, width = 300, height=180) 
flagC.pack()

beninButton=tk.Button(window, text="Benin") 
beninButton.pack() 
beninButton['command' ] = benin_flag

estoniaButton=tk.Button(window, text="Estonia") 
estoniaButton.pack() 
estoniaButton['command' ] = estonia_flag

franceButton=tk.Button(window, text="France") 
franceButton.pack()
franceButton['command'] = france_flag

quitButton=tk.Button(window, text="Quit") 
quitButton.pack()
quitButton['command'] = window.destroy

window.mainloop()
