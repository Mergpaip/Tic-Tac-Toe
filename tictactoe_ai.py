import tkinter as tk
from PIL import Image, ImageTk
import pygame

root = tk.Tk()
root.title("Tic Tac Toe")

#####################################

pygame.mixer.init()
pygame.mixer.music.load(r"C:\Users\Sam\Documents\Python\Tic Tac Toe\soundtrack_tictactoe.mp3")
pygame.mixer.music.play(loops=100)

####################################

canvas = tk.Canvas(root, height=500, width=500, bg="blue")
canvas.grid(rowspan=7, columnspan=7)

#####################################

image_big = Image.open(r"C:\Users\Sam\Documents\Python\Tic Tac Toe\logo_tictactoe.png")
image= image_big.resize((400, 110))
Logo = ImageTk.PhotoImage(image)

logo = tk.Label(image=Logo)
logo.image = Logo
logo.place(x=50, y=15)

tk.Label(root, bg="blue", width=60, height=1).place(x=50, y=5)
tk.Label(root, bg="blue", width=60, height=1).place(x=50, y=125)
tk.Label(root, bg="blue", width=1, height=10).place(x=40, y=5)
tk.Label(root, bg="blue", width=1, height=10).place(x=450, y=5)

#####################################

#tk.Label(root, text="Tic Tac Toe", font = ("Bauhaus 93", 30), fg='white', bg="blue").grid(row=0, column=2, rowspan=3, columnspan=3)

#####################################

tk.Label(root, text="score o: 0", font = ("Bell MT", 12), bg="#f0f0f0", borderwidth=10, relief="sunken").grid(row=5, column=1, rowspan=6, columnspan=3)
tk.Label(root, text="ties: 0", font = ("Bell MT", 12), bg="#f0f0f0", borderwidth=10, relief="sunken").grid(row=5, column=2, rowspan=6, columnspan=3)
tk.Label(root, text="score x: 0", font = ("Bell MT", 12), bg="#f0f0f0", borderwidth=10, relief="sunken").grid(row=5, column=3, rowspan=6, columnspan=3)

#####################################

button1 = tk.Button(root, text=" ", font = ("Algerian", 10), height=3, width=6, borderwidth=5, command = lambda:button1_response())
button1.grid(row=1, column=1, rowspan=3, columnspan=3)

button2 = tk.Button(root, text=" ", font = ("Algerian", 10), height=3, width=6, borderwidth=5, command = lambda:button2_response())
button2.grid(row=1, column=2, rowspan=3, columnspan=3)

button3 = tk.Button(root, text=" ", font = ("Algerian", 10), height=3, width=6, borderwidth=5, command = lambda:button3_response())
button3.grid(row=1, column=3, rowspan=3, columnspan=3)

button4 = tk.Button(root, text=" ", font = ("Algerian", 10), height=3, width=6, borderwidth=5, command = lambda:button4_response())
button4.grid(row=2, column=1, rowspan=3, columnspan=3)

button5 = tk.Button(root, text=" ", font = ("Algerian", 10), height=3, width=6, borderwidth=5, command = lambda:button5_response())
button5.grid(row=2, column=2, rowspan=3, columnspan=3)

button6 = tk.Button(root, text=" ", font = ("Algerian", 10), height=3, width=6, borderwidth=5, command = lambda:button6_response())
button6.grid(row=2, column=3, rowspan=3, columnspan=3)

button7 = tk.Button(root, text=" ", font = ("Algerian", 10), height=3, width=6, borderwidth=5, command = lambda:button7_response())
button7.grid(row=3, column=1, rowspan=3, columnspan=3)

button8 = tk.Button(root, text=" ", font = ("Algerian", 10), height=3, width=6, borderwidth=5, command = lambda:button8_response())
button8.grid(row=3, column=2, rowspan=3, columnspan=3)

button9 = tk.Button(root, text=" ", font = ("Algerian", 10), height=3, width=6, borderwidth=5, command = lambda:button9_response())
button9.grid(row=3, column=3, rowspan=3, columnspan=3)

