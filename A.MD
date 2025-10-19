\section{Modelagem em Python}

A etapa de modelagem computacional foi desenvolvida na linguagem Python. O código abaixo demonstra a geração de dados sintéticos, ajuste de regressão linear, experimentos com dados simulados de idade vs pressão arterial e visualização dos resultados.

\begin{lstlisting}[language=Python, caption={Experimentos de modelagem em Python com Mínimos Quadrados}]
# ============================
# Imports necessários
# ============================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# ============================
# Experimento 1 - Dados Sintéticos
# ============================
np.random.seed(123)

# Dados sintéticos: y = 3x + 4 + ruído
x = np.linspace(0, 10, 100).reshape(-1, 1)
y = 3 * x + 4 + np.random.normal(0, 1, 100).reshape(-1, 1)

# Ajuste do modelo linear
modelo_sint = LinearRegression()
modelo_sint.fit(x, y)
y_pred = modelo_sint.predict(x)
mse_sint = mean_squared_error(y, y_pred)

# Gráfico sintético
plt.figure(figsize=(6, 4))
plt.scatter(x, y, color="blue", alpha=0.6, label="Dados sintéticos")
plt.plot(x, y_pred, color="red", linewidth=2, label="Ajuste linear")
plt.title("Problema Sintético")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.savefig("resultado_sintetico.png", dpi=300)
plt.close()

# ============================
# Experimento 2 - Dados Reais Simulados
# ============================
np.random.seed(123)

# Simulação de idade e pressão arterial
idade = np.random.randint(20, 80, 100).reshape(-1, 1)
pressao = 90 + 0.6 * idade.flatten() + np.random.normal(0, 10, 100)

# Ajuste do modelo linear
modelo_real = LinearRegression()
modelo_real.fit(idade, pressao)
pressao_pred = modelo_real.predict(idade)
mse_real = mean_squared_error(pressao, pressao_pred)

# Gráfico real
plt.figure(figsize=(6, 4))
plt.scatter(idade, pressao, color="green", alpha=0.6, label="Dados simulados")
plt.plot(idade, pressao_pred, color="black", linewidth=2, label="Ajuste linear")
plt.title("Idade vs Pressão Arterial (Simulação)")
plt.xlabel("Idade (anos)")
plt.ylabel("Pressão Arterial Sistólica (mmHg)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.savefig("resultado_real.png", dpi=300)
plt.close()

# ============================
# Comparação dos Resultados
# ============================
resultados = pd.DataFrame({
    "Problema": ["Sintético", "Real (Idade vs Pressão)"],
    "Intercepto": [modelo_sint.intercept_[0], modelo_real.intercept_],
    "Coeficiente": [modelo_sint.coef_[0][0], modelo_real.coef_[0]],
    "MSE": [mse_sint, mse_real]
})

print("Resultados dos Experimentos:\n")
print(resultados)
\end{lstlisting}
