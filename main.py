import pygame
import tkinter as tk
from facade import GameFacade

def start_game():
    root.destroy()  
    pygame.init()
    screen = pygame.display.set_mode((GameFacade.SCREEN_WIDTH, GameFacade.SCREEN_HEIGHT))
    game = GameFacade(screen)
    game.run()  
    root.quit()  
def exit_game():
    root.quit()

root = tk.Tk()
root.title("Menu do Jogo - Gabriel")
root.geometry("400x200")  

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

title = tk.Label(frame, text="Jogo do Gabriel", font=("Arial", 24, "bold"))
title.pack(pady=10)

start_btn = tk.Button(frame, text="Iniciar Jogo", font=("Arial", 16), command=start_game)
start_btn.pack(pady=5)

instructions = tk.Label(frame, text="Goku: Setas | Naruto: W/A/S/D\nZ: Kamehameha | X: Rasengan", font=("Arial", 10))
instructions.pack(pady=5)

exit_btn = tk.Button(frame, text="Sair", font=("Arial", 16), command=exit_game)
exit_btn.pack(pady=5)

root.mainloop()
