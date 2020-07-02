from selenium import webdriver
from selenium.webdriver.common.by import By
import time

palavra = input("digite o que você busca:")

driver = webdriver.Chrome(executable_path=r'C://Users/Python/PycharmProjects/google/Chromedriver.exe')

driver.get('https://www.google.com.br/')

driver.find_element(By.NAME,"q").send_keys(palavra)
time.sleep(1)

while True:
    print(" busca com sorte digite 1 , busca normal digite 2 , 3 para buscar outra vez")
    buscaq = int(input("Digite a opção:"))
    time.sleep(1)
    if buscaq == 1:
        driver.find_element(By.NAME,"btnI").click()
    if buscaq ==2:
        driver.find_element(By.NAME,"btnK").click()
    elif buscaq == 3:
        palavra = input("digite o que você busca:")
        driver.get('https://www.google.com.br/')
        driver.find_element(By.NAME, "q").send_keys(palavra)
    else:
        driver.close()
        break


