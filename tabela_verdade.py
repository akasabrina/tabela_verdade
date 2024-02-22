# calculadora de tabela verdade
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas as pd
import numpy as np
import os 
df = pd.DataFrame()

def Conectivo():
    while True:

        try:
            print("Escolha um conectivo lógico para a tabela verdade\n1- Negação ¬\n2- Conjunção ∧\n3- Disjunção V\n4- Condicional →\n5- Bicondicional ↔")
            conectivo = int(input("Digite o número do conectivo lógico: "))

            if 1 <= conectivo <= 5:
                os.system("cls")
                return conectivo
            else:
                os.system("cls")
                print("Escolha uma opção válida!\n")

        except ValueError: # Se for inserido algo diferente de um número
            os.system("cls")
            print("Escolha uma opção válida!\n")


def CriaTabela(nome_tabela):
    tabela = []
    i = 0

    while i < 4:

        try:
            num = int(input(f"Digite 0 ou 1 para o {i+1}º número da tabela {nome_tabela}: "))

            if 0 <= num <= 1:
                tabela.append(num)
                i+=1
                os.system("cls")
            else:
                os.system("cls")
                print("Digito inválido\n")

        except ValueError: # Se for inserido algo diferente de um número
            os.system("cls")
            print("Digito inválido\n")

    df.insert(0, nome_tabela, tabela)
    os.system("cls")


def ConstroiTabela():
    cnt = Conectivo() # o tipo de conectivo influencia na forma da construção da tabela verdade

    match cnt:
        
        case 1: # contrução da tabela verdade com o conectivo lógico "Negação"
            CriaTabela('A')
            cond = [df["A"] == 1, df["A"] == 0]
            choiceNOT = [0, 1]
            df["¬A"] = np.select(cond, choiceNOT, default=np.nan)

        case _:
            CriaTabela('B')
            CriaTabela('A')
            cond = [(df["A"] == 1) & (df["B"] == 1), (df["A"] == 1) & (df["B"] == 0), (df["A"] == 0) & (df["B"] == 1), (df["A"] == 0) & (df["B"] == 0)]

            if cnt == 2: # contrução da tabela verdade com o conectivo lógico "Conjunção"
                choiceAND = [1, 0, 0, 0]
                df["A ∧ B"] = np.select(cond, choiceAND, default=np.nan)
            
            elif cnt == 3: # contrução da tabela verdade com o conectivo lógico "Disjunção"
                choiceOR = [1, 1, 1, 0]
                df["A V B"] = np.select(cond, choiceOR, default=np.nan)
            
            elif cnt == 4: # contrução da tabela verdade com o conectivo lógico "Condicional"
                choiceCOND = [1, 0, 1, 1]
                df["A → B"] = np.select(cond, choiceCOND, default=np.nan)
            
            elif cnt == 5: # contrução da tabela verdade com o conectivo lógico "Bicondicional"
                choiceBICOND = [1, 0, 0, 1]
                df["A ↔ B"] = np.select(cond, choiceBICOND, default=np.nan)

    for col in df.columns.values:
        df[col] = df[col].astype('int64')
    
    return df
    
if(__name__ == '__main__'):
    tabela_verdade = ConstroiTabela()
    print(tabela_verdade)