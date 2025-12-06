__________________________________________________
Comando pra baixar as bibliotecas, nesse py -3.13, coloque a versão baixada em sua maquina:
py -3.13 -m pip install numpy matplotlib
__________________________________________________

🔋 Algoritmo Genético para Seleção Ótima de Usinas de Energia

Um algoritmo genético implementado em Python que soluciona o problema de seleção de projetos energéticos sob restrições orçamentárias e ambientais. O algoritmo encontra a combinação ideal de usinas que maximiza a geração de energia enquanto minimiza o impacto ambiental e respeita um orçamento limitado.

🎯 Objetivo
Selecionar o conjunto ótimo de usinas para construção, considerando:
- **Maximização** de energia gerada (MW)
- **Minimização** do impacto ambiental (índice de poluição 0-10)
- **Respeito** ao orçamento máximo (R$ 1000 milhões)

🧬 Características do Algoritmo
- **Representação binária**: Cromossomos como vetores de 0s e 1s (16 usinas)
- **Função de fitness personalizada**: Penaliza poluição e excedentes orçamentários
- **Operadores genéticos**:
  - Seleção por torneio (tamanho 3)
  - Crossover de dois pontos (80%)
  - Mutação por bit flip (1% e 20% nos experimentos)
- **Elitismo**: Preserva 10% dos melhores indivíduos

📊 Experimentos Realizados
1. **Taxa de mutação baixa (1%)**: Convergência rápida e estável
2. **Taxa de mutação alta (20%)**: Maior exploração e soluções superiores

📈 Resultados e Visualizações
O código gera automaticamente:
- Ranking individual de usinas por eficiência
- Gráficos de evolução do fitness por geração
- Análise comparativa entre os experimentos
- Relatórios detalhados das soluções encontradas

🛠️ Tecnologias
- **Python 3.x**
- **Matplotlib** para visualizações
- **NumPy** para cálculos estatísticos

## 📁 Estrutura do Projeto
