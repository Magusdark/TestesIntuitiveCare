import tabula
import pandas as pd
from zipfile import ZipFile

file_path = "./Padrão_TISS_Componente_Organizacional_202103.pdf"

dfs = tabula.read_pdf(file_path, pages=[79,80,81,82,83,84,85])
#Aqui eu concatenei os DataFrames para formar a tabela de categoria padrão, mas eu não estou conseguindo achar solução para um erro que está ocorrendo.
tabela = pd.concat([dfs[1],dfs[2],dfs[3],dfs[4],dfs[5],dfs[6]], ignore_index = True)
#print(tabela)
dfs[0].to_csv("Tabela de tipo de demandante.csv", index = False)
tabela.to_csv("Tabela de categoria do Padrão TISS.csv", index = False)
dfs[7].to_csv("Tabela de tipo de solicitação.csv", index = False)

with ZipFile("Teste_Intuitive_Care_MatheusIgnacio.zip", "w") as arqZip:
    arqZip.write("Tabela de tipo de demandante.csv")
    arqZip.write("Tabela de categoria do Padrão TISS.csv")
    arqZip.write("Tabela de tipo de solicitação.csv")
    
arqZip.close()


