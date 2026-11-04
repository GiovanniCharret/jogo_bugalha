"""
Código 'artesanal' do jogo bugalha
"""

import random
import tkinter as tk

# As duas matrizes que representam os tabuleiros dos jogadores
j1 = [[0,0,0],[0,0,0],[0,0,0]]
j2 = [[0,0,0],[0,0,0],[0,0,0]]

# A vez de qual jogador. Se j1_row == False, então é j2. Não é necessário criar uma j2_row
j1_time = True
game_over = False

# Variáveis de tela:
window = tk.Tk()
window.title("Bugalha_by_gio")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)


def print_tabuleiro(j1, j2, cel_row_j1_coloring=0, cel_row_j2_coloring=0, j1_name="J1", j2_name="J2"):
    """
    Organizar a tela de impressão de dados do tabuleiro dos jogadores

    """

    # Inicializando a estrutura de cores 
    l1c1, l1c2, l1c3 = "37", "37", "37"
    l2c1, l2c2, l2c3 = "37", "37", "37"
    l3c1, l3c2, l3c3 = "37", "37", "37"
    l4c1, l4c2, l4c3 = "37", "37", "37"
    l5c1, l5c2, l5c3 = "37", "37", "37"
    l6c1, l6c2, l6c3 = "37", "37", "37"

       
    #  Troca de cor da célula da jogador 1
    if cel_row_j1_coloring == 1:
        # Esse arranjo permite bebugar e visualizar mais fácil
        l1c1, l1c2, l1c3 = "37", "37", "37"
        l2c1, l2c2, l2c3 = "37", "37", "37"
        l3c1, l3c2, l3c3 = "33", "37", "37"
    elif cel_row_j1_coloring == 2:
        # Esse arranjo permite bebugar e visualizar mais fácil
        l1c1, l1c2, l1c3 = "37", "37", "37"
        l2c1, l2c2, l2c3 = "37", "37", "37"
        l3c1, l3c2, l3c3 = "37", "33", "37"
    elif cel_row_j1_coloring == 3:
        # Esse arranjo permite bebugar e visualizar mais fácil
        l1c1, l1c2, l1c3 = "37", "37", "37"
        l2c1, l2c2, l2c3 = "37", "37", "37"
        l3c1, l3c2, l3c3 = "37", "37", "33"
    elif cel_row_j1_coloring == 4:
        # Esse arranjo permite bebugar e visualizar mais fácil
        l1c1, l1c2, l1c3 = "37", "37", "37"
        l2c1, l2c2, l2c3 = "33", "37", "37"
        l3c1, l3c2, l3c3 = "37", "37", "37"
    elif cel_row_j1_coloring == 5:
        # Esse arranjo permite bebugar e visualizar mais fácil
        l1c1, l1c2, l1c3 = "37", "37", "37"
        l2c1, l2c2, l2c3 = "37", "33", "37"
        l3c1, l3c2, l3c3 = "37", "37", "37"
    elif cel_row_j1_coloring == 6:
        # Esse arranjo permite bebugar e visualizar mais fácil
        l1c1, l1c2, l1c3 = "37", "37", "37"
        l2c1, l2c2, l2c3 = "37", "37", "33"
        l3c1, l3c2, l3c3 = "37", "37", "37"
    elif cel_row_j1_coloring == 7:
        # Esse arranjo permite bebugar e visualizar mais fácil
        l1c1, l1c2, l1c3 = "33", "37", "37"
        l2c1, l2c2, l2c3 = "37", "37", "37"
        l3c1, l3c2, l3c3 = "37", "37", "37"
    elif cel_row_j1_coloring == 8:
        # Esse arranjo permite bebugar e visualizar mais fácil
        l1c1, l1c2, l1c3 = "37", "33", "37"
        l2c1, l2c2, l2c3 = "37", "37", "37"
        l3c1, l3c2, l3c3 = "37", "37", "37"
    elif cel_row_j1_coloring == 9:
        # Esse arranjo permite bebugar e visualizar mais fácil
        l1c1, l1c2, l1c3 = "37", "37", "33"
        l2c1, l2c2, l2c3 = "37", "37", "37"
        l3c1, l3c2, l3c3 = "37", "37", "37"

    #  Troca de cor da célula da jogador 2
    if cel_row_j2_coloring == 1:
        # Esse arranjo permite bebugar e visualizar mais fácil
        l4c1, l4c2, l4c3 = "37", "37", "37"
        l5c1, l5c2, l5c3 = "37", "37", "37"
        l6c1, l6c2, l6c3 = "33", "37", "37"
    elif cel_row_j2_coloring == 2:
        # Esse arranjo permite bebugar e visualizar mais fácil
        l4c1, l4c2, l4c3 = "37", "37", "37"
        l5c1, l5c2, l5c3 = "37", "37", "37"
        l6c1, l6c2, l6c3 = "37", "33", "37"
    elif cel_row_j2_coloring == 3:
        # Esse arranjo permite bebugar e visualizar mais fácil
        l4c1, l4c2, l4c3 = "37", "37", "37"
        l5c1, l5c2, l5c3 = "37", "37", "37"
        l6c1, l6c2, l6c3 = "37", "37", "33"
    elif cel_row_j2_coloring == 4:
        # Esse arranjo permite bebugar e visualizar mais fácil
        l4c1, l4c2, l4c3 = "37", "37", "37"
        l5c1, l5c2, l5c3 = "33", "37", "37"
        l6c1, l6c2, l6c3 = "37", "37", "37"
    elif cel_row_j2_coloring == 5:
        # Esse arranjo permite bebugar e visualizar mais fácil
        l4c1, l4c2, l4c3 = "37", "37", "37"
        l5c1, l5c2, l5c3 = "37", "33", "37"
        l6c1, l6c2, l6c3 = "37", "37", "37"
    elif cel_row_j2_coloring == 6:
        # Esse arranjo permite bebugar e visualizar mais fácil
        l4c1, l4c2, l4c3 = "37", "37", "37"
        l5c1, l5c2, l5c3 = "37", "37", "33"
        l6c1, l6c2, l6c3 = "37", "37", "37"
    elif cel_row_j2_coloring == 7:
        # Esse arranjo permite bebugar e visualizar mais fácil
        l4c1, l4c2, l4c3 = "33", "37", "37"
        l5c1, l5c2, l5c3 = "37", "37", "37"
        l6c1, l6c2, l6c3 = "37", "37", "37"
    elif cel_row_j2_coloring == 8:
        # Esse arranjo permite bebugar e visualizar mais fácil
        l4c1, l4c2, l4c3 = "37", "33", "37"
        l5c1, l5c2, l5c3 = "37", "37", "37"
        l6c1, l6c2, l6c3 = "37", "37", "37"
    elif cel_row_j2_coloring == 9:
        # Esse arranjo permite bebugar e visualizar mais fácil
        l4c1, l4c2, l4c3 = "37", "37", "33"
        l5c1, l5c2, l5c3 = "37", "37", "37"
        l6c1, l6c2, l6c3 = "37", "37", "37"


    # Se o nome do jogador não for informado, será usado o padrão J1 e J2
    print(' | ',f"\033[{l1c1}m{j1[0][0]}\033[m",' . ', f"\033[{l1c2}m{j1[1][0]}\033[m",' . ', f"\033[{l1c3}m{j1[2][0]}\033[m",' |' ,'\n', 
        '| ',f"\033[{l2c1}m{j1[0][1]}\033[m",' . ', f"\033[{l2c2}m{j1[1][1]}\033[m",' . ', f"\033[{l2c3}m{j1[2][1]}\033[m",' |','    j1_name','\n',
        '| ',f"\033[{l3c1}m{j1[0][2]}\033[m",' . ', f"\033[{l3c2}m{j1[1][2]}\033[m",' . ', f"\033[{l3c3}m{j1[2][2]}\033[m",' |','\n',
        '-------------------','\n',
        '         X         ','\n',
        '-------------------','\n',
        '| ',f"\033[{l4c1}m{j2[0][0]}\033[m",' . ', f"\033[{l4c2}m{j2[1][0]}\033[m",' . ', f"\033[{l4c3}m{j2[2][0]}\033[m",' |' ,'\n', 
        '| ',f"\033[{l5c1}m{j2[0][1]}\033[m",' . ', f"\033[{l5c2}m{j2[1][1]}\033[m",' . ', f"\033[{l5c3}m{j2[2][1]}\033[m",' |','    j2_name','\n',
        '| ',f"\033[{l6c1}m{j2[0][2]}\033[m",' . ', f"\033[{l6c2}m{j2[1][2]}\033[m",' . ', f"\033[{l6c3}m{j2[2][2]}\033[m",' |','\n',
        )


