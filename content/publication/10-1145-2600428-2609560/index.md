---
title: 'New and improved: modeling versions to improve app recommendation'
authors:
- Jovian Lin
- kaz
- min
- Tat-Seng Chua
date: '2014-01-01'
publishDate: '2024-07-23T15:26:59.189065Z'
publication_types:
- paper-conference
publication: '*Proceedings of the 37th International ACM SIGIR Conference on Research
  & Development in Information Retrieval*'
doi: 10.1145/2600428.2609560
abstract: Existing recommender systems usually model items as static -- unchanging
  in attributes, description, and features. However, in domains such as mobile apps,
  a version update may provide substantial changes to an app as updates, reflected
  by an increment in its version number, may attract a consumer's interest for a previously
  unappealing version. Version descriptions constitute an important recommendation
  evidence source as well as a basis for understanding the rationale for a recommendation.
  We present a novel framework that incorporates features distilled from version descriptions
  into app recommendation. We use a semi-supervised topic model to construct a representation
  of an app's version as a set of latent topics from version metadata and textual
  descriptions. We then discriminate the topics based on genre information and weight
  them on a per-user basis to generate a version-sensitive ranked list of apps for
  a target user. Incorporating our version features with state-of-the-art individual
  and hybrid recommendation techniques significantly improves recommendation quality.
  An important advantage of our method is that it targets particular versions of apps,
  allowing previously disfavored apps to be recommended when user-relevant features
  are added.
tags:
- version sensitive
- recommender systems
- mobile apps
- app store
links:
- name: URL
  url: https://doi.org/10.1145/2600428.2609560
---
