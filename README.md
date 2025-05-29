# 📊 Projeto de Análise com IA: Relatórios de Vendas Meganium

Este projeto faz parte de um desafio prático da plataforma DIO, com o objetivo de aplicar o uso de prompts com ferramentas de inteligência artificial para analisar relatórios de vendas e extrair insights valiosos para a empresa fictícia *Meganium*, especializada na fabricação de consoles.

## 🚀 Objetivo do Projeto

Utilizar inteligência artificial e engenharia de prompts para:

* Interpretar dados de vendas;
* Identificar padrões relevantes;
* Gerar conclusões estratégicas para o negócio;
* Documentar de forma clara o processo de análise.

---

## 🧠 Tecnologias e Ferramentas Utilizadas

* **Python** (Pandas): Para tratamento e compilação dos dados.
* **ChatGPT Plus**: Para análise dos dados e extração de insights.
* **GitHub Copilot**: Para geração de scripts de automação.
* **Planilhas CSV**: Como fonte de dados.
* **GitHub**: Para versionamento e documentação.

---

## 📂 Estrutura do Repositório

```
📁 raw_data/
    └─ Meganium_Sales_Data_-_AliExpress.csv
    └─ Meganium_Sales_Data_-_Etsy.csv
    └─ Meganium_Sales_Data_-_Shopee.csv
📁 processed_data/
    └─ compiled_sales_data.csv
📁 scripts/
    └─ compile_sheets_.csv
📄 prompts_chatgpt.md
📄 prompts_github_copilot.md
📄 insights.md
📄 README.md
```

---

## 📌 Etapas Realizadas

### 1. Compilação dos Dados

Utilizei o seguinte script Python, gerado com auxílio do GitHub Copilot, para compilar múltiplas planilhas em uma única base de dados:

```python
import pandas as pd
import glob
import os

# Caminho para os arquivos CSV
csv_folder = './raw_data/'
csv_files = glob.glob(os.path.join(csv_folder, 'Meganium_Sales_Data_*.csv'))

# Lê e concatena todos os arquivos
df_list = [pd.read_csv(f) for f in csv_files]
df_concat = pd.concat(df_list, ignore_index=True)

# Salva o resultado em um novo arquivo
df_concat.to_csv('./compiled_sales_data.csv', index=False)

print(f'Compilado {len(csv_files)} arquivos em compiled_sales_data.csv')
```

Veja os prompts para a criação do script em [`prompts_github_copilot.md`](prompts_github_copilot.md).

---

### 2. Configuração do Assistente IA

Criei um GPT personalizado com o seguinte propósito:

> **Atuar como analista da empresa Meganium**, focando exclusivamente na **fabricação de consoles**. O assistente foi configurado para analisar dados de vendas, identificar padrões e propor conclusões estratégicas com base em dados reais.

Veja o comportamento e as regras configuradas no arquivo [`prompts_chatgpt.md`](prompts_chatgpt.md).

---

### 3. Geração de Insights

A partir da base compilada, a IA gerou insights como:

* 📈 **Modelo mais vendido:** NEW MEGANIUM RG 40XXV (41 unidades, €3.426,93).
* 💡 **Produto com melhor rentabilidade:** RG353M (menos vendas, mas ticket médio alto).
* 🛒 **Canal mais eficiente:** Shopee, com 64 unidades vendidas.
* 📆 **Sazonalidade positiva:** Picos de vendas no terceiro trimestre de 2024.

Recomendações estratégicas:

* Focar em promoção do RG 40XXV.
* Reforçar o marketing do RG353M.
* Aumentar investimentos no Shopee.
* Preparar estoques e campanhas para Q3.

Mais detalhes estão documentados em [`insights.md`](insights.md).

---

## 📚 Aprendizados

Durante o desenvolvimento deste projeto, aprendi a:

* Construir e aplicar **prompts estruturados** para análise de dados com IA.
* Utilizar **Python e Pandas** para manipulação de dados em larga escala.
* Transformar dados brutos em **informações estratégicas**.
* Documentar tecnicamente um projeto no **GitHub** com clareza e organização.

---

## 🧑‍💻 Autor

**laisbastosbg**
Projeto realizado como parte do curso da DIO - Digital Innovation One.
[LinkedIn](https://www.linkedin.com/in/lais-godinho/)

