# Lista 09 — Jogo do Puzzle de 8 Peças 🧩

## 🎯 Objetivo

Este projeto tem como foco a criação de um **jogo interativo do 8-Puzzle**, utilizando diferentes algoritmos de busca para encontrar a solução ideal. A proposta exige a implementação de **pelo menos três métodos de busca**, incluindo obrigatoriamente o **A\*** com **duas heurísticas distintas**.

### O que foi feito:

* Desenvolvimento da interface gráfica do jogo;
* Implementação dos seguintes algoritmos de busca:

  * Busca em Largura (BFS)
  * Busca em Profundidade (DFS)
  * A\* com duas heurísticas diferentes
* Elaboração de um relatório comparando o desempenho de cada método.

---

## 🧠 Algoritmos de Busca Implementados

* **Busca em Largura (BFS)**: explora todos os estados no mesmo nível antes de ir mais fundo.
* **Busca em Profundidade (DFS)**: mergulha fundo no grafo, podendo ser arriscada sem um limite de profundidade.
* **A\***: combina custo acumulado + heurística (f(n) = g(n) + h(n)) para decisões mais equilibradas.

---

## 📏 Heurísticas Utilizadas

Para as buscas com heurística (A\*), foram testadas:

1. **Número de peças fora do lugar**: simples e direta, oferece soluções rápidas, mas não necessariamente eficientes.
2. **Distância de Manhattan**: soma das distâncias verticais e horizontais das peças até suas posições corretas — mais precisa na maioria dos casos.

---

## 📄 Sobre o Relatório

O relatório detalhado acompanha a análise dos resultados obtidos com cada método e inclui:

* Explicações claras dos algoritmos e heurísticas;
* Comparações com os mesmos estados iniciais;
* Avaliação de tempo de execução;
* Observações sobre eficiência e escalabilidade;
* Considerações finais sobre o melhor desempenho.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem**: Python 🐍
* **Interface Gráfica**: Tkinter 🎨

---

## 📁 Estrutura do Projeto

```
8puzzle/
│
├── 8puzzle.exe          # Executável do jogo
├── __init__.py
├── main.py
├── build_exe.py         # Script para gerar o executável
├── requirements.txt
├── puzzle/              # Lógica do jogo e manipulação de estados
│   ├── state.py
│   ├── actions.py
│   ├── heuristics.py
│   └── algorithms.py
├── search/              # Implementações dos algoritmos
│   ├── bfs.py
│   ├── dfs.py
│   └── astar.py
├── heuristics/          # Heurísticas específicas
│   ├── misplaced.py
│   └── manhattan.py
├── gui/                 # Interface gráfica
│   └── app.py
├── utils/               # Funções auxiliares
│   └── util.py
├── icon.ico             # Ícone do executável
├── .gitignore
└── README.md
```
