---
title: 'BiRank: Towards Ranking on Bipartite Graphs'
authors:
- Xiangnan He
- Ming Gao
- Min-Yen Kan
- Dingxian Wang
date: '2017-01-01'
publishDate: '2024-07-23T15:26:59.196448Z'
publication_types:
- article-journal
publication: '*IEEE Trans. on Knowl. and Data Eng.*'
doi: 10.1109/TKDE.2016.2611584
abstract: "The bipartite graph is a ubiquitous data structure that can model the relationship
  between two entity types: for instance, users and items, queries and webpages. In
  this paper, we study the problem of ranking vertices of a bipartite graph, based
  on the graph's link structure as well as prior information about vertices (which
  we term a  query vector ). We present a new solution, BiRank, which iteratively
  assigns scores to vertices and finally converges to a unique stationary ranking.
  In contrast to the traditional random walk-based methods, BiRank iterates towards
  optimizing a regularization function, which smooths the graph under the guidance
  of the query vector. Importantly, we establish how BiRank relates to the Bayesian
  methodology, enabling the future extension in a probabilistic way. To show the rationale
  and extendability of the ranking methodology, we further extend it to rank for the
  more generic  $n$ -partite graphs. BiRank's generic modeling of both the graph structure
  and vertex features enables it to model various ranking hypotheses flexibly. To
  illustrate its functionality, we apply the BiRank and TriRank (ranking for tripartite
  graphs) algorithms to two real-world applications: a general ranking scenario that
  predicts the future popularity of items, and a personalized ranking scenario that
  recommends items of interest to users. Extensive experiments on both synthetic and
  real-world datasets demonstrate BiRank's soundness&nbsp;(fast convergence), efficiency&nbsp;(linear
  in the number of graph edges), and effectiveness&nbsp;(achieving state-of-the-art
  in the two real-world tasks)."
links:
- name: URL
  url: https://doi.org/10.1109/TKDE.2016.2611584
---
