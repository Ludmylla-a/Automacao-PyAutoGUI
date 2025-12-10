
import pyautogui
import time

pyautogui.FAILSAFE = True

print("Prepare-se! A automação começará em 5 segundos...")
time.sleep(5)

pyautogui.click(300, 300)
pyautogui.hotkey("ctrl", "l")
time.sleep(0.5)
pyautogui.write("https://www.google.com")
pyautogui.press("enter")

time.sleep(3)

pyautogui.write("Clima hoje na minha cidade")
pyautogui.press("enter")
time.sleep(4)

screenshot = pyautogui.screenshot()
screenshot.save("previsao.png")

pyautogui.alert("Automação concluída com sucesso! Arquivo salvo como previsao.png")