def j1_row(dice_roll):
    """
    
    """
    # Declaração só de ramp up do loop e da cor da célula
    which_col = 0
    cel_color = 0

    print("Sua vez. \n\n",
        "O lance do dado foi... \n\n",
        dice_roll,
        "\n\n",
        "Escolha uma coluna para jogar... \n"
    )

    # which_col é como uma flag para anotar na coluna. Se ela está diferente de 1, 2 ou 3, o script não preenche a coluna 
    while which_col not in [1, 2, 3]:
        which_col = int(input("\nDigite apenas 1 ou 2 ou 3: "))

        # Meramente para organizar o script. 
        # Se which_col dentro de 1,2 ou 3, vai preencher a coluna e depois vai voltar para 0
        if which_col in [1, 2, 3]:

            # Preenchendo a coluna e destruindo os elementos da col adversária
            if j1[which_col-1][2] == 0:
                # A primeira casa preenchida é o terceiro item do array
                j1[which_col-1][2] = dice_roll
                # Ternário da cor
                cel_color = 1 if which_col == 1 else 2 if  which_col == 2 else 3
            elif j1[which_col-1][1] == 0:
                j1[which_col-1][1] = dice_roll
                # Ternário da cor
                cel_color = 4 if which_col == 1 else 5 if  which_col == 2 else 6
            elif j1[which_col-1][0] == 0:                    
                # A última casa preenchida é o primeiro item do array    
                j1[which_col-1][0] = dice_roll
                # Ternário da cor
                cel_color = 7 if which_col == 1 else 8 if  which_col == 2 else 9
            else:
                print("\n\n A coluna está cheia! \n Escoha outra coluna.\n\n")
                # which_col volta para 0, impedindo a coluna de ser preenchida novamente.
                which_col = 0

    # Destruir os elementos do oponente
    for j in range(3):
        if j2[which_col-1][j] == dice_roll:
            j2[which_col-1].remove(dice_roll)
            j2[which_col-1].insert(0,0) 

    # Mostra a jogada
    print_tabuleiro(j1, j2, cel_color)

    # which_col volta para 0, impedindo a coluna de ser preenchida novamente.
    which_col = 0


def j2_row(dice_roll):
    """
    """
    # Declaração só de ramp up do loop e da cor
    which_col = 0
    cel_color = 0

    print("Vez do Oponente. \n\n",
        "O lance do dado foi... \n\n",
        dice_roll,
        "\n\n"
    )

    while which_col == 0:
    
        # which_col é como uma flag para anotar na coluna. Se ela está diferente de 1, 2 ou 3, o script não preenche a coluna 
        which_col = random.randint(1, 3)

        # Preenchendo a coluna e destruindo os elementos da coluna adversária
        if j2[which_col-1][2] == 0:
            # A primeira casa preenchida é o terceiro item do array
            j2[which_col-1][2] = dice_roll
            # Ternário da cor
            cel_color = 1 if which_col == 1 else 2 if  which_col == 2 else 3
        elif j2[which_col-1][1] == 0:
            j2[which_col-1][1] = dice_roll
            # Ternário da cor
            cel_color = 4 if which_col == 1 else 5 if  which_col == 2 else 6
        elif j2[which_col-1][0] == 0:                    
            # A última casa preenchida é o primeiro item do array    
            j2[which_col-1][0] = dice_roll
            # Ternário da cor
            cel_color = 7 if which_col == 1 else 8 if  which_col == 2 else 9
        else:
            # Retorna o while para tentar preencher outra coluna. Sem isso, o if passa direto nas coluna já preenchidas e o j2 perde o registro
            which_col = 0


    # Destruir os elementos do oponente
    for j in range(3):
        if j1[which_col-1][j] == dice_roll:
            j1[which_col-1].remove(dice_roll)
            j1[which_col-1].insert(0,0) 

    # Mostra a jogada
    print_tabuleiro(j1, j2, 0 , cel_color)


