
def adicionar_nos(G):

    G.add_node("Jogo Base", tipo="base")
    #Vértice central, jogo base
    G.nodes["Jogo Base"].update({
        "mundos": ["Willow Creek", "Oasis Springs", "Newcrest"],
        "trouxe_mundo": True,
        "itens_no_CAS": 315,
        "itens_modo_construcao": 232,
        "trouxe_oculto": True,
        "oculto": "PlantaSim",
        "mecanicas": [
            "Sistema de Idades",
            "Necessidades",
            "Relacionamentos",
            "Aspirações",
            "Empregos Básicos",
            "Construção de Lotes",
            "Multitarefa",
            "Traços de Personalidade"
        ]
    })


    #Expansões
    expansoes = {
        "Natureza Encantada": {
            "trouxe_mundo": True,
            "mundo": "Everdew",
            "itens_no_CAS": 181,
            "itens_modo_construcao": 163,
            "trouxe_oculto": True,
            "oculto": "Fadas",
            "mecanicas": ["Apotécario", "Conhecimento de Fada"]
        },
        "Pé Na Cova": {
            "trouxe_mundo": True,
            "mundo": "Baía da Morte",
            "itens_no_CAS": 190,
            "itens_modo_construcao": 148,
            "trouxe_oculto": True,
            "oculto": "Ceifador",
            "mecanicas": ["Tanatologia", "Luto"]
        },
        "Ilhas Tropicais": {
            "trouxe_mundo": True,
            "mundo": "Sulani",
            "itens_no_CAS": 136,
            "itens_modo_construcao": 182,
            "trouxe_oculto": True,
            "oculto": "Sereias",
            "mecanicas": ["Canções de Sereia", "Ecologia"]
        },
        "Vida Campestre": {
            "trouxe_mundo": True,
            "mundo": "Henford-on-Bagley",
            "itens_no_CAS": 132,
            "itens_modo_construcao": 170,
            "trouxe_oculto": False,
            "oculto": None,
            "mecanicas": ["Criação de Animais", "Feiras"]
        },
        "Estações": {
            "trouxe_mundo": False,
            "mundo": None,
            "itens_no_CAS": 150,
            "itens_modo_construcao": 179,
            "trouxe_oculto": False,
            "oculto": None,
            "mecanicas": ["Clima Dinâmico", "Feriados"]
        },
        "Vampiros": {
            "trouxe_mundo": True,
            "mundo": "Forgotten Hollow",
            "itens_no_CAS": 72,
            "itens_modo_construcao": 144,
            "trouxe_oculto": True,
            "oculto": "Vampiros",
            "mecanicas": ["Sistema de Vampiro", "Árvore de Poderes"]
        },
        "LobiSims": {
            "trouxe_mundo": True,
            "mundo": "Moonwood Mill",
            "itens_no_CAS": 110,
            "itens_modo_construcao": 89,
            "trouxe_oculto": True,
            "oculto": "LobiSims",
            "mecanicas": ["Sistema de Lobisomem", "Manada"]
        },
        "Reino da Magia": {
            "trouxe_mundo": True,
            "mundo": "Glimmerbrook",
            "itens_no_CAS": 56,
            "itens_modo_construcao": 79,
            "trouxe_oculto": True,
            "oculto": "Feiticeiros",
            "mecanicas": ["Feitiçaria", "Duelos"]
        }

    }


    #Mundos
    mundos = {
        "Everdew": {
            "lotes": 9,
            "tema": "mágico",
            "expansao_origem": "Natureza Encantada"
        },
        "Baía da Morte": {
            "lotes": 6,
            "tema": "gótico",
            "expansao_origem": "Pé Na Cova"
        },
        "Sulani": {
            "lotes": 14,
            "tema": "praia",
            "expansao_origem": "Ilhas Tropicais"
        },
        "Henford-on-Bagley": {
            "lotes": 12,
            "tema": "rural",
            "expansao_origem": "Vida Campestre"
        },
        "Forgotten Hollow": {
            "lotes": 5,
            "tema": "vampírico",
            "expansao_origem": "Vampiros"
        },
        "Moonwood Mill": {
            "lotes": 6,
            "tema": "floresta/lobisomem",
            "expansao_origem": "LobiSims"
        },
        "Glimmerbrook": {
            "lotes": 13,
            "tema": "bruxos",
            "expansao_origem": "Reino da Magia"
        }
    } 


    #Mecânicas
    mecanicas = {
        "Apotecaria": {
            "descricao": "Coleta e criação de remédios naturais",
            "tipo": "magia",
            "se_e_habilidade": True,
            "habilidade": "Apotecário",
            "expansao_origem": "Natureza Encantada"
        },
        "Sistema de Luto": {
            "descricao": "Novas interações após morte de Sims",
            "tipo": "vida/morte",
            "se_e_habilidade": False,
            "habilidade": None,
            "expansao_origem": "Pé Na Cova"
        },
        "Vida Oceânica": {
            "descricao": "Sims podem nadar e interagir com o oceano",
            "tipo": "ambiental",
            "se_e_habilidade": False,
            "habilidade": None,
            "expansao_origem": "Ilhas Tropicais"
        },
        "Criação de Animais": {
            "descricao": "Cuidar de vacas, galinhas e lhamas",
            "tipo": "vida rural",
            "se_e_habilidade": True,
            "habilidade": "Criação de Animais",
            "expansao_origem": "Vida Campestre"
        },
        "Clima Dinâmico": {
            "descricao": "Sistema de estações e eventos climáticos",
            "tipo": "ambiental",
            "se_e_habilidade": False,
            "habilidade": None,
            "expansao_origem": "Estações"
        },
        "Sistema de Vampiro": {
            "descricao": "Árvore de poderes e fraquezas vampíricas",
            "tipo": "sobrenatural",
            "se_e_habilidade": True,
            "habilidade": "Vampirismo",
            "expansao_origem": "Vampiros"
        },
        "Sistema de Lobisomem": {
            "descricao": "Transformações e ciclos lunares",
            "tipo": "sobrenatural",
            "se_e_habilidade": True,
            "habilidade": "Lobisomens",
            "expansao_origem": "LobiSims"
        },
        "Feitiçaria": {
            "descricao": "Feitiços, poções e duelos",
            "tipo": "mágica",
            "se_e_habilidade": True,
            "habilidade": "Feitiçaria",
            "expansao_origem": "Reino da Magia"
        }
    }


    #Sims
    sims = {
        "Caleb Vatore": {
            "origem": "Vampiros",
            "mundo": "Forgotten Hollow",
            "mecanicas_que_pode_usar": ["Sistema de Vampiro", "Árvore de Poderes"],
            "se_e_oculto": True,
            "tipo_oculto": "Vampiros",
            "habilidades": ["Vampirismo"],
            "carreira": "Detetive",
            "relacionamentos": ["Lilith", "Vladislaus"],
            "aspiracao": "Senhor das Trevas",
            "idade": "Jovem Adulto"
        },
        "Morgyn Ember": {
            "origem": "Reino da Magia",
            "mundo": "Glimmerbrook",
            "mecanicas_que_pode_usar": ["Feitiçaria", "Duelos"],
            "se_e_oculto": True,
            "tipo_oculto": "Feiticeiro",
            "habilidades": ["Feitiçaria"],
            "carreira": "Detetive",
            "relacionamentos": ["Maga Suprema"],
            "aspiracao": "Mestre das Artes Mágicas",
            "idade": "Adulto"
        },
        "Greg": {
            "origem": "LobiSims",
            "mundo": "Moonwood Mill",
            "mecanicas_que_pode_usar": ["Sistema de Lobisomem", "Manada"],
            "se_e_oculto": True,
            "tipo_oculto": "LobiSims",
            "habilidades": ["Lobisomens"],
            "carreira": "Agricultor/Pecuarista",
            "relacionamentos": [],
            "aspiracao": "Alfa Solitário",
            "idade": "Adulto"
        },
        "Makoa Kealoha": {
            "origem": "Ilhas Tropicais",
            "mundo": "Sulani",
            "mecanicas_que_pode_usar": ["Vida Oceânica"],
            "se_e_oculto": False,
            "tipo_oculto": "Sereia",
            "habilidades": ["Natação"],
            "carreira": "Ecologista",
            "relacionamentos": ["Lilliana Kealoha"],
            "aspiracao": "Filho do Oceano",
            "idade": "Adulto"
        },
        "Bonehilda": {
            "origem": "Pé Na Cova",
            "mundo": "Baía da Morte",
            "mecanicas_que_pode_usar": ["Sistema de Luto"],
            "se_e_oculto": True,
            "tipo_oculto": "Ceifador",
            "habilidades": ["Assombração"],
            "carreira": "Agente Funerário",
            "relacionamentos": [],
            "aspiracao": "Protetora Fantasmagórica",
            "idade": "Desconhecida"
        },
        "Vladislaus": {
            "origem": "Vampiros",
            "mundo": "Forgotten Hollow",
            "mecanicas_que_pode_usar": ["Sistema de Vampiro"],
            "se_e_oculto": True,
            "tipo_oculto": "Vampiros",
            "habilidades": ["Vampirismo"],
            "carreira": "Desempregado",
            "relacionamentos": ["Caleb", "Lilith"],
            "aspiracao": "Mestre Vampiro",
            "idade": "Adulto"
        },
        "Yuki Behr": {
            "origem": "Jogo Base",
            "mundo": "Willow Creek",
            "mecanicas_que_pode_usar": [],
            "se_e_oculto": False,
            "tipo_oculto": None,
            "habilidades": ["Programação"],
            "carreira": "Autônomo",
            "relacionamentos": ["Candy Behr"],
            "aspiracao": "Gênio da Informática",
            "idade": "Adolescente"
        }
    }


    #Carreiras
    carreiras = {
        "Detetive": {
            "descricao": "Resolver crimes em lotes de trabalho",
            "expansao": "Jogo Base",
            "mecanicas_que_pode_usar": []
        },
        "Médico": {
            "descricao": "Atender pacientes em hospital jogável",
            "expansao": "Jogo Base",
            "mecanicas_que_pode_usar": []
        },
        "Cientista": {
            "descricao": "Inventar e explorar tecnologia alienígena",
            "expansao": "Jogo Base",
            "mecanicas_que_pode_usar": []
        },
        "Ecologista": {
            "descricao": "Cuidar do meio ambiente",
            "expansao": "Ilhas Tropicais",
            "mecanicas_que_pode_usar": ["Vida Oceânica"]
        },
        "Agricultor/Pecuarista": {
            "descricao": "Criar animais e cultivar plantações",
            "expansao": "Vida Campestre",
            "mecanicas_que_pode_usar": ["Criação de Animais"]
        },
        "Agente Funerário": {
            "descricao": "Gerenciar e organizar funerais",
            "expansao": "Pé Na Cova",
            "mecanicas_que_pode_usar": ["Sistema de Luto"]
        },
        "Freelancer": {
            "descricao": "Trabalhar em casa como programador, escritor, artista",
            "expansao": "Jogo Base",
            "mecanicas_que_pode_usar": []
        },
        "Autônomo": {
            "descricao": "Carreiras tradicionais como Chef, Pintor, etc.",
            "expansao": "Jogo Base",
            "mecanicas_que_pode_usar": []
        },
        "Desempregado": {
           "descricao": "Possue muito tempo livre",
            "expansao": "Jogo Base",
            "mecanicas_que_pode_usar": []
        }
    }

    #Expansões - Base
    for nome, attr in expansoes.items():
        G.add_node(nome, tipo="expansao", **attr)
        G.add_edge("Jogo Base", nome, relacao="expansão_de")

    
    #Mundos - Expansões
    for nome, attr in mundos.items():
        G.add_node(nome, tipo="mundo", **attr)
        G.add_edge(attr["expansao_origem"], nome, relacao="mundo_de")
    
    #Mecânicas - Expansões
    for nome, attr in mecanicas.items():
        G.add_node(nome, tipo="mecanica", descricao=attr["descricao"], tipo_mecanica=attr["tipo"],
                se_e_habilidade=attr["se_e_habilidade"], habilidade=attr["habilidade"])
        G.add_edge(attr["expansao_origem"], nome, relacao="traz")

    #Carreiras - Expansões
    for nome, attr in carreiras.items():
        G.add_node(nome, tipo="carreira", descricao=attr["descricao"], expansao=attr["expansao"])
        G.add_edge(attr["expansao"], nome, relacao="trabalhos_adicionados")
    






    #Sims
    for nome, attr in sims.items():
        G.add_node(nome, tipo="sim", **attr)
        G.add_edge(attr["origem"], nome, relacao="sims")
        if attr["mundo"] in G:
            G.add_edge(attr["mundo"], nome, relacao="moram")
        for mec in attr["mecanicas_que_pode_usar"]:
            if mec in G:
                G.add_edge(mec, nome, relacao="usam")

    #Sims - Oculto
    for nome, attr in sims.items():
        if attr.get("se_e_oculto") and "tipo_oculto" in attr and "origem" in attr:
            expansao_origem = attr["origem"]
            if expansao_origem in G:
                G.add_edge(nome, expansao_origem, relacao="oculto")


 
    #Sims - Mecânicas
    for sim_nome, sim_attr in sims.items():
        if nome in sim_attr.get("mecanicas_que_pode_usar", []):
            G.add_edge(sim_nome, nome, relacao="usa_mec")


    #Sims - Carreiras
    for nome, attr in sims.items():
        carreira_nome = attr.get("carreira")
        if carreira_nome and carreira_nome in G:
            G.add_edge(nome, carreira_nome, relacao="trabalha_em")

            if carreira_nome in carreiras:
                mecanicas_da_carreira = (
                    carreiras[carreira_nome].get("mecanicas_que_pode_usar") or
                    carreiras[carreira_nome].get("mecanicas") or []
                )
                for mec in mecanicas_da_carreira:
                    if mec in G:
                        G.add_edge(nome, mec, relacao="usa_mec_para_trabalho")

        

 