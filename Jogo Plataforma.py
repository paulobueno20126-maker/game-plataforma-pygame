import pygame
import sys

# =========================
# INICIALIZAÇÃO
# =========================

pygame.init()

# Tela
LARGURA = 800
ALTURA = 600

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo Plataforma")

relogio = pygame.time.Clock()

# =========================
# CORES
# =========================

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
MARROM = (139, 69, 19)
AZUL = (100, 149, 237)

# =========================
# PLAYER
# =========================

player_largura = 50
player_altura = 50

player_x = 100
player_y = 400

velocidade_player = 5

gravidade = 0.5
velocidade_y = 0

pulando = False
forca_pulo = -12

vidas = 6

# =========================
# PLATAFORMA
# =========================

plataforma_y = 550
plataforma_altura = 50

# =========================
# FONTE
# =========================

fonte = pygame.font.SysFont("Arial", 30)

# =========================
# CLASSE INIMIGO
# =========================

class Inimigo:

    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.largura = 50
        self.altura = 50

        self.velocidade = 3

        self.direcao = 1

    def mover(self):

        self.x += self.velocidade * self.direcao

        if self.x <= 0:
            self.direcao = 1

        if self.x >= LARGURA - self.largura:
            self.direcao = -1

    def desenhar(self):

        pygame.draw.rect(
            tela,
            VERMELHO,
            (self.x, self.y, self.largura, self.altura)
        )

# =========================
# INIMIGO
# =========================

inimigo = Inimigo(500, 500)

# =========================
# FUNÇÃO COLISÃO
# =========================

def verificar_colisao():

    player_rect = pygame.Rect(
        player_x,
        player_y,
        player_largura,
        player_altura
    )

    inimigo_rect = pygame.Rect(
        inimigo.x,
        inimigo.y,
        inimigo.largura,
        inimigo.altura
    )

    return player_rect.colliderect(inimigo_rect)

# =========================
# LOOP PRINCIPAL
# =========================

ultimo_dano = 0
cooldown_dano = 1000

while True:

    relogio.tick(60)

    # =========================
    # EVENTOS
    # =========================

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # =========================
    # TECLAS
    # =========================

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT]:
        player_x -= velocidade_player

    if teclas[pygame.K_RIGHT]:
        player_x += velocidade_player

    # Pulo
    if teclas[pygame.K_UP] and not pulando:

        velocidade_y = forca_pulo
        pulando = True

    # =========================
    # GRAVIDADE
    # =========================

    velocidade_y += gravidade
    player_y += velocidade_y

    # Chão
    if player_y >= plataforma_y - player_altura:

        player_y = plataforma_y - player_altura
        velocidade_y = 0
        pulando = False

    # Limites
    if player_x < 0:
        player_x = 0

    if player_x > LARGURA - player_largura:
        player_x = LARGURA - player_largura

    # =========================
    # INIMIGO
    # =========================

    inimigo.mover()

    # =========================
    # COLISÃO
    # =========================

    tempo_atual = pygame.time.get_ticks()

    if verificar_colisao():

        if tempo_atual - ultimo_dano > cooldown_dano:

            vidas -= 1
            ultimo_dano = tempo_atual

            print("Vidas:", vidas)

    # =========================
    # GAME OVER
    # =========================

    if vidas <= 0:

        tela.fill(PRETO)

        texto_game_over = fonte.render(
            "GAME OVER",
            True,
            VERMELHO
        )

        tela.blit(
            texto_game_over,
            (
                LARGURA // 2 - texto_game_over.get_width() // 2,
                ALTURA // 2
            )
        )

        pygame.display.update()

        pygame.time.wait(3000)

        pygame.quit()
        sys.exit()

    # =========================
    # DESENHAR
    # =========================

    tela.fill(AZUL)

    # Plataforma
    pygame.draw.rect(
        tela,
        MARROM,
        (0, plataforma_y, LARGURA, plataforma_altura)
    )

    # Jogador
    pygame.draw.rect(
        tela,
        VERDE,
        (player_x, player_y, player_largura, player_altura)
    )

    # Inimigo
    inimigo.desenhar()

    # Texto vidas
    texto_vidas = fonte.render(
        f"Vidas: {vidas}",
        True,
        BRANCO
    )

    tela.blit(texto_vidas, (10, 10))

    # Atualizar tela
    pygame.display.update()
