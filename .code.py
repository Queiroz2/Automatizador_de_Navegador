print ("Hello, World!")
print ("Hello, Python!")

import pyautogui 
import time

#Abrir o navegador 

pyautogui.press("win")    
pyautogui.write("chrome")
pyautogui.press("enter")

#escrever youtube.com

time.sleep(5) #vai esperar 5 segundos paa o navegador abrir
pyautogui.write("youtube.com")
pyautogui.press("enter")
time.sleep(10) #vai esperar o youtube carregar


#clicar no campo de pesquisa

pyautogui.click(x=586 , y=149) #clicar no campo de pesquisa
time.sleep(10)

#digitar "Python"

pyautogui.write("O nome dela e Jeniffer")
time.sleep(5)

#Pressionar"Enter"

pyautogui.press("enter")
time.sleep(5)
pyautogui.click(x=528 , y=384)

#Escolher o primeiro vídeo
