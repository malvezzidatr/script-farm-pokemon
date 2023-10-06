from pywinauto.application import Application
import pytesseract
import pyautogui
import time

emulator_path = 'C:\\Users\\caiom\\OneDrive\\Área de Trabalho\\visualboyadvance-m-Win-x86_64\\visualboyadvance-m.exe'
app = Application(backend="win32").start(emulator_path)

# Obtenha a janela do emulador do Gameboy
window = app.window(title_re="VisualBoyAdvance-M 2.1.6")  # Substitua pelo título da janela do seu emulador
print(window)
# Clique na palavra "File" (ou onde quer que ela esteja)
pyautogui.hotkey('alt', 'f')
pyautogui.hotkey('enter')

# caminho = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

pyautogui.write('pokemon')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
