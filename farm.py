import pyautogui
import time
from PIL import Image
import cv2
import numpy as np

direcao = 'right'
# Lista de nomes de arquivo das imagens de exemplo
nomes_das_imagens = ['luta_pokemon.png', 'luta_pokemon2.png', 'luta_pokemon3.png', 'luta_pokemon4.png']

# Carregar as imagens de exemplo em uma lista
imagens_de_exemplo = []
for nome_do_arquivo in nomes_das_imagens:
    imagem = cv2.imread(nome_do_arquivo)
    imagens_de_exemplo.append(imagem)

while True:
    # Capture uma imagem da tela atual
    pyautogui.keyDown('space') 
    screenshot = pyautogui.screenshot()

    # Converta a captura de tela para uma matriz OpenCV (numpy array)
    tela = np.array(screenshot)

    # Converta a captura de tela para escala de cinza de 8 bits
    tela_cinza = cv2.cvtColor(tela, cv2.COLOR_BGR2GRAY).astype(np.uint8)

    # Variável para controlar se alguma correspondência foi encontrada
    correspondencia_encontrada = False

    # Itere por cada imagem de exemplo
    for imagem_de_exemplo in imagens_de_exemplo:
        # Converta a imagem de exemplo para escala de cinza
        imagem_de_exemplo_cinza = cv2.cvtColor(imagem_de_exemplo, cv2.COLOR_BGR2GRAY)

        # Realize a correspondência da imagem de exemplo na tela
        correspondencia = cv2.matchTemplate(tela_cinza, imagem_de_exemplo_cinza, cv2.TM_CCOEFF_NORMED)

        # Defina um limite de correspondência (ajuste conforme necessário)
        limite_correspondencia = 0.5

        # Encontre as posições onde a imagem de exemplo corresponde à tela
        loc = np.where(correspondencia >= limite_correspondencia)

        # Se houver pelo menos uma correspondência, você está em uma batalha
        if loc[0].size > 0:
            print("Entrou em uma batalha!")
            pyautogui.keyDown('z')
            pyautogui.keyUp('z')

            # Realize as ações de batalha, como usar ataques (adapte conforme necessário)

            # Defina a variável como True para indicar que uma correspondência foi encontrada
            correspondencia_encontrada = True

            # Saia do loop para evitar verificação adicional
            break

    if not correspondencia_encontrada:
        print("Não está em uma batalha.")
        pyautogui.keyDown(direcao)
        time.sleep(0.2) 
        pyautogui.keyUp(direcao)  # Solte a tecla pressionada

        # Alterne a direção
        if direcao == 'right':
            direcao = 'left'
        else:      
            direcao = 'right' 

    # Aguarde um momento antes de verificar novamente (ajuste o tempo conforme necessário)
    pyautogui.sleep(0.2)

# Continue o loop ou outras ações conforme necessário
       