import pygame
from pygame.locals import *
from sys import exit

# Inicialização
pygame.init()

# Tela
largura = 800
altura = 600

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo de Plataforma")

relogio = pygame.time.Clock()

# Cores
COR_PLATAFORMA = (139, 69, 19)
COR_TEXTO = (255, 255, 255)

# Fundo
fundo_imagem = pygame.image.load(r"C:\Users\SENAI\Downloads\fundo.png")
fundo_imagem = pygame.transform.scale(fundo_imagem, (largura * 2, altura))

# Jogador
player_width = 100
player_height = 100

player_imagem = pygame.image.load(r"C:\Users\SENAI\Documents\paulo\slime.png")
player_imagem = pygame.transform.scale(player_imagem, (player_width, player_height))

# Imagem acima da cabeça
imagem_acima_cabeca = pygame.image.load(r"C:\Users\SENAI\Downloads\icone.png")

# Inimigo
imagem_inimigo = pygame.image.load(r"C:\Users\SENAI\Downloads\inimigo.png")
imagem_inimigo = pygame.transform.scale(imagem_inimigo, (80, 80))

# Fonte
fonte = pygame.font.SysFont("Arial", 30)

# Jogador posição
player_x = 100
player_y = altura - player_height - 50

# Movimento
player_vel = 5

# Física
gravidade = 0.5
player_vel_y = 0

em_pulo = False
forca_pulo = -12

# Plataforma
plataforma_altura = 50
plataforma_y = altura - plataforma_altura

# Camera
camera_x = 0
limite_x = largura // 2

# Colisão
contador_colisoes = 0
ultimo_tempo_colisao = 0
cooldown_colisao = 1000

# Classe inimigo
class Inimigo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidade = 2
        self.subindo = True
        self.altura_max = y - 100
        self.altura_min = y + 100

    def mover(self):

        # Movimento vertical
        if self.subindo:
            self.y -= self.velocidade

            if self.y <= self.altura_max:
                self.subindo = False

        else:
            self.y += self.velocidade

            if self.y >= self.altura_min:
                self.subindo = True

        # Movimento horizontal
        self.x -= self.velocidade

        if self.x < -80:
            self.x = largura + 200

# Criar inimigo
inimigo = Inimigo(700, 200)

# Função colisão
def verificar_colisao(px, py, ix, iy):

    rect_player = pygame.Rect(px, py, player_width, player_height)
    rect_inimigo = pygame.Rect(ix, iy, 80, 80)

    return rect_player.colliderect(rect_inimigo)

# Loop principal
while True:

    relogio.tick(60)

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            exit()

    teclas = pygame.key.get_pressed()

    mov_horizontal = 0

    # Movimento
    if teclas[K_LEFT]:
        player_x -= player_vel
        mov_horizontal = -1

    if teclas[K_RIGHT]:
        player_x += player_vel
        mov_horizontal = 1

    # Pulo
    if teclas[K_UP] and not em_pulo:
        player_vel_y = forca_pulo
        em_pulo = True

    # Gravidade
    player_vel_y += gravidade
    player_y += player_vel_y

    # Colisão com chão
    if player_y >= plataforma_y - player_height:
        player_y = plataforma_y - player_height
        player_vel_y = 0
        em_pulo = False

    # Limites
    if player_x < 0:
        player_x = 0

    # Camera
    if player_x > limite_x:
        camera_x = player_x - limite_x

    # Mover inimigo
    inimigo.mover()

    # Verificar colisão
    tempo_atual = pygame.time.get_ticks()

    if verificar_colisao(player_x, player_y, inimigo.x, inimigo.y):

        if tempo_atual - ultimo_tempo_colisao > cooldown_colisao:

            contador_colisoes += 1
            ultimo_tempo_colisao = tempo_atual

            print("Colisão:", contador_colisoes)

    # Game Over
    if contador_colisoes >= 6:

        tela.fill((0, 0, 0))

        texto = fonte.render("GAME OVER", True, (255, 0, 0))

        tela.blit(
            texto,
            (
                largura // 2 - texto.get_width() // 2,
                altura // 2
            )
        )

        pygame.display.update()

        pygame.time.wait(3000)

        pygame.quit()
        exit()

    # Desenhar fundo
    tela.blit(fundo_imagem, (-camera_x, 0))

    # Plataforma
    pygame.draw.rect(
        tela,
        COR_PLATAFORMA,
        (0 - camera_x, plataforma_y, largura * 2, plataforma_altura)
    )

    # Jogador
    tela.blit(player_imagem, (player_x - camera_x, player_y))

    # Imagem acima da cabeça
    tela.blit(
        imagem_acima_cabeca,
        (
            player_x - camera_x + 25,
            player_y - 50
        )
    )

    # Inimigo
    tela.blit(imagem_inimigo, (inimigo.x - camera_x, inimigo.y))

    # Texto nível
    texto_nivel = fonte.render("Nível 1", True, COR_TEXTO)
    tela.blit(texto_nivel, (10, 10))

    pygame.display.update()
