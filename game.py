from pprint import pprint 
import pygame
import abstractmethod

pprint(pygame.color.THECOLORS)
pygame.metodo()
# Inicializar o pygame
pygame.init()


# Configurar a janela do jogo
screen = pygame.display.set_mode([1920, 1080])

# Corrigir o nome da função, deve ser set_caption
pygame.display.set_caption('Jogo do Gabriel')


#Classe de Construção(construtor):

class game():
    def __init__(self, power, life, fly ) :
        self.power = power 
        self.life = life
        self.fly = fly
    def basic(sef):
        return game 
    




imagem_fundo = pygame.image.load('POO-Aulas-Aplica-o\assets\cenario.jpg')
goku_ssj = pygame.image.load('POO-Aulas-Aplica-o\assets\goku.jpg')
naruto = pygame.image.load('POO-Aulas-Aplica-o\assets\naruto.jpg')

#posição do player 1
pos_y_player = 600 
pos_x_player = 600
vel_goku_player = 15

#posição do player 2

# Corrigir o nome da variável "Looop" para "loop"
loop = True 

# Loop principal do jogo
while loop:
    for event in pygame.event.get():  # Corrigir "events" para "event"
        # Corrigir a verificação do tipo de evento de saída
        if event.type == pygame.QUIT:
            loop = False

    teclas = pygame.key.get_pressed()

    #Posição pra cima e pra baixo
    if teclas[pygame.K_UP]:
       pos_y_player -= vel_goku_player
    if teclas[pygame.K_DOWN]:
        pos_y_player += vel_goku_player

    #Posição Esquerda e Direita
    if teclas[pygame.K_LEFT]:
       pos_x_player -= vel_goku_player
    if teclas[pygame.K_RIGHT]:
        pos_x_player += vel_goku_player
        
    #Limitando o movimentação Player 1
    if pos_y_player <= -10:
        pos_y_player = -10
    if pos_y_player <= 400:
          pos_y_player = 440
    if pos_x_player <= 0:
        pos_x_player = 0
    if pos_x_player >= 1500:
        pos_x_player = 1500


    #Janelas 
    BLUE = pygame.color("blue")
    screen(imagem_fundo, (0, 0))
    screen(goku_ssj, (pos_x_player, pos_y_player))
    screen(naruto, (700, 30))
    
    # Atualizar a tela
    pygame.display.update()