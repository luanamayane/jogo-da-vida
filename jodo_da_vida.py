import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

# Configurações do jogo
tam_x = 50  # Tamanho da grade no eixo x
tam_y = 50  # Tamanho da grade no eixo y


# Função para atualizar a grade para a próxima geração
def atualizar_grade(grid):
    nova_grade = np.copy(grid)

    for i in range(tam_x):
        for j in range(tam_y):
            vizinhos = np.sum(grid[max(0, i - 1):min(i + 2, tam_x), max(0, j - 1):min(j + 2, tam_y)]) - grid[i][j]

            if grid[i][j] == 1 and (vizinhos < 2 or vizinhos > 3):
                nova_grade[i][j] = 0
            elif grid[i][j] == 0 and vizinhos == 3:
                nova_grade[i][j] = 1

    return nova_grade


# Função para inicializar a grade com células aleatórias
def inicializar_grade():
    return np.random.choice([0, 1], size=(tam_x, tam_y))


# Função para atualizar a animação ao pressionar o botão
def atualizar_animacao():
    num_geracoes = int(entry_geracoes.get())

    grid = inicializar_grade()
    fig, ax = plt.subplots()
    img = ax.imshow(grid, cmap='binary')
    ax.set_xticks([])
    ax.set_yticks([])
    plt.show(block=False)

    for geracao in range(num_geracoes):
        grid = atualizar_grade(grid)
        img.set_array(grid)
        plt.pause(0.1)


# Criação da janela
janela = tk.Tk()

# Criação do campo de entrada
label_geracoes = tk.Label(janela, text="Número de gerações:")
label_geracoes.pack()
entry_geracoes = tk.Entry(janela)
entry_geracoes.pack()

# Criação do botão
botao_atualizar = tk.Button(janela, text="Atualizar", command=atualizar_animacao)
botao_atualizar.pack()

# Exibição da janela
janela.mainloop()
