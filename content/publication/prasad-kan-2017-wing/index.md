---
title: 'WING-NUS at SemEval-2017 Task 10: Keyphrase Extraction and Classification
  as Joint Sequence Labeling'
authors:
- Animesh Prasad
- min
date: '2017-08-01'
publishDate: '2024-07-11T07:40:56.382115Z'
publication_types:
- paper-conference
publication: '*Proceedings of the 11th International Workshop on Semantic Evaluation
  (SemEval-2017)*'
doi: 10.18653/v1/S17-2170
abstract: We describe an end-to-end pipeline processing approach for SemEval 2017′s
  Task 10 to extract keyphrases and their relations from scientific publications.
  We jointly identify and classify keyphrases by modeling the subtasks as sequential
  labeling. Our system utilizes standard, surface-level features along with the adjacent
  word features, and performs conditional decoding on whole text to extract keyphrases.
  We focus only on the identification and typing of keyphrases (Subtasks A and B,
  together referred as extraction), but provide an end-to-end system inclusive of
  keyphrase relation identification (Subtask C) for completeness. Our top performing
  configuration achieves an $F_1$ of 0.27 for the end-to-end keyphrase extraction
  and relation identification scenario on the final test data, and compares on par
  to other top ranked systems for keyphrase extraction. Our system outperforms other
  techniques that do not employ global decoding and hence do not account for dependencies
  between keyphrases. We believe this is crucial for keyphrase classification in the
  given context of scientific document mining.
links:
- name: URL
  url: https://aclanthology.org/S17-2170
---