button_reset = tk.Button(root, text="reset", font=("Arial Black", 8), fg='white', borderwidth=10, bg="red",  height=3, width=6, command = lambda:response_reset())
button_reset.grid(row=5, column=5, rowspan=6, columnspan=6)

#####################################

count = 0
score_x = 0
score_o = 0
score_gelijk = 0
game_over = 0

#####################################

def winner_x():
    tk.Label(root, text="x wins", font = ("Berlin Sans FB", 15), width=10, fg='white', bg="blue").grid(row=4, column=2, rowspan=6, columnspan=3)
    
    button1['state'] = tk.DISABLED
    button2['state'] = tk.DISABLED
    button3['state'] = tk.DISABLED
    button4['state'] = tk.DISABLED
    button5['state'] = tk.DISABLED
    button6['state'] = tk.DISABLED
    button7['state'] = tk.DISABLED
    button8['state'] = tk.DISABLED
    button9['state'] = tk.DISABLED
    
    global score_x
    score_x = score_x + 1
    score_x_text = "score x: " + str(score_x)
    tk.Label(root, text=score_x_text, font = ("Bell MT", 12), bg="#f0f0f0").grid(row=5, column=3, rowspan=6, columnspan=3)
    
    global game_over
    game_over = game_over + 1
        
def winner_o():
    tk.Label(root, text="o wins", font = ("Berlin Sans FB", 15), width=10, bg="blue").grid(row=4, column=2, rowspan=6, columnspan=3)
    
    button1['state'] = tk.DISABLED
    button2['state'] = tk.DISABLED
    button3['state'] = tk.DISABLED
    button4['state'] = tk.DISABLED
    button5['state'] = tk.DISABLED
    button6['state'] = tk.DISABLED
    button7['state'] = tk.DISABLED
    button8['state'] = tk.DISABLED
    button9['state'] = tk.DISABLED
        
    global score_o
    score_o = score_o + 1
    score_o_text = "score o: " + str(score_o)
    tk.Label(root, text=score_o_text, font = ("Bell MT", 12), bg="#f0f0f0").grid(row=5, column=1, rowspan=6, columnspan=3)
    
    global game_over
    game_over = game_over + 1

#####################################

def check_winner():
    
    if button1['text'] == 'x' and button2['text'] == 'x' and button3['text'] == 'x':
        winner_x()
    elif button4['text'] == 'x' and button5['text'] == 'x' and button6['text'] == 'x':
        winner_x()      
    elif button7['text'] == 'x' and button8['text'] == 'x' and button9['text'] == 'x':
        winner_x()
    
    elif button1['text'] == 'o' and button2['text'] == 'o' and button3['text'] == 'o':
        winner_o()
    elif button4['text'] == 'o' and button5['text'] == 'o' and button6['text'] == 'o':
        winner_o()      
    elif button7['text'] == 'o' and button8['text'] == 'o' and button9['text'] == 'o':
        winner_o()

    elif button1['text'] == 'x' and button4['text'] == 'x' and button7['text'] == 'x':
        winner_x()
    elif button2['text'] == 'x' and button5['text'] == 'x' and button8['text'] == 'x':
        winner_x()      
    elif button3['text'] == 'x' and button6['text'] == 'x' and button9['text'] == 'x':
        winner_x()
    
    elif button1['text'] == 'o' and button4['text'] == 'o' and button7['text'] == 'o':
        winner_o()
    elif button2['text'] == 'o' and button5['text'] == 'o' and button8['text'] == 'o':
        winner_o()      
    elif button3['text'] == 'o' and button6['text'] == 'o' and button9['text'] == 'o':
        winner_o()
        
    elif button1['text'] == 'x' and button5['text'] == 'x' and button9['text'] == 'x':
        winner_x()
    elif button3['text'] == 'x' and button5['text'] == 'x' and button7['text'] == 'x':
        winner_x()      
    
    elif button1['text'] == 'o' and button5['text'] == 'o' and button9['text'] == 'o':
        winner_o()
    elif button3['text'] == 'o' and button5['text'] == 'o' and button7['text'] == 'o':
        winner_o()
        
    elif count == 9:
        tk.Label(root, text="tie", font = ("Berlin Sans FB", 15), width=10, fg="white", bg="blue").grid(row=4, column=2, rowspan=6, columnspan=3)
        
        global score_gelijk
        score_gelijk = score_gelijk + 1
        score_gelijk_text = "ties: " + str(score_gelijk)
        tk.Label(root, text=score_gelijk_text, font = ("Bell MT", 12), bg="#f0f0f0").grid(row=5, column=2, rowspan=6, columnspan=3)
        
        button1['state'] = tk.DISABLED
        button2['state'] = tk.DISABLED
        button3['state'] = tk.DISABLED
        button4['state'] = tk.DISABLED
        button5['state'] = tk.DISABLED
        button6['state'] = tk.DISABLED
        button7['state'] = tk.DISABLED
        button8['state'] = tk.DISABLED
        button9['state'] = tk.DISABLED
        
        global game_over
        game_over = game_over + 1

