# Boas-vindas ao repositório do TING (Trybe is not Google)!

Neste projeto, feito pela escola de desenvolvimento web Trybe, implementei um programa que simula um algoritmo de indexação de documentos similar ao do Google. O programa é capaz de identificar ocorrências de termos em arquivos _TXT_.
  
Para isso, o programa desenvolvido possui dois módulos:
- **Módulo de gerenciamento de arquivos** que permite anexar arquivos de texto (formato _TXT_) e;
- **Módulo de buscas** que permite operar funções de busca sobre os arquivos anexados.

## Habilidades exercitadas:

 - Manipular Pilhas;

 - Manipular Deque;

 - Manipular Nó & Listas Ligadas e;

 - Manipular Listas Duplamente Ligadas.
 
 # Orientações
<details>
  <summary><strong>⚠ Para rodar o projeto</strong></summary><br />

  1. Clone o repositório

  - Use o comando: `git clone git@github.com:Abreupamm/project-ting.git`
  - Entre na pasta do repositório que você acabou de clonar

  2. Crie o ambiente virtual python para o projeto

  - `python3 -m venv .venv && source .venv/bin/activate`

  3. Instale as dependências

  - `python3 -m pip install -r dev-requirements.txt`

  4. Crie uma branch a partir da branch `main`
 </details>
 
 ## O que desenvolvi:
  
  #### 1 - Implementei uma fila para armazenar os arquivos que serão lidos.
  
  - Implementei a classe `Queue`, presente no arquivo `queue.py`
  - A fila (Queue) é uma estrutura `FIFO`, ou seja, o primeiro item a entrar, deve ser o primeiro a sair.
  
  #### 2 - Implementei a função `txt_importer` dentro do módulo `file_management` capaz de importar notícias a partir de um arquivo TXT, utilizando "\n" como separador.
  
 #### 3 - Implementei a função `process` no módulo `file_process`. Essa função é capaz de transformar o conteúdo da lista gerada pela função `txt_importer` em um dicionário que será armazenado dentro da `Queue`.
 
#### 4 - Implementei a função `remove` dentro do módulo `file_process` capaz de remover o primeiro arquivo processado.

#### 5 - Implementei a função `file_metadata` dentro do módulo `file_process` capaz de apresentar as informações superficiais de um arquivo processado.

#### 6 - Implementei os testes para a classe `PriorityQueue` capaz de armazenar arquivos pequenos de forma prioritária.

#### 7 - Implementei a função `exists_word`, dentro do módulo `word_search`, que verifique a existência de uma palavra em todos os arquivos processados.

#### 8 - Implementei a função `search_by_word` dentro do módulo `word_search`, que busque uma palavra em todos os arquivos processados.
 
  
  
  