def score(j1, j2, j1_name="J1", j2_name="J2"):
    """
    """

    # Inicializando variáveis
    j1_score, j2_score = 0, 0

    # Se o set de j é uma unidade menor que len de j, então o número é repetido. Multiplica por 2.
    # Se o set de j são duas unidades menor que len de j, então o a coluna toda é o mesmo número. Multiplica por 3.
    # For para somar cada coluna. 
    for n in range(0,3):
        #j1
        for j in range(1,7):
            # Check ------------------------------
            #print("n", n, "j", j, f"count{j}", j2[n].count(j), "score", j2_score)
            #Conta 1 a 6, procura a quandidade de casa. Se tem 2, então * 2. Sem tem 3, então * 3.
            # ==1 porque se não colocar o igual, o loop fica somando tudo.
            # O zero porque senão ele soma algum elemento errado
            # Explicação da fórmula: j1_score += j * 3 é meramente a soma dos três números. Precisa multiplicar os 3 números por 3
            # então, j1_score += j * 9.
            # A mesma coisa para j * 4 (são a soma de dois números iguais, vezes 2)
            j1_score += j * 9 if j1[n].count(j) == 3 else j * 4 if j1[n].count(j) == 2 else j if j1[n].count(j) == 1 else 0    
            # ------------------------------------
        #j2
        for j in range(1,7): 
            #Check --------------------------------------
            
            #print("n", n, "j", j, f"count{j}", j2[n].count(j), "score", j2_score)
            #-------------------------------------------
            # Mesma lógica acima. Sem o ternário para facilitar o racionio. 
            if j2[n].count(j) == 3:
                j2_score += j * 9
            elif j2[n].count(j) == 2:
                j2_score += j * 4
            elif j2[n].count(j) == 1:
                j2_score += j
            else:
                j2_score += 0


    print("---------------------\n"
          "O score está em: \n",
          j1_name, ": ", j1_score, "\n",
          j2_name, ": ", j2_score, "\n",
          "---------------------", ""
    )

# Window



# Main
if __name__ == "__main__":
    
    while game_over == False:

       # O número do dado
       row = random.randint(1,6)
       
       if j1_time:
           j1_row(row)
           # Troca a flag para j2 jogar
           j1_time = False
       else:
           j2_row(row)
           # Troca a flag para j1 jogar
           j1_time = True

       # Placar do jogo
       score(j1, j2) 

       # Decidindo sobre encerramento
       # Se nenhum zero em j1 ou nenhum zero em j2
       if 0 not in j1[0] and 0 not in j1[1] and 0 not in j1[2] or 0 not in j2[0] and 0 not in j2[1] and 0 not in j2[2]:
           game_over = True
           print("\n","fim")

    #    elif 0 not in j2[0] and 0 not in j2[1] and 0 not in j2[2]:         
    #        game_over = True
    #        print("\n","fim")