#####################################

def response1():
    global count
    count = count + 1
    
    if button1['text'] == ' ':
        if count % 2 == 0:
            button1['text'] = 'x'
        else:
            button1['text'] = 'o'
    else:
        count = count - 1
    
    check_winner()
    
#####################################

def response2():
    global count
    count = count + 1
    
    if button2['text'] == ' ':
        if count % 2 == 0:
            button2['text'] = 'x'
        else:
            button2['text'] = 'o'
    else:
        count = count - 1
        
    check_winner()
    
#####################################

def response3():
    global count
    count = count + 1
    
    if button3['text'] == ' ':
        if count % 2 == 0:
            button3['text'] = 'x'
        else:
            button3['text'] = 'o'
    else:
        count = count - 1
        
    check_winner()
    
#####################################

def response4():
    global count
    count = count + 1
    
    if button4['text'] == ' ':
        if count % 2 == 0:
            button4['text'] = 'x'
        else:
            button4['text'] = 'o'
    else:
        count = count - 1
    
    check_winner() 
    
#####################################

def response5():
    global count
    count = count + 1
    
    if button5['text'] == ' ':
        if count % 2 == 0:
            button5['text'] = 'x'
        else:
            button5['text'] = 'o'
    else:
        count = count - 1
    
    check_winner()
    
#####################################

def response6():
    global count
    count = count + 1
    
    if button6['text'] == ' ':
        if count % 2 == 0:
            button6['text'] = 'x'
        else:
            button6['text'] = 'o'
    else:
        count = count - 1
        
    check_winner()
    
#####################################

def response7():
    global count
    count = count + 1
    
    if button7['text'] == ' ':
        if count % 2 == 0:
            button7['text'] = 'x'
        else:
            button7['text'] = 'o'
    else:
        count = count - 1
        
    check_winner()
    
#####################################

def response8():
    global count
    count = count + 1
    
    if button8['text'] == ' ':
        if count % 2 == 0:
            button8['text'] = 'x'
        else:
            button8['text'] = 'o'
    else:
        count = count - 1
        
    check_winner()
    
#####################################

def response9():
    global count
    count = count + 1
    
    if button9['text'] == ' ':
        if count % 2 == 0:
            button9['text'] = 'x'
        else:
            button9['text'] = 'o'
    else:
        count = count - 1
        
    check_winner()
    
#####################################

