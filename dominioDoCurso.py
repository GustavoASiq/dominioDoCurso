from collections import Counter
from random import randint
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from sklearn.metrics import r2_score


# Gerando os dados
armazenamento = Counter(randint(1, 50) for _ in range(100000))

# Ordenando os números e suas frequências
numero, frequencia = zip(*sorted(armazenamento.items()))

# Calculando a diferença entre a frequência atual e a anterior
diferenca_frequencia = [(frequencia[i] - frequencia[i - 1]) if i > 0 else 0 for i in range(len(frequencia))]

# Calculando a média e o desvio padrão das frequências
media_frequencia = np.mean(frequencia)

#Desvio padrão mais próximo de 0, mais homogêneo são os meus estudos em 
#cada matéria.
desvio_padrao_frequencia = np.std(frequencia) 

print(f"Média das frequências: {media_frequencia}")
print(f"Desvio padrão das frequências: {desvio_padrao_frequencia}")

# Exibindo a soma das diferenças de frequência e a quantidade de números positivos e negativos
numNeg = []
numPos = []
for i in diferenca_frequencia:
    if i < 0:
        numNeg.append(i)
    else:
        numPos.append(i)
print(f'Tem {abs(len(numPos))} números positivos e {len(numNeg)} negativas.')

difFreqSum = [((frequencia[i] - frequencia[i - 1]) / sum(diferenca_frequencia)) / 100 if i > 0 else 0 for i in range(len(frequencia))]

# Criando subplots com 2 linhas e 1 coluna
fig = make_subplots(rows=2, cols=1, subplot_titles=(
    "Frequência das Matérias",
    "Diferença de Frequência das Matérias"
))

# Adicionando o gráfico da frequência no primeiro subplot
fig.add_trace(
    go.Scatter(
        x=numero,
        y=frequencia,
        mode='lines+markers',
        name='Frequência'
    ),
    row=1, col=1
)

# Adicionando o gráfico da diferença de frequência no segundo subplot
fig.add_trace(
    go.Scatter(
        x=numero,
        y=difFreqSum,
        mode='lines+markers',
        name='Diferença de Frequência'
    ),
    row=2, col=1
)

# Configurando o layout do gráfico
fig.update_layout(
    title="Curvas de Assuntos Dominados do Curso do Aluno",
    xaxis_title="Matérias",
    yaxis_title="Frequência",
    legend_title="Legenda",
    template="plotly_white",
    height=800  # Altura do gráfico para acomodar os subplots
)

# Exibindo o gráfico
fig.show()