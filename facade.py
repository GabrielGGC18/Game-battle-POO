import pygame
from game_manager import GameManager
from events import GameEvent, ConsoleNotifier
from characters import CharacterFactory
from strategies import NormalMove, FastMove

class HUD:
    def __init__(self, surface):
        self.surface = surface
        self.font = pygame.font.SysFont("Arial", 24)
        self.small_font = pygame.font.SysFont("Arial", 18)

    def draw_life_bar(self, character, x, y):
        pygame.draw.rect(self.surface, (255, 0, 0), (x, y, 200, 20))  # vida máxima
        pygame.draw.rect(self.surface, (0, 255, 0), (x, y, character.life, 20))  # vida atual
        text = self.font.render(f"{character.name} - Vida: {character.life}", True, (255, 255, 255))
        self.surface.blit(text, (x, y - 25))

    def draw_score(self, score, x, y):
        text = self.font.render(f"Pontuação: {score}", True, (255, 255, 0))
        self.surface.blit(text, (x, y))
    
    def draw_special_move(self, character, x, y):
        if character.special_move_timer > 0:
            text = self.small_font.render(character.special_move_text, True, (255, 100, 0))
            self.surface.blit(text, (x, y))
    
    def draw_exit_hint(self):
        text = self.small_font.render("Pressione ESC para sair", True, (200, 200, 200))
        self.surface.blit(text, (self.surface.get_width() - 250, self.surface.get_height() - 25))


class GameFacade:
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 369
    
    def __init__(self, surface):
        self.surface = surface
        pygame.display.set_caption("Jogo do Gabriel")


        #background
        self.bg = pygame.image.load("assets/cenario.jpg").convert()
        # Observer  
        self.events = GameEvent()
        self.events.add_observer(ConsoleNotifier())

        # Singleton
        self.manager = GameManager()

        # Factory + Strategy
        self.goku = CharacterFactory.create("goku", NormalMove())
        self.naruto = CharacterFactory.create("naruto", FastMove())

        # HUD
        self.hud = HUD(surface)

        # Posições iniciais - frente a frente para combate (posições horizontais fixas)
        self.goku_x = 80
        self.naruto_x = 600
        self.goku_y = self.SCREEN_HEIGHT - self.goku.image.get_height() - 10
        self.naruto_y = self.SCREEN_HEIGHT - self.naruto.image.get_height() - 10
        self.score = 0
        
        # Controle de ataques especiais (para evitar múltiplos ataques simultâneos)
        self.goku_attack_cooldown = 0
        self.naruto_attack_cooldown = 0

    def run(self):
        clock = pygame.time.Clock()
        while True :
            clock.tick(60)  # 60 FPS
            
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.manager.stop()
                    return
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        self.manager.stop()
                        return

            keys = pygame.key.get_pressed()
            
            # Movimento do Goku (Setas)
            if keys[pygame.K_UP]: 
                self.goku_y -= 10
            if keys[pygame.K_DOWN]: 
                self.goku_y += 10
            if keys[pygame.K_LEFT]: 
                self.goku_x -= 10
            if keys[pygame.K_RIGHT]: 
                self.goku_x += 10
            
            # Movimento do Naruto (W, A, S, D)
            if keys[pygame.K_w]: 
                self.naruto_y -= 10
            if keys[pygame.K_s]: 
                self.naruto_y += 10
            if keys[pygame.K_a]: 
                self.naruto_x -= 10
            if keys[pygame.K_d]: 
                self.naruto_x += 10
            
            # Limite de movimento para ambos não saírem da tela
            self.goku_x = max(0, min(self.goku_x, self.SCREEN_WIDTH - self.goku.image.get_width()))
            self.goku_y = max(0, min(self.goku_y, self.SCREEN_HEIGHT - self.goku.image.get_height() - 10))
            
            self.naruto_x = max(0, min(self.naruto_x, self.SCREEN_WIDTH - self.naruto.image.get_width()))
            self.naruto_y = max(0, min(self.naruto_y, self.SCREEN_HEIGHT - self.naruto.image.get_height() - 10))
            
            # Poder especial do Goku - Tecla Z (com cooldown)
            if keys[pygame.K_z] and self.goku_attack_cooldown == 0:
                self.goku.special_move()
                self.goku_attack_cooldown = 30  # 30 frames de cooldown
                # Dano ao Naruto
                self.naruto.life -= 20
                self.events.notify(f"Goku usou Kamehameha! Naruto recebeu 20 de dano!")
            
            # Poder especial do Naruto - Tecla X (com cooldown)
            if keys[pygame.K_x] and self.naruto_attack_cooldown == 0:
                self.naruto.special_move()
                self.naruto_attack_cooldown = 30  # 30 frames de cooldown
                # Dano ao Goku
                self.goku.life -= 15
                self.events.notify(f"Naruto usou Rasengan! Goku recebeu 15 de dano!")
            
            # Decrementar cooldowns
            if self.goku_attack_cooldown > 0:
                self.goku_attack_cooldown -= 1
            if self.naruto_attack_cooldown > 0:
                self.naruto_attack_cooldown -= 1
            
            # Decrementar timer dos ataques especiais
            if self.goku.special_move_timer > 0:
                self.goku.special_move_timer -= 1
            if self.naruto.special_move_timer > 0:
                self.naruto.special_move_timer -= 1
            
            # Verificar se alguém morreu
            if self.goku.life <= 0:
                self.events.notify("Naruto venceu!")
                self.score += 100
                break
            if self.naruto.life <= 0:
                self.events.notify("Goku venceu!")
                self.score += 100
                break

            # Renderização
            self.surface.blit(self.bg, (0, 0))
            self.surface.blit(self.goku.image, (self.goku_x, self.goku_y))
            self.surface.blit(self.naruto.image, (self.naruto_x, self.naruto_y))

            # HUD
            self.hud.draw_life_bar(self.goku, 20, 20)
            self.hud.draw_life_bar(self.naruto, 20, 80)
            self.hud.draw_score(self.score, 600, 20)
            self.hud.draw_special_move(self.goku, 20, 130)
            self.hud.draw_special_move(self.naruto, 20, 160)
            self.hud.draw_exit_hint()

            pygame.display.update()

