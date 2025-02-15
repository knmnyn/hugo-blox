---
title: 'UNO-DST: Leveraging Unlabelled Data in Zero-Shot Dialogue State Tracking'
authors:
- victor
- Yan Zhang
- min
- Haizhou Li
date: '2024-06-01'
publishDate: '2024-07-06T02:22:24.510368Z'
publication_types:
- paper-conference
publication: '*Findings of the Association for Computational Linguistics: NAACL 2024*'
abstract: Previous zero-shot dialogue state tracking (DST) methods only apply transfer
  learning, but ignore unlabelled data in the target domain.We transform zero-shot
  DST into few-shot DST by utilising such unlabelled data via joint and self-training
  methods. Our method incorporates auxiliary tasks that generate slot types as inverse
  prompts for main tasks, creating slot values during joint training. Cycle consistency
  between these two tasks enables the generation and selection of quality samples
  in unknown target domains for subsequent fine-tuning. This approach also facilitates
  automatic label creation, thereby optimizing the training and fine-tuning of DST
  models. We demonstrate this method′s effectiveness on general language models in
  zero-shot scenarios, improving average joint goal accuracy by 8% across all domains
  in MultiWOZ.
links:
- name: URL
  url: https://aclanthology.org/2024.findings-naacl.187
---
