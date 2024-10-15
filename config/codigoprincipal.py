"""
Este projeto tem como finalidade possibilitar ao agricultor familiar acesso a tecnologia, é importante
ressaltar que os dados são uma mistura de dados reais e fictícios, utilizados para fins acadêmicos
Autor:
Hilmar Gomes Marques da Silva (RM560007)
Iolanda Helena Fabbrini Manzali de Oliveira (RM560595)
Murilo Carone Nasser (RM560464)
Pedro Eduardo Soares de Sousa (RM560903)
Yago Brendon Iama (RM560674)

Data: 15/10/2024

"""

import pyodbc
from rpy2 import robjects
r = robjects.r
while True:
    print("------------Menu Príncipal------------")
    print(" 1. Informações Cadastrais \n 2. Plano de Cultura \n 3. Infromações Sobre, Clima, Solo e Agricultura \n 4. Sugestões de Melhorias \n 5. Sair")
    op = int(input("Digite o número referente a opção de sua escolha:"))
    if op == 1:
        while True:
            print("-----Menu Cadastral-----")
            print(" 1. Efetuar cadastro \n 2. Voltar ao menu principal")
            op = int(input("Digite o número referente a opção de sua escolha:"))
            if op == 1:
                # Criando um dicionário para armazenar os dados cadastrais
                dados_cadastrais = {}
                #Solicitando as informaçoes e armazenando-os no dicionário
                dados_cadastrais['nome'] = input ('Digite seu nome completo:')
                dados_cadastrais['email'] = input ('Digite seu email:')
                dados_cadastrais['car'] = input ('Digite seu Car:')
                #Exibindo confirmação de cadastro e os dados armazenados
                print('\nCadastro realizado com sucesso!')
                print('Dados armazenados:')
                print(f'Nome: {dados_cadastrais['nome']}')
                print(f'Email:{dados_cadastrais['email']}')
                print(f'Car: {dados_cadastrais['car']}')
                break
            elif op == 2:
                print("Volatndo ao menu principal")
                break
            else:
                print("Opção invalida, escolha novamente")
    elif op == 2:
        while True:
            print("----------Regiões do País----------")
            print(" 1. Região Sul \n 2. Região Sudeste \n 3. Região Norte \n 4. Região Nordeste \n 5. Região Centro-Oeste \n 6. Voltar ao Menu Principla")
            op = int(input("Digite o número referente a região em que mora: "))
            #-----------Definindo Funções Gerais---------
            #---Área Util---
            def area_util(at:float)-> float:#  at = área total 
                return at/4
            #---Número Total de Mudas---
            def num_mudas_total(at:float, n_mudas_m:float)-> float:  # at = área total e n_mudas_m = números de mudas por m²
                return (at/4)* n_mudas_m
            #---Número Total de Ruas (50 ruas por hectar)---
            def numero_ruas_total (at:float) -> float:
                return (at/10000)*50
            #--- Calcio Toal---  -> (0.75 toneladas de calcio por hectar ²) - (1 hectar = 10000 m²)
            def calcio_total (at: float) -> float: #  at = área total 
                return (at/10000) * 0.75
            #---Adubo NPK  -> 0.85 kga cada m²
            def adubo_NPK(at:float) ->float: # at = área total 
                return at * 0.85
            #---Inseticida Aplicação 1 - 2.75/m²
            def inseticida1(at:float) -> float: # at = área total 
                return at * 2.75
            #---Inseticida Aplicação 2 - 1.50/m²
            def inseticida2(at:float) -> float: # at = área total 
                return at * 1.50
            #---Fungicida Aplicação 1 - 2.50/m²
            def fungicida1(at:float) -> float: # at = área total 
                return at * 2.50
            #---Fungicida Aplicação 2 - 1.75/m²
            def fungicida2(at:float) -> float: # at = área total 
                return at * 1.75
            if op == 1:
                #-----Região Sul-----
                print("------Culturas------")
                print(" 1. Trigo (grão) \n 2. Bata (hortaliça) \n 3. Maçã (fruta) \n 4 Voltar") 
                op = int(input("Digite o número referente a  opção que deseja plantar: ")) 
                if op == 1:
                    #---------------------------------------------------------------------Cultura - Trigo ---------------------------------------------------------------------
                    # a cultur do trigo é dividida em duas fases cada uma com duaração de 2 meses
                    #----------Definir Funções Específicas----------
                    #---Irrigação1 (8.75L de água por m²)---
                    def irrigação1_diaria_total_trigo(at:float) -> float:
                        return at * 8.75
                    #---Irrigação2 (7.25L de água por m²)---
                    def irrigação2_diaria_total_trigo(at:float) -> float:
                        return at * 7.25
                    #---Número de Grãos Total (3 kg por muda de trigo)
                    def ngraos_total_trigo (at:float) -> float:
                        return 3 * ((at/4) * 5)
                    #----------Código Principal----------
                    #---------- Fase1----------
                    dados_trigo = {}
                    print("Um cilco completo do Trigo duara 120 dia, ou seja, 4 mêses")
                    print("A cultura do trigo é divida em duas fases cada uma com duração de 2 meses ")
                    print("Aplantação posuirá ruas com espaçamente de 1 m entre as ruas e as mudas devem ser plantads com espaçamento de 1 m entr elas")
                    #criando varias para as funções apra que possam ser vetorizadas
                    dados_trigo["area_total_trigo"] = float(input("Área disponível para plantação em m²: "))
                    # Calculando e armazenando os resultados no dicionário
                    # Informações Básicas----------------------------------------------------------------------------------------
                    dados_trigo["area_util_trigo"] = area_util(dados_trigo["area_total_trigo"])  
                    dados_trigo["numero_mudas_total_trigo"] = num_mudas_total(dados_trigo["area_total_trigo"], 5)  # 5 mudas por m²
                    dados_trigo["numero_graos_total_trigo"] = ngraos_total_trigo(dados_trigo["area_total_trigo"]) 
                    dados_trigo["num_ruas_trigo"] = numero_ruas_total(dados_trigo["area_total_trigo"])
                    # Insumos--------------------------------------------------------------------------------------------------------
                    dados_trigo["calcio_total_trigo"] = calcio_total(dados_trigo["area_total_trigo"])
                    dados_trigo["npk_fase1_trigo"] = adubo_NPK(dados_trigo["area_total_trigo"])
                    dados_trigo["inseticida_aplicacao1_trigo"] = inseticida1(dados_trigo["area_total_trigo"])
                    dados_trigo["fungicida_aplicacao1_trigo"] = fungicida1(dados_trigo["area_total_trigo"])
                    dados_trigo["ir_fase1_diária_total_trigo"] = irrigação1_diaria_total_trigo(dados_trigo["area_total_trigo"])
                    dados_trigo["ir_fase1_semanal_total_trigo"] = dados_trigo["ir_fase1_diária_total_trigo"] * 7
                    dados_trigo["ir_fase1_mes_total_trigo"] = dados_trigo["ir_fase1_semanal_total_trigo"] * 4
                    dados_trigo["ir_fase1_total_trigo"] = dados_trigo["ir_fase1_mes_total_trigo"] * 2 # fase 1 duara 2 meses
                   #Prints Informações Básicas + Insumos----------------------------------------------------------------------------------------------------------------------------------
                    print("----------Informações Básicas----------")
                    print(f"A área util é de: {dados_trigo["area_util_trigo"]:.2f} m²")
                    print(f"O número total de mudas a serem plantadas é de {dados_trigo["numero_mudas_total_trigo"]:.1f} mudas")
                    print(f"A plantação terá {dados_trigo["num_ruas_trigo"]:.1f} ruas")
                    print(f"O a quantidade de grãos de trigo obitidas após um ciclo completo é de {dados_trigo["numero_graos_total_trigo"]:.2f}kg")
                    print("-----------Insumos 1°Fase----------")
                    print(f"O calcio deve ser aplicado 1 vez, sendo necessário aplicar 0.7 toneladas de cálcio por hectare, totalizando {dados_trigo["calcio_total_trigo"]:.2f} toneladas de cálcio")
                    print(f"O Adubo deve ser aplicado 1 vez, sendo necessário aplicar 0.85 kg de Adubo(NPK) por m², totlizando {dados_trigo["npk_fase1_trigo"]:.2f}kg de NPK")
                    print(f"O Inseticida è dividido em 2 aplicação, sendo uma aplicação para cada fase")
                    print(f"Na 1° Aplicação do Inseticida são necessários 2.75 L/m², totalizando {dados_trigo["inseticida_aplicacao1_trigo"]:.2f}L")
                    print(f"O Fungicida è dividido em 2 aplicação, sendo uma aplicação para cada fase")
                    print(f"Na 1° Aplicação do fungiciada são necessários 2.50 L/m², totalizando {dados_trigo["fungicida_aplicacao1_trigo"]:.2f}L")
                    print(f"São necessários 8.75 L de água /m², totalizando:  \n {dados_trigo["ir_fase1_diária_total_trigo"]:.2f} L de água diário \n {dados_trigo["ir_fase1_semanal_total_trigo"]:.2f} L de água semanal \n {dados_trigo["ir_fase1_mes_total_trigo"]:.2f} L de água mensal \n {dados_trigo["ir_fase1_total_trigo"]:.2f} L de água duarante  a fase 1 ( 2 meses)")
                    #---------- Fase2----------  
                    dados_trigo["npk_fase2_trigo"] = adubo_NPK(dados_trigo["area_total_trigo"])
                    dados_trigo["inseticida_aplicacao2_trigo"] = inseticida2(dados_trigo["area_total_trigo"])
                    dados_trigo["fungicida_aplicacao2_trigo"] = fungicida2(dados_trigo["area_total_trigo"])
                    dados_trigo["ir_fase2_diária_total_trigo"] = irrigação2_diaria_total_trigo(dados_trigo["area_total_trigo"])
                    dados_trigo["ir_fase2_semanal_total_trigo"] = dados_trigo["ir_fase2_diária_total_trigo"] * 7
                    dados_trigo["ir_fase2_mes_total_trigo"] = dados_trigo["ir_fase2_semanal_total_trigo"] * 4
                    dados_trigo["ir_fase2_total_trigo"] = dados_trigo["ir_fase2_mes_total_trigo"] * 2 # fase 2 duara 2 meses  
                    dados_trigo["ir_Ciclo_Completo_trigo"] = dados_trigo["ir_fase2_total_trigo"] +  dados_trigo["ir_fase1_total_trigo"]
                    #Prints Informações Básicas + Insumos----------------------------------------------------------------------------------------------------------------------------------
                    print("-----------Insumos 2°Fase----------")
                    print(f"O Adubo deve ser aplicado 1 vez, sendo necessário aplicar 0.85 kg de Adubo(NPK) por m², totlizando { dados_trigo["npk_fase2_trigo"]:.2f}kg de NPK")
                    print(f"Na 2° Aplicação do Inseticida são necessários 1.50 L/m², totalizando { dados_trigo["inseticida_aplicacao2_trigo"]:.2f}L")
                    print(f"Na 2° Aplicação do fungiciada são necessários 1.75 L/m², totalizando {dados_trigo["fungicida_aplicacao2_trigo"]:.2f}L")
                    print(f"São necessários 7.25 L de água /m², totalizando:  \n {dados_trigo["ir_fase2_diária_total_trigo"]} L de água diário \n {dados_trigo["ir_fase2_semanal_total_trigo"]:.2f} L de água semanal \n {dados_trigo["ir_fase2_mes_total_trigo"]:.2f} L de água mensal \n {dados_trigo["ir_fase2_total_trigo"]:.2f} L de água duarante  a fase 2 ( 2 meses)")
                    print(f"Em um ciclo completo será utilizado { dados_trigo["ir_Ciclo_Completo_trigo"]:.2f} L de água")   
                    #---------- Médias (R) ----------
                    # Vetor com os dados da aplicações de inseticida:
                    inseticida_trigo = r.c(dados_trigo["inseticida_aplicacao1_trigo"], dados_trigo["inseticida_aplicacao2_trigo"])
                    # Calculando média, mediana e desvio padrão:
                    media_inseticida_trigo = r.mean(inseticida_trigo)
                    desvio_padrao_inseticida_trigo = r.sd(inseticida_trigo) 
                    print(f'A média de inseticida ultizada é de {media_inseticida_trigo[0]} L/m², com desvio padrão de {desvio_padrao_inseticida_trigo[0]:.2f} L/m²')
                    # Vetor com os dados da aplicações de fungicida:
                    fungicida_trigo = r.c(dados_trigo["fungicida_aplicacao1_trigo"], dados_trigo["fungicida_aplicacao2_trigo"])
                    # Calculando média, mediana e desvio padrão:
                    media_fungicida_trigo = r.mean(fungicida_trigo)
                    desvio_padrao_fungicida_trigo = r.sd(fungicida_trigo)
                    print(f'A média de fungicida utilizada é de {media_fungicida_trigo[0]} L/m², com desvio padrão de {desvio_padrao_fungicida_trigo[0]:.2f} L/m²')
                    # Vetor com os dados da irrigação por fase:
                    irrigacao_trigo = r.c(dados_trigo["ir_fase1_total_trigo"], dados_trigo["ir_fase2_total_trigo"])
                    # Calculando média, mediana e desvio padrão:
                    media_irrigacao_trigo = r.mean(irrigacao_trigo)
                    desvio_padrao_irrigacao_trigo = r.sd(irrigacao_trigo)
                    print(f'A média de água utilizada é de {media_irrigacao_trigo[0]:.2f} L, com desvio padrão de {desvio_padrao_irrigacao_trigo[0]:.2f} L')
                    #---------- Disvios (R) ----------
                elif op == 2:
                    #---------------------------------------------------------------------Cultura - Batata ---------------------------------------------------------------------
                     # a cultur de batata é dividida em duas fases cada uma com duaração de 2 meses
                    #----------Definir Funções Específicas----------
                    #---Irrigação1 (8.75L de água por m²)---
                    def irrigação1_diaria_total_batata(at:float) -> float:
                        return at * 8.75
                    #---Irrigação2 (6.75L de água por m²)---
                    def irrigação2_diaria_total_batata(at:float) -> float:
                        return at * 6.75
                    #---Número de hortaliças Total (3.5 kg por muda de batata)
                    def nhortalicas_total_batata (at:float) -> float:
                        return 3.5 * ((at/4) * 6)
                    
                    #----------Código Principal----------
                    #---------- Fase1----------
                    dados_batata = {}
                    print("Um cilco completo de Batata duara 120 dia, ou seja, 4 mêses")
                    print("A cultura da batata é divida em duas fases cada uma com duração de 2 meses ")
                    print("Aplantação posuirá ruas com espaçamente de 1 m entre as ruas e as mudas devem ser plantads com espaçamento de 1 m entr elas")
                    #criando varias para as funções apra que possam ser vetorizadas
                    dados_batata["area_total_batata"] = float(input("Área disponível para plantação em m²: "))
                    # Calculando e armazenando os resultados no dicionário
                    # Informações Básicas----------------------------------------------------------------------------------------
                    dados_batata["area_util_batata"] = area_util(dados_batata["area_total_batata"])  
                    dados_batata["numero_mudas_total_batata"] = num_mudas_total(dados_batata["area_total_batata"],6 )  # 6 mudas por m²
                    dados_batata["numero_hortalicas_total_batata"] = nhortalicas_total_batata(dados_batata["area_total_batata"])
                    dados_batata["num_ruas_batata"] = numero_ruas_total(dados_batata["area_total_batata"])
                    # Insumos--------------------------------------------------------------------------------------------------------
                    dados_batata["calcio_total_batata"] = calcio_total(dados_batata["area_total_batata"])
                    dados_batata["npk_fase1_batata"] = adubo_NPK(dados_batata["area_total_batata"])
                    dados_batata["inseticida_aplicacao1_batata"] = inseticida1(dados_batata["area_total_batata"])
                    dados_batata["fungicida_aplicacao1_batata"] = fungicida1(dados_batata["area_total_batata"])
                    dados_batata["ir_fase1_diária_total_batata"] = irrigação1_diaria_total_batata(dados_batata["area_total_batata"])
                    dados_batata["ir_fase1_semanal_total_batata"] = dados_batata["ir_fase1_diária_total_batata"] * 7
                    dados_batata["ir_fase1_mes_total_batata"] = dados_batata["ir_fase1_semanal_total_batata"] * 4
                    dados_batata["ir_fase1_total_batata"] = dados_batata["ir_fase1_mes_total_batata"] * 2 # fase 1 duara 2 meses
                   #Prints Informações Básicas + Insumos----------------------------------------------------------------------------------------------------------------------------------
                    print("----------Informações Básicas----------")
                    print(f"A área util é de: {dados_batata["area_util_batata"]:.2f} m²")
                    print(f"O número total de mudas a serem plantadas é de {dados_batata["numero_mudas_total_batata"]:.1f} mudas")
                    print(f"A plantação terá {dados_batata["num_ruas_batata"]:.1f} ruas")
                    print(f"O a quantidade de batadas obitidas após um ciclo completo é de {dados_batata["numero_hortalicas_total_batata"]:.2f}kg")
                    print("-----------Insumos 1°Fase----------")
                    print(f"O calcio deve ser aplicado 1 vez, sendo necessário aplicar 0.7 toneladas de cálcio por hectare, totalizando {dados_batata["calcio_total_batata"]:.2f} toneladas de cálcio")
                    print(f"O Adubo deve ser aplicado 1 vez, sendo necessário aplicar 0.85 kg de Adubo(NPK) por m², totlizando {dados_batata["npk_fase1_batata"]:.2f}kg de NPK")
                    print(f"O Inseticida è dividido em 2 aplicação, sendo uma aplicação para cada fase")
                    print(f"Na 1° Aplicação do Inseticida são necessários 2.75 L/m², totalizando {dados_batata["inseticida_aplicacao1_batata"]:.2f}L")
                    print(f"O Fungicida è dividido em 2 aplicação, sendo uma aplicação para cada fase")
                    print(f"Na 1° Aplicação do fungiciada são necessários 2.50 L/m², totalizando { dados_batata["fungicida_aplicacao1_batata"]:.2f}L")
                    print(f"São necessários 6.75 L de água /m², totalizando:  \n {dados_batata["ir_fase1_diária_total_batata"]:.2f} L de água diário \n {dados_batata["ir_fase1_semanal_total_batata"]:.2f} L de água semanal \n {dados_batata["ir_fase1_mes_total_batatata"]:.2f} L de água mensal \n {dados_batata["ir_fase1_total_batata"]:.2f} L de água duarante  a fase 1 ( 2 meses)")
                    #---------- Fase2----------  
                    dados_batata["npk_fase2_batata"] = adubo_NPK(dados_batata["area_total_batata"])
                    dados_batata["inseticida_aplicacao2_batata"] = inseticida2(dados_batata["area_total_batata"])
                    dados_batata["fungicida_aplicacao2_batata"] = fungicida2(dados_batata["area_total_batata"])
                    dados_batata["ir_fase2_diária_total_batata"] = irrigação2_diaria_total_batata(dados_batata["area_total_batata"])
                    dados_batata["ir_fase2_semanal_total_batata"] = dados_batata["ir_fase2_diária_total_batata"] * 7
                    dados_batata["ir_fase2_mes_total_batata"] = dados_batata["ir_fase2_semanal_total_batata"] * 4
                    dados_batata["ir_fase2_total_batata"] = dados_batata["ir_fase2_mes_total_batata"] * 2 # fase 2 duara 2 meses  
                    dados_batata["ir_Ciclo_Completo_batata"] = dados_batata["ir_fase2_total_batata"] +  dados_batata["ir_fase1_total_batata"]
                    #Prints Informações Básicas + Insumos----------------------------------------------------------------------------------------------------------------------------------
                    print("-----------Insumos 2°Fase----------")
                    print(f"O Adubo deve ser aplicado 1 vez, sendo necessário aplicar 0.85 kg de Adubo(NPK) por m², totlizando {dados_batata["npk_fase2_batata"]:.2f}kg de NPK")
                    print(f"Na 2° Aplicação do Inseticida são necessários 1.50 L/m², totalizando {dados_batata["inseticida_aplicacao2_batata"]:.2f}L")
                    print(f"Na 2° Aplicação do fungiciada são necessários 1.75 L/m², totalizando {dados_batata["fungicida_aplicacao2_batata"]:.2f}L")
                    print(f"São necessários 7.25 L de água /m², totalizando: \n { dados_batata["ir_fase2_diária_total_batata"]:.2f} L de água diário \n {dados_batata["ir_fase2_semanal_total_batata"]:.2f} L de água semanal \n {dados_batata["ir_fase2_mes_total_batata"]:.2f} L de água mensal \n {dados_batata["ir_fase2_total_batata"]:.2f} L de água duarante  a fase 2 ( 2 meses)")
                    print(f"Em um ciclo completo será utilizado { dados_batata["ir_Ciclo_Completo_batata"]:.2f} L de água")   
                    #---------- Médias (R) ----------
                    # Vetor com os dados da aplicações de inseticida:
                    inseticida_batata = r.c(dados_batata["inseticida_aplicacao1_batata"], dados_batata["inseticida_aplicacao2_batata"])
                    # Calculando média, mediana e desvio padrão:
                    media_inseticida_batata = r.mean(inseticida_batata)
                    desvio_padrao_inseticida_batata = r.sd(inseticida_batata) 
                    print(f'A média de inseticida ultizada é de {media_inseticida_batata[0]} L/m², com desvio padrão de {desvio_padrao_inseticida_batata[0]:.2f} L/m²')
                    # Vetor com os dados da aplicações de fungicida:
                    fungicida_batata = r.c(dados_batata["fungicida_aplicacao1_batata"], dados_batata["fungicida_aplicacao2_batata"])
                    # Calculando média, mediana e desvio padrão:
                    media_fungicida_batata = r.mean(fungicida_batata)
                    desvio_padrao_fungicida_batata = r.sd(fungicida_batata)
                    print(f'A média de fungicida utilizada é de {media_fungicida_batata[0]} L/m², com desvio padrão de {desvio_padrao_fungicida_batata[0]:.2f} L/m²')
                    # Vetor com os dados da irrigação por fase:
                    irrigacao_batata = r.c(dados_batata["ir_fase1_total_batata"], dados_batata["ir_fase2_total_batata"])
                    # Calculando média, mediana e desvio padrão:
                    media_irrigacao_batata = r.mean(irrigacao_batata)
                    desvio_padrao_irrigacao_batata = r.sd(irrigacao_batata)
                    print(f'A média de água utilizada é de {media_irrigacao_batata[0]:.2f} L, com desvio padrão de {desvio_padrao_irrigacao_batata[0]:.2f} L')
                elif op == 3:
                    #---------------------------------------------------------------------Cultura - Maça---------------------------------------------------------------------
                     # a cultur de maça é dividida em duas fases cada uma com duaração de 4 meses
                    #----------Definir Funções Específicas----------
                    #---Irrigação1 (9.00L de água por m²)---
                    def irrigação1_diaria_total_maça(at:float) -> float:
                        return at * 9.00
                    #---Irrigação2 (7.00L de água por m²)---
                    def irrigação2_diaria_total_maça(at:float) -> float:
                        return at * 7.00
                    #---Número de hortaliças Total (4 kg por muda de maça)
                    def nhortalicas_total_maça (at:float) -> float:
                        return 4 * ((at/4) * 2)
                    #----------Código Principal----------
                    #---------- Fase1----------
                    dados_maça = {}
                    print("Um cilco completo de maça duara 240 dia, ou seja, 8 mêses")
                    print("A cultura da maça é divida em duas fases cada uma com duração de 4 meses ")
                    print("Aplantação posuirá ruas com espaçamente de 1 m entre as ruas e as mudas devem ser plantads com espaçamento de 1 m entr elas")
                    #criando varias para as funções apra que possam ser vetorizadas
                    dados_maça["area_total_maça"] = float(input("Área disponível para plantação em m²: "))
                    # Calculando e armazenando os resultados no dicionário
                    # Informações Básicas----------------------------------------------------------------------------------------
                    dados_maça["area_util_maça"] = area_util(dados_maça["area_total_maça"])  
                    dados_maça["numero_mudas_total_maça"] = num_mudas_total(dados_maça["area_total_maça"],2 )  # 2 mudas por m²
                    dados_maça["num_ruas_maça"] = numero_ruas_total(dados_maça["area_total_maça"])
                    dados_maça["numero_hortalicas_total_maça"] = nhortalicas_total_maça(dados_maça["area_total_maça"])
                    # Insumos--------------------------------------------------------------------------------------------------------
                    dados_maça["calcio_fase1_total_maça"] = calcio_total(dados_maça["area_total_maça"])
                    dados_maça["npk_fase1_maça"] = adubo_NPK(dados_maça["area_total_maça"])
                    dados_maça["inseticida_aplicacao1_maça"] = inseticida1(dados_maça["area_total_maça"])
                    dados_maça["fungicida_aplicacao1_maça"] = fungicida1(dados_maça["area_total_maça"])
                    dados_maça["ir_fase1_diária_total_maça"] = irrigação1_diaria_total_maça(dados_maça["area_total_maça"])
                    dados_maça["ir_fase1_semanal_total_maça"] = dados_maça["ir_fase1_diária_total_maça"] * 7
                    dados_maça["ir_fase1_mes_total_maça"] = dados_maça["ir_fase1_semanal_total_maça"] * 4
                    dados_maça["ir_fase1_total_maça"] = dados_maça["ir_fase1_mes_total_maça"] * 4 # fase 1 duara 4 meses
                   #Prints Informações Básicas + Insumos----------------------------------------------------------------------------------------------------------------------------------
                    print("----------Informações Básicas----------")
                    print(f"A área util é de: {dados_maça["area_util_maça"]:.2f} m²")
                    print(f"O número total de mudas a serem plantadas é de {dados_maça["numero_mudas_total_maça"]:.1f} mudas")
                    print(f"A plantação terá {dados_maça["num_ruas_maça"]:.1f} ruas")
                    print(f"O a quantidade de batadas obitidas após um ciclo completo é de {dados_maça["numero_hortalicas_total_maça"]:.2f}kg")
                    print("-----------Insumos 1°Fase----------")
                    print(f"O calcio deve ser aplicado 1 vez, sendo necessário aplicar 0.7 toneladas de cálcio por hectare, totalizando { dados_maça["calcio_fase1_total_maça"]:.2f} toneladas de cálcio")
                    print(f"O Adubo deve ser aplicado 1 vez, sendo necessário aplicar 0.85 kg de Adubo(NPK) por m², totlizando {dados_maça["npk_fase1_maça"]:.2f}kg de NPK")
                    print(f"O Inseticida è dividido em 2 aplicação, sendo uma aplicação para cada fase")
                    print(f"Na 1° Aplicação do Inseticida são necessários 2.75 L/m², totalizando {dados_maça["inseticida_aplicacao1_maça"]:.2f}L")
                    print(f"O Fungicida è dividido em 2 aplicação, sendo uma aplicação para cada fase")
                    print(f"Na 1° Aplicação do fungiciada são necessários 2.50 L/m², totalizando {dados_maça["fungicida_aplicacao1_maça"] :.2f}L")
                    print(f"São necessários 9.00 L de água /m², totalizando: \n {dados_maça["ir_fase1_diária_total_maça"]:.2f} L de água diário \n {dados_maça["ir_fase1_semanal_total_maça"]:.2f} L de água semanal \n {dados_maça["ir_fase1_mes_total_maça"] :.2f} L de água mensal \n {dados_maça["ir_fase1_total_maça"]:.2f} L de água duarante  a fase 1 ( 4 meses)")
                    #---------- Fase2----------  
                    dados_maça["calcio_fase2_total_maça"] = calcio_total(dados_maça["area_total_maça"])
                    dados_maça["npk_fase2_maça"] = adubo_NPK(dados_maça["area_total_maça"])
                    dados_maça["inseticida_aplicacao2_maça"] = inseticida2(dados_maça["area_total_maça"])
                    dados_maça["fungicida_aplicacao2_maça"] = fungicida2(dados_maça["area_total_maça"])
                    dados_maça["ir_fase2_diária_total_maça"] = irrigação2_diaria_total_maça(dados_maça["area_total_maça"])
                    dados_maça["ir_fase2_semanal_total_maça"] = dados_maça["ir_fase2_diária_total_maça"] * 7
                    dados_maça["ir_fase2_mes_total_maça"] = dados_maça["ir_fase2_semanal_total_maça"] * 4
                    dados_maça["ir_fase2_total_maça"] = dados_maça["ir_fase2_mes_total_maça"] * 4 # fase 2 duara 4 meses  
                    dados_maça["ir_Ciclo_Completo_maça"] = dados_maça["ir_fase2_total_maça"] +  dados_maça["ir_fase1_total_maça"]
                    #Prints Informações Básicas + Insumos----------------------------------------------------------------------------------------------------------------------------------
                    print("-----------Insumos 2°Fase----------")
                    print(f"O calcio deve ser aplicado 1 vez, sendo necessário aplicar 0.7 toneladas de cálcio por hectare, totalizando { dados_maça["calcio_fase2_total_maça"]:.2f} toneladas de cálcio")
                    print(f"O Adubo deve ser aplicado 1 vez, sendo necessário aplicar 0.85 kg de Adubo(NPK) por m², totlizando {dados_maça["npk_fase2_maça"]:.2f}kg de NPK")
                    print(f"Na 2° Aplicação do Inseticida são necessários 1.50 L/m², totalizando {dados_maça["inseticida_aplicacao2_maça"]:.2f}L")
                    print(f"Na 2° Aplicação do fungiciada são necessários 1.75 L/m², totalizando { dados_maça["fungicida_aplicacao2_maça"]:.2f}L")
                    print(f"São necessários 7.00 L de água /m², totalizando: \n {dados_maça["ir_fase2_diária_total_maça"]:.2f} L de água diário \n {dados_maça["ir_fase2_semanal_total_maça"]:.2f} L de água semanal \n {dados_maça["ir_fase2_mes_total_maça"]:.2f} L de água mensal \n {dados_maça["ir_fase2_total_maça"]:.2f} L de água duarante  a fase 2 ( 4 meses)")
                    print(f"Em um ciclo completo será utilizado {dados_maça["ir_Ciclo_Completo_maça"]:.2f} L de água")   
                    #---------- Médias (R) -----------
                    # Vetor com os dados da aplicações de inseticida:
                    inseticida_maça = r.c(dados_maça["inseticida_aplicacao1_maça"], dados_maça["inseticida_aplicacao2_maça"])
                    # Calculando média, mediana e desvio padrão:
                    media_inseticida_maça = r.mean(inseticida_maça)
                    desvio_padrao_inseticida_maça = r.sd(inseticida_maça) 
                    print(f'A média de inseticida ultizada é de {media_inseticida_maça[0]} L/m², com desvio padrão de {desvio_padrao_inseticida_maça[0]:.2f} L/m²')
                    # Vetor com os dados da aplicações de fungicida:
                    fungicida_maça = r.c(dados_maça["fungicida_aplicacao1_maça"], dados_maça["fungicida_aplicacao2_maça"])
                    # Calculando média, mediana e desvio padrão:
                    media_fungicida_maça = r.mean(fungicida_maça)
                    desvio_padrao_fungicida_maça = r.sd(fungicida_maça)
                    print(f'A média de fungicida utilizada é de {media_fungicida_maça[0]} L/m², com desvio padrão de {desvio_padrao_fungicida_maça[0]:.2f} L/m²')
                    # Vetor com os dados da irrigação por fase:
                    irrigacao_maça = r.c(dados_maça["ir_fase1_total_maça"], dados_maça["ir_fase2_total_maça"])
                    # Calculando média, mediana e desvio padrão:
                    media_irrigacao_maça = r.mean(irrigacao_maça)
                    desvio_padrao_irrigacao_maça = r.sd(irrigacao_maça)
                    print(f'A média de água utilizada é de {media_irrigacao_maça[0]:.2f} L, com desvio padrão de {desvio_padrao_irrigacao_maça[0]:.2f} L')  
                elif op == 4:
                    print("voltando ao menu das regiões")
                    break  
                else:
                    print("Opção invalida, tente novamnete")
            elif op == 2:
               #----- Região Suldeste -----
                while True:
                    print("------Culturas------")
                    print(" 1. Arroz (grão) \n 2. Alface (hortaliça) \n 3. Banana (fruta) \n 4 Voltar") 
                    op = int(input("Digite o número referente a opção que deseja plantar: "))    
                    if op == 1:
                        #---------------------------------------------------------------------Cultura - Arroz---------------------------------------------------------------------
                        # a cultur de arroz é dividida em duas fases cada uma com duaração de 2 meses
                        #----------Definir Funções Específicas----------
                        #---Irrigação1 (9.50L de água por m²)---
                        def irrigação1_diaria_total_arroz(at:float) -> float:
                            return at * 9.50
                        #---Irrigação2 (7.00L de água por m²)---
                        def irrigação2_diaria_total_arroz(at:float) -> float:
                            return at * 7.00
                        #---Número de Grãos Total (3.5 kg por muda de arroz)
                        def ngraos_total_arroz (at:float) -> float:
                            return 3.5 * ((at/4) * 6)
                        #----------Código Principal----------
                        #---------- Fase1----------
                        dados_arroz = {}
                        print("Um cilco completo do arroz duara 120 dias, ou seja, 4 mêses")
                        print("A cultura do arroz é divida em duas fases cada uma com duração de 2 meses")
                        print("Aplantação posuirá ruas com espaçamente de 1 m entre as ruas e as mudas devem ser plantads com espaçamento de 1 m entr elas")
                        #criando varias para as funções apra que possam ser vetorizadas
                        dados_arroz["area_total_arroz"] = float(input("Área disponível para plantação em m²: "))
                        # Calculando e armazenando os resultados no dicionário
                        # Informações Básicas----------------------------------------------------------------------------------------
                        dados_arroz["area_util_arroz"] = area_util(dados_arroz["area_total_arroz"])  
                        dados_arroz["numero_mudas_total_arroz"] = num_mudas_total(dados_arroz["area_total_arroz"], 6) # 6 mudas por m²
                        dados_arroz["numero_graos_total_arroz"] = ngraos_total_arroz(dados_arroz["area_total_arroz"]) 
                        dados_arroz["num_ruas_arroz"] = numero_ruas_total(dados_arroz["area_total_arroz"])
                        # Insumos--------------------------------------------------------------------------------------------------------
                        dados_arroz["calcio_total_arrozo"] = calcio_total(dados_arroz["area_total_arroz"])
                        dados_arroz["npk_fase1_arroz"] = adubo_NPK(dados_arroz["area_total_arroz"])
                        dados_arroz["inseticida_aplicacao1_arroz"] = inseticida1(dados_arroz["area_total_arroz"])
                        dados_arroz["fungicida_aplicacao1_arroz"] = fungicida1(dados_arroz["area_total_arroz"])
                        dados_arroz["ir_fase1_diária_total_arroz"] = irrigação1_diaria_total_arroz(dados_arroz["area_total_arroz"])
                        dados_arroz["ir_fase1_semanal_total_arroz"] = dados_arroz["ir_fase1_diária_total_arroz"] * 7
                        dados_arroz["ir_fase1_mes_total_arroz"] = dados_arroz["ir_fase1_semanal_total_arroz"] * 4
                        dados_arroz["ir_fase1_total_arroz"] = dados_arroz["ir_fase1_mes_total_arroz"] * 2 # fase 1 duara 2 meses
                        #Prints Informações Básicas + Insumos----------------------------------------------------------------------------------------------------------------------------------
                        print("----------Informações Básicas----------")
                        print(f"A área util é de: {dados_arroz["area_util_arroz"]:.2f} m²")
                        print(f"O número total de mudas a serem plantadas é de {dados_arroz["numero_mudas_total_arroz"] :.1f} mudas")
                        print(f"A plantação terá {dados_arroz["num_ruas_arroz"]:.1f} ruas")
                        print(f"O a quantidade de grãos de arroz obitidas após um ciclo completo é de {dados_arroz["numero_graos_total_arroz"]:.2f}kg")
                        print("-----------Insumos 1°Fase----------")
                        print(f"O calcio deve ser aplicado 1 vez, sendo necessário aplicar 0.7 toneladas de cálcio por hectare, totalizando {dados_arroz['calcio_total_arrozo']:.2f} toneladas de cálcio")
                        print(f"O Adubo deve ser aplicado 1 vez, sendo necessário aplicar 0.85 kg de Adubo(NPK) por m², totlizando {dados_arroz["npk_fase1_arroz"]:.2f}kg de NPK")
                        print(f"O Inseticida è dividido em 2 aplicação, sendo uma aplicação para cada fase")
                        print(f"Na 1° Aplicação do Inseticida são necessários 2.75 L/m², totalizando {dados_arroz["inseticida_aplicacao1_arroz"]:.2f}L")
                        print(f"O Fungicida è dividido em 2 aplicação, sendo uma aplicação para cada fase")
                        print(f"Na 1° Aplicação do fungiciada são necessários 2.50 L/m², totalizando {dados_arroz["fungicida_aplicacao1_arroz"]:.2f}L")
                        print(f"São necessários 9.50 L de água /m², totalizando:  \n {dados_arroz["ir_fase1_diária_total_arroz"]:.2f} L de água diário \n {dados_arroz["ir_fase1_semanal_total_arroz"]:.2f} L de água semanal \n {dados_arroz["ir_fase1_mes_total_arroz"]:.2f} L de água mensal \n {dados_arroz["ir_fase1_total_arroz"]:.2f} L de água duarante  a fase 1 ( 2 meses)")
                        #---------- Fase2----------  
                        dados_arroz["npk_fase2_arroz"] = adubo_NPK(dados_arroz["area_total_arroz"])
                        dados_arroz["inseticida_aplicacao2_arroz"] = inseticida2(dados_arroz["area_total_arroz"])
                        dados_arroz["fungicida_aplicacao2_arroz"] = fungicida2(dados_arroz["area_total_arroz"])
                        dados_arroz["ir_fase2_diária_total_arroz"] = irrigação2_diaria_total_arroz(dados_arroz["area_total_arroz"])
                        dados_arroz["ir_fase2_semanal_total_arroz"] = dados_arroz["ir_fase2_diária_total_arroz"] * 7
                        dados_arroz["ir_fase2_mes_total_arroz"] = dados_arroz["ir_fase2_semanal_total_arroz"] * 4
                        dados_arroz["ir_fase2_total_arroz"] = dados_arroz["ir_fase2_mes_total_arroz"] * 2 # fase 2 duara 2 meses  
                        dados_arroz["ir_Ciclo_Completo_arroz"] = dados_arroz["ir_fase2_total_arroz"] +  dados_arroz["ir_fase1_total_arroz"]
                        #Prints Informações Básicas + Insumos----------------------------------------------------------------------------------------------------------------------------------
                        print("-----------Insumos 2°Fase----------")
                        print(f"O Adubo deve ser aplicado 1 vez, sendo necessário aplicar 0.85 kg de Adubo(NPK) por m², totlizando {dados_arroz['npk_fase2_arroz']:.2f}kg de NPK")
                        print(f"Na 2° Aplicação do Inseticida são necessários 1.50 L/m², totalizando {dados_arroz["inseticida_aplicacao2_arroz"]:.2f}L")
                        print(f"Na 2° Aplicação do fungiciada são necessários 1.75 L/m², totalizando {dados_arroz["fungicida_aplicacao2_arroz"]:.2f}L")
                        print(f"São necessários 7.25 L de água /m², totalizando: \n {dados_arroz["ir_fase2_diária_total_arroz"]:.2f} L de água diário \n {dados_arroz["ir_fase2_semanal_total_arroz"]:.2f} L de água semanal \n {dados_arroz["ir_fase2_mes_total_arroz"]:.2f} L de água mensal \n {dados_arroz["ir_fase2_total_arroz"]:.2f} L de água duarante  a fase 2 ( 2 meses)")
                        print(f"Em um ciclo completo será utilizado {dados_arroz["ir_Ciclo_Completo_arroz"]:.2f} L de água")   
                        #---------- Médias (R) -----------
                        # Vetor com os dados da aplicações de inseticida:
                        inseticida_arroz = r.c(dados_arroz["inseticida_aplicacao1_arroz"], dados_arroz["inseticida_aplicacao2_arroz"])
                        # Calculando média, mediana e desvio padrão:
                        media_inseticida_arroz = r.mean(inseticida_arroz)
                        desvio_padrao_inseticida_arroz = r.sd(inseticida_arroz) 
                        print(f'A média de inseticida ultizada é de {media_inseticida_arroz[0]} L/m², com desvio padrão de {desvio_padrao_inseticida_arroz[0]:.2f} L/m²')
                        # Vetor com os dados da aplicações de fungicida:
                        fungicida_arroz = r.c(dados_arroz["fungicida_aplicacao1_arroz"], dados_arroz["fungicida_aplicacao2_arroz"])
                        # Calculando média, mediana e desvio padrão:
                        media_fungicida_arroz = r.mean(fungicida_arroz)
                        desvio_padrao_fungicida_arroz = r.sd(fungicida_arroz)
                        print(f'A média de fungicida utilizada é de {media_fungicida_arroz[0]} L/m², com desvio padrão de {desvio_padrao_fungicida_arroz[0]:.2f} L/m²')
                        # Vetor com os dados da irrigação por fase:
                        irrigacao_arroz = r.c(dados_arroz["ir_fase1_total_arroz"], dados_arroz["ir_fase2_total_arroz"])
                        # Calculando média, mediana e desvio padrão:
                        media_irrigacao_arroz = r.mean(irrigacao_arroz)
                        desvio_padrao_irrigacao_arroz = r.sd(irrigacao_arroz)
                        print(f'A média de água utilizada é de {media_irrigacao_arroz[0]:.2f} L, com desvio padrão de {desvio_padrao_irrigacao_arroz[0]:.2f} L')
                        #---------- Disvios (R) ----------
                    elif op == 2:
                        #---------------------------------------------------------------------Cultura - Alface---------------------------------------------------------------------
                        # a cultur de alface dividida em duas fases cada uma com duaração de 2 meses
                        #----------Definir Funções Específicas----------
                        #---Irrigação1 (8.50L de água por m²)---
                        def irrigação1_diaria_total_alface(at:float) -> float:
                            return at * 8.50
                        #---Irrigação2 (7.50L de água por m²)---
                        def irrigação2_diaria_total_alface(at:float) -> float:
                            return at * 7.50
                        #---Número de Afaces Total (3 kg por muda de alface)
                        def ngraos_total_alface (at:float) -> float:
                            return 1 * ((at/4) * 6)
                        #----------Código Principal----------
                        #---------- Fase1----------
                        dados_alface = {}
                        print("Um cilco completo do alface duara 60 dias, ou seja, 2 mêses")
                        print("A cultura da alface é divida em duas fases cada uma com duração de 1 meses")
                        print("Aplantação posuirá ruas com espaçamente de 1 m entre as ruas e as mudas devem ser plantads com espaçamento de 1 m entr elas")
                        #criando varias para as funções apra que possam ser vetorizadas
                        dados_alface["area_total_alface"] = float(input("Área disponível para plantação em m²: "))
                        # Calculando e armazenando os resultados no dicionário
                        # Informações Básicas----------------------------------------------------------------------------------------
                        dados_alface["area_util_alface"] = area_util(dados_alface["area_total_alface"])  
                        dados_alface["numero_mudas_total_alface"] = num_mudas_total(dados_alface["area_total_alface"], 6) # 6 mudas por m²
                        dados_alface["numero_graos_total_alface"] = ngraos_total_alface(dados_alface["area_total_alface"]) 
                        dados_alface["num_ruas_alface"] = numero_ruas_total(dados_alface["area_total_alface"])
                        # Insumos--------------------------------------------------------------------------------------------------------
                        dados_alface["calcio_total_alface"] = calcio_total(dados_alface["area_total_alface"])
                        dados_alface["npk_fase1_alface"] = adubo_NPK(dados_alface["area_total_alface"])
                        dados_alface["inseticida_aplicacao1_alface"] = inseticida1(dados_alface["area_total_alface"])
                        dados_alface["fungicida_aplicacao1_alface"] = fungicida1(dados_alface["area_total_alface"])
                        dados_alface["ir_fase1_diária_total_alface"] = irrigação1_diaria_total_alface(dados_alface["area_total_alface"])
                        dados_alface["ir_fase1_semanal_total_alface"] = dados_alface["ir_fase1_diária_total_alface"] * 7
                        dados_alface["ir_fase1_mes_total_alface"] = dados_alface["ir_fase1_semanal_total_alface"] * 4
                        dados_alface["ir_fase1_total_alface"] = dados_alface["ir_fase1_mes_total_alface"] * 1 # fase 1 duara 2 meses
                        #Prints Informações Básicas + Insumos----------------------------------------------------------------------------------------------------------------------------------
                        print("----------Informações Básicas----------")
                        print(f"A área util é de: {dados_alface["area_util_alface"]:.2f} m²")
                        print(f"O número total de mudas a serem plantadas é de {dados_alface["numero_mudas_total_alface"]:.1f} mudas")
                        print(f"A plantação terá {dados_alface["num_ruas_alface"]:.1f} ruas")
                        print(f"O a quantidade de alface obitidas após um ciclo completo é de {dados_alface["numero_graos_total_alface"]:.2f}kg")
                        print("-----------Insumos 1°Fase----------")
                        print(f"O calcio deve ser aplicado 1 vez, sendo necessário aplicar 0.7 toneladas de cálcio por hectare, totalizando {dados_alface["calcio_total_alface"]:.2f} toneladas de cálcio")
                        print(f"O Adubo deve ser aplicado 1 vez, sendo necessário aplicar 0.85 kg de Adubo(NPK) por m², totlizando {dados_alface["npk_fase1_alface"]:.2f}kg de NPK")
                        print(f"O Inseticida è dividido em 2 aplicação, sendo uma aplicação para cada fase")
                        print(f"Na 1° Aplicação do Inseticida são necessários 2.75 L/m², totalizando {dados_alface["inseticida_aplicacao1_alface"]:.2f}L")
                        print(f"O Fungicida è dividido em 2 aplicação, sendo uma aplicação para cada fase")
                        print(f"Na 1° Aplicação do fungiciada são necessários 2.50 L/m², totalizando {dados_alface["fungicida_aplicacao1_alface"]:.2f}L")
                        print(f"São necessários 8.50 L de água /m², totalizando: \n {dados_alface["ir_fase1_diária_total_alface"]:.2f} L de água diário \n {dados_alface["ir_fase1_semanal_total_alface"]:.2f} L de água semanal \n {dados_alface["ir_fase1_mes_total_alface"]:.2f} L de água mensal \n {dados_alface["ir_fase1_total_alface"]:.2f} L de água duarante  a fase 1(1 meses)")
                        #---------- Fase2----------  
                        dados_alface["npk_fase2_alface"] = adubo_NPK(dados_alface["area_total_alface"])
                        dados_alface["inseticida_aplicacao2_alface"] = inseticida2(dados_alface["area_total_alface"])
                        dados_alface["fungicida_aplicacao2_alface"] = fungicida2(dados_alface["area_total_alface"])
                        dados_alface["ir_fase2_diária_total_alface"] = irrigação2_diaria_total_alface(dados_alface["area_total_alface"])
                        dados_alface["ir_fase2_semanal_total_alface"] = dados_alface["ir_fase2_diária_total_alface"] * 7
                        dados_alface["ir_fase2_mes_total_alface"] = dados_alface["ir_fase2_semanal_total_alface"] * 4
                        dados_alface["ir_fase2_total_alface"] = dados_alface["ir_fase2_mes_total_alface"] * 1 # fase 2 duara  meses  
                        dados_alface["ir_Ciclo_Completo_alface"] = dados_alface["ir_fase2_total_alface"] + dados_alface["ir_fase1_total_alface"]
                        #Prints Informações Básicas + Insumos----------------------------------------------------------------------------------------------------------------------------------
                        print("-----------Insumos 2°Fase----------")
                        print(f"O Adubo deve ser aplicado 1 vez, sendo necessário aplicar 0.85 kg de Adubo(NPK) por m², totlizando {dados_alface["inseticida_aplicacao2_alface"]:.2f}kg de NPK")
                        print(f"Na 2° Aplicação do Inseticida são necessários 1.50 L/m², totalizando {dados_alface["inseticida_aplicacao2_alface"]:.2f}L")
                        print(f"Na 2° Aplicação do fungiciada são necessários 1.75 L/m², totalizando {dados_alface["fungicida_aplicacao2_alface"]:.2f}L")
                        print(f"São necessários 7.50 L de água /m², totalizando: \n {dados_alface["ir_fase2_diária_total_alface"]:.2f} L de água diário \n {dados_alface["ir_fase2_semanal_total_alface"]:.2f} L de água semanal \n {dados_alface["ir_fase2_mes_total_alface"]:.2f} L de água mensal \n {dados_alface["ir_fase2_total_alface"]:.2f} L de água duarante  a fase 2 ( 1 meses)")
                        print(f"Em um ciclo completo será utilizado {dados_alface["ir_Ciclo_Completo_alface"]:.2f} L de água")  
                        #---------- Médias (R) -----------
                        # Vetor com os dados da aplicações de inseticida:
                        inseticida_alface = r.c(dados_alface["inseticida_aplicacao1_alface"], dados_alface["inseticida_aplicacao2_alface"])
                        # Calculando média, mediana e desvio padrão:
                        media_inseticida_alface = r.mean(inseticida_alface)
                        desvio_padrao_inseticida_alface = r.sd(inseticida_alface) 
                        print(f'A média de inseticida ultizada é de {media_inseticida_alface[0]} L/m², com desvio padrão de {desvio_padrao_inseticida_alface[0]:.2f} L/m²')
                        # Vetor com os dados da aplicações de fungicida:
                        fungicida_alface = r.c(dados_alface["fungicida_aplicacao1_alface"], dados_alface["fungicida_aplicacao2_alface"])
                        # Calculando média, mediana e desvio padrão:
                        media_fungicida_alface = r.mean(fungicida_alface)
                        desvio_padrao_fungicida_alface = r.sd(fungicida_alface)
                        print(f'A média de fungicida utilizada é de {media_fungicida_alface[0]} L/m², com desvio padrão de {desvio_padrao_fungicida_alface[0]:.2f} L/m²')
                        # Vetor com os dados da irrigação por fase:
                        irrigacao_alface = r.c(dados_alface["ir_fase1_total_alface"], dados_alface["ir_fase2_total_alface"])
                        # Calculando média, mediana e desvio padrão:
                        media_irrigacao_alface = r.mean(irrigacao_alface)
                        desvio_padrao_irrigacao_alface = r.sd(irrigacao_alface)
                        print(f'A média de água utilizada é de {media_irrigacao_alface[0]:.2f} L, com desvio padrão de {desvio_padrao_irrigacao_alface[0]:.2f} L')
                    elif op == 3: 
                        #---------------------------------------------------------------------Cultura - Banana---------------------------------------------------------------------
                        # a cultur de banana dividida em duas fases cada uma com duaração de 3 meses
                        #----------Definir Funções Específicas----------
                        #---Irrigação1 (8.50L de água por m²)---
                        def irrigação1_diaria_total_banana(at:float) -> float:
                            return at * 8.50
                        #---Irrigação2 (7.50L de água por m²)---
                        def irrigação2_diaria_total_banana(at:float) -> float:
                            return at * 7.50
                        #---Número de Afaces Total (3 kg por muda de banana)
                        def ngraos_total_banana (at:float) -> float:
                            return 4 * ((at/4) * 2)
                        #----------Código Principal----------
                        #---------- Fase1----------
                        dados_banana = {}
                        print("Um cilco completo do banana duara 180 dias, ou seja, 6 mêses")
                        print("A cultura da banana é divida em duas fases cada uma com duração de 3 meses")
                        print("Aplantação posuirá ruas com espaçamente de 1 m entre as ruas e as mudas devem ser plantads com espaçamento de 1 m entr elas")
                        #criando varias para as funções apra que possam ser vetorizadas
                        dados_banana["area_total_banana"] = float(input("Área disponível para plantação em m²: "))
                        # Calculando e armazenando os resultados no dicionário
                        # Informações Básicas----------------------------------------------------------------------------------------
                        dados_banana["area_util_banana"] = area_util(dados_banana["area_total_banana"])  
                        dados_banana["numero_mudas_total_banana"] = num_mudas_total(dados_banana["area_total_banana"], 2) # 2 mudas por m²
                        dados_banana["numero_graos_total_banana"] = ngraos_total_banana(dados_banana["area_total_banana"]) 
                        dados_banana["num_ruas_banana"] = numero_ruas_total(dados_banana["area_total_banana"])
                        # Insumos--------------------------------------------------------------------------------------------------------
                        dados_banana["calcio_total_banana"] = calcio_total(dados_banana["area_total_banana"])
                        dados_banana["npk_fase1_banana"] = adubo_NPK(dados_banana["area_total_banana"])
                        dados_banana["fungicida_aplicacao1_banana"] = inseticida1(dados_banana["area_total_banana"])
                        dados_banana["fungicida_aplicacao1_banana"] = fungicida1(dados_banana["area_total_banana"])
                        dados_banana["ir_fase1_diária_total_banana"] = irrigação1_diaria_total_banana(dados_banana["area_total_banana"])
                        dados_banana["ir_fase1_semanal_total_banana"] = dados_banana["ir_fase1_diária_total_banana"] * 7
                        dados_banana["ir_fase1_mes_total_banana"] = dados_banana["ir_fase1_semanal_total_banana"] * 4
                        dados_banana["ir_fase1_total_banana"] = dados_banana["ir_fase1_mes_total_banana"] * 1 # fase 1 duara 2 meses
                        #Prints Informações Básicas + Insumos----------------------------------------------------------------------------------------------------------------------------------
                        print("----------Informações Básicas----------")
                        print(f"A área util é de: {dados_banana["area_util_banana"]:.2f} m²")
                        print(f"O número total de mudas a serem plantadas é de {dados_banana["numero_mudas_total_banana"]:.1f} mudas")
                        print(f"A plantação terá {dados_banana["num_ruas_banana"]:.1f} ruas")
                        print(f"O a quantidade de banana obitidas após um ciclo completo é de {dados_banana["numero_graos_total_banana"]:.2f}kg")
                        print("-----------Insumos 1°Fase----------")
                        print(f"O calcio deve ser aplicado 1 vez, sendo necessário aplicar 0.7 toneladas de cálcio por hectare, totalizando {dados_banana["calcio_total_banana"]:.2f} toneladas de cálcio")
                        print(f"O Adubo deve ser aplicado 1 vez, sendo necessário aplicar 0.85 kg de Adubo(NPK) por m², totlizando {dados_banana["npk_fase1_banana"]:.2f}kg de NPK")
                        print(f"O Inseticida è dividido em 2 aplicação, sendo uma aplicação para cada fase")
                        print(f"Na 1° Aplicação do Inseticida são necessários 2.75 L/m², totalizando {dados_banana["fungicida_aplicacao1_banana"]:.2f}L")
                        print(f"O Fungicida è dividido em 2 aplicação, sendo uma aplicação para cada fase")
                        print(f"Na 1° Aplicação do fungiciada são necessários 2.50 L/m², totalizando {dados_banana["fungicida_aplicacao1_banana"]:.2f}L")
                        print(f"São necessários 8.50 L de água /m², totalizando: \n {dados_banana["ir_fase1_diária_total_banana"]:.2f} L de água diário \n {dados_banana["ir_fase1_semanal_total_banana"]:.2f} L de água semanal \n {dados_banana["ir_fase1_mes_total_banana"]:.2f} L de água mensal \n {dados_banana["ir_fase1_total_banana"]:.2f} L de água duarante  a fase 1(3 meses)")
                        #---------- Fase2----------  
                        dados_banana["npk_fase2_banana"] = adubo_NPK(dados_banana["area_total_banana"])
                        dados_banana["inseticida_aplicacao2_banana"] = inseticida2(dados_banana["area_total_banana"])
                        dados_banana["fungicida_aplicacao2_banana"] = fungicida2(dados_banana["area_total_banana"])
                        dados_banana["ir_fase2_diária_total_banana"] = irrigação2_diaria_total_banana(dados_banana["area_total_banana"])
                        dados_banana["ir_fase2_semanal_total_banana"] = dados_banana["ir_fase2_diária_total_banana"] * 7
                        dados_banana["ir_fase2_mes_total_banana"] = dados_banana["ir_fase2_semanal_total_banana"] * 4
                        dados_banana["ir_fase2_total_banana"] = dados_banana["ir_fase2_mes_total_banana"] * 1 # fase 2 duara  meses  
                        dados_banana["ir_Ciclo_Completo_banana"] = dados_banana["ir_fase2_total_banana"] + dados_banana["ir_fase1_total_banana"]
                        #Prints Informações Básicas + Insumos----------------------------------------------------------------------------------------------------------------------------------
                        print("-----------Insumos 2°Fase----------")
                        print(f"O Adubo deve ser aplicado 1 vez, sendo necessário aplicar 0.85 kg de Adubo(NPK) por m², totlizando {dados_banana["npk_fase2_banana"]:.2f}kg de NPK")
                        print(f"Na 2° Aplicação do Inseticida são necessários 1.50 L/m², totalizando {dados_banana["inseticida_aplicacao2_banana"]:.2f}L")
                        print(f"Na 2° Aplicação do fungiciada são necessários 1.75 L/m², totalizando {dados_banana["fungicida_aplicacao2_banana"]:.2f}L")
                        print(f"São necessários 7.50 L de água /m², totalizando: \n {dados_banana["ir_fase2_diária_total_banana"]:.2f} L de água diário \n {dados_banana["ir_fase2_semanal_total_banana"]:.2f} L de água semanal \n {dados_banana["ir_fase2_mes_total_banana"]:.2f} L de água mensal \n {dados_banana["ir_fase2_total_banana"]:.2f} L de água duarante  a fase 2 ( 3 meses)")
                        print(f"Em um ciclo completo será utilizado {dados_banana["ir_Ciclo_Completo_banana"]:.2f} L de água")  
                        #---------- Médias (R) -----------
                        # Vetor com os dados da aplicações de inseticida:
                        inseticida_banana = r.c(dados_banana["inseticida_aplicacao1_banana"], dados_banana["inseticida_aplicacao2_banana"])
                        # Calculando média, mediana e desvio padrão:
                        media_inseticida_banana = r.mean(inseticida_banana)
                        desvio_padrao_inseticida_banana = r.sd(inseticida_banana) 
                        print(f'A média de inseticida ultizada é de {media_inseticida_banana[0]} L/m², com desvio padrão de {desvio_padrao_inseticida_banana[0]:.2f} L/m²')
                        # Vetor com os dados da aplicações de fungicida:
                        fungicida_banana = r.c(dados_banana["fungicida_aplicacao1_banana"], dados_banana["fungicida_aplicacao2_banana"])
                        # Calculando média, mediana e desvio padrão:
                        media_fungicida_banana = r.mean(fungicida_banana)
                        desvio_padrao_fungicida_banana = r.sd(fungicida_banana)
                        print(f'A média de fungicida utilizada é de {media_fungicida_banana[0]} L/m², com desvio padrão de {desvio_padrao_fungicida_banana[0]:.2f} L/m²')
                        # Vetor com os dados da irrigação por fase:
                        irrigacao_banana = r.c(dados_banana["ir_fase1_total_banana"], dados_banana["ir_fase2_total_banana"])
                        # Calculando média, mediana e desvio padrão:
                        media_irrigacao_banana = r.mean(irrigacao_banana)
                        desvio_padrao_irrigacao_banana = r.sd(irrigacao_banana)
                        print(f'A média de água utilizada é de {media_irrigacao_banana[0]:.2f} L, com desvio padrão de {desvio_padrao_irrigacao_banana[0]:.2f} L') 
                    elif op == 4:
                        print("voltando ao menu das regiões")
                        break 
                    else:
                        print("Opção invalida, tente novamnete")
            elif op == 3:
                #----- Região Norte -----
                while True:
                    print("------Culturas------")
                    print(" 1. Milho (grão) \n 2. Batata Doce (hortaliça) \n 3. Açaí (fruta) \n 4 Voltar") 
                    op = int(input("Digite o número referente a opção que deseja plantar: "))    
                    if op == 1:
                     #---------------------------------------------------------------------Cultura - Milho---------------------------------------------------------------------
                     # a cultur de milho é dividida em duas fases cada uma com duaração de 4 meses
                     #----------Definir Funções Específicas----------
                     #---Irrigação1 (8.50L de água por m²)---
                     def irrigação1_diaria_total_milho(at:float) -> float:
                         return at * 8.50
                     #---Irrigação2 (7.50L de água por m²)---
                     def irrigação2_diaria_total_milho(at:float) -> float:
                         return at * 7.50
                     #---Número de hortaliças Total (4 kg por muda de milho)
                     def nhortalicas_total_milho (at:float) -> float:
                         return 4 * ((at/4) * 8)
                     #----------Código Principal----------
                     #---------- Fase1----------
                     dados_milho = {}
                     print("Um cilco completo de milho duara 120 dia, ou seja, 4 mêses")
                     print("A cultura da milho é divida em duas fases cada uma com duração de 4 meses ")
                     print("Aplantação posuirá ruas com espaçamente de 1 m entre as ruas e as mudas devem ser plantads com espaçamento de 1 m entr elas")
                     #criando varias para as funções apra que possam ser vetorizadas
                     dados_milho["area_total_milho"] = float(input("Área disponível para plantação em m²: "))
                     # Calculando e armazenando os resultados no dicionário
                     # Informações Básicas----------------------------------------------------------------------------------------
                     dados_milho["area_util_milho"] = area_util(dados_milho["area_total_milho"])  
                     dados_milho["numero_mudas_total_milho"] = num_mudas_total(dados_milho["area_total_milho"],2 )  # 2 mudas por m²
                     dados_milho["num_ruas_milho"] = numero_ruas_total(dados_milho["area_total_milho"])
                     dados_milho["numero_hortalicas_total_milho"] = nhortalicas_total_milho(dados_milho["area_total_milho"])
                     # Insumos--------------------------------------------------------------------------------------------------------
                     dados_milho["calcio_fase1_total_milho"] = calcio_total(dados_milho["area_total_milho"])
                     dados_milho["npk_fase1_milho"] = adubo_NPK(dados_milho["area_total_milho"])
                     dados_milho["inseticida_aplicacao1_milho"] = inseticida1(dados_milho["area_total_milho"])
                     dados_milho["fungicida_aplicacao1_milho"] = fungicida1(dados_milho["area_total_milho"])
                     dados_milho["ir_fase1_diária_total_milho"] = irrigação1_diaria_total_milho(dados_milho["area_total_milho"])
                     dados_milho["ir_fase1_semanal_total_milho"] = dados_milho["ir_fase1_diária_total_milho"] * 7
                     dados_milho["ir_fase1_mes_total_milho"] = dados_milho["ir_fase1_semanal_total_milho"] * 4
                     dados_milho["ir_fase1_total_milho"] = dados_milho["ir_fase1_mes_total_milho"] * 4 # fase 1 duara 4 meses
                     #Prints Informações Básicas + Insumos----------------------------------------------------------------------------------------------------------------------------------
                     print("----------Informações Básicas----------")
                     print(f"A área util é de: {dados_milho["area_util_milho"]:.2f} m²")
                     print(f"O número total de mudas a serem plantadas é de {dados_milho["numero_mudas_total_milho"]:.1f} mudas")
                     print(f"A plantação terá {dados_milho["num_ruas_milho"]:.1f} ruas")
                     print(f"O a quantidade de batadas obitidas após um ciclo completo é de {dados_milho["numero_hortalicas_total_milho"]:.2f}kg")
                     print("-----------Insumos 1°Fase----------")
                     print(f"O calcio deve ser aplicado 1 vez, sendo necessário aplicar 0.7 toneladas de cálcio por hectare, totalizando {dados_milho["calcio_fase1_total_milho"]:.2f} toneladas de cálcio")
                     print(f"O Adubo deve ser aplicado 1 vez, sendo necessário aplicar 0.85 kg de Adubo(NPK) por m², totlizando {dados_milho["npk_fase1_milho"]:.2f}kg de NPK")
                     print(f"O Inseticida è dividido em 2 aplicação, sendo uma aplicação para cada fase")
                     print(f"Na 1° Aplicação do Inseticida são necessários 2.75 L/m², totalizando {dados_milho["inseticida_aplicacao1_milho"]:.2f}L")
                     print(f"O Fungicida è dividido em 2 aplicação, sendo uma aplicação para cada fase")
                     print(f"Na 1° Aplicação do fungiciada são necessários 2.50 L/m², totalizando {dados_milho["fungicida_aplicacao1_milho"]:.2f}L")
                     print(f"São necessários 9.00 L de água /m², totalizando: \n {dados_milho["ir_fase1_diária_total_milho"]:.2f} L de água diário \n {dados_milho["ir_fase1_semanal_total_milho"]:.2f} L de água semanal \n {dados_milho["ir_fase1_mes_total_milho"]:.2f} L de água mensal \n {dados_milho["ir_fase1_total_milho"]:.2f} L de água duarante  a fase 1 ( 2 meses)")
                     #---------- Fase2----------  
                     dados_milho["calcio_fase2_total_milho"] = calcio_total(dados_milho["area_total_milho"])
                     dados_milho["npk_fase2_milho"] = adubo_NPK(dados_milho["area_total_milho"])
                     dados_milho["inseticida_aplicacao2_milho"] = inseticida2(dados_milho["area_total_milho"])
                     dados_milho["fungicida_aplicacao2_milho"] = fungicida2(dados_milho["area_total_milho"])
                     dados_milho["ir_fase2_diária_total_milho"] = irrigação2_diaria_total_milho(dados_milho["area_total_milho"])
                     dados_milho["ir_fase2_semanal_total_milho"] = dados_milho["ir_fase2_diária_total_milho"] * 7
                     dados_milho["ir_fase2_mes_total_milho"] = dados_milho["ir_fase2_semanal_total_milho"] * 4
                     dados_milho["ir_fase2_total_milho"] = dados_milho["ir_fase2_mes_total_milho"] * 4 # fase 2 duara 4 meses  
                     dados_milho["ir_Ciclo_Completo_milho"] = dados_milho["ir_fase2_total_milho"] + dados_milho["ir_fase1_total_milho"]
                     #Prints Informações Básicas + Insumos----------------------------------------------------------------------------------------------------------------------------------
                     print("-----------Insumos 2°Fase----------")
                     print(f"O calcio deve ser aplicado 1 vez, sendo necessário aplicar 0.7 toneladas de cálcio por hectare, totalizando {dados_milho["calcio_fase2_total_milho"]:.2f} toneladas de cálcio")
                     print(f"O Adubo deve ser aplicado 1 vez, sendo necessário aplicar 0.85 kg de Adubo(NPK) por m², totlizando {dados_milho["npk_fase2_milho"]:.2f}kg de NPK")
                     print(f"Na 2° Aplicação do Inseticida são necessários 1.50 L/m², totalizando {dados_milho["inseticida_aplicacao2_milho"]:.2f}L")
                     print(f"Na 2° Aplicação do fungiciada são necessários 1.75 L/m², totalizando {dados_milho["fungicida_aplicacao2_milho"]:.2f}L")
                     print(f"São necessários 7.00 L de água /m², totalizando: \n {dados_milho["ir_fase2_diária_total_milho"]:.2f} L de água diário \n {dados_milho["ir_fase2_semanal_total_milho"]:.2f} L de água semanal \n {dados_milho["ir_fase2_mes_total_milho"]:.2f} L de água mensal \n {dados_milho["ir_fase2_total_milho"]:.2f} L de água duarante  a fase 2 ( 2 meses)")
                     print(f"Em um ciclo completo será utilizado {dados_milho["ir_Ciclo_Completo_milho"]:.2f} L de água")   
                     #---------- Médias (R) -----------
                     # Vetor com os dados da aplicações de inseticida:
                     inseticida_milho = r.c(dados_milho["inseticida_aplicacao1_milho"], dados_milho["inseticida_aplicacao2_milho"])
                     # Calculando média, mediana e desvio padrão:
                     media_inseticida_milho = r.mean(inseticida_milho)
                     desvio_padrao_inseticida_milho = r.sd(inseticida_milho) 
                     print(f'A média de inseticida ultizada é de {media_inseticida_milho[0]} L/m², com desvio padrão de {desvio_padrao_inseticida_milho[0]:.2f} L/m²')
                     # Vetor com os dados da aplicações de fungicida:
                     fungicida_milho = r.c(dados_milho["fungicida_aplicacao1_milho"], dados_milho["fungicida_aplicacao2_milho"])
                     # Calculando média, mediana e desvio padrão:
                     media_fungicida_milho = r.mean(fungicida_milho)
                     desvio_padrao_fungicida_milho = r.sd(fungicida_milho)
                     print(f'A média de fungicida utilizada é de {media_fungicida_milho[0]} L/m², com desvio padrão de {desvio_padrao_fungicida_milho[0]:.2f} L/m²')
                     # Vetor com os dados da irrigação por fase:
                     irrigacao_milho = r.c(dados_milho["ir_fase1_total_milho"], dados_milho["ir_fase2_total_milho"])
                     # Calculando média, mediana e desvio padrão:
                     media_irrigacao_milho = r.mean(irrigacao_milho)
                     desvio_padrao_irrigacao_milho = r.sd(irrigacao_milho)
                     print(f'A média de água utilizada é de {media_irrigacao_milho[0]:.2f} L, com desvio padrão de {desvio_padrao_irrigacao_milho[0]:.2f} L') 
                    elif op == 2:
                     #---------------------------------------------------------------------Cultura - batata doce---------------------------------------------------------------------
                     # a cultura de batata doce é dividida em duas fases cada uma com duaração de 3 meses
                     #----------Definir Funções Específicas----------
                     #---Irrigação1 (8.00L de água por m²)---
                     def irrigação1_diaria_total_batata_doce(at:float) -> float:
                         return at * 8.00
                     #---Irrigação2 (7.00L de água por m²)---
                     def irrigação2_diaria_total_batata_doce(at:float) -> float:
                         return at * 7.00
                     #---Número de hortaliças Total (4 kg por muda de batata doce)
                     def nhortalicas_total_batata_doce (at:float) -> float:
                         return 4 * ((at/4) * 6)
                     #----------Código Principal----------
                     #---------- Fase1----------
                     dados_batata_doce = {}
                     print("Um cilco completo de batata doce duara 180 dia, ou seja, 6 mêses")
                     print("A cultura da batata doce é divida em duas fases cada uma com duração de 3 meses ")
                     print("Aplantação posuirá ruas com espaçamente de 1 m entre as ruas e as mudas devem ser plantads com espaçamento de 1 m entr elas")
                     #criando varias para as funções apra que possam ser vetorizadas
                     dados_batata_doce["area_total_batata_doce"] = float(input("Área disponível para plantação em m²: "))
                     # Calculando e armazenando os resultados no dicionário
                     # Informações Básicas----------------------------------------------------------------------------------------
                     dados_batata_doce["area_util_batata_doce"] = area_util(dados_batata_doce["area_total_batata_doce"])  
                     dados_batata_doce["numero_mudas_total_batata_doce"] = num_mudas_total(dados_batata_doce["area_total_batata_doce"],2 )  # 2 mudas por m²
                     dados_batata_doce["num_ruas_batata_doce"] = numero_ruas_total(dados_batata_doce["area_total_batata_doce"])
                     dados_batata_doce["numero_hortalicas_total_batata_doce"] = nhortalicas_total_batata_doce(dados_batata_doce["area_total_batata_doce"])
                     # Insumos--------------------------------------------------------------------------------------------------------
                     dados_batata_doce["calcio_fase1_total_batata_doce"] = calcio_total(dados_batata_doce["area_total_batata_doce"])
                     dados_batata_doce["npk_fase1_batata_doce"] = adubo_NPK(dados_batata_doce["area_total_batata_doce"])
                     dados_batata_doce["inseticida_aplicacao1_batata_doce"] = inseticida1(dados_batata_doce["area_total_batata_doce"])
                     dados_batata_doce["fungicida_aplicacao1_batata_doce"] = fungicida1(dados_batata_doce["area_total_batata_doce"])
                     dados_batata_doce["ir_fase1_diária_total_batata_doce"] = irrigação1_diaria_total_batata_doce(dados_batata_doce["area_total_batata_doce"])
                     dados_batata_doce["ir_fase1_semanal_total_batata_doce"] = dados_batata_doce["ir_fase1_diária_total_batata_doce"] * 7
                     dados_batata_doce["ir_fase1_mes_total_batata_doce"] = dados_batata_doce["ir_fase1_semanal_total_batata_doce"] * 4
                     dados_batata_doce["ir_fase1_total_batata_doce"] = dados_batata_doce["ir_fase1_mes_total_batata_doce"] * 3 # fase 1 duara 3 meses
                     #Prints Informações Básicas + Insumos----------------------------------------------------------------------------------------------------------------------------------
                     print("----------Informações Básicas----------")
                     print(f"A área util é de: {dados_batata_doce["area_util_batata_doce"]:.2f} m²")
                     print(f"O número total de mudas a serem plantadas é de {dados_batata_doce["numero_mudas_total_batata_doce"]:.1f} mudas")
                     print(f"A plantação terá {dados_batata_doce["num_ruas_batata_doce"]:.1f} ruas")
                     print(f"O a quantidade de batadas obitidas após um ciclo completo é de {dados_batata_doce["numero_hortalicas_total_batata_doce"]:.2f}kg")
                     print("-----------Insumos 1°Fase----------")
                     print(f"O calcio deve ser aplicado 1 vez, sendo necessário aplicar 0.7 toneladas de cálcio por hectare, totalizando {dados_batata_doce["calcio_fase1_total_batata_doce"]:.2f} toneladas de cálcio")
                     print(f"O Adubo deve ser aplicado 1 vez, sendo necessário aplicar 0.85 kg de Adubo(NPK) por m², totlizando {dados_batata_doce["npk_fase1_batata_doce"]:.2f}kg de NPK")
                     print(f"O Inseticida è dividido em 2 aplicação, sendo uma aplicação para cada fase")
                     print(f"Na 1° Aplicação do Inseticida são necessários 2.75 L/m², totalizando {dados_batata_doce["inseticida_aplicacao1_batata_doce"]:.2f}L")
                     print(f"O Fungicida è dividido em 2 aplicação, sendo uma aplicação para cada fase")
                     print(f"Na 1° Aplicação do fungiciada são necessários 2.50 L/m², totalizando  {dados_batata_doce["fungicida_aplicacao1_batata_doce"]:.2f}L")
                     print(f"São necessários 9.00 L de água /m², totalizando: \n {dados_batata_doce["ir_fase1_diária_total_batata_doce"]:.2f} L de água diário \n {dados_batata_doce["ir_fase1_semanal_total_batata_doce"]:.2f} L de água semanal \n {dados_batata_doce["ir_fase1_mes_total_batata_doce"]:.2f} L de água mensal \n {dados_batata_doce["ir_fase1_total_batata_doce"]:.2f} L de água duarante  toda a fase 1 ( 3 meses)")
                     #---------- Fase2----------  
                     dados_batata_doce["calcio_fase2_total_batata_doce"] = calcio_total(dados_batata_doce["area_total_batata_doce"])
                     dados_batata_doce["npk_fase2_batata_doce"] = adubo_NPK(dados_batata_doce["area_total_batata_doce"])
                     dados_batata_doce["inseticida_aplicacao2_batata_doce"] = inseticida2(dados_batata_doce["area_total_batata_doce"])
                     dados_batata_doce["fungicida_aplicacao2_batata_doce"] = fungicida2(dados_batata_doce["area_total_batata_doce"])
                     dados_batata_doce["ir_fase2_diária_total_batata_doce"] = irrigação2_diaria_total_batata_doce(dados_batata_doce["area_total_batata_doce"])
                     dados_batata_doce["ir_fase2_semanal_total_batata_doce"] = dados_batata_doce["ir_fase2_diária_total_batata_doce"] * 7
                     dados_batata_doce["ir_fase2_mes_total_batata_doce"] = dados_batata_doce["ir_fase2_semanal_total_batata_doce"] * 4
                     dados_batata_doce["ir_fase2_total_batata_doce"] = dados_batata_doce["ir_fase2_mes_total_batata_doce"] * 4 # fase 2 duara 4 meses  
                     dados_batata_doce["ir_Ciclo_Completo_batata_doce"] = dados_batata_doce["ir_fase2_total_batata_doce"] + dados_batata_doce["ir_fase1_total_batata_doce"]
                     #Prints Informações Básicas + Insumos----------------------------------------------------------------------------------------------------------------------------------
                     print("-----------Insumos 2°Fase----------")
                     print(f"O calcio deve ser aplicado 1 vez, sendo necessário aplicar 0.7 toneladas de cálcio por hectare, totalizando {dados_batata_doce["calcio_fase2_total_batata_doce"]:.2f} toneladas de cálcio")
                     print(f"O Adubo deve ser aplicado 1 vez, sendo necessário aplicar 0.85 kg de Adubo(NPK) por m², totlizando { dados_batata_doce["npk_fase2_batata_doce"]:.2f}kg de NPK")
                     print(f"Na 2° Aplicação do Inseticida são necessários 1.50 L/m², totalizando {dados_batata_doce["inseticida_aplicacao2_batata_doce"]:.2f}L")
                     print(f"Na 2° Aplicação do fungiciada são necessários 1.75 L/m², totalizando { dados_batata_doce["fungicida_aplicacao2_batata_doce"]:.2f}L")
                     print(f"São necessários 7.00 L de água /m², totalizando: \n {dados_batata_doce["ir_fase2_diária_total_batata_doce"]:.2f} L de água diário \n {dados_batata_doce["ir_fase2_semanal_total_batata_doce"]:.2f} L de água semanal \n {dados_batata_doce["ir_fase2_mes_total_batata_doce"]:.2f} L de água mensal \n {dados_batata_doce["ir_fase2_total_batata_doce"]:.2f} L de água duarante  a fase 2 (3  meses)")
                     print(f"Em um ciclo completo será utilizado {dados_batata_doce["ir_Ciclo_Completo_batata_doce"]:.2f} L de água")   
                     #---------- Médias (R) -----------
                     # Vetor com os dados da aplicações de inseticida:
                     inseticida_batata_doce = r.c(dados_batata_doce["inseticida_aplicacao1_batata_doce"], dados_batata_doce["inseticida_aplicacao2_batata_doce"])
                     # Calculando média, mediana e desvio padrão:
                     media_inseticida_batata_doce = r.mean(inseticida_batata_doce)
                     desvio_padrao_inseticida_batata_doce = r.sd(inseticida_batata_doce) 
                     print(f'A média de inseticida ultizada é de {media_inseticida_batata_doce[0]} L/m², com desvio padrão de {desvio_padrao_inseticida_batata_doce[0]:.2f} L/m²')
                     # Vetor com os dados da aplicações de fungicida:
                     fungicida_batata_doce = r.c(dados_batata_doce["fungicida_aplicacao1_batata_doce"], dados_batata_doce["fungicida_aplicacao2_batata_doce"])
                     # Calculando média, mediana e desvio padrão:
                     media_fungicida_batata_doce = r.mean(fungicida_batata_doce)
                     desvio_padrao_fungicida_batata_doce = r.sd(fungicida_batata_doce)
                     print(f'A média de fungicida utilizada é de {media_fungicida_batata_doce[0]} L/m², com desvio padrão de {desvio_padrao_fungicida_batata_doce[0]:.2f} L/m²')
                     # Vetor com os dados da irrigação por fase:
                     irrigacao_batata_doce = r.c(dados_batata_doce["ir_fase1_total_batata_doce"], dados_batata_doce["ir_fase2_total_batata_doce"])
                     # Calculando média, mediana e desvio padrão:
                     media_irrigacao_batata_doce = r.mean(irrigacao_batata_doce)
                     desvio_padrao_irrigacao_batata_doce = r.sd(irrigacao_batata_doce)
                     print(f'A média de água utilizada é de {media_irrigacao_batata_doce[0]:.2f} L, com desvio padrão de {desvio_padrao_irrigacao_batata_doce[0]:.2f} L')
                     #---------- Disvios (R) ----------     
                    elif op == 3:
                     #---------------------------------------------------------------------Cultura - Açai---------------------------------------------------------------------
                     # a cultura de açai é dividida em duas fases cada uma com duaração de 4 meses
                     #----------Definir Funções Específicas----------
                     #---Irrigação1 (8.50L de água por m²)---
                     def irrigação1_diaria_total_acai(at:float) -> float:
                         return at * 8.00
                     #---Irrigação2 (6.50L de água por m²)---
                     def irrigação2_diaria_total_acai(at:float) -> float:
                         return at * 6.50
                     #---Número de hortaliças Total (4 kg por muda de Açai)
                     def nhortalicas_total_acai (at:float) -> float:
                         return 3.5 * ((at/4) * 3)
                     #----------Código Principal----------
                     #---------- Fase1----------
                     dados_acai = {}
                     print("Um cilco completo de açai doce duara 180 dia, ou seja, 6 mêses")
                     print("A cultura da açai doce é divida em duas fases cada uma com duração de 3 meses ")
                     print("Aplantação posuirá ruas com espaçamente de 1 m entre as ruas e as mudas devem ser plantads com espaçamento de 1 m entr elas")
                     #criando varias para as funções apra que possam ser vetorizadas
                     dados_acai["area_total_acai"] = float(input("Área disponível para plantação em m²: "))
                     # Calculando e armazenando os resultados no dicionário
                     # Informações Básicas----------------------------------------------------------------------------------------
                     dados_acai["area_util_acai"] = area_util(dados_acai["area_total_acai"])  
                     dados_acai["numero_mudas_total_acai"] = num_mudas_total(dados_acai["area_total_acai"],2 )  # 2 mudas por m²
                     dados_acai["num_ruas_acai"] = numero_ruas_total(dados_acai["area_total_acai"])
                     dados_acai["numero_hortalicas_total_acai"] = nhortalicas_total_acai(dados_acai["area_total_acai"])
                     # Insumos--------------------------------------------------------------------------------------------------------
                     dados_acai["calcio_fase1_total_acai"] = calcio_total(dados_acai["area_total_acai"])
                     dados_acai["npk_fase1_acai"] = adubo_NPK(dados_acai["area_total_acai"])
                     dados_acai["inseticida_aplicacao1_acai"] = inseticida1(dados_acai["area_total_acai"])
                     dados_acai["fungicida_aplicacao1_acai"] = fungicida1(dados_acai["area_total_acai"])
                     dados_acai["ir_fase1_diária_total_acai"] = irrigação1_diaria_total_acai(dados_acai["area_total_acai"])
                     dados_acai["ir_fase1_semanal_total_acai"] = dados_acai["ir_fase1_diária_total_acai"] * 7
                     dados_acai["ir_fase1_mes_total_acai"] = dados_acai["ir_fase1_semanal_total_acai"] * 4
                     dados_acai["ir_fase1_total_acai"] = dados_acai["ir_fase1_mes_total_acai"] * 3 # fase 1 duara 3 meses
                     #Prints Informações Básicas + Insumos----------------------------------------------------------------------------------------------------------------------------------
                     print("----------Informações Básicas----------")
                     print(f"A área util é de: {dados_acai["area_util_acai"]:.2f} m²")
                     print(f"O número total de mudas a serem plantadas é de {dados_acai["numero_mudas_total_acai"]:.1f} mudas")
                     print(f"A plantação terá {dados_acai["num_ruas_acai"]:.1f} ruas")
                     print(f"O a quantidade de batadas obitidas após um ciclo completo é de {dados_acai["numero_hortalicas_total_acai"]:.2f}kg")
                     print("-----------Insumos 1°Fase----------")
                     print(f"O calcio deve ser aplicado 1 vez, sendo necessário aplicar 0.7 toneladas de cálcio por hectare, totalizando {dados_acai["calcio_fase1_total_acai"]:.2f} toneladas de cálcio")
                     print(f"O Adubo deve ser aplicado 1 vez, sendo necessário aplicar 0.85 kg de Adubo(NPK) por m², totlizando {dados_acai["npk_fase1_acai"]:.2f}kg de NPK")
                     print(f"O Inseticida è dividido em 2 aplicação, sendo uma aplicação para cada fase")
                     print(f"Na 1° Aplicação do Inseticida são necessários 2.75 L/m², totalizando {dados_acai["inseticida_aplicacao1_acai"]:.2f}L")
                     print(f"O Fungicida è dividido em 2 aplicação, sendo uma aplicação para cada fase")
                     print(f"Na 1° Aplicação do fungiciada são necessários 2.50 L/m², totalizando  {dados_acai["fungicida_aplicacao1_acai"]:.2f}L")
                     print(f"São necessários 9.00 L de água /m², totalizando: \n {dados_acai["ir_fase1_diária_total_acai"]:.2f} L de água diário \n {dados_acai["ir_fase1_semanal_total_acai"]:.2f} L de água semanal \n {dados_acai["ir_fase1_mes_total_acai"]:.2f} L de água mensal \n {dados_acai["ir_fase1_total_acai"]:.2f} L de água duarante  toda a fase 1 ( 3 meses)")
                     #---------- Fase2----------  
                     dados_acai["calcio_fase2_total_acai"] = calcio_total(dados_acai["area_total_acai"])
                     dados_acai["npk_fase2_acai"] = adubo_NPK(dados_acai["area_total_acai"])
                     dados_acai["inseticida_aplicacao2_acai"] = inseticida2(dados_acai["area_total_acai"])
                     dados_acai["fungicida_aplicacao2_acai"] = fungicida2(dados_acai["area_total_acai"])
                     dados_acai["ir_fase2_diária_total_acai"] = irrigação2_diaria_total_acai(dados_acai["area_total_acai"])
                     dados_acai["ir_fase2_semanal_total_acai"] = dados_acai["ir_fase2_diária_total_acai"] * 7
                     dados_acai["ir_fase2_mes_total_acai"] = dados_acai["ir_fase2_semanal_total_acai"] * 4
                     dados_acai["ir_fase2_total_acai"] = dados_acai["ir_fase2_mes_total_acai"] * 3 # fase 2 duara 4 meses  
                     dados_acai["ir_Ciclo_Completo_acai"] = dados_acai["ir_fase2_total_acai"] + dados_acai["ir_fase1_total_acai"]
                     #Prints Informações Básicas + Insumos----------------------------------------------------------------------------------------------------------------------------------
                     print("-----------Insumos 2°Fase----------")
                     print(f"O calcio deve ser aplicado 1 vez, sendo necessário aplicar 0.7 toneladas de cálcio por hectare, totalizando {dados_acai["calcio_fase2_total_acai"]:.2f} toneladas de cálcio")
                     print(f"O Adubo deve ser aplicado 1 vez, sendo necessário aplicar 0.85 kg de Adubo(NPK) por m², totlizando { dados_acai["npk_fase2_acai"]:.2f}kg de NPK")
                     print(f"Na 2° Aplicação do Inseticida são necessários 1.50 L/m², totalizando {dados_acai["inseticida_aplicacao2_acai"]:.2f}L")
                     print(f"Na 2° Aplicação do fungiciada são necessários 1.75 L/m², totalizando { dados_acai["fungicida_aplicacao2_acai"]:.2f}L")
                     print(f"São necessários 7.00 L de água /m², totalizando: \n {dados_acai["ir_fase2_diária_total_acai"]:.2f} L de água diário \n {dados_acai["ir_fase2_semanal_total_acai"]:.2f} L de água semanal \n {dados_acai["ir_fase2_mes_total_acai"]:.2f} L de água mensal \n {dados_acai["ir_fase2_total_acai"]:.2f} L de água duarante  a fase 2 (3 meses)")
                     print(f"Em um ciclo completo será utilizado {dados_acai["ir_Ciclo_Completo_acai"]:.2f} L de água")   
                     #---------- Médias (R) -----------
                     # Vetor com os dados da aplicações de inseticida:
                     inseticida_acai = r.c(dados_acai["inseticida_aplicacao1_acai"], dados_acai["inseticida_aplicacao2_acai"])
                     # Calculando média, mediana e desvio padrão:
                     media_inseticida_acai = r.mean(inseticida_acai)
                     desvio_padrao_inseticida_acai = r.sd(inseticida_acai) 
                     print(f'A média de inseticida ultizada é de {media_inseticida_acai[0]} L/m², com desvio padrão de {desvio_padrao_inseticida_acai[0]:.2f} L/m²')
                     # Vetor com os dados da aplicações de fungicida:
                     fungicida_acai = r.c(dados_acai["fungicida_aplicacao1_acai"], dados_acai["fungicida_aplicacao2_acai"])
                     # Calculando média, mediana e desvio padrão:
                     media_fungicida_acai = r.mean(fungicida_acai)
                     desvio_padrao_fungicida_acai = r.sd(fungicida_acai)
                     print(f'A média de fungicida utilizada é de {media_fungicida_acai[0]} L/m², com desvio padrão de {desvio_padrao_fungicida_acai[0]:.2f} L/m²')
                     # Vetor com os dados da irrigação por fase:
                     irrigacao_acai = r.c(dados_acai["ir_fase1_total_acai"], dados_acai["ir_fase2_total_acai"])
                     # Calculando média, mediana e desvio padrão:
                     media_irrigacao_acai = r.mean(irrigacao_acai)
                     desvio_padrao_irrigacao_acai = r.sd(irrigacao_acai)
                     print(f'A média de água utilizada é de {media_irrigacao_acai[0]:.2f} L, com desvio padrão de {desvio_padrao_irrigacao_acai[0]:.2f} L') 
                    elif op == 4:
                        print("Voltando ao menu anterior")
                        break
                    else:
                        print("Opção Invalida, escolha novamente")
            elif op == 4:
                #----- Região Nordeste-----
                while True:
                    print("------Culturas------")
                    print(" 1. Algodão (fibra) \n 2. Mandióca (hortaliça) \n 3. Caju (fruta) \n 4 Voltar") 
                    op = int(input("Digite o número referente a  opção que deseja plantar: "))    
                    if op == 1:
                        #---------------------------------------------------------------------Cultura - Algodão---------------------------------------------------------------------
                        # a cultur de algodão é dividida em duas fases cada uma com duaração de 3 meses
                        #----------Definir Funções Específicas----------
                        #---Irrigação1 (8.50L de água por m²)---
                        def irrigação1_diaria_total_algodao(at:float) -> float:
                            return at * 8.50
                        #---Irrigação2 (7.50L de água por m²)---
                        def irrigação2_diaria_total_algodao(at:float) -> float:
                            return at * 7.50
                        #---Número de Afaces Total (4 kg por muda de algodão)
                        def ngraos_total_algodao (at:float) -> float:
                            return 4 * ((at/4) * 6)
                        #----------Código Principal----------
                        #---------- Fase1----------
                        dados_algodao = {}
                        print("Um cilco completo do algodão duara 180 dias, ou seja, 6 mêses")
                        print("A cultura do algodão é divida em duas fases cada uma com duração de 3 meses")
                        print("Aplantação posuirá ruas com espaçamente de 1 m entre as ruas e as mudas devem ser plantads com espaçamento de 1 m entr elas")
                        #criando varias para as funções pra que possam ser vetorizadas
                        dados_algodao["area_total_algodao"] = float(input("Área disponível para plantação em m²: "))
                        # Calculando e armazenando os resultados no dicionário
                        # Informações Básicas----------------------------------------------------------------------------------------
                        dados_algodao["area_util_algodao"] = area_util(dados_algodao["area_total_algodao"])  
                        dados_algodao["numero_mudas_total_algodao"] = num_mudas_total(dados_algodao["area_total_algodao"], 2) # 2 mudas por m²
                        dados_algodao["numero_graos_total_algodao"] = ngraos_total_algodao(dados_algodao["area_total_algodao"]) 
                        dados_algodao["num_ruas_algodao"] = numero_ruas_total(dados_algodao["area_total_algodao"])
                        # Insumos--------------------------------------------------------------------------------------------------------
                        dados_algodao["calcio_total_algodao"] = calcio_total(dados_algodao["area_total_algodao"])
                        dados_algodao["npk_fase1_algodao"] = adubo_NPK(dados_algodao["area_total_algodao"])
                        dados_algodao["fungicida_aplicacao1_algodao"] = inseticida1(dados_algodao["area_total_v"])
                        dados_algodao["fungicida_aplicacao1_algodao"] = fungicida1(dados_algodao["area_total_algodao"])
                        dados_algodao["ir_fase1_diária_total_algodao"] = irrigação1_diaria_total_algodao(dados_algodao["area_total_algodao"])
                        dados_algodao["ir_fase1_semanal_total_algodao"] = dados_algodao["ir_fase1_diária_total_algodao"] * 7
                        dados_algodao["ir_fase1_mes_total_algodao"] = dados_algodao["ir_fase1_semanal_total_algodao"] * 4
                        dados_algodao["ir_fase1_total_algodao"] = dados_algodao["ir_fase1_mes_total_algodao"] * 1 # fase 1 duara 2 meses
                        #Prints Informações Básicas + Insumos----------------------------------------------------------------------------------------------------------------------------------
                        print("----------Informações Básicas----------")
                        print(f"A área util é de: {dados_algodao["area_util_algodao"]:.2f} m²")
                        print(f"O número total de mudas a serem plantadas é de {dados_algodao["numero_mudas_total_algodao"]:.1f} mudas")
                        print(f"A plantação terá {dados_algodao["num_ruas_algodao"]:.1f} ruas")
                        print(f"O a quantidade de algodao obitidos após um ciclo completo é de {dados_algodao["numero_graos_total_algodao"]:.2f}kg")
                        print("-----------Insumos 1°Fase----------")
                        print(f"O calcio deve ser aplicado 1 vez, sendo necessário aplicar 0.7 toneladas de cálcio por hectare, totalizando {dados_algodao["calcio_total_algodao"]:.2f} toneladas de cálcio")
                        print(f"O Adubo deve ser aplicado 1 vez, sendo necessário aplicar 0.85 kg de Adubo(NPK) por m², totlizando {dados_algodao["npk_fase1_algodao"]:.2f}kg de NPK")
                        print(f"O Inseticida è dividido em 2 aplicação, sendo uma aplicação para cada fase")
                        print(f"Na 1° Aplicação do Inseticida são necessários 2.75 L/m², totalizando {dados_algodao["fungicida_aplicacao1_algodao"]:.2f}L")
                        print(f"O Fungicida è dividido em 2 aplicação, sendo uma aplicação para cada fase")
                        print(f"Na 1° Aplicação do fungiciada são necessários 2.50 L/m², totalizando {dados_algodao["fungicida_aplicacao1_algodao"]:.2f}L")
                        print(f"São necessários 8.50 L de água /m², totalizando: \n {dados_algodao["ir_fase1_diária_total_algodao"]:.2f} L de água diário \n {dados_algodao["ir_fase1_semanal_total_algodao"]:.2f} L de água semanal \n {dados_algodao["ir_fase1_mes_total_algodao"]:.2f} L de água mensal \n {dados_algodao["ir_fase1_total_algodao"]:.2f} L de água duarante  a fase 1 (3 meses)")
                        #---------- Fase2----------  
                        dados_algodao["npk_fase2_algodao"] = adubo_NPK(dados_algodao["area_total_algodao"])
                        dados_algodao["fungicida_aplicacao2_algodao"] = inseticida2(dados_algodao["area_total_v"])
                        dados_algodao["fungicida_aplicacao2_algodao"] = fungicida2(dados_algodao["area_total_algodao"])
                        dados_algodao["ir_fase2_diária_total_algodao"] = irrigação2_diaria_total_algodao(dados_algodao["area_total_algodao"])
                        dados_algodao["ir_fase2_semanal_total_algodao"] = dados_algodao["ir_fase2_diária_total_algodao"] * 7
                        dados_algodao["ir_fase2_mes_total_algodao"] = dados_algodao["ir_fase2_semanal_total_algodao"] * 4
                        dados_algodao["ir_fase2_total_algodao"] = dados_algodao["ir_fase2_mes_total_algodao"] * 1 # fase 2 duara  meses  
                        dados_algodao["ir_Ciclo_Completo_algodao"] = dados_algodao["ir_fase2_total_algodao"] + dados_algodao["ir_fase1_total_algodao"]
                        #Prints Informações Básicas + Insumos----------------------------------------------------------------------------------------------------------------------------------
                        print("-----------Insumos 2°Fase----------")
                        print(f"O Adubo deve ser aplicado 1 vez, sendo necessário aplicar 0.85 kg de Adubo(NPK) por m², totlizando {dados_algodao["npk_fase_algodao"]:.2f}kg de NPK")
                        print(f"Na 2° Aplicação do Inseticida são necessários 1.50 L/m², totalizando {dados_algodao["inseticida_aplicacao2_algodao"]:.2f}L")
                        print(f"Na 2° Aplicação do fungiciada são necessários 1.75 L/m², totalizando {dados_algodao["fungicida_aplicacao2_algodao"]:.2f}L")
                        print(f"São necessários 7.50 L de água /m², totalizando: \n {dados_algodao["ir_fase2_diária_total_algodao"]:.2f} L de água diário \n {dados_algodao["ir_fase2_semanal_total_algodao"]:.2f} L de água semanal \n {dados_algodao["ir_fase2_mes_total_algodao"]:.2f} L de água mensal \n {dados_algodao["ir_fase2_total_algodao"]:.2f} L de água duarante  a fase 1 (3 meses)")
                        print(f"Em um ciclo completo será utilizado {dados_algodao["ir_Ciclo_Completo_algodao"]:.2f} L de água")  
                        #---------- Médias (R) -----------
                        # Vetor com os dados da aplicações de inseticida:
                        inseticida_algodao = r.c(dados_algodao["inseticida_aplicacao1_algodao"], dados_algodao["inseticida_aplicacao2_algodao"])
                        # Calculando média, mediana e desvio padrão:
                        media_inseticida_algodao = r.mean(inseticida_algodao)
                        desvio_padrao_inseticida_algodao = r.sd(inseticida_algodao) 
                        print(f'A média de inseticida ultizada é de {media_inseticida_algodao[0]} L/m², com desvio padrão de {desvio_padrao_inseticida_algodao[0]:.2f} L/m²')
                        # Vetor com os dados da aplicações de fungicida:
                        fungicida_algodao = r.c(dados_algodao["fungicida_aplicacao1_algodao"], dados_algodao["fungicida_aplicacao2_algodao"])
                        # Calculando média, mediana e desvio padrão:
                        media_fungicida_algodao = r.mean(fungicida_algodao)
                        desvio_padrao_fungicida_algodao = r.sd(fungicida_algodao)
                        print(f'A média de fungicida utilizada é de {media_fungicida_algodao[0]} L/m², com desvio padrão de {desvio_padrao_fungicida_algodao[0]:.2f} L/m²')
                        # Vetor com os dados da irrigação por fase:
                        irrigacao_algodao = r.c(dados_algodao["ir_fase1_total_algodao"], dados_algodao["ir_fase2_total_algodao"])
                        # Calculando média, mediana e desvio padrão:
                        media_irrigacao_algodao = r.mean(irrigacao_algodao)
                        desvio_padrao_irrigacao_algodao = r.sd(irrigacao_algodao)
                        print(f'A média de água utilizada é de {media_irrigacao_algodao[0]:.2f} L, com desvio padrão de {desvio_padrao_irrigacao_algodao[0]:.2f} L') 
                    elif op == 2: 
                        #---------------------------------------------------------------------Cultura - mandioca---------------------------------------------------------------------
                        # A cultura de mandioca é dividida em duas fases cada uma com duração de 4 meses
                        #----------Definir Funções Específicas----------
                        #---Irrigação1 (8.00L de água por m²)---
                        def irrigação1_diaria_total_mandioca(at:float) -> float:
                            return at * 8.00
                        #---Irrigação2 (7.00L de água por m²)---
                        def irrigação2_diaria_total_mandioca(at:float) -> float:
                            return at * 7.00
                        #---Número de hortaliças Total (4 kg por muda de mandioca)
                        def nhortalicas_total_mandioca (at:float) -> float:
                             return 4 * ((at/4) * 2)
                        #----------Código Principal----------
                        #---------- Fase1----------
                        dados_mandioca = {}
                        print("Um ciclo completo de mandioca dura 180 dias, ou seja, 6 meses")
                        print("A cultura da mandioca é dividida em duas fases, cada uma com duração de 3 meses")
                        print("A plantação possuirá ruas com espaçamento de 1 m entre as ruas, e as mudas devem ser plantadas com espaçamento de 1 m entre elas")
                        # criando variáveis para as funções para que possam ser vetorizadas
                        dados_mandioca["area_total_mandioca"] = float(input("Área disponível para plantação em m²: "))
                        # Calculando e armazenando os resultados no dicionário
                        # Informações Básicas----------------------------------------------------------------------------------------
                        dados_mandioca["area_util_mandioca"] = area_util(dados_mandioca["area_total_mandioca"])  
                        dados_mandioca["numero_mudas_total_mandioca"] = num_mudas_total(dados_mandioca["area_total_mandioca"], 2)  # 2 mudas por m²
                        dados_mandioca["num_ruas_mandioca"] = numero_ruas_total(dados_mandioca["area_total_mandioca"])
                        dados_mandioca["numero_hortalicas_total_mandioca"] = nhortalicas_total_mandioca(dados_mandioca["area_total_mandioca"])
                        # Insumos--------------------------------------------------------------------------------------------------------
                        dados_mandioca["calcio_fase1_total_mandioca"] = calcio_total(dados_mandioca["area_total_mandioca"])
                        dados_mandioca["npk_fase1_mandioca"] = adubo_NPK(dados_mandioca["area_total_mandioca"])
                        dados_mandioca["inseticida_aplicacao1_mandioca"] = inseticida1(dados_mandioca["area_total_mandioca"])
                        dados_mandioca["fungicida_aplicacao1_mandioca"] = fungicida1(dados_mandioca["area_total_mandioca"])
                        dados_mandioca["ir_fase1_diária_total_mandioca"] = irrigação1_diaria_total_mandioca(dados_mandioca["area_total_mandioca"])
                        dados_mandioca["ir_fase1_semanal_total_mandioca"] = dados_mandioca["ir_fase1_diária_total_mandioca"] * 7
                        dados_mandioca["ir_fase1_mes_total_mandioca"] = dados_mandioca["ir_fase1_semanal_total_mandioca"] * 4
                        dados_mandioca["ir_fase1_total_mandioca"] = dados_mandioca["ir_fase1_mes_total_mandioca"] * 3 # fase 1 dura 3 meses
                        # Prints Informações Básicas + Insumos----------------------------------------------------------------------------------------------------------------------------------
                        print("----------Informações Básicas----------")
                        print(f"A área útil é de: {dados_mandioca['area_util_mandioca']:.2f} m²")
                        print(f"O número total de mudas a serem plantadas é de {dados_mandioca['numero_mudas_total_mandioca']:.1f} mudas")
                        print(f"A plantação terá {dados_mandioca['num_ruas_mandioca']:.1f} ruas")
                        print(f"A quantidade de mandioca obtida após um ciclo completo é de {dados_mandioca['numero_hortalicas_total_mandioca']:.2f} kg")
                        print("-----------Insumos 1°Fase----------")
                        print(f"O cálcio deve ser aplicado 1 vez, sendo necessário aplicar 0.7 toneladas de cálcio por hectare, totalizando {dados_mandioca['calcio_fase1_total_mandioca']:.2f} toneladas de cálcio")
                        print(f"O Adubo deve ser aplicado 1 vez, sendo necessário aplicar 0.85 kg de Adubo(NPK) por m², totalizando {dados_mandioca['npk_fase1_mandioca']:.2f} kg de NPK")
                        print(f"O Inseticida é dividido em 2 aplicações, sendo uma aplicação para cada fase")
                        print(f"Na 1ª Aplicação do Inseticida são necessários 2.75 L/m², totalizando {dados_mandioca['inseticida_aplicacao1_mandioca']:.2f} L")
                        print(f"O Fungicida é dividido em 2 aplicações, sendo uma aplicação para cada fase")
                        print(f"Na 1ª Aplicação do fungicida são necessários 2.50 L/m², totalizando {dados_mandioca['fungicida_aplicacao1_mandioca']:.2f} L")
                        print(f"São necessários 9.00 L de água /m², totalizando: \n {dados_mandioca['ir_fase1_diária_total_mandioca']:.2f} L de água diário \n {dados_mandioca['ir_fase1_semanal_total_mandioca']:.2f} L de água semanal \n {dados_mandioca['ir_fase1_mes_total_mandioca']:.2f} L de água mensal \n {dados_mandioca['ir_fase1_total_mandioca']:.2f} L de água durante toda a fase 1 (3 meses)")
                        #---------- Fase2----------  
                        dados_mandioca["calcio_fase2_total_mandioca"] = calcio_total(dados_mandioca["area_total_mandioca"])
                        dados_mandioca["npk_fase2_mandioca"] = adubo_NPK(dados_mandioca["area_total_mandioca"])
                        dados_mandioca["inseticida_aplicacao2_mandioca"] = inseticida2(dados_mandioca["area_total_mandioca"])
                        dados_mandioca["fungicida_aplicacao2_mandioca"] = fungicida2(dados_mandioca["area_total_mandioca"])
                        dados_mandioca["ir_fase2_diária_total_mandioca"] = irrigação2_diaria_total_mandioca(dados_mandioca["area_total_mandioca"])
                        dados_mandioca["ir_fase2_semanal_total_mandioca"] = dados_mandioca["ir_fase2_diária_total_mandioca"] * 7
                        dados_mandioca["ir_fase2_mes_total_mandioca"] = dados_mandioca["ir_fase2_semanal_total_mandioca"] * 4
                        dados_mandioca["ir_fase2_total_mandioca"] = dados_mandioca["ir_fase2_mes_total_mandioca"] * 4 # fase 2 dura 4 meses  
                        dados_mandioca["ir_Ciclo_Completo_mandioca"] = dados_mandioca["ir_fase2_total_mandioca"] + dados_mandioca["ir_fase1_total_mandioca"]
                        # Prints Informações Básicas + Insumos----------------------------------------------------------------------------------------------------------------------------------
                        print("-----------Insumos 2°Fase----------")
                        print(f"O cálcio deve ser aplicado 1 vez, sendo necessário aplicar 0.7 toneladas de cálcio por hectare, totalizando {dados_mandioca['calcio_fase2_total_mandioca']:.2f} toneladas de cálcio")
                        print(f"O Adubo deve ser aplicado 1 vez, sendo necessário aplicar 0.85 kg de Adubo(NPK) por m², totalizando {dados_mandioca['npk_fase2_mandioca']:.2f} kg de NPK")
                        print(f"Na 2ª Aplicação do Inseticida são necessários 1.50 L/m², totalizando {dados_mandioca['inseticida_aplicacao2_mandioca']:.2f} L")
                        print(f"Na 2ª Aplicação do fungicida são necessários 1.75 L/m², totalizando {dados_mandioca['fungicida_aplicacao2_mandioca']:.2f} L")
                        print(f"São necessários 7.00 L de água /m², totalizando: \n {dados_mandioca['ir_fase2_diária_total_mandioca']:.2f} L de água diário \n {dados_mandioca['ir_fase2_semanal_total_mandioca']:.2f} L de água semanal \n {dados_mandioca['ir_fase2_mes_total_mandioca']:.2f} L de água mensal \n {dados_mandioca['ir_fase2_total_mandioca']:.2f} L de água durante a fase 2 (4 meses)")
                        print(f"Em um ciclo completo será utilizado {dados_mandioca['ir_Ciclo_Completo_mandioca']:.2f} L de água")  
                        #---------- Médias (R) -----------
                        # Vetor com os dados da aplicações de inseticida:
                        inseticida_mandioca = r.c(dados_mandioca["inseticida_aplicacao1_mandioca"], dados_mandioca["inseticida_aplicacao2_mandioca"])
                        # Calculando média, mediana e desvio padrão:
                        media_inseticida_mandioca = r.mean(inseticida_mandioca)
                        desvio_padrao_inseticida_mandioca = r.sd(inseticida_mandioca) 
                        print(f'A média de inseticida ultizada é de {media_inseticida_mandioca[0]} L/m², com desvio padrão de {desvio_padrao_inseticida_mandioca[0]:.2f} L/m²')
                        # Vetor com os dados da aplicações de fungicida:
                        fungicida_mandioca = r.c(dados_mandioca["fungicida_aplicacao1_mandioca"], dados_mandioca["fungicida_aplicacao2_mandioca"])
                        # Calculando média, mediana e desvio padrão:
                        media_fungicida_mandioca = r.mean(fungicida_mandioca)
                        desvio_padrao_fungicida_mandioca = r.sd(fungicida_mandioca)
                        print(f'A média de fungicida utilizada é de {media_fungicida_mandioca[0]} L/m², com desvio padrão de {desvio_padrao_fungicida_mandioca[0]:.2f} L/m²')
                        # Vetor com os dados da irrigação por fase:
                        irrigacao_mandioca = r.c(dados_mandioca["ir_fase1_total_mandioca"], dados_mandioca["ir_fase2_total_mandioca"])
                        # Calculando média, mediana e desvio padrão:
                        media_irrigacao_mandioca = r.mean(irrigacao_mandioca)
                        desvio_padrao_irrigacao_mandioca = r.sd(irrigacao_mandioca)
                        print(f'A média de água utilizada é de {media_irrigacao_mandioca[0]:.2f} L, com desvio padrão de {desvio_padrao_irrigacao_mandioca[0]:.2f} L')
                    elif op == 3:
                        # ---------------------------------------------------------------------Cultura - Caju---------------------------------------------------------------------
                        # A cultura de caju é dividida em duas fases cada uma com duaração de 8 meses
                        #  ---------- Definir Funções Específicas ----------
                        #  --- Irrigação1 (9.00L de água por m²) ---
                        def irrigacao1_diaria_total_caju(at: float) -> float:
                            return at * 9.00 
                        # --- Irrigação2 (8.00L de água por m²) ---
                        def irrigacao2_diaria_total_caju(at: float) -> float:
                            return at * 8.00
                        # --- Número de cajueiros Total (5 kg de caju por muda de caju) ---
                        def ncajueiros_total_caju(at: float) -> float:
                            return 5 * ((at / 4) * 3) 
                        # ---------- Código Principal ----------
                        # # ---------- Fase 1 ----------
                        dados_caju = {}
                        print("Um ciclo completo de caju dura 240 dias, ou seja, 8 meses.")
                        print("A cultura do caju é dividida em duas fases, cada uma com duração de 8 meses.")
                        print("A plantação terá espaçamento de 3m entre linhas e 3m entre mudas.")
                        # Coletando dados da área disponível
                        dados_caju["area_total_caju"] = float(input("Área disponível para plantação em m²: "))
                        # Calculando e armazenando os resultados no dicionário
                        # Informações Básicas
                        dados_caju["area_util_caju"] = area_util(dados_caju["area_total_caju"])
                        dados_caju["numero_mudas_total_caju"] = num_mudas_total(dados_caju["area_total_caju"], 3)  # 3 mudas por m²
                        dados_caju["num_linhas_caju"] = numero_ruas_total(dados_caju["area_total_caju"])
                        dados_caju["numero_cajueiros_total_caju"] = ncajueiros_total_caju(dados_caju["area_total_caju"])
                        # Insumos
                        dados_caju["calcio_fase1_total_caju"] = calcio_total(dados_caju["area_total_caju"])
                        dados_caju["npk_fase1_caju"] = adubo_NPK(dados_caju["area_total_caju"])
                        dados_caju["inseticida_aplicacao1_caju"] = inseticida1(dados_caju["area_total_caju"])
                        dados_caju["fungicida_aplicacao1_caju"] = fungicida1(dados_caju["area_total_caju"])
                        dados_caju["ir_fase1_diaria_total_caju"] = irrigacao1_diaria_total_caju(dados_caju["area_total_caju"])
                        dados_caju["ir_fase1_semanal_total_caju"] = dados_caju["ir_fase1_diaria_total_caju"] * 7
                        dados_caju["ir_fase1_mes_total_caju"] = dados_caju["ir_fase1_semanal_total_caju"] * 4
                        dados_caju["ir_fase1_total_caju"] = dados_caju["ir_fase1_mes_total_caju"] * 4  # Fase 1 dura 4 meses
                        # Prints Informações Básicas + Insumos
                        print("---------- Informações Básicas ----------")
                        print(f"A área útil é de: {dados_caju['area_util_caju']:.2f} m²")
                        print(f"O número total de mudas a serem plantadas é de {dados_caju['numero_mudas_total_caju']:.1f} mudas")
                        print(f"A plantação terá {dados_caju['num_linhas_caju']:.1f} linhas")
                        print(f"A quantidade de caju obtida após um ciclo completo é de {dados_caju['numero_cajueiros_total_caju']:.2f}kg") 
                        print("----------- Insumos 1°Fase ----------")
                        print(f"O cálcio deve ser aplicado 1 vez, sendo necessário aplicar 0.7 toneladas por hectare, totalizando {dados_caju['calcio_fase1_total_caju']:.2f} toneladas de cálcio")
                        print(f"O Adubo (NPK) deve ser aplicado 1 vez, totalizando {dados_caju['npk_fase1_caju']:.2f}kg de NPK")
                        print(f"Na 1° Aplicação do Inseticida são necessários 2.75 L/m², totalizando {dados_caju['inseticida_aplicacao1_caju']:.2f}L")
                        print(f"Na 1° Aplicação do Fungicida são necessários 2.50 L/m², totalizando {dados_caju['fungicida_aplicacao1_caju']:.2f}L")
                        print(f"São necessários 9.00 L de água por m², totalizando: \n{dados_caju['ir_fase1_diaria_total_caju']:.2f} L de água diário \n{dados_caju['ir_fase1_semanal_total_caju']:.2f} L semanal \n{dados_caju['ir_fase1_mes_total_caju']:.2f} L mensal \n{dados_caju['ir_fase1_total_caju']:.2f} L durante toda a fase 1 (4 meses)")
                        # ---------- Fase 2 ----------
                        dados_caju["calcio_fase2_total_caju"] = calcio_total(dados_caju["area_total_caju"])
                        dados_caju["npk_fase2_caju"] = adubo_NPK(dados_caju["area_total_caju"])
                        dados_caju["inseticida_aplicacao2_caju"] = inseticida2(dados_caju["area_total_caju"])
                        dados_caju["fungicida_aplicacao2_caju"] = fungicida2(dados_caju["area_total_caju"])
                        dados_caju["ir_fase2_diaria_total_caju"] = irrigacao2_diaria_total_caju(dados_caju["area_total_caju"])
                        dados_caju["ir_fase2_semanal_total_caju"] = dados_caju["ir_fase2_diaria_total_caju"] * 7
                        dados_caju["ir_fase2_mes_total_caju"] = dados_caju["ir_fase2_semanal_total_caju"] * 4
                        dados_caju["ir_fase2_total_caju"] = dados_caju["ir_fase2_mes_total_caju"] * 4  # Fase 2 dura 4 meses
                        dados_caju["ir_Ciclo_Completo_caju"] = dados_caju["ir_fase2_total_caju"] + dados_caju["ir_fase1_total_caju"]
                        # Prints Informações Básicas + Insumos
                        print("----------- Insumos 2°Fase ----------")
                        print(f"O cálcio deve ser aplicado 1 vez, totalizando {dados_caju['calcio_fase2_total_caju']:.2f} toneladas de cálcio")
                        print(f"O Adubo (NPK) deve ser aplicado 1 vez, totalizando {dados_caju['npk_fase2_caju']:.2f}kg de NPK")
                        print(f"Na 2° Aplicação do Inseticida são necessários 1.50 L/m², totalizando {dados_caju['inseticida_aplicacao2_caju']:.2f}L")
                        print(f"Na 2° Aplicação do Fungicida são necessários 1.75 L/m², totalizando {dados_caju['fungicida_aplicacao2_caju']:.2f}L")
                        print(f"São necessários 8.00 L de água por m², totalizando: \n{dados_caju['ir_fase2_diaria_total_caju']:.2f} L diário \n{dados_caju['ir_fase2_semanal_total_caju']:.2f} L semanal \n{dados_caju['ir_fase2_mes_total_caju']:.2f} L mensal \n{dados_caju['ir_fase2_total_caju']:.2f} L durante a fase 2 (4 meses)")
                        print(f"Em um ciclo completo será utilizado {dados_caju['ir_Ciclo_Completo_caju']:.2f} L de água.")
                        # Vetor com os dados da aplicações de inseticida:
                        inseticida_caju = r.c(dados_caju["inseticida_aplicacao1_caju"], dados_caju["inseticida_aplicacao2_caju"])
                        # Calculando média, mediana e desvio padrão:
                        media_inseticida_caju = r.mean(inseticida_caju)
                        desvio_padrao_inseticida_caju = r.sd(inseticida_caju) 
                        print(f'A média de inseticida ultizada é de {media_inseticida_caju[0]} L/m², com desvio padrão de {desvio_padrao_inseticida_caju[0]:.2f} L/m²')
                        # Vetor com os dados da aplicações de fungicida:
                        fungicida_caju = r.c(dados_caju["fungicida_aplicacao1_caju"], dados_caju["fungicida_aplicacao2_caju"])
                        # Calculando média, mediana e desvio padrão:
                        media_fungicida_caju = r.mean(fungicida_caju)
                        desvio_padrao_fungicida_caju = r.sd(fungicida_caju)
                        print(f'A média de fungicida utilizada é de {media_fungicida_caju[0]} L/m², com desvio padrão de {desvio_padrao_fungicida_caju[0]:.2f} L/m²')
                        # Vetor com os dados da irrigação por fase:
                        irrigacao_caju = r.c(dados_caju["ir_fase1_total_caju"], dados_caju["ir_fase2_total_caju"])
                        # Calculando média, mediana e desvio padrão:
                        media_irrigacao_caju = r.mean(irrigacao_caju)
                        desvio_padrao_irrigacao_caju = r.sd(irrigacao_caju)
                        print(f'A média de água utilizada é de {media_irrigacao_caju[0]:.2f} L, com desvio padrão de {desvio_padrao_irrigacao_caju[0]:.2f} L')
                    elif op == 4:
                        print("Voltando ao menu anterior")
                        break
                    else:
                        print("Opção Invalida, escolha novamente")
            elif op == 5:
                #----- Centro Oeste -----
                while True:
                    print("------Culturas------")
                    print(" 1. Soja (grão) \n 2. Tomate (hortaliça) \n 3. Laranja (fruta) \n 4 Voltar") 
                    op = int(input("Digite o número referente a  opção que deseja plantar: "))    
                    if op == 1:
                     #---------------------------------------------------------------------Cultura - Soja---------------------------------------------------------------------
                     # a cultur de soja é dividida em duas fases cada uma com duaração de 2 meses
                     #----------Definir Funções Específicas----------
                     #---Irrigação1 (9.00L de água por m²)---
                     def irrigação1_diaria_total_soja(at:float) -> float:
                         return at * 9.00
                     #---Irrigação2 (8.00L de água por m²)---
                     def irrigação2_diaria_total_soja(at:float) -> float:
                         return at * 8.00
                     #---Número de hortaliças Total (4 kg por muda de soja)
                     def nhortalicas_total_soja (at:float) -> float:
                         return 4 * ((at/4) * 3)
                     #----------Código Principal----------
                     #---------- Fase1----------
                     dados_soja = {}
                     print("Um cilco completo de soja duara 120 dia, ou seja, 4 mêses")
                     print("A cultura da soja é divida em duas fases cada uma com duração de 2 meses ")
                     print("Aplantação posuirá ruas com espaçamente de 1 m entre as ruas e as mudas devem ser plantads com espaçamento de 1 m entr elas")
                     #criando varias para as funções apra que possam ser vetorizadas
                     dados_soja["area_total_soja"] = float(input("Área disponível para plantação em m²: "))
                     # Calculando e armazenando os resultados no dicionário
                     # Informações Básicas----------------------------------------------------------------------------------------
                     dados_soja["area_util_soja"] = area_util(dados_soja["area_total_soja"])  
                     dados_soja["numero_mudas_total_soja"] = num_mudas_total(dados_soja["area_total_soja"],3 )  # 3 mudas por m²
                     dados_soja["num_ruas_soja"] = numero_ruas_total(dados_soja["area_total_soja"])
                     dados_soja["numero_hortalicas_total_soja"] = nhortalicas_total_soja(dados_soja["area_total_soja"])
                     # Insumos--------------------------------------------------------------------------------------------------------
                     dados_soja["calcio_fase1_total_soja"] = calcio_total(dados_soja["area_total_soja"])
                     dados_soja["npk_fase1_soja"] = adubo_NPK(dados_soja["area_total_soja"])
                     dados_soja["inseticida_aplicacao1_soja"] = inseticida1(dados_soja["area_total_soja"])
                     dados_soja["fungicida_aplicacao1_soja"] = fungicida1(dados_soja["area_total_soja"])
                     dados_soja["ir_fase1_diária_total_soja"] = irrigação1_diaria_total_soja(dados_soja["area_total_soja"])
                     dados_soja["ir_fase1_semanal_total_soja"] = dados_soja["ir_fase1_diária_total_soja"] * 7
                     dados_soja["ir_fase1_mes_total_soja"] = dados_soja["ir_fase1_semanal_total_soja"] * 4
                     dados_soja["ir_fase1_total_soja"] = dados_soja["ir_fase1_mes_total_soja"] * 4 # fase 1 duara 4 meses
                     #Prints Informações Básicas + Insumos----------------------------------------------------------------------------------------------------------------------------------
                     print("----------Informações Básicas----------")
                     print(f"A área util é de: {dados_soja["area_util_soja"]:.2f} m²")
                     print(f"O número total de mudas a serem plantadas é de {dados_soja["numero_mudas_total_soja"]:.1f} mudas")
                     print(f"A plantação terá {dados_soja["num_ruas_soja"]:.1f} ruas")
                     print(f"O a quantidade de batadas obitidas após um ciclo completo é de {dados_soja["numero_hortalicas_total_soja"]:.2f}kg")
                     print("-----------Insumos 1°Fase----------")
                     print(f"O calcio deve ser aplicado 1 vez, sendo necessário aplicar 0.7 toneladas de cálcio por hectare, totalizando {dados_soja["calcio_fase1_total_soja"]:.2f} toneladas de cálcio")
                     print(f"O Adubo deve ser aplicado 1 vez, sendo necessário aplicar 0.85 kg de Adubo(NPK) por m², totlizando {dados_soja["npk_fase1_soja"]:.2f}kg de NPK")
                     print(f"O Inseticida è dividido em 2 aplicação, sendo uma aplicação para cada fase")
                     print(f"Na 1° Aplicação do Inseticida são necessários 2.75 L/m², totalizando {dados_soja["inseticida_aplicacao1_soja"]:.2f}L")
                     print(f"O Fungicida è dividido em 2 aplicação, sendo uma aplicação para cada fase")
                     print(f"Na 1° Aplicação do fungiciada são necessários 2.50 L/m², totalizando {dados_soja["fungicida_aplicacao1_soja"] :.2f}L")
                     print(f"São necessários 9.00 L de água /m², totalizando: \n {dados_soja["ir_fase1_diária_total_soja"]:.2f} L de água diário \n {dados_soja["ir_fase1_semanal_total_soja"]:.2f} L de água semanal \n {dados_soja["ir_fase1_mes_total_soja"] :.2f} L de água mensal \n {dados_soja["ir_fase1_total_soja"]:.2f} L de água duarante  a fase 1 ( 2 meses)")
                     #---------- Fase2----------  
                     dados_soja["calcio_fase2_total_soja"] = calcio_total(dados_soja["area_total_soja"])
                     dados_soja["npk_fase2_soja"] = adubo_NPK(dados_soja["area_total_soja"])
                     dados_soja["inseticida_aplicacao2_soja"] = inseticida2(dados_soja["area_total_soja"])
                     dados_soja["fungicida_aplicacao2_soja"] = fungicida2(dados_soja["area_total_soja"])
                     dados_soja["ir_fase2_diária_total_soja"] = irrigação2_diaria_total_soja(dados_soja["area_total_soja"])
                     dados_soja["ir_fase2_semanal_total_soja"] = dados_soja["ir_fase2_diária_total_soja"] * 7
                     dados_soja["ir_fase2_mes_total_soja"] = dados_soja["ir_fase2_semanal_total_soja"] * 4
                     dados_soja["ir_fase2_total_soja"] = dados_soja["ir_fase2_mes_total_soja"] * 4 # fase 2 duara 4 meses  
                     dados_soja["ir_Ciclo_Completo_soja"] = dados_soja["ir_fase2_total_soja"] +  dados_soja["ir_fase1_total_soja"]
                     #Prints Informações Básicas + Insumos----------------------------------------------------------------------------------------------------------------------------------
                     print("-----------Insumos 2°Fase----------")
                     print(f"O calcio deve ser aplicado 1 vez, sendo necessário aplicar 0.7 toneladas de cálcio por hectare, totalizando {dados_soja["calcio_fase2_total_soja"]:.2f} toneladas de cálcio")
                     print(f"O Adubo deve ser aplicado 1 vez, sendo necessário aplicar 0.85 kg de Adubo(NPK) por m², totlizando {dados_soja["npk_fase2_soja"]:.2f}kg de NPK")
                     print(f"Na 2° Aplicação do Inseticida são necessários 1.50 L/m², totalizando {dados_soja["inseticida_aplicacao2_soja"]:.2f}L")
                     print(f"Na 2° Aplicação do fungiciada são necessários 1.75 L/m², totalizando {dados_soja["fungicida_aplicacao2_soja"]:.2f}L")
                     print(f"São necessários 8.00 L de água /m², totalizando: \n {dados_soja["ir_fase2_diária_total_soja"]:.2f} L de água diário \n {dados_soja["ir_fase2_semanal_total_soja"]:.2f} L de água semanal \n {dados_soja["ir_fase2_mes_total_soja"]:.2f} L de água mensal \n {dados_soja["ir_fase2_total_soja"]:.2f} L de água duarante  a fase 2 ( 2 meses)")
                     print(f"Em um ciclo completo será utilizado {dados_soja["ir_Ciclo_Completo_soja"]:.2f} L de água")   
                     #---------- Médias (R) -----------
                     # Vetor com os dados da aplicações de inseticida:
                     inseticida_soja = r.c(dados_soja["inseticida_aplicacao1_soja"], dados_soja["inseticida_aplicacao2_soja"])
                     # Calculando média, mediana e desvio padrão:
                     media_inseticida_soja = r.mean(inseticida_soja)
                     desvio_padrao_inseticida_soja = r.sd(inseticida_soja) 
                     print(f'A média de inseticida ultizada é de {media_inseticida_soja[0]} L/m², com desvio padrão de {desvio_padrao_inseticida_soja[0]:.2f} L/m²')
                     # Vetor com os dados da aplicações de fungicida:
                     fungicida_soja = r.c(dados_soja["fungicida_aplicacao1_soja"], dados_soja["fungicida_aplicacao2_soja"])
                     # Calculando média, mediana e desvio padrão:
                     media_fungicida_soja = r.mean(fungicida_soja)
                     desvio_padrao_fungicida_soja = r.sd(fungicida_soja)
                     print(f'A média de fungicida utilizada é de {media_fungicida_soja[0]} L/m², com desvio padrão de {desvio_padrao_fungicida_soja[0]:.2f} L/m²')
                     # Vetor com os dados da irrigação por fase:
                     irrigacao_soja = r.c(dados_soja["ir_fase1_total_soja"], dados_soja["ir_fase2_total_soja"])
                     # Calculando média, mediana e desvio padrão:
                     media_irrigacao_soja = r.mean(irrigacao_soja)
                     desvio_padrao_irrigacao_soja = r.sd(irrigacao_soja)
                     print(f'A média de água utilizada é de {media_irrigacao_soja[0]:.2f} L, com desvio padrão de {desvio_padrao_irrigacao_soja[0]:.2f} L')
                    elif op == 2:
                         #------------------------------------------------------------- Cultura - tomate -------------------------------------------------------------  
                         # A cultura do tomate é dividida em duas fases, cada uma com duração de 4 meses
                         #----------Definir Funções Específicas----------
                         #---Irrigação1 (8.00L de água por m²)---
                         def irrigação1_diaria_total_tomate(at: float) -> float:
                              return at * 8.00
                         #---Irrigação2 (7.50L de água por m²)---
                         def irrigação2_diaria_total_tomate(at: float) -> float:
                              return at * 7.00
                         #---Número de hortaliças Total (4 kg por muda de tomate)---
                         def nhortalicas_total_tomate(at: float) -> float:
                              return 4 * ((at / 4) * 6)
                         #----------Código Principal----------
                         #---------- Fase1----------
                         dados_tomate = {}
                         print("Um ciclo completo de tomate dura 180 dias, ou seja, 6 meses")
                         print("A cultura do tomate é dividida em duas fases, cada uma com duração de 3 meses")
                         print("A plantação possuirá ruas com espaçamento de 1 m entre as ruas, e as mudas devem ser plantadas com espaçamento de 1 m entre elas")
                         # criando variáveis para as funções para que possam ser vetorizadas
                         dados_tomate["area_total_tomate"] = float(input("Área disponível para plantação em m²: "))
                         # Calculando e armazenando os resultados no dicionário
                         # Informações Básicas----------------------------------------------------------------------------------------
                         dados_tomate["area_util_tomate"] = area_util(dados_tomate["area_total_tomate"])  
                         dados_tomate["numero_mudas_total_tomate"] = num_mudas_total(dados_tomate["area_total_tomate"], 2)  # 2 mudas por m²
                         dados_tomate["num_ruas_tomate"] = numero_ruas_total(dados_tomate["area_total_tomate"])
                         dados_tomate["numero_hortalicas_total_tomate"] = nhortalicas_total_tomate(dados_tomate["area_total_tomate"]) 
                          # Insumos--------------------------------------------------------------------------------------------------------
                         dados_tomate["calcio_fase1_total_tomate"] = calcio_total(dados_tomate["area_total_tomate"])
                         dados_tomate["npk_fase1_tomate"] = adubo_NPK(dados_tomate["area_total_tomate"])
                         dados_tomate["inseticida_aplicacao1_tomate"] = inseticida1(dados_tomate["area_total_tomate"])
                         dados_tomate["fungicida_aplicacao1_tomate"] = fungicida1(dados_tomate["area_total_tomate"])
                         dados_tomate["ir_fase1_diária_total_tomate"] = irrigação1_diaria_total_tomate(dados_tomate["area_total_tomate"])
                         dados_tomate["ir_fase1_semanal_total_tomate"] = dados_tomate["ir_fase1_diária_total_tomate"] * 7
                         dados_tomate["ir_fase1_mes_total_tomate"] = dados_tomate["ir_fase1_semanal_total_tomate"] * 4
                         dados_tomate["ir_fase1_total_tomate"] = dados_tomate["ir_fase1_mes_total_tomate"] * 3  # fase 1 dura 3 meses 
                         # Prints Informações Básicas + Insumos----------------------------------------------------------------------------------------------------------------------------------
                         print("----------Informações Básicas----------")
                         print(f"A área útil é de: {dados_tomate['area_util_tomate']:.2f} m²")
                         print(f"O número total de mudas a serem plantadas é de {dados_tomate['numero_mudas_total_tomate']:.1f} mudas")
                         print(f"A plantação terá {dados_tomate['num_ruas_tomate']:.1f} ruas")
                         print(f"A quantidade de tomate obtida após um ciclo completo é de {dados_tomate['numero_hortalicas_total_tomate']:.2f} kg")
                         print("-----------Insumos 1°Fase----------")
                         print(f"O cálcio deve ser aplicado 1 vez, sendo necessário aplicar 0.7 toneladas de cálcio por hectare, totalizando {dados_tomate['calcio_fase1_total_tomate']:.2f} toneladas de cálcio")
                         print(f"O Adubo deve ser aplicado 1 vez, sendo necessário aplicar 0.85 kg de Adubo(NPK) por m², totalizando {dados_tomate['npk_fase1_tomate']:.2f} kg de NPK")
                         print(f"OInseticida é dividido em 2 aplicações, sendo uma aplicação para cada fase")
                         print(f"Na 1ª Aplicação do Inseticida são necessários 2.75 L/m², totalizando {dados_tomate['inseticida_aplicacao1_tomate']:.2f} L")
                         print(f"O Fungicida é dividido em 2 aplicações, sendo uma aplicação para cada fase")
                         print(f"Na 1ª Aplicação do fungicida são necessários 2.50 L/m², totalizando {dados_tomate['fungicida_aplicacao1_tomate']:.2f} L")
                         print(f"São necessários 9.00 L de água /m², totalizando: \n {dados_tomate['ir_fase1_diária_total_tomate']:.2f} L de água diário \n {dados_tomate['ir_fase1_semanal_total_tomate']:.2f} L de água semanal \n {dados_tomate['ir_fase1_mes_total_tomate']:.2f} L de água mensal \n {dados_tomate['ir_fase1_total_tomate']:.2f} L de água durante toda a fase 1 (3 meses)")
                         #---------- Fase2----------  
                         dados_tomate["calcio_fase2_total_tomate"] = calcio_total(dados_tomate["area_total_tomate"])
                         dados_tomate["npk_fase2_tomate"] = adubo_NPK(dados_tomate["area_total_tomate"])
                         dados_tomate["inseticida_aplicacao2_tomate"] = inseticida2(dados_tomate["area_total_tomate"])
                         dados_tomate["fungicida_aplicacao2_tomate"] = fungicida2(dados_tomate["area_total_tomate"])
                         dados_tomate["ir_fase2_diária_total_tomate"] = irrigação2_diaria_total_tomate(dados_tomate["area_total_tomate"])
                         dados_tomate["ir_fase2_semanal_total_tomate"] = dados_tomate["ir_fase2_diária_total_tomate"] * 7
                         dados_tomate["ir_fase2_mes_total_tomate"] = dados_tomate["ir_fase2_semanal_total_tomate"] * 4
                         dados_tomate["ir_fase2_total_tomate"] = dados_tomate["ir_fase2_mes_total_tomate"] * 4  # fase 2 dura 4 meses  
                         dados_tomate["ir_Ciclo_Completo_tomate"] = dados_tomate["ir_fase2_total_tomate"] + dados_tomate["ir_fase1_total_tomate"]
                         # Prints Informações Básicas + Insumos----------------------------------------------------------------------------------------------------------------------------------
                         print("-----------Insumos 2°Fase----------")
                         print(f"O cálcio deve ser aplicado 1 vez, sendo necessário aplicar 0.7 toneladas de cálcio por hectare, totalizando {dados_tomate['calcio_fase2_total_tomate']:.2f} toneladas de cálcio")
                         print(f"O Adubo deve ser aplicado 1 vez, sendo necessário aplicar 0.85 kg de Adubo(NPK) por m², totalizando {dados_tomate['npk_fase2_tomate']:.2f} kg de NPK")
                         print(f"Na 2ª Aplicação do Inseticida são necessários 1.50 L/m², totalizando {dados_tomate['inseticida_aplicacao2_tomate']:.2f} L")
                         print(f"Na 2ª Aplicação do fungicida são necessários 1.75 L/m², totalizando {dados_tomate['fungicida_aplicacao2_tomate']:.2f} L")
                         print(f"São necessários 7.00 L de água /m², totalizando: \n {dados_tomate['ir_fase2_diária_total_tomate']:.2f} L de água diário \n {dados_tomate['ir_fase2_semanal_total_tomate']:.2f} L de água semanal \n {dados_tomate['ir_fase2_mes_total_tomate']:.2f} L de água mensal \n {dados_tomate['ir_fase2_total_tomate']:.2f} L de água durante a fase 2 (4 meses)")
                         print(f"Em um ciclo completo será utilizado {dados_tomate['ir_Ciclo_Completo_tomate']:.2f} L de água")  
                         #---------- Médias (R) ----------
                         # Vetor com os dados da aplicações de inseticida:
                         inseticida_tomate = r.c(dados_tomate["inseticida_aplicacao1_tomate"], dados_tomate["inseticida_aplicacao2_tomate"])
                         # Calculando média, mediana e desvio padrão:
                         media_inseticida_tomate = r.mean(inseticida_tomate)
                         desvio_padrao_inseticida_tomate = r.sd(inseticida_tomate) 
                         print(f'A média de inseticida ultizada é de {media_inseticida_tomate[0]} L/m², com desvio padrão de {desvio_padrao_inseticida_tomate[0]:.2f} L/m²')
                         # Vetor com os dados da aplicações de fungicida:
                         fungicida_tomate = r.c(dados_tomate["fungicida_aplicacao1_tomate"], dados_tomate["fungicida_aplicacao2_tomate"])
                         # Calculando média, mediana e desvio padrão:
                         media_fungicida_tomate = r.mean(fungicida_tomate)
                         desvio_padrao_fungicida_tomate = r.sd(fungicida_tomate)
                         print(f'A média de fungicida utilizada é de {media_fungicida_tomate[0]} L/m², com desvio padrão de {desvio_padrao_fungicida_tomate[0]:.2f} L/m²')
                         # Vetor com os dados da irrigação por fase:
                         irrigacao_tomate = r.c(dados_tomate["ir_fase1_total_tomate"], dados_tomate["ir_fase2_total_tomate"])
                         # Calculando média, mediana e desvio padrão:
                         media_irrigacao_tomate = r.mean(irrigacao_tomate)
                         desvio_padrao_irrigacao_tomate = r.sd(irrigacao_tomate)
                         print(f'A média de água utilizada é de {media_irrigacao_tomate[0]:.2f} L, com desvio padrão de {desvio_padrao_irrigacao_tomate[0]:.2f} L')
                    elif op == 3:
                        #---------------------------------------------------------------------Cultura - laranja---------------------------------------------------------------------
                        # A cultura de laranja é dividida em duas fases cada uma com duração de 4 meses
                        #----------Definir Funções Específicas----------
                        #---Irrigação1 (9.00L de água por m²)---
                        def irrigação1_diaria_total_laranaja(at:float) -> float:
                            return at * 9.00
                        #---Irrigação2 (7.50L de água por m²)---
                        def irrigação2_diaria_total_laranja(at:float) -> float:
                            return at * 7.00
                        #---Número de hortaliças Total (4 kg por muda de laranja)
                        def nhortalicas_total_laranja (at:float) -> float:
                            return 4.5 * ((at/4) *4)
                        #----------Código Principal----------
                        #---------- Fase1----------
                        dados_laranja = {}
                        print("Um ciclo completo de laranja dura 180 dias, ou seja, 6 meses")
                        print("A cultura da laranaja é dividida em duas fases, cada uma com duração de 3 meses")
                        print("A plantação possuirá ruas com espaçamento de 1 m entre as ruas, e as mudas devem ser plantadas com espaçamento de 1 m entre elas")
                        # criando variáveis para as funções para que possam ser vetorizadas
                        dados_laranja["area_total_laranja"] = float(input("Área disponível para plantação em m²: "))
                        # Calculando e armazenando os resultados no dicionário
                        # # Informações Básicas----------------------------------------------------------------------------------------
                        dados_laranja["area_util_laranja"] = area_util(dados_laranja["area_total_laranja"])  
                        dados_laranja["numero_mudas_total_laranja"] = num_mudas_total(dados_laranja["area_total_laranja"], 2)  # 2 mudas por m²
                        dados_laranja["num_ruas_mandioca"] = numero_ruas_total(dados_laranja["area_total_laranja"])
                        dados_laranja["numero_hortalicas_total_laranja"] = nhortalicas_total_laranja(dados_laranja["area_total_laranja"])
                        # Insumos--------------------------------------------------------------------------------------------------------
                        dados_laranja["calcio_fase1_total_laranja"] = calcio_total(dados_laranja["area_total_laranja"])
                        dados_laranja["npk_fase1_laranja"] = adubo_NPK(dados_laranja["area_total_laranja"])
                        dados_laranja["inseticida_aplicacao1_laranja"] = inseticida1(dados_laranja["area_total_laranja"])
                        dados_laranja["fungicida_aplicacao1_laranja"] = fungicida1(dados_laranja["area_total_laranja"])
                        dados_laranja["ir_fase1_diária_total_laranja"] = irrigação1_diaria_total_laranaja(dados_laranja["area_total_laranja"])
                        dados_laranja["ir_fase1_semanal_total_laranja"] = dados_laranja["ir_fase1_diária_total_laranja"] * 7
                        dados_laranja["ir_fase1_mes_total_laranja"] = dados_laranja["ir_fase1_semanal_total_laranja"] * 4
                        dados_laranja["ir_fase1_total_laranja"] = dados_laranja["ir_fase1_mes_total_mandioca"] * 3 # fase 1 dura 3 meses
                        # Prints Informações Básicas + Insumos----------------------------------------------------------------------------------------------------------------------------------
                        print("----------Informações Básicas----------")
                        print(f"A área útil é de: {dados_laranja['area_util_mandioca']:.2f} m²")
                        print(f"O número total de mudas a serem plantadas é de {dados_laranja['numero_mudas_total_laranja']:.1f} mudas")
                        print(f"A plantação terá {dados_laranja['num_ruas_mandioca']:.1f} ruas")
                        print(f"A quantidade de laranja obtida após um ciclo completo é de {dados_laranja['numero_hortalicas_total_laranja']:.2f} kg")
                        print("-----------Insumos 1°Fase----------")
                        print(f"O cálcio deve ser aplicado 1 vez, sendo necessário aplicar 0.7 toneladas de cálcio por hectare, totalizando {dados_laranja['calcio_fase1_total_mandioca']:.2f} toneladas de cálcio")
                        print(f"O Adubo deve ser aplicado 1 vez, sendo necessário aplicar 0.85 kg de Adubo(NPK) por m², totalizando {dados_laranja['npk_fase1_laranja']:.2f} kg de NPK")
                        print(f"O Inseticida é dividido em 2 aplicações, sendo uma aplicação para cada fase")
                        print(f"Na 1ª Aplicação do Inseticida são necessários 2.75 L/m², totalizando {dados_laranja['inseticida_aplicacao1_laranja']:.2f} L")
                        print(f"O Fungicida é dividido em 2 aplicações, sendo uma aplicação para cada fase")
                        print(f"Na 1ª Aplicação do fungicida são necessários 2.50 L/m², totalizando {dados_laranja['fungicida_aplicacao1_laranja']:.2f} L")
                        print(f"São necessários 9.00 L de água /m², totalizando: \n {dados_laranja['ir_fase1_diária_total_laranja']:.2f} L de água diário \n {dados_laranja['ir_fase1_semanal_total_mandioca']:.2f} L de água semanal \n {dados_mandioca['ir_fase1_mes_total_mandioca']:.2f} L de água mensal \n {dados_mandioca['ir_fase1_total_mandioca']:.2f} L de água durante toda a fase 1 (3 meses)")
                        #---------- Fase2----------  
                        dados_laranja["calcio_fase2_total_laranja"] = calcio_total(dados_laranja["area_total_laranja"])
                        dados_laranja["npk_fase2_laranja"] = adubo_NPK(dados_laranja["area_total_laranja"])
                        dados_laranja["inseticida_aplicacao2_laranja"] = inseticida2(dados_laranja["area_total_laranja"])
                        dados_laranja["fungicida_aplicacao2_"] = fungicida2(dados_laranja["area_total_laranja"])
                        dados_laranja["ir_fase2_diária_total_laranja"] = irrigação2_diaria_total_laranja(dados_laranja["area_total_laranja"])
                        dados_laranja["ir_fase2_semanal_total_laranja"] = dados_laranja["ir_fase2_diária_total_laranja"] * 7
                        dados_laranja["ir_fase2_mes_total_laranja"] = dados_laranja["ir_fase2_semanal_total_laranja"] * 4
                        dados_laranja["ir_fase2_total_laranja"] = dados_laranja["ir_fase2_mes_total_laranja"] * 4 # fase 2 dura 4 meses  
                        dados_laranja["ir_Ciclo_Completo_laranja"] = dados_laranja["ir_fase2_total_laranja"] + dados_laranja["ir_fase1_total_laranja"]
                        # Prints Informações Básicas + Insumos----------------------------------------------------------------------------------------------------------------------------------
                        print("-----------Insumos 2°Fase----------")
                        print(f"O cálcio deve ser aplicado 1 vez, sendo necessário aplicar 0.7 toneladas de cálcio por hectare, totalizando {dados_laranja['calcio_fase2_total_laranja']:.2f} toneladas de cálcio")
                        print(f"O Adubo deve ser aplicado 1 vez, sendo necessário aplicar 0.85 kg de Adubo(NPK) por m², totalizando {dados_laranja['npk_fase2_laranja']:.2f} kg de NPK")
                        print(f"Na 2ª Aplicação do Inseticida são necessários 1.50 L/m², totalizando {dados_laranja['inseticida_aplicacao2_laranja']:.2f} L")
                        print(f"Na 2ª Aplicação do fungicida são necessários 1.75 L/m², totalizando {dados_laranja['fungicida_aplicacao2_laranja']:.2f} L")
                        print(f"São necessários 7.00 L de água /m², totalizando: \n {dados_laranja['ir_fase2_diária_total_laranja']:.2f} L de água diário \n {dados_laranja['ir_fase2_semanal_total_mandioca']:.2f} L de água semanal \n {dados_mandioca['ir_fase2_mes_total_mandioca']:.2f} L de água mensal \n {dados_mandioca['ir_fase2_total_mandioca']:.2f} L de água durante a fase 2 (3 meses)")
                        print(f"Em um ciclo completo será utilizado {dados_laranja['ir_Ciclo_Completo_laranja']:.2f} L de água")  
                        #---------- Médias (R) -----------
                        # Vetor com os dados da aplicações de inseticida:
                        inseticida_laranja = r.c(dados_laranja["inseticida_aplicacao1_laranja"], dados_laranja["inseticida_aplicacao2_laranja"])
                        # Calculando média, mediana e desvio padrão:
                        media_inseticida_laranja = r.mean(inseticida_laranja)
                        desvio_padrao_inseticida_laranja = r.sd(inseticida_laranja) 
                        print(f'A média de inseticida ultizada é de {media_inseticida_laranja[0]} L/m², com desvio padrão de {desvio_padrao_inseticida_laranja[0]:.2f} L/m²')
                        # Vetor com os dados da aplicações de fungicida:
                        fungicida_laranja = r.c(dados_laranja["fungicida_aplicacao1_laranja"], dados_laranja["fungicida_aplicacao2_laranja"])
                        # Calculando média, mediana e desvio padrão:
                        media_fungicida_laranja = r.mean(fungicida_laranja)
                        desvio_padrao_fungicida_laranja = r.sd(fungicida_laranja)
                        print(f'A média de fungicida utilizada é de {media_fungicida_laranja[0]} L/m², com desvio padrão de {desvio_padrao_fungicida_laranja[0]:.2f} L/m²')
                        # Vetor com os dados da irrigação por fase:
                        irrigacao_laranja = r.c(dados_laranja["ir_fase1_total_laranja"], dados_laranja["ir_fase2_total_laranja"])
                        # Calculando média, mediana e desvio padrão:
                        media_irrigacao_laranja = r.mean(irrigacao_laranja)
                        desvio_padrao_irrigacao_laranja = r.sd(irrigacao_laranja)
                        print(f'A média de água utilizada é de {media_irrigacao_laranja[0]:.2f} L, com desvio padrão de {desvio_padrao_irrigacao_laranja[0]:.2f} L')
                    elif op == 4: 
                        print("Voltando ao menu anterior")
                        break
                    else:
                        print("Opção incorreta,tente novamente")
            elif op == 6:
               print("voltando ao menu principal")
               break
            else:
                print("Opção invalida, tente novamnete")
    elif op == 3:
        dados_conexao = (
            "Driver={SQL Server};"
            "Server=DESKTOP-FQOLT90;"
            "Database=DadosRegiao;"
        )
        conexao = pyodbc.connect(dados_conexao)
        print('Conexao Bem Sucedida')

        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM dadosagro ")

        rows = cursor.fetchall()

        for row in rows:
            print(row.nome, row.clima, row.solo, row.cultura)

    elif op == 4:
        # Supondo que o arquivo 'meus_dados.txt' esteja na mesma pasta que o script

        with open('Melhorias.txt', 'r') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
    elif op == 5:
        print("Obrigado por utilizar o programa, espero que tenham gostado")
        break
    else:
        print("Opção invalida, tente novamente")

