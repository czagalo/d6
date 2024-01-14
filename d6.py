import pyautogui
import time


pyautogui.PAUSE = 1

time.sleep(2)
pyautogui.hotkey('win', 'm')

abrir = ['Navegador Opera GX', 'Firecast', 'Explorador de Arquivos', 
         'Visual Studio Code', 'Discord']

for item in abrir:
    pyautogui.press('win')   
    pyautogui.write(item, interval=0.05)
    pyautogui.press('enter')

    #abrindo o navegador opera
    if item == 'Navegador Opera GX':
        time.sleep(4)
        pyautogui.hotkey('ctrl', 'e')
        sites = ('https://firecast.app/sdk3/RRPG%20SDK%203.html',
                 'https://github.com/czagalo')
        
        cont = 1
        for site in sites:
            time.sleep(1)
            pyautogui.write(site, interval=0.05)
            pyautogui.press('enter')
            
            if cont < len(sites):
                pyautogui.hotkey('ctrl', 't')
                cont = cont  + 1

    #abrindo o firecast
    if item == 'Firecast':
        time.sleep(4)
        pyautogui.moveTo(32, 121, duration=2, tween=pyautogui.easeInOutQuad)
        pyautogui.click()
        pyautogui.moveTo(121, 223, duration=2, tween=pyautogui.easeInOutQuad)
        pyautogui.click()

    #abrindo o explorador de arquivos
    if item == 'Explorador de Arquivos':
        time.sleep(4)
        for tab in range(1, 12):
            pyautogui.PAUSE = 0.3
            pyautogui.press('tab')
        for tab in range(1, 6):
            pyautogui.PAUSE = 0.5
            pyautogui.press('down')
        pyautogui.press('enter')
        pyautogui.press('tab')
        for tab in range(1, 3):
            pyautogui.press('down')
        pyautogui.press('enter')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('enter')
        pyautogui.press('down')
        pyautogui.press('up')
        pyautogui.press('enter')
        pyautogui.PAUSE = 1

    #abrindo o vscode
    if item == 'Visual Studio Code':
        time.sleep(6)
        for tab in range(1, 4):
            pyautogui.PAUSE = 0.5
            pyautogui.press('tab')
        pyautogui.press('enter')
        time.sleep(2)
        for tab in range(1, 8):
            pyautogui.PAUSE = 0.5
            pyautogui.press('tab')
        for tab in range(1, 4):
            pyautogui.PAUSE = 0.5
            pyautogui.press('down')
        pyautogui.press('enter')
        pyautogui.press('tab')
        for tab in range(1,3):
            pyautogui.press('down')
        pyautogui.press('enter')
        for tab in range(1,2):
            pyautogui.PAUSE = 0.5
            pyautogui.press('down')
        for tab in range(1,4):
            pyautogui.press('tab')
        pyautogui.press('enter')
