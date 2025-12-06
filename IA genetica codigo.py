# ====================================================================
# Grupo: Richard Rodrigues, Vitor Henrique e Robson Ribeiro
# ====================================================================
# PARTE 1: DADOS E FITNESS - CORRIGIDA
# ====================================================================

# 1. Configuração do Problema
ORCAMENTO_MAXIMO = 1000  # Milhões em R$
FATOR_PENALIDADE_POLUICAO = 10  # REDUZIDO de 15 para 10 para evitar fitness negativo

# 2. A "Loja" de Usinas (Dataset)
lista_usinas = [
    {"id": 0,  "nome": "Solar Parque A",      "custo": 120, "mw": 30,  "poluicao": 0},
    {"id": 1,  "nome": "Solar Parque B",      "custo": 140, "mw": 35,  "poluicao": 0},
    {"id": 2,  "nome": "Eólica Ventos Sul",   "custo": 180, "mw": 60,  "poluicao": 1},
    {"id": 3,  "nome": "Eólica Costeira",     "custo": 200, "mw": 70,  "poluicao": 1},
    {"id": 4,  "nome": "Hidrelétrica Pequena","custo": 300, "mw": 100, "poluicao": 3},
    {"id": 5,  "nome": "Termelétrica Carvão 1","custo": 80, "mw": 120, "poluicao": 9},
    {"id": 6,  "nome": "Termelétrica Carvão 2","custo": 90, "mw": 130, "poluicao": 9},
    {"id": 7,  "nome": "Gás Natural A",       "custo": 150, "mw": 110, "poluicao": 6},
    {"id": 8,  "nome": "Gás Natural B",       "custo": 160, "mw": 115, "poluicao": 6},
    {"id": 9,  "nome": "Nuclear Angra 3",     "custo": 500, "mw": 400, "poluicao": 5},
    {"id": 10, "nome": "Biomassa Cana",       "custo": 50,  "mw": 20,  "poluicao": 2},
    {"id": 11, "nome": "Biomassa Madeira",    "custo": 60,  "mw": 25,  "poluicao": 2},
    {"id": 12, "nome": "Solar Telhados",      "custo": 90,  "mw": 15,  "poluicao": 0},
    {"id": 13, "nome": "Diesel Emergência 1", "custo": 30,  "mw": 40,  "poluicao": 10},
    {"id": 14, "nome": "Diesel Emergência 2", "custo": 35,  "mw": 45,  "poluicao": 10},
    {"id": 15, "nome": "Ondas do Mar (Exp)",  "custo": 250, "mw": 50,  "poluicao": 0},
]

# 3. A Função de Fitness
def calcular_fitness(individuo):
    energia_total = 0
    custo_total = 0
    poluicao_total = 0
    
    for i in range(len(individuo)):
        if individuo[i] == 1:
            usina = lista_usinas[i]
            energia_total += usina["mw"]
            custo_total += usina["custo"]
            poluicao_total += usina["poluicao"]
            
    # CRITÉRIO 1: Penalidade SEVERA para orçamento excedido
    if custo_total > ORCAMENTO_MAXIMO:
        # Em vez de retornar 1, retorna valor NEGATIVO proporcional ao excesso
        excesso = custo_total - ORCAMENTO_MAXIMO
        return -excesso  # Quanto maior o excesso, mais negativo
    
    # CRITÉRIO 2: Cálculo do Fitness normal
    fitness = energia_total - (poluicao_total * FATOR_PENALIDADE_POLUICAO)
    
    # Garantir que fitness seja pelo menos 0
    return max(fitness, 0)

# ====================================================================
# ANÁLISE INDIVIDUAL DAS USINAS
# ====================================================================

def analisar_usinas_individualmente():
    """
    Analisa cada usina individualmente e retorna um ranking.
    Calcula a pontuação individual baseada na mesma fórmula do fitness.
    """
    ranking_usinas = []
    
    for usina in lista_usinas:
        # Calcula a pontuação individual (fitness se apenas essa usina fosse construída)
        pontuacao_individual = usina["mw"] - (usina["poluicao"] * FATOR_PENALIDADE_POLUICAO)
        
        # Calcula eficiência (MW por R$ milhão)
        eficiencia = usina["mw"] / usina["custo"] if usina["custo"] > 0 else 0
        
        ranking_usinas.append({
            "id": usina["id"],
            "nome": usina["nome"],
            "custo": usina["custo"],
            "mw": usina["mw"],
            "poluicao": usina["poluicao"],
            "pontuacao_individual": pontuacao_individual,
            "eficiencia": eficiencia,
            "custo_beneficio": pontuacao_individual / usina["custo"] if usina["custo"] > 0 else 0
        })
    
    # Ordena por pontuação individual (maior primeiro)
    ranking_usinas.sort(key=lambda x: x["pontuacao_individual"], reverse=True)
    
    return ranking_usinas

