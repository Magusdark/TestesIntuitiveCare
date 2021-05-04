from tqdm import tqdm
import requests
import cgi
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

buffer_size = 1024


url = "http://www.ans.gov.br/prestadores/tiss-troca-de-informacao-de-saude-suplementar"
option = Options()
option.headless = True
browser = webdriver.Chrome(options = option)
browser.get(url)

url2 = browser.find_element_by_xpath("/html/body/div[9]/div/div[2]/div[2]/div[2]/a").get_attribute("href")
browser.get(url2)

url3 = browser.find_element_by_xpath("/html/body/div[9]/div/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[3]/a").get_attribute("href")

req = requests.get(url3)
nomeArquivo = req.url[url3.rfind('/')+1:]

file_size = int(req.headers.get("Content-Length", 0))

#Barra de progresso
progress = tqdm(req.iter_content(buffer_size), f"Downloading {nomeArquivo}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024)

#Mostra a barra de progresso e faz o download do arquivo
with open(nomeArquivo, "wb") as f:
    for data in progress.iterable:
        f.write(data)
        progress.update(len(data))
