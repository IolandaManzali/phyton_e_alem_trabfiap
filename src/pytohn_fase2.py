while True:
    print("------------Menu Príncipal------------")
    print(" 1. Informações Cadastrais \n 2. Plano de Cultura \n 3. Infromações Sobre, Clima, Solo, Pragas e Agricultura \n 4. Sugestões de Melhorias \n 5. API Meterológica \n 6. Sair")
    op = int(input("Digite o número referente a opção de sua escolha:"))
    if op == 1:
        while True:
            print("-----Menu Cadastral-----")
            print(" 1. Efetuar cadastro \n 2. Voltar ao menu rpincipal")
            op = int(input("Digite o número referente a opção de sua escolha:"))
            if op == 1:
                # 1° Vetorizar as variveis para que os dados cadastrais sejam aramzenados
               
                # 2° Pesso as informações e armazeno-as
                nome = input("Digite seu nome completo:")
                email = input("Digite seu email:")
                car = input("Digite seu car:")# o que é o car e ele é numero o texto
                #mereamnete para provar o armazenamneto
                print("Cadastro realizado com sucesso!")
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
            #---------Definido e Codando os Subalgoritmos--------
            #---Área Util
            # At -> area total
            # Re -> relação entre as ruas e o espaçamento entre mudas
            def area_util(at:float, re:float )-> float:
                return at/re
            #---Calcio
            def calcio_total(at:float)-> float:
                def calcio_por_hectar(v1:float, v2:float, t:float, prnt:float)-> float:
                    #v1, v2 e Prnt -> porcentagem
                    v1 = 0.5  
                    v2 = 0.75  
                    t= 50
                    prnt = 0.7
                    return ((v2 - v1) * t / prnt)
                return (at/10000) * calcio_por_hectar
            #---NPK  -> 1.25kg a cada 10m²
            def adubo_NPK(at:float) ->float:
                return (at/10)*1.25
            #---Inseticida Aplicação 1 - 2.75/m²
            def inseticida(at:float) -> float:
                return at * 2.75
            #---Inseticida Aplicação 2 - 1.50/m²
            def inseticida(at:float) -> float:
                return at * 1.50
            #---Fungicida Aplicação 1 - 2.50/m²
            def inseticida(at:float) -> float:
                return at * 2.50
            #---Fungicida Aplicação 2 - 1.75/m²
            def inseticida(at:float) -> float:
                return at * 1.75
            def num_ruas(at:float) -> float:
                return (at/10000) * 50
            def irrigação_diaria_total(at:float, quantide_agua_metroquadrado: float)-> float:
                return at * quantide_agua_metroquadrado
            def num_mudadas_total(at:float, n_mudas_Mquadrado:float)-> float:
                return at * n_mudas_Mquadrado
           
            if op == 1:
                #----- Região Sul -----
                while True:
                    print("------Culturas------")
                    print(" 1. Trigo (grão) \n 2. Bata (hortaliça) \n 3. Maçã (fruta) \n 4 Voltar")
                    op = int(input("Digite o número referente a  opção que deseja plantar: "))    
                    if op == 1:
                        #-----Subalgoritmos Expecíficos do Trigo
                        def irrigação1(at:float)-> float:
                            return at * 9.0
                        def irrigação2(at:float)-> float:
                            return at * 7.50                
                        print("Um cilco completo do Trigo duara 120 dia, ou seja, 4 mêses")
                        print("Aplantação posuirá ruas a cada 1m e ")
                        areat_total = float(input("Área disponível para plnatação em m²: "))
                        area_ut = area_util(areat_total,4)
                        numero_mudas = (num_mudadas_total())
                       
                    elif op == 2:
                        print("oi")
                    elif op == 3:
                        print("oi")
                    elif op == 4:
                        print("Voltando ao menu anterior")
                        break
                    else:
                        print("Opção Invalida, escolha novamente")
            elif op == 2:
                #----- Região Suldeste -----
                while True:
                    print("------Culturas------")
                    print(" 1. Arroz (grão) \n 2. Alface (hortaliça) \n 3. Banana (fruta) \n 4 Voltar")
                    op = int(input("Digite o número referente a  opção que deseja plantar: "))    
                    if op == 1:
                        print("oi")
                        #vetorização
                    elif op == 2:
                        print("oi")
                    elif op == 3:
                        print("oi")
                    elif op == 4:
                        print("Voltando ao menu anterior")
                        break
                    else:
                        print("Opção Invalida, escolha novamente")
            elif op == 3:
                #----- Região Norte -----
                while True:
                    print("------Culturas------")
                    print(" 1. Milho (grão) \n 2. Batata Doce (hortaliça) \n 3. Açaí (fruta) \n 4 Voltar")
                    op = int(input("Digite o número referente a  opção que deseja plantar: "))    
                    if op == 1:
                        print("oi")
                    elif op == 2:
                        print("oi")
                    elif op == 3:
                        print("oi")
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
                        print("oi")
                    elif op == 2:
                        print("oi")
                    elif op == 3:
                        print("oi")
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
                        print("oi")
                    elif op == 2:
                        print("oi")
                    elif op == 3:
                        print("oi")
                    elif op == 4:
                        print("Voltando ao menu anterior")
                        break
            elif op == 6:
                print("Volatndo ao menu principal")
                break
            else:
                print("Opção Invalida, escolha novamente")    
               
    elif op == 3:
        print("oi")
    elif op == 4:
        print("oi")
    elif op == 5:
        print("oi")
    elif op == 6:
       print("Obrigado por utilizar nosso sistema!")
       break
    else:1