def imprimir_ranking_usinas(ranking_usinas):
    """
    Imprime o ranking completo de todas as usinas individualmente.
    """
    print("\n" + "="*90)
    print("🏆 RANKING INDIVIDUAL DE USINAS (ordenado por pontuação)")
    print("="*90)
    print(f"{'POS':<4} {'NOME':<25} {'CUSTO (R$ mi)':<12} {'ENERGIA (MW)':<12} {'POLUIÇÃO':<10} {'PONTUAÇÃO':<12} {'EFICIÊNCIA':<10}")
    print("-"*90)
    
    for pos, usina in enumerate(ranking_usinas, 1):
        print(f"{pos:<4} {usina['nome']:<25} "
              f"{usina['custo']:<12} {usina['mw']:<12} {usina['poluicao']:<10} "
              f"{usina['pontuacao_individual']:<12.1f} {usina['eficiencia']:<10.3f}")
    
    print("="*90)
    
    # Mostra a melhor usina
    melhor_usina = ranking_usinas[0]
    print(f"\n⭐ MELHOR USINA INDIVIDUAL: {melhor_usina['nome']}")
    print(f"   • Pontuação: {melhor_usina['pontuacao_individual']:.1f}")
    print(f"   • Energia: {melhor_usina['mw']} MW")
    print(f"   • Custo: R$ {melhor_usina['custo']} milhões")
    print(f"   • Poluição: {melhor_usina['poluicao']}")
    print(f"   • Eficiência: {melhor_usina['eficiencia']:.3f} MW/R$ mi")
    print("="*90)

# ====================================================================
# PARTE 2: IMPLEMENTAÇÃO DO MOTOR DO ALGORITMO GENÉTICO
# ====================================================================

import random
import matplotlib.pyplot as plt
import numpy as np

# --- PARÂMETROS DO ALGORITMO GENÉTICO---
TAMANHO_POPULACAO = 50
NUMERO_GERACOES = 50
TAXA_CROSSOVER = 0.8
TAXA_MUTACAO = 0.01
ELITISMO = True
TAMANHO_TORNEIO = 3
PORCENTAGEM_ELITISMO = 0.1 

# --- FUNÇÕES DA PARTE 2---

def gerar_individuo_viavel():
    """Gera um indivíduo que tem chance de ser viável"""
    individuo = [0] * len(lista_usinas)
    # Escolhe aleatoriamente algumas usinas, mas limitando o custo
    usinas_disponiveis = list(range(len(lista_usinas)))
    random.shuffle(usinas_disponiveis)
    
    custo_atual = 0
    for usina_id in usinas_disponiveis:
        if random.random() < 0.3:  # 30% de chance de selecionar cada usina
            custo_usina = lista_usinas[usina_id]["custo"]
            if custo_atual + custo_usina <= ORCAMENTO_MAXIMO * 1.5:  # Limite mais flexível
                individuo[usina_id] = 1
                custo_atual += custo_usina
    
    return individuo

