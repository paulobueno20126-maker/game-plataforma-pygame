# 🕹️ Jogo de Plataforma - Pygame Edition

Este projeto é uma implementação de um jogo de plataforma desenvolvido em Python utilizando a biblioteca **Pygame**. O foco principal foi aplicar conceitos de física, inteligência artificial e gestão de colisões.

> **Nota:** O jogo original utilizava recursos visuais (imagens e sprites) provenientes do repositório interno do SENAI, os quais não se encontram disponíveis para distribuição pública. Esta versão utiliza formas geométricas para garantir a funcionalidade do código em qualquer ambiente.

## 🚀 Funcionalidades Implementadas
- **Física de Movimento:** Sistema de gravidade constante e lógica de pulo com detecção de solo.
- **Inteligência Artificial (IA):** Inimigo com comportamento de patrulha automática (movimentação lateral contínua).
- **Sistema de Vida e Dano:** Mecanismo de colisão com intervalo de segurança (cooldown) de 1 segundo para evitar perda instantânea de progresso.
- **Interface de Utilizador (HUD):** Exibição de pontuação de vidas em tempo real e ecrã de encerramento (Game Over).

## 🛠️ Tecnologias e Conceitos
- **Python 3:** Linguagem base do projeto.
- **Pygame:** Biblioteca utilizada para renderização gráfica e controlo de eventos.
- **POO (Programação Orientada a Objetos):** Utilização de classes para estruturar o inimigo e os seus comportamentos.
- **Lógica de Colisão:** Implementação de retângulos matemáticos para interações precisas entre os elementos do jogo.

## 🎮 Como Jogar
- **Setas Esquerda/Direita:** Movimentação do personagem.
- **Seta Cima:** Pular.
- **Desafio:** Sobreviver ao contacto com o inimigo vermelho e evitar que as vidas cheguem a zero.

---
*Projeto desenvolvido como parte do portfólio técnico de Programação em Python.*