def response_reset():
    button1['text'] = " "
    button2['text'] = " "
    button3['text'] = " "
    button4['text'] = " "
    button5['text'] = " "
    button6['text'] = " "
    button7['text'] = " "
    button8['text'] = " "
    button9['text'] = " "
    
    tk.Label(root, width=30, bg="blue").grid(row=4, column=2, rowspan=6, columnspan=3)
    
    global count
    count = 0
    
    button1['state'] = tk.NORMAL
    button2['state'] = tk.NORMAL
    button3['state'] = tk.NORMAL
    button4['state'] = tk.NORMAL
    button5['state'] = tk.NORMAL
    button6['state'] = tk.NORMAL
    button7['state'] = tk.NORMAL
    button8['state'] = tk.NORMAL
    button9['state'] = tk.NORMAL
    
    global game_over
    if game_over == 1:
        game_over = game_over - 1
    
#########################################

def AI_turn():
#tenzij game over
    if game_over == 0:

    #horizontaal
        if button1['text'] == 'x' and button2['text'] == 'x' and button3['text'] == ' ':
            response3()
        elif button1['text'] == 'x' and button3['text'] == 'x' and button2['text'] == ' ':
            response2()     
        elif button2['text'] == 'x' and button3['text'] == 'x' and button1['text'] == ' ':
            response1()
    
        elif button4['text'] == 'x' and button5['text'] == 'x' and button6['text'] == ' ':
            response6()
        elif button4['text'] == 'x' and button6['text'] == 'x' and button5['text'] == ' ':
            response5()     
        elif button5['text'] == 'x' and button6['text'] == 'x' and button4['text'] == ' ':
            response4()
            
        elif button7['text'] == 'x' and button8['text'] == 'x' and button9['text'] == ' ':
            response9()
        elif button7['text'] == 'x' and button9['text'] == 'x' and button8['text'] == ' ':
            response8()     
        elif button8['text'] == 'x' and button9['text'] == 'x' and button7['text'] == ' ':
            response7() 
        
        #verticaal
        elif button1['text'] == 'x' and button4['text'] == 'x' and button7['text'] == ' ':
            response7()
        elif button1['text'] == 'x' and button7['text'] == 'x' and button4['text'] == ' ':
            response4()     
        elif button4['text'] == 'x' and button7['text'] == 'x' and button1['text'] == ' ':
            response1()
    
        elif button2['text'] == 'x' and button5['text'] == 'x' and button8['text'] == ' ':
            response8()
        elif button2['text'] == 'x' and button8['text'] == 'x' and button5['text'] == ' ':
            response5()     
        elif button5['text'] == 'x' and button8['text'] == 'x' and button2['text'] == ' ':
            response2()
            
        elif button3['text'] == 'x' and button6['text'] == 'x' and button9['text'] == ' ':
            response9()
        elif button3['text'] == 'x' and button9['text'] == 'x' and button6['text'] == ' ':
            response6()     
        elif button6['text'] == 'x' and button9['text'] == 'x' and button3['text'] == ' ':
            response3()
            
    #diagonaal
        elif button1['text'] == 'x' and button5['text'] == 'x' and button9['text'] == ' ':
            response9()
        elif button1['text'] == 'x' and button9['text'] == 'x' and button5['text'] == ' ':
            response5()     
        elif button5['text'] == 'x' and button9['text'] == 'x' and button1['text'] == ' ':
            response1()
        
        elif button3['text'] == 'x' and button5['text'] == 'x' and button7['text'] == ' ':
            response7()
        elif button3['text'] == 'x' and button7['text'] == 'x' and button5['text'] == ' ':
            response5()     
        elif button5['text'] == 'x' and button7['text'] == 'x' and button3['text'] == ' ':
            response3()
    
    #verticaal
    
        elif button1['text'] == 'o' and button2['text'] == 'o' and button3['text'] == ' ':
            response3()
        elif button1['text'] == 'o' and button3['text'] == 'o' and button2['text'] == ' ':
            response2()     
        elif button2['text'] == 'o' and button3['text'] == 'o' and button1['text'] == ' ':
            response1()
    
        elif button4['text'] == 'o' and button5['text'] == 'o' and button6['text'] == ' ':
            response6()
        elif button4['text'] == 'o' and button6['text'] == 'o' and button5['text'] == ' ':
            response5()     
        elif button5['text'] == 'o' and button6['text'] == 'o' and button4['text'] == ' ':
            response4()
            
        elif button7['text'] == 'o' and button8['text'] == 'o' and button9['text'] == ' ':
            response9()
        elif button7['text'] == 'o' and button9['text'] == 'o' and button8['text'] == ' ':
            response8()     
        elif button8['text'] == 'o' and button9['text'] == 'o' and button7['text'] == ' ':
            response7() 
        
        #verticaal
        elif button1['text'] == 'o' and button4['text'] == 'o' and button7['text'] == ' ':
            response7()
        elif button1['text'] == 'o' and button7['text'] == 'o' and button4['text'] == ' ':
            response4()     
        elif button4['text'] == 'o' and button7['text'] == 'o' and button1['text'] == ' ':
            response1()
    
        elif button2['text'] == 'o' and button5['text'] == 'o' and button8['text'] == ' ':
            response8()
        elif button2['text'] == 'o' and button8['text'] == 'o' and button5['text'] == ' ':
            response5()     
        elif button5['text'] == 'o' and button8['text'] == 'o' and button2['text'] == ' ':
            response2()
            
        elif button3['text'] == 'o' and button6['text'] == 'o' and button9['text'] == ' ':
            response9()
        elif button3['text'] == 'o' and button9['text'] == 'o' and button6['text'] == ' ':
            response6()     
        elif button6['text'] == 'o' and button9['text'] == 'o' and button3['text'] == ' ':
            response3()
            
    #diagonaal
        elif button1['text'] == 'o' and button5['text'] == 'o' and button9['text'] == ' ':
            response9()
        elif button1['text'] == 'o' and button9['text'] == 'o' and button5['text'] == ' ':
            response5()     
        elif button5['text'] == 'o' and button9['text'] == 'o' and button1['text'] == ' ':
            response1()
        
        elif button3['text'] == 'o' and button5['text'] == 'o' and button7['text'] == ' ':
            response7()
        elif button3['text'] == 'o' and button7['text'] == 'o' and button5['text'] == ' ':
            response5()     
        elif button5['text'] == 'o' and button7['text'] == 'o' and button3['text'] == ' ':
            response3()
            
    ###############################
       
    #if middle middle is free then there
        elif button5['text'] == ' ':
            response5()
        
    #if bottom right is no good option then bottom left scenario 1
        elif button1['text'] == 'o' and button6['text'] == 'o' and button7['text'] == ' ':
            response7()
        
    #if bottom right is no good option then bottom left scenario 2
        elif button1['text'] == 'o' and button8['text'] == 'o' and button7['text'] == ' ':
            response7()
            
    #if bottom right is free then there
        elif button9['text'] == ' ':
            response9()
    
    #if bottom left is free then there
        elif button7['text'] == ' ':
            response7()
    
    #pick whats left
        elif button1['text'] == ' ':
            response1()
        elif button2['text'] == ' ':
            response2()
        elif button3['text'] == ' ':
            response3()
        elif button4['text'] == ' ':
            response4()
        elif button6['text'] == ' ':
            response6()
        elif button8['text'] == ' ':
            response8()  
        
    #################################
    
def button1_response():
        if button1['text'] == ' ':
            response1()
            AI_turn()
    
def button2_response():
        if button2['text'] == ' ':
            response2()
            AI_turn()
    
def button3_response():
        if button3['text'] == ' ':
            response3()
            AI_turn()
            
def button4_response():
        if button4['text'] == ' ':
            response4()
            AI_turn()
            
def button5_response():
        if button5['text'] == ' ':
            response5()
            AI_turn()
            
def button6_response():
        if button6['text'] == ' ':
            response6()
            AI_turn()
    
def button7_response():
        if button7['text'] == ' ':
            response7()
            AI_turn()
    
def button8_response():
        if button8['text'] == ' ':
            response8()
            AI_turn()
            
def button9_response():
        if button9['text'] == ' ':
            response9()
            AI_turn()
        
#####################################

root.mainloop()