def gerar_populacao_inicial():
    """Gera população com 50% indivíduos viáveis e 50% aleatórios"""
    populacao = []
    
    # 50% de indivíduos viáveis
    for _ in range(TAMANHO_POPULACAO // 2):
        populacao.append(gerar_individuo_viavel())
    
    # 50% de indivíduos totalmente aleatórios
    for _ in range(TAMANHO_POPULACAO // 2):
        populacao.append([random.randint(0, 1) for _ in range(len(lista_usinas))])
    
    return populacao

def selecao_torneio(populacao, fitness_populacao):
    indices_torneio = random.sample(range(len(populacao)), TAMANHO_TORNEIO)
    
    melhor_indice = indices_torneio[0]
    melhor_fitness = fitness_populacao[melhor_indice]
    
    for idx in indices_torneio[1:]:
        if fitness_populacao[idx] > melhor_fitness:
            melhor_indice = idx
            melhor_fitness = fitness_populacao[idx]
    
    return populacao[melhor_indice]

def crossover_dois_pontos(pai1, pai2):
    """Crossover de dois pontos para mais diversidade"""
    if random.random() > TAXA_CROSSOVER:
        return pai1[:], pai2[:]
    
    # Escolhe dois pontos de corte
    ponto1 = random.randint(1, len(pai1) // 2)
    ponto2 = random.randint(ponto1 + 1, len(pai1) - 1)
    
    # Cria os filhos
    filho1 = pai1[:ponto1] + pai2[ponto1:ponto2] + pai1[ponto2:]
    filho2 = pai2[:ponto1] + pai1[ponto1:ponto2] + pai2[ponto2:]
    
    return filho1, filho2

def mutacao_bit_flip_inteligente(individuo, taxa_mutacao):
    """Mutação que evita tornar soluções viáveis em inviáveis"""
    individuo_mutado = individuo[:]
    
    # Analisa o indivíduo atual
    custo_total = sum(lista_usinas[i]["custo"] for i in range(len(individuo)) if individuo[i] == 1)
    
    for i in range(len(individuo_mutado)):
        if random.random() < taxa_mutacao:
            if individuo_mutado[i] == 1:
                # Se está ligado, desligar é sempre seguro (reduz custo)
                individuo_mutado[i] = 0
            else:
                # Se está desligado, ligar só se não estourar muito o orçamento
                custo_usina = lista_usinas[i]["custo"]
                if custo_total + custo_usina <= ORCAMENTO_MAXIMO * 1.2:
                    individuo_mutado[i] = 1
                    custo_total += custo_usina
    
    return individuo_mutado

def executar_algoritmo_genetico(taxa_mutacao=TAXA_MUTACAO, 
                                numero_geracoes=NUMERO_GERACOES, 
                                mostrar_progresso=True):
    
    populacao = gerar_populacao_inicial()
    melhor_individuo_global = None
    melhor_fitness_global = -float('inf')
    
    historico_melhores = []
    historico_media = []
    historico_piores = []
    
    if mostrar_progresso:
        print(f"\n{'='*60}")
        print(f"ALGORITMO GENÉTICO - Mutação: {taxa_mutacao*100}%")
        print(f"{'='*60}")
        print(f"População: {TAMANHO_POPULACAO} | Gerações: {numero_geracoes}")
        print(f"{'-'*60}")
    
    for geracao in range(numero_geracoes):
        # Calcular fitness
        fitness_populacao = [calcular_fitness(individuo) for individuo in populacao]
        
        # Estatísticas
        melhor_fitness = max(fitness_populacao)
        pior_fitness = min(fitness_populacao)
        media_fitness = np.mean(fitness_populacao)
        indice_melhor = fitness_populacao.index(melhor_fitness)
        melhor_individuo = populacao[indice_melhor]
        
        # Atualizar melhor global
        if melhor_fitness > melhor_fitness_global:
            melhor_fitness_global = melhor_fitness
            melhor_individuo_global = melhor_individuo[:]
        
        # Armazenar histórico
        historico_melhores.append(melhor_fitness)
        historico_media.append(media_fitness)
        historico_piores.append(pior_fitness)
        
        # Nova população com elitismo
        nova_populacao = []
        
        # ELITISMO: manter os 10% melhores
        num_elite = max(1, int(PORCENTAGEM_ELITISMO * TAMANHO_POPULACAO))
        indices_ordenados = np.argsort(fitness_populacao)[::-1]  # Ordem decrescente
        for i in range(num_elite):
            nova_populacao.append(populacao[indices_ordenados[i]])
        
        # Preencher o restante
        while len(nova_populacao) < TAMANHO_POPULACAO:
            # Seleção
            pai1 = selecao_torneio(populacao, fitness_populacao)
            pai2 = selecao_torneio(populacao, fitness_populacao)
            
            # Crossover
            filho1, filho2 = crossover_dois_pontos(pai1, pai2)
            
            # Mutação
            filho1 = mutacao_bit_flip_inteligente(filho1, taxa_mutacao)
            filho2 = mutacao_bit_flip_inteligente(filho2, taxa_mutacao)
            
            nova_populacao.append(filho1)
            if len(nova_populacao) < TAMANHO_POPULACAO:
                nova_populacao.append(filho2)
        
        populacao = nova_populacao
        
        # Progresso
        if mostrar_progresso and (geracao + 1) % 10 == 0:
            print(f"Geração {geracao + 1:3d}: "
                  f"Melhor = {melhor_fitness:6.1f} | "
                  f"Média = {media_fitness:6.1f} | "
                  f"Pior = {pior_fitness:6.1f}")
    
    if mostrar_progresso:
        print(f"{'='*60}")
        print(f"CONCLUÍDO! Melhor fitness: {melhor_fitness_global:.1f}")
        print(f"{'='*60}")
    
    return melhor_individuo_global, melhor_fitness_global, historico_melhores, historico_media, historico_piores

def analisar_solucao_detalhada(individuo):
    """Análise detalhada com ranking das usinas"""
    energia_total = 0
    custo_total = 0
    poluicao_total = 0
    usinas_selecionadas = []
    
    for i in range(len(individuo)):
        if individuo[i] == 1:
            usina = lista_usinas[i]
            energia_total += usina["mw"]
            custo_total += usina["custo"]
            poluicao_total += usina["poluicao"]
            usinas_selecionadas.append({
                "id": usina["id"],
                "nome": usina["nome"],
                "custo": usina["custo"],
                "mw": usina["mw"],
                "poluicao": usina["poluicao"],
                "eficiencia": usina["mw"] / max(usina["custo"], 1),  # MW por R$ mi
                "pontuacao": usina["mw"] - (usina["poluicao"] * FATOR_PENALIDADE_POLUICAO)
            })
    
    # Ordenar usinas por pontuação (melhores primeiro)
    usinas_selecionadas.sort(key=lambda x: x["pontuacao"], reverse=True)
    
    return {
        "individuo": individuo,
        "fitness": calcular_fitness(individuo),
        "energia_total": energia_total,
        "custo_total": custo_total,
        "poluicao_total": poluicao_total,
        "usinas_selecionadas": usinas_selecionadas,
        "numero_usinas": len(usinas_selecionadas),
        "esta_dentro_orcamento": custo_total <= ORCAMENTO_MAXIMO,
        "eficiencia_media": energia_total / max(custo_total, 1)
    }

def imprimir_relatorio_completo(analise, titulo="SOLUÇÃO ENCONTRADA"):
    """Relatório completo com análise das usinas"""
    print("\n" + "="*80)
    print(f"{titulo}")
    print("="*80)
    
    print(f"\n📈 DESEMPENHO GERAL:")
    print(f"   Fitness total: {analise['fitness']:.1f} pontos")
    print(f"   Energia gerada: {analise['energia_total']} MW")
    print(f"   Custo total: R$ {analise['custo_total']:.2f} milhões")
    print(f"   Orçamento limite: R$ {ORCAMENTO_MAXIMO} milhões")
    print(f"   Poluição total: {analise['poluicao_total']} (0 = limpo, 10 = poluente)")
    print(f"   Eficiência: {analise['eficiencia_media']:.2f} MW/R$ mi")
    print(f"   Usinas selecionadas: {analise['numero_usinas']}/16")
    
    status = "✅ DENTRO DO ORÇAMENTO" if analise['esta_dentro_orcamento'] else "❌ EXCEDE ORÇAMENTO"
    print(f"   Status: {status}")
    
    # Mostrar a melhor usina individual na solução
    if analise['usinas_selecionadas']:
        melhor_usina_solucao = analise['usinas_selecionadas'][0]
        print(f"\n⭐ MELHOR USINA NA SOLUÇÃO: {melhor_usina_solucao['nome']}")
        print(f"   • Pontuação: {melhor_usina_solucao['pontuacao']:.1f}")
        print(f"   • Energia: {melhor_usina_solucao['mw']} MW")
        print(f"   • Custo: R$ {melhor_usina_solucao['custo']} milhões")
        print(f"   • Poluição: {melhor_usina_solucao['poluicao']}")
        print(f"   • Eficiência: {melhor_usina_solucao['eficiencia']:.3f} MW/R$ mi")
    
    print(f"\n🏆 USINAS SELECIONADAS (ordenadas por pontuação):")
    print("-"*80)
    print(f"{'#':<2} {'NOME':<25} {'CUSTO (R$ mi)':<12} {'ENERGIA (MW)':<12} {'POLUIÇÃO':<10} {'PONTUAÇÃO':<12}")
    print("-"*80)
    
    for idx, usina in enumerate(analise['usinas_selecionadas'], 1):
        print(f"{idx:<2} {usina['nome']:<25} "
              f"{usina['custo']:<12} {usina['mw']:<12} {usina['poluicao']:<10} "
              f"{usina['pontuacao']:<12.1f}")
    
    print("="*80)

def plotar_evolucao_melhorada(historico_melhores, historico_media, historico_piores, taxa_mutacao):
    """Gráfico de evolução melhorado"""
    geracoes = list(range(1, len(historico_melhores) + 1))
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), gridspec_kw={'height_ratios': [2, 1]})
    
    # Gráfico 1: Evolução do fitness
    ax1.plot(geracoes, historico_melhores, 'g-', linewidth=3, label='Melhor Fitness', marker='o', markersize=4)
    ax1.plot(geracoes, historico_media, 'b-', linewidth=2, label='Média Fitness', alpha=0.8)
    ax1.plot(geracoes, historico_piores, 'r-', linewidth=1, label='Pior Fitness', alpha=0.6)
    
    ax1.fill_between(geracoes, historico_piores, historico_melhores, alpha=0.1, color='gray')
    
    ax1.set_xlabel('Geração', fontsize=12)
    ax1.set_ylabel('Fitness', fontsize=12)
    ax1.set_title(f'EVOLUÇÃO DO FITNESS - MUTAÇÃO {taxa_mutacao*100}%', fontsize=14, fontweight='bold', pad=20)
    ax1.grid(True, alpha=0.3)
    ax1.legend(loc='best')
    
    # Linha de referência para orçamento ideal
    ax1.axhline(y=200, color='orange', linestyle='--', alpha=0.5, label='Meta de Fitness')
    
    # Anotação do melhor
    melhor_fitness = max(historico_melhores)
    melhor_geracao = historico_melhores.index(melhor_fitness) + 1
    ax1.annotate(f'Melhor: {melhor_fitness:.1f}\n(Geração {melhor_geracao})',
                 xy=(melhor_geracao, melhor_fitness),
                 xytext=(melhor_geracao + 2, melhor_fitness - 50),
                 arrowprops=dict(facecolor='green', shrink=0.05, width=2, headwidth=8),
                 fontsize=11,
                 bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgreen", alpha=0.8))
    
    # Gráfico 2: Diferença entre melhor e média
    diferencas = [melhor - media for melhor, media in zip(historico_melhores, historico_media)]
    ax2.bar(geracoes, diferencas, color='purple', alpha=0.6, label='Diferença (Melhor - Média)')
    ax2.axhline(y=0, color='black', linewidth=0.5)
    
    ax2.set_xlabel('Geração', fontsize=12)
    ax2.set_ylabel('Diferença', fontsize=12)
    ax2.set_title('DIFERENÇA ENTRE MELHOR E MÉDIA', fontsize=12, fontweight='bold')
    ax2.grid(True, alpha=0.3, axis='y')
    ax2.legend(loc='upper right')
    
    plt.tight_layout()
    return fig

def executar_experimento_comparativo_avancado():
    """Experimento comparativo avançado"""
    print("\n" + "="*80)
    print("EXPERIMENTO COMPARATIVO AVANÇADO: MUTAÇÃO 1% vs 20%")
    print("="*80)
    
    # PRIMEIRO: Mostrar ranking individual das usinas
    print("\n📊 ANALISANDO USINAS INDIVIDUALMENTE...")
    ranking_usinas = analisar_usinas_individualmente()
    imprimir_ranking_usinas(ranking_usinas)
    
    resultados = {}
    
    # Experimento 1: Mutação baixa (1%)
    print("\n" + "🔵"*40)
    print("EXPERIMENTO 1: MUTAÇÃO BAIXA (1%)")
    print("🔵"*40)
    
    melhor_individuo_1, melhor_fitness_1, hist_melhores_1, hist_media_1, hist_piores_1 = executar_algoritmo_genetico(
        taxa_mutacao=0.01, 
        numero_geracoes=50,
        mostrar_progresso=True
    )
    
    analise_1 = analisar_solucao_detalhada(melhor_individuo_1)
    imprimir_relatorio_completo(analise_1, "SOLUÇÃO - MUTAÇÃO 1%")
    
    # Gráfico 1
    fig1 = plotar_evolucao_melhorada(hist_melhores_1, hist_media_1, hist_piores_1, 0.01)
    fig1.savefig('evolucao_mutacao_1porcento_melhorado.png', dpi=300, bbox_inches='tight')
    plt.close(fig1)  # Fechar a figura para liberar memória
    
    # Experimento 2: Mutação alta (20%)
    print("\n" + "🔴"*40)
    print("EXPERIMENTO 2: MUTAÇÃO ALTA (20%)")
    print("🔴"*40)
    
    melhor_individuo_2, melhor_fitness_2, hist_melhores_2, hist_media_2, hist_piores_2 = executar_algoritmo_genetico(
        taxa_mutacao=0.20, 
        numero_geracoes=50,
        mostrar_progresso=True
    )
    
    analise_2 = analisar_solucao_detalhada(melhor_individuo_2)
    imprimir_relatorio_completo(analise_2, "SOLUÇÃO - MUTAÇÃO 20%")
    
    # Gráfico 2
    fig2 = plotar_evolucao_melhorada(hist_melhores_2, hist_media_2, hist_piores_2, 0.20)
    fig2.savefig('evolucao_mutacao_20porcento_melhorado.png', dpi=300, bbox_inches='tight')
    plt.close(fig2)  # Fechar a figura para liberar memória
    
    # Análise comparativa avançada
    print("\n" + "📊"*40)
    print("ANÁLISE COMPARATIVA DETALHADA")
    print("📊"*40)
    
    print(f"\n{'COMPARAÇÃO':<30} {'MUTAÇÃO 1%':<15} {'MUTAÇÃO 20%':<15} {'VENCEDOR':<10} {'ANÁLISE':<20}")
    print("-"*90)
    
    # Fitness
    vencedor_fitness = "1%" if melhor_fitness_1 > melhor_fitness_2 else "20%"
    analise_fitness = "Mais estável" if vencedor_fitness == "1%" else "Mais exploratório"
    print(f"{'Melhor Fitness':<30} {melhor_fitness_1:<15.1f} {melhor_fitness_2:<15.1f} {vencedor_fitness:<10} {analise_fitness:<20}")
    
    # Energia
    vencedor_energia = "1%" if analise_1['energia_total'] > analise_2['energia_total'] else "20%"
    print(f"{'Energia Total (MW)':<30} {analise_1['energia_total']:<15} {analise_2['energia_total']:<15} {vencedor_energia:<10} {'Maior produção':<20}")
    
    # Custo
    vencedor_custo = "1%" if analise_1['custo_total'] < analise_2['custo_total'] else "20%"
    status_custo_1 = "✅" if analise_1['esta_dentro_orcamento'] else "❌"
    status_custo_2 = "✅" if analise_2['esta_dentro_orcamento'] else "❌"
    print(f"{'Custo Total (R$ mi)':<30} {status_custo_1} {analise_1['custo_total']:<13.1f} {status_custo_2} {analise_2['custo_total']:<13.1f} {vencedor_custo:<10} {'Mais econômico':<20}")
    
    # Poluição
    vencedor_pol = "1%" if analise_1['poluicao_total'] < analise_2['poluicao_total'] else "20%"
    print(f"{'Poluição Total':<30} {analise_1['poluicao_total']:<15} {analise_2['poluicao_total']:<15} {vencedor_pol:<10} {'Mais limpo':<20}")
    
    # Eficiência
    vencedor_ef = "1%" if analise_1['eficiencia_media'] > analise_2['eficiencia_media'] else "20%"
    print(f"{'Eficiência (MW/R$ mi)':<30} {analise_1['eficiencia_media']:<15.2f} {analise_2['eficiencia_media']:<15.2f} {vencedor_ef:<10} {'Melhor custo-benefício':<20}")
    
    # Estabilidade (desvio padrão)
    desvio_1 = np.std(hist_melhores_1[-10:]) if len(hist_melhores_1) >= 10 else 0
    desvio_2 = np.std(hist_melhores_2[-10:]) if len(hist_melhores_2) >= 10 else 0
    vencedor_est = "1%" if desvio_1 < desvio_2 else "20%"
    print(f"{'Estabilidade (desvio)':<30} {desvio_1:<15.4f} {desvio_2:<15.4f} {vencedor_est:<10} {'Mais consistente':<20}")
    
    print("-"*90)
    
    # Conclusão
    print(f"\n🎯 CONCLUSÃO DO EXPERIMENTO:")
    
    if melhor_fitness_1 > melhor_fitness_2:
        print(f"  • A mutação de 1% encontrou uma solução MELHOR (fitness: {melhor_fitness_1:.1f} vs {melhor_fitness_2:.1f})")
        print(f"  • Isso indica que para este problema, uma mutação BAIXA é mais eficaz")
    else:
        print(f"  • A mutação de 20% encontrou uma solução MELHOR (fitness: {melhor_fitness_2:.1f} vs {melhor_fitness_1:.1f})")
        print(f"  • Isso indica que para este problema, uma mutação ALTA é mais eficaz")
    
    print(f"\n📈 OBSERVAÇÕES:")
    print(f"  1. A diferença entre melhor e média deve DIMINUIR ao longo das gerações")
    print(f"  2. Soluções viáveis (dentro do orçamento) têm fitness POSITIVO")
    print(f"  3. A evolução deve mostrar MELHORA CONTÍNUA no fitness")
    
    # Gráfico comparativo final
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    
    # Subplot 1: Evolução 1%
    axes[0, 0].plot(hist_melhores_1, 'g-', label='Melhor', linewidth=2)
    axes[0, 0].plot(hist_media_1, 'b-', label='Média', alpha=0.7)
    axes[0, 0].fill_between(range(len(hist_melhores_1)), hist_media_1, hist_melhores_1, alpha=0.1, color='green')
    axes[0, 0].set_title('Mutação 1% - Evolução', fontweight='bold')
    axes[0, 0].set_xlabel('Geração')
    axes[0, 0].set_ylabel('Fitness')
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].legend()
    
    # Subplot 2: Evolução 20%
    axes[0, 1].plot(hist_melhores_2, 'r-', label='Melhor', linewidth=2)
    axes[0, 1].plot(hist_media_2, 'm-', label='Média', alpha=0.7)
    axes[0, 1].fill_between(range(len(hist_melhores_2)), hist_media_2, hist_melhores_2, alpha=0.1, color='red')
    axes[0, 1].set_title('Mutação 20% - Evolução', fontweight='bold')
    axes[0, 1].set_xlabel('Geração')
    axes[0, 1].set_ylabel('Fitness')
    axes[0, 1].grid(True, alpha=0.3)
    axes[0, 1].legend()
    
    # Subplot 3: Comparação dos melhores
    axes[1, 0].plot(hist_melhores_1, 'g-', label='Mutação 1%', linewidth=2)
    axes[1, 0].plot(hist_melhores_2, 'r-', label='Mutação 20%', linewidth=2)
    axes[1, 0].set_title('Comparação: Melhor Fitness', fontweight='bold')
    axes[1, 0].set_xlabel('Geração')
    axes[1, 0].set_ylabel('Fitness')
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].legend()
    
    # Subplot 4: Diferença entre melhor e média
    dif_1 = [m - a for m, a in zip(hist_melhores_1, hist_media_1)]
    dif_2 = [m - a for m, a in zip(hist_melhores_2, hist_media_2)]
    axes[1, 1].plot(dif_1, 'g--', label='Diferença 1%', alpha=0.7)
    axes[1, 1].plot(dif_2, 'r--', label='Diferença 20%', alpha=0.7)
    axes[1, 1].set_title('Diferença: Melhor vs Média', fontweight='bold')
    axes[1, 1].set_xlabel('Geração')
    axes[1, 1].set_ylabel('Diferença')
    axes[1, 1].grid(True, alpha=0.3)
    axes[1, 1].legend()
    
    plt.suptitle('COMPARAÇÃO COMPLETA: EFEITO DA TAXA DE MUTAÇÃO', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig('comparacao_completa_mutacoes.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("\n" + "="*80)
    print("📁 ARQUIVOS GERADOS:")
    print("="*80)
    print("✓ evolucao_mutacao_1porcento_melhorado.png - Gráfico detalhado (1%)")
    print("✓ evolucao_mutacao_20porcento_melhorado.png - Gráfico detalhado (20%)")
    print("✓ comparacao_completa_mutacoes.png - Comparação completa")
    print("="*80)
    
    return analise_1, analise_2, ranking_usinas

# --- PROGRAMA PRINCIPAL ---
if __name__ == "__main__":
    print("\n" + "="*80)
    print("ALGORITMO GENÉTICO - SELEÇÃO ÓTIMA DE USINAS DE ENERGIA")
    print("="*80)
    print("Grupo: Richard Rodrigues, Vitor Henrique e Robson Ribeiro")
    print("="*80)
    
    print(f"\n🔧 CONFIGURAÇÃO DO PROBLEMA:")
    print(f"   • Orçamento máximo: R$ {ORCAMENTO_MAXIMO} milhões")
    print(f"   • Penalidade por poluição: {FATOR_PENALIDADE_POLUICAO} pontos por unidade")
    print(f"   • Usinas disponíveis: {len(lista_usinas)} opções")
    
    print(f"\n⚙️  PARÂMETROS DO ALGORITMO GENÉTICO:")
    print(f"   • População: {TAMANHO_POPULACAO} indivíduos")
    print(f"   • Gerações: {NUMERO_GERACOES}")
    print(f"   • Crossover: {TAXA_CROSSOVER*100}% (dois pontos)")
    print(f"   • Elitismo: {PORCENTAGEM_ELITISMO*100}% dos melhores preservados")
    print(f"   • Seleção: Torneio (tamanho {TAMANHO_TORNEIO})")
    
    print(f"\n🎯 OBJETIVOS DO EXPERIMENTO:")
    print("   1. Encontrar a combinação ótima de usinas")
    print("   2. Maximizar energia dentro do orçamento")
    print("   3. Minimizar o impacto ambiental")
    print("   4. Comparar taxas de mutação (1% vs 20%)")
    print("   5. Identificar a MELHOR USINA individual")
    
    input("\nPressione ENTER para iniciar os experimentos...")
    
    try:
        analise_1, analise_2, ranking_usinas = executar_experimento_comparativo_avancado()
        print("\n✅ EXPERIMENTOS CONCLUÍDOS COM SUCESSO!")
        print("   Todos os gráficos e análises foram gerados.")
        
        # Resumo final
        print("\n" + "🎉"*40)
        print("RESUMO FINAL DOS RESULTADOS")
        print("🎉"*40)
        
        melhor_geral = analise_1 if analise_1['fitness'] > analise_2['fitness'] else analise_2
        taxa_melhor = "1%" if analise_1['fitness'] > analise_2['fitness'] else "20%"
        
        print(f"\n🏆 MELHOR SOLUÇÃO ENCONTRADA (Mutação {taxa_melhor}):")
        print(f"   • Fitness: {melhor_geral['fitness']:.1f} pontos")
        print(f"   • Energia: {melhor_geral['energia_total']} MW")
        print(f"   • Custo: R$ {melhor_geral['custo_total']:.1f} milhões")
        print(f"   • Poluição: {melhor_geral['poluicao_total']}")
        print(f"   • Usinas selecionadas: {melhor_geral['numero_usinas']}")
        print(f"   • Dentro do orçamento: {'SIM ✅' if melhor_geral['esta_dentro_orcamento'] else 'NÃO ❌'}")
        
        # Melhor usina individual
        melhor_usina_individual = ranking_usinas[0]
        print(f"\n⭐ MELHOR USINA INDIVIDUAL (de todas):")
        print(f"   • Nome: {melhor_usina_individual['nome']}")
        print(f"   • Pontuação: {melhor_usina_individual['pontuacao_individual']:.1f}")
        print(f"   • Energia: {melhor_usina_individual['mw']} MW")
        print(f"   • Custo: R$ {melhor_usina_individual['custo']} milhões")
        print(f"   • Poluição: {melhor_usina_individual['poluicao']}")
        print(f"   • Eficiência: {melhor_usina_individual['eficiencia']:.3f} MW/R$ mi")
        
        print(f"\n📊 LIÇÕES APRENDIDAS:")
        print("   1. A Nuclear Angra 3 é a melhor usina individual (alta energia, poluição média)")
        print("   2. Usinas solares têm poluição 0, mas custo alto por MW")
        print("   3. Usinas a carvão geram muita energia, mas com alta poluição")
        print("   4. O AG prioriza usinas com melhor relação energia/poluição/custo")
        
    except Exception as e:
        print(f"\n❌ ERRO DURANTE A EXECUÇÃO: {e}")
        print("Executando diagnóstico...")
        
        # Diagnóstico básico
        print("\n🔍 DIAGNÓSTICO:")
        individuo_teste = [1] * len(lista_usinas)  # Todas as usinas
        fitness_teste = calcular_fitness(individuo_teste)
        print(f"   • Fitness com TODAS usinas: {fitness_teste}")
        print(f"   • (Esperado: negativo, pois custo excede orçamento)")
        
        individuo_vazio = [0] * len(lista_usinas)  # Nenhuma usina
        fitness_vazio = calcular_fitness(individuo_vazio)
        print(f"   • Fitness com NENHUMA usina: {fitness_vazio}")
        print(f"   • (Esperado: 0)")
        
        print("\n⚡ TESTE RÁPIDO (3 gerações)...")
        melhor, fitness, _, _, _ = executar_algoritmo_genetico(
            taxa_mutacao=0.01,
            numero_geracoes=3,
            mostrar_progresso=False
        )
        print(f"   • Melhor fitness após 3 gerações: {fitness:.2f}")