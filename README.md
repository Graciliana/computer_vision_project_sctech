# Inspeção Visual de Peças Metalúrgicas com Visão Computacional

## 📝 Descrição do Projeto

Este projeto consiste no desenvolvimento de um pipeline autônomo de pré-processamento de imagens em Python utilizando a biblioteca **OpenCV**. O objetivo principal é automatizar o tratamento de imagens de peças metálicas da indústria metalúrgica (base de dados *Casting Product Image Data*), aplicando uma sequência lógica de filtros e transformações para evidenciar ranhuras, defeitos estruturais e contornos.

O resultado final do processamento prepara o lote de imagens de forma padronizada para que, futuramente, equipes de Machine Learning possam treinar modelos preditivos de controle de qualidade.

---

## 📽️ Vídeo de Apresentação e Demonstração

A apresentação do projeto, explicação da arquitetura, fluxo de branches do Git e demonstração do pipeline funcionando pode ser assistida pelo link abaixo:

👉 **[Assistir ao Vídeo do Projeto no Google Drive](COLE_AQUI_O_LINK_COMPLETO_DO_SEU_VIDEO_NO_GOOGLE_DRIVE)**

---

## 🛠️ Arquitetura do Sistema e Tecnologias

Para evitar consumo excessivo de hardware local, a arquitetura foi desenhada dividindo o desenvolvimento e o processamento:

* **VSCode (IDE Local):** Utilizado para escrita do código modular (`.py`), criação da documentação técnica e controle de versão via Git.
* **GitHub (Repositório Remote):** Gerenciamento e versionamento do código através das branches `main` e `development`.
* **Kaggle / Google Colab (Servidor em Nuvem):** Execução do processamento pesado em lote (batch processing) utilizando a infraestrutura e aceleradores de hardware da nuvem.

### Tecnologias Utilizadas

* **Python 3.x**
* **OpenCV (`cv2`)** - Processamento de imagem e visão computacional
* **NumPy** - Manipulação matricial de imagens
* **Matplotlib** - Visualização e plotagem de comparações
* **tqdm** - Gerenciamento visual da barra de progresso do processamento em lote

---

## 📂 Estrutura do Repositório

```text
projeto-visao-computacional/
├── .gitignore               # Arquivos ignorados pelo versionamento (dados e venvs)
├── README.md                # Documentação do projeto
├── requirements.txt         # Lista de dependências Python
├── notebooks/
│   └── 01_processing.ipynb # Execução e testes em lote na nuvem
└── src/
    ├── __init__.py          # Identificador de pacote Python
    ├── utils.py             # Funções de leitura de imagens em lote e salvamento
    └── pipeline.py          # Sequência de transformações da imagem via OpenCV

```

---

## ⚙️ Estágios do Pipeline de Pré-processamento (src/pipeline.py)

A função principal preprocess_image() executa as seguintes etapas sequenciais:

1. **Leitura da Imagem:** Carregamento da amostra bruta em disco (cv2.imread).

2. **Conversão de Espaço de Cor:** Transformação de BGR para Escala de Cinza (cv2.COLOR_BGR2GRAY) para reduzir complexidade de canais mantendo informação de luminância.

3. **Suavização (Blur):** Aplicação de Filtro Gaussiano (cv2.GaussianBlur) com kernel $5 \times 5$ para redução de ruídos de alta frequência.

4. **Limiarização (Thresholding):** Binarização com o Método de Otsu (cv2.THRESH_OTSU) para isolar a peça metálica do fundo.

5. **Detecção de Bordas:** Aplicação do algoritmo de Canny (cv2.Canny) para destacar ranhuras, rachaduras e limites estruturais da peça.

6. **Refinamento Morfológico:** Operação morfológica de Fechamento (cv2.MORPH_CLOSE) com elemento estruturante $3 \times 3$ para eliminação de ruídos residuais e preenchimento de pequenas lacunas.

7. **Redimensionamento Padronizado:** Padronização dimensional para a resolução de $256 \times 256$ pixels (cv2.resize).

## 🚀 Como Executar o Projeto

### Pré-requisitos

- Python 3.8+ instalado

- Git instalado


## Execução Local (VSCode)

1. Clone o repositório:

```
git clone [https://github.com/SEU_USUARIO/projeto-visao-computacional.git](https://github.com/SEU_USUARIO/projeto-visao-computacional.git)
cd projeto-visao-computacional

```
2. Crie e ative um ambiente virtual:

```

python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate

```

3. Instale as dependências:


```
pip install -r requirements.txt

```
## Execução na Nuvem (Kaggle ou Google Colab)

1. Abra o arquivo notebooks/01_processamento_kaggle.ipynb no ambiente de sua escolha.

2. Sincronize o código do repositório clonando a branch development:

```

!git clone -b development [https://github.com/SEU_USUARIO/projeto-visao-computacional.git](https://github.com/SEU_USUARIO/projeto-visao-computacional.git)

```

3. Execute o script de leitura em lote apontando para o diretório das imagens de entrada e saída.

## 🌿 Versionamento e Branches

O fluxo de trabalho Git foi organizado em duas branches principais:

- `development:` Branch de desenvolvimento ativo onde os módulos `src/` e notebooks foram construídos iterativamente através de Sprints.

- `main:` Branch estável e consolidada contendo o código final pronto para produção e entrega.
