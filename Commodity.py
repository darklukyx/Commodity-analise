import csv

dados_paises = {}
def carregar_dados_do_csv(value_of_imports): #Busca dados arquivo
    with open(value_of_imports, encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        cabecalho = next(leitor)

        for linha in leitor:
            pais = linha[5]
            commodity = linha[7]
            try:
                valor = float(linha[-1])
            except ValueError:
                continue

            if pais not in dados_paises:
                dados_paises[pais] = {
                    "valor_total": 0,
                    "commodities": []
                }

            dados_paises[pais]["valor_total"] += valor
            if commodity not in dados_paises[pais]["commodities"]:
                dados_paises[pais]["commodities"].append(commodity)

    return dados_paises
##############################################################################################
def busca_dado(pais): 
    total = dados_paises[pais]["valor_total"] # tq[0]
    quantidade = len(dados_paises[pais]["commodities"]) #tq[1]
    tq = total, quantidade
    return tq

################################################################################################
# ver lista de commodities
def ver_lista_commodities():
    print("Alimentos & Bebidas")
    print("--------------------------------------------------")
    print("Animais vivos (exceto peixes) - Live animals except fish etc. (00)")
    print("Carnes e preparados de carne - Meat and meat preparations (01)")
    print("Laticínios e ovos - Dairy products and birds eggs (02)")
    print("Peixes, crustáceos e moluscos - Fish, crustaceans, molluscs and preparations thereof (03)")
    print("Cereais e derivados - Cereals and cereal preparations (04)")
    print("Vegetais e frutas - Vegetables and fruit (05)")
    print("Açúcar e mel - Sugar, sugar preparations and honey (06)")
    print("Café, chá, cacau e especiarias - Coffee, tea, cocoa, spices and manufactures thereof (07)")
    print("Rações animais - Feeding stuffs for animals, excluding unmilled cereals (08)")
    print("Produtos alimentícios diversos - Miscellaneous edible products and preparations (09)")
    print("Bebidas - Beverages (11)")
    print("Tabaco e derivados - Tobacco and tobacco manufactures (12)")
    print("--------------------------------------------------")
    print("Energia & Minerais")
    print("---------------------------------------------------")
    print("Peles e couros brutos - Hides, skins and furskins, raw (21)")
    print("Oleaginosas (soja, girassol) - Oilseeds and oleaginous fruit (22)")
    print("Borracha natural/sintética - Crude rubber, including synthetic and reclaimed rubber (23)")
    print("Cortiça e madeira - Cork and wood (24)")
    print("Celulose e papel reciclado - Pulp and waste paper (25)")
    print("Fibras têxteis - Textile fibres, excluding wool tops, and their wastes (26)")
    print("Fertilizantes brutos - Crude fertilisers and minerals, excluding coal, petroleum etc. (27)")
    print("Minérios metálicos (ferro, cobre) - Metalliferous ores and metal scrap (28)")
    print("Matérias-primas animais/vegetais - Crude animal and vegetable materials, n.e.s. (29)")
    print("Carvão e coque - Coal, coke and briquettes (32)")
    print("Petróleo e derivados - Petroleum, petroleum products and related materials (33)")
    print("Gás natural - Gas, natural and manufactured (34)")
    print("Energia elétrica - Electric current (35)")
    print("---------------------------------------------------")
    print("Químicos & Industriais")
    print("---------------------------------------------------")
    print("Óleos animais - Animal oils and fats (41)")
    print("Óleos vegetais - Fixed vegetable oils and fats (42)")
    print("Gorduras e ceras processadas - Animal and vegetable oils and fats, processed, and waxes (43)")
    print("Químicos orgânicos - Organic chemicals (51)")
    print("Químicos inorgânicos - Inorganic chemicals (52)")
    print("Corantes e taninos - Dyeing, tanning and colouring materials (53)")
    print("Produtos farmacêuticos - Medicinal and pharmaceutical products (54)")
    print("Perfumes e óleos essenciais - Essential oils, perfume materials, toilet preparations etc. (55)")
    print("Fertilizantes industrializados - Fertilisers, manufactured (56)")
    print("Plásticos primários - Plastics in primary forms (57)")
    print("Plásticos não-primários - Plastics in non-primary forms (58)")
    print("Produtos químicos diversos - Chemical materials and products, n.e.s. (59)")
    print("---------------------------------------------------")
    print("Manufaturados")
    print("---------------------------------------------------")
    print("Couro e artigos de couro - Leather, leather manufactures and dressed furskins (61)")
    print("Artigos de borracha - Rubber manufactures, n.e.s. (62)")
    print("Produtos de madeira (exceto móveis) - Cork and wood manufactures, excluding furniture (63)")
    print("Papel e derivados - Paper, paperboard and articles of paper pulp, paper etc. (64)")
    print("Fios e tecidos - Textile yarn, fabrics, made-up articles and related products (65)")
    print("Produtos minerais não-metálicos - Non-metallic mineral manufactures, n.e.s. (66)")
    print("Ferro e aço - Iron and steel (67)")
    print("Metais não-ferrosos (ouro, cobre) - Non-ferrous metals (68)")
    print("Artigos de metal diversos - Manufactures of metal, n.e.s. (69)")
    print("---------------------------------------------------")
    print("Máquinas & Equipamentos")
    print("---------------------------------------------------")
    print("Geradores de energia - Power generating machinery and equipment (71)")
    print("Máquinas industriais especializadas - Machinery specialised for particular industries (72)")
    print("Máquinas para metalurgia - Metalworking machinery (73)")
    print("Maquinário industrial geral - General industrial machinery and parts, n.e.s. (74)")
    print("Equipamentos de escritório - Office machines and automatic data processing equipment (75)")
    print("Telecomunicações - Telecommunications and sound recording, reproducing equipment (76)")
    print("Eletrodomésticos e equipamentos elétricos - Electrical machinery, appliances etc., n.e.s. (77)")
    print("Veículos automotores - Road vehicles (78)")
    print("Outros equipamentos de transporte - Other transport equipment (79)")
    print('---------------------------------------------------')
    print("Bens de Consumo")
    print("---------------------------------------------------")
    print("Construções pré-fabricadas - Prefab buildings; plumbing and electrical fixtures and fittings (81)")
    print("Móveis e partes - Furniture and parts thereof (82)")
    print("Malas e bolsas - Travel goods, handbags and similar containers (83)")
    print("Vestuário e acessórios - Articles of apparel and clothing accessories (84)")
    print("Calçados - Footwear (85)")
    print("Instrumentos científicos - Professional, scientific and controlling apparatus (87)")
    print("Câmeras e relógios - Photographic apparatus, optical goods, watches and clocks (88)")
    print("Artigos manufaturados diversos - Miscellaneous manufactured articles, n.e.s. (89)")
    print("---------------------------------------------------")
    print("Outros")
    print("----------------------------------------------------")
    print("Commodities não especificadas - Commodities and transactions n.e.s. (9)")
    print("Estimativas não classificadas - Unclassified estimates")
################################################################################################
def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Ver ranking dos países")
        print("2. Buscar um país")
        print("3. Ver lista de commodity")
        print("4. Ver países por commodity")
        print("5. Recomendação")
        print("6. Sair")
        opcao = input("Escolha uma opção (1 a 6): ")

        if opcao == "1":
            exibir_ranking()
        elif opcao == "2":
            nome = input("Digite o nome do país: ")
            buscar_pais( nome)
        elif opcao == "3":
            print("\nLista de commodities disponíveis:")
            ver_lista_commodities()
        elif opcao == "4":
            commodity = input("Digite o nome da commodity e o número Ex:Footwear (85): ")
            listar_paises_por_commodity(commodity)
        elif opcao == "5":
            perfil= definir_perfil()
            recomendar_comodities(perfil)
        elif opcao == "6":
            print("OK, programa sera encerrado ")
            break
        else:
            print("Opção inválida! Tente novamente.")

##################################################################################################

def exibir_ranking(top=10): #opição 1 que mostra o top 10
    ranking = [] #crio  a lista que vai mostrar o rank
    for pais in dados_paises: 
        tq = busca_dado(pais)
        ranking.append((pais,tq[0],tq[1]))

    # ordena com dois for (sem usar sort)
    for i in range(len(ranking)):
        for j in range(i + 1, len(ranking)):
            if ranking[j][1] > ranking[i][1]:
                ranking[i], ranking[j] = ranking[j], ranking[i]

    print(f"Top {top} países por valor total de importações:")
    for i in range(top):
        pais, valor, qtd = ranking[i]
        print(f"{i+1}. {pais} - €{valor:,.2f} mil euros - {qtd} tipos de commodities")
# fim  do codigo do rank#
#####################################################################################################
# opção dois :  buscar paises
def buscar_pais( pais):
    if pais in dados_paises:
        tq = busca_dado(pais)
        print(f"\nDados do país: {pais}")
        print(f"Valor total importado: €{tq[0]:,.2f} mil euros")
        print(f"Tipos de commodities importadas: {tq[1]}")
        print("Lista de commodities:")
        for c in dados_paises[pais]["commodities"]:
            print(f"- {c}")
    else:
        print("País não encontrado.")
 # fim da opção dois       
#######################################################################################################        
# commodity      
def listar_paises_por_commodity(nome_commodity):
    print(f"\nPaíses que importam a commodity '{nome_commodity}':")
    encontrou = False
    for pais in dados_paises:
        if nome_commodity in dados_paises[pais]["commodities"]:
            print(f"- {pais}")
            encontrou = True
    if not encontrou:
        print("Nenhum país encontrado com essa commodity.")
########################################################################################################
def definir_perfil():
    pontos = 0
    r1=  r2 = r3 = 0 
    
    print("\nResponda com 's' para sim e 'n' para não:")
    while r1 != 's'  and r1 != 'n' :
      r1 = input("Você prefere segurança a retorno alto? (s/n): ").lower()
      if r1 == 's':
       pontos += 1
     
    while r2 != 's'  and r2 != 'n' :
     r2 = input("Você aceitaria ver seu investimento oscilar para ganhar mais? (s/n): ").lower()
    
     if r2 == 'n':
        pontos += 1
    
    while r3 != 's'  and r3 !='n' :
     r3 = input("Você prefere diversificar para não perder tudo de uma vez? (s/n): ").lower()
     if r3 == 's':
        pontos += 1
   
 
    # Define o perfil com base na pontuação
    if pontos >= 2:
        perfil = "Conservador"
    elif pontos == 1:
        perfil = "Moderado"
    else:
        perfil = "Ousado"

    print(f"\nSeu perfil de investidor é: {perfil}")
    return perfil
#####################################################################################################
def recomendar_comodities(perfil):
    print("\nRecomendações de commodities para seu perfil:")

    if perfil == "Conservador":
        print("- Ouro")
        print("- Alimentos básicos")
        print("- Energia (petróleo estável)")
    elif perfil == "Moderado":
        print("- Soja")
        print("- Minério de ferro")
        print("- Gás natural")
    elif perfil == "Ousado":
        print("- Petróleo")
        print("- Metais raros")
        print("- Commodities com variação cambial")
################################################################################################################
carregar_dados_do_csv("value_of_imports.csv")
menu()