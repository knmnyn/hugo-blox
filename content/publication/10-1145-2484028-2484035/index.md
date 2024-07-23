---
title: 'Addressing cold-start in app recommendation: latent user models constructed
  from twitter followers'
authors:
- Jovian Lin
- Kazunari Sugiyama
- Min-Yen Kan
- Tat-Seng Chua
date: '2013-01-01'
publishDate: '2024-07-23T15:26:59.107639Z'
publication_types:
- paper-conference
publication: '*Proceedings of the 36th International ACM SIGIR Conference on Research
  and Development in Information Retrieval*'
doi: 10.1145/2484028.2484035
abstract: As a tremendous number of mobile applications (apps) are readily available,
  users have difficulty in identifying apps that are relevant to their interests.
  Recommender systems that depend on previous user ratings (i.e., collaborative filtering,
  or CF) can address this problem for apps that have sufficient ratings from past
  users. But for apps that are newly released, CF does not have any user ratings to
  base recommendations on, which leads to the cold-start problem.In this paper, we
  describe a method that accounts for nascent information culled from Twitter to provide
  relevant recommendation in such cold-start situations. We use Twitter handles to
  access an app's Twitter account and extract the IDs of their Twitter-followers.
  We create pseudo-documents that contain the IDs of Twitter users interested in an
  app and then apply latent Dirichlet allocation to generate latent groups. At test
  time, a target user seeking recommendations is mapped to these latent groups. By
  using the transitive relationship of latent groups to apps, we estimate the probability
  of the user liking the app. We show that by incorporating information from Twitter,
  our approach overcomes the difficulty of cold-start app recommendation and significantly
  outperforms other state-of-the-art recommendation techniques by up to 33%.
tags:
- twitter
- recommender systems
- mobile apps
- latent user models
- collaborative filtering
- cold-start problem
links:
- name: URL
  url: https://doi.org/10.1145/2484028.2484035
---
