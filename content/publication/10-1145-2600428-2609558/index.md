---
title: Predicting the popularity of web 2.0 items based on user comments
authors:
- Xiangnan He
- Ming Gao
- min
- Yiqun Liu
- kaz
date: '2014-01-01'
publishDate: '2024-07-23T15:26:59.152586Z'
publication_types:
- paper-conference
publication: '*Proceedings of the 37th International ACM SIGIR Conference on Research
  & Development in Information Retrieval*'
doi: 10.1145/2600428.2609558
abstract: In the current Web 2.0 era, the popularity of Web resources fluctuates ephemerally,
  based on trends and social interest. As a result, content-based relevance signals
  are insufficient to meet users' constantly evolving information needs in searching
  for Web 2.0 items. Incorporating future popularity into ranking is one way to counter
  this. However, predicting popularity as a third party (as in the case of general
  search engines) is difficult in practice, due to their limited access to item view
  histories. To enable popularity prediction externally without excessive crawling,
  we propose an alternative solution by leveraging user comments, which are more accessible
  than view counts. Due to the sparsity of comments, traditional solutions that are
  solely based on view histories do not perform well. To deal with this sparsity,
  we mine comments to recover additional signal, such as social influence. By modeling
  comments as a time-aware bipartite graph, we propose a regularization-based ranking
  algorithm that accounts for temporal, social influence and current popularity factors
  to predict the future popularity of items. Experimental results on three real-world
  datasets --- crawled from YouTube, Flickr and Last.fm --- show that our method consistently
  outperforms competitive baselines in several evaluation tasks.
tags:
- bipartite graph ranking
- buir
- comments mining
- item ranking
- popularity prediction
links:
- name: URL
  url: https://doi.org/10.1145/2600428.2609558
---
