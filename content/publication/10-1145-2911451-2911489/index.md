---
title: Fast Matrix Factorization for Online Recommendation with Implicit Feedback
authors:
- xiangnanhe
- Hanwang Zhang
- min
- Tat-Seng Chua
date: '2016-01-01'
publishDate: '2024-07-23T15:26:59.071156Z'
publication_types:
- paper-conference
publication: '*Proceedings of the 39th International ACM SIGIR Conference on Research
  and Development in Information Retrieval*'
doi: 10.1145/2911451.2911489
abstract: This paper contributes improvements on both the effectiveness and efficiency
  of Matrix Factorization (MF) methods for implicit feedback. We highlight two critical
  issues of existing works. First, due to the large space of unobserved feedback,
  most existing works resort to assign a uniform weight to the missing data to reduce
  computational complexity. However, such a uniform assumption is invalid in real-world
  settings. Second, most methods are also designed in an offline setting and fail
  to keep up with the dynamic nature of online data. We address the above two issues
  in learning MF models from implicit feedback. We first propose to weight the missing
  data based on item popularity, which is more effective and flexible than the uniform-weight
  assumption. However, such a non-uniform weighting poses efficiency challenge in
  learning the model. To address this, we specifically design a new learning algorithm
  based on the element-wise Alternating Least Squares (eALS) technique, for efficiently
  optimizing a MF model with variably-weighted missing data. We exploit this efficiency
  to then seamlessly devise an incremental update strategy that instantly refreshes
  a MF model given new feedback. Through comprehensive experiments on two public datasets
  in both offline and online protocols, we show that our implemented, open-source
  (https://github.com/hexiangnan/sigir16-eals) eALS consistently outperforms state-of-the-art
  implicit MF methods.
tags:
- ALS
- coordinate descent
- implicit feedback
- item recommendation
- matrix factorization
- online learning
links:
- name: URL
  url: https://doi.org/10.1145/2911451.2911489
---
