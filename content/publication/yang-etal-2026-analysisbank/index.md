---
title: 'AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation'
authors:
- yajing
- yunshan
- kelvin
- min
date: '2026-09-01'
publishDate: '2026-09-01T00:00:00Z'
publication_types:
- paper-conference
publication: 'In *Proceedings of the 2026 Conference on Empirical Methods in Natural Language Processing (EMNLP 2026)*'
publication_short: '*EMNLP 2026*'
doi: 10.48550/arXiv.2609.00818
abstract: We argue that financial report generation should operate at the analytical rather than structural level, composing content from data-derived insights rather than high-level topics or sections. To this end, we propose AnalysisBank, which distills expert reports into a reusable library of Analyses, each pairing a data signal, an analytical move, and the expert span it was derived from. At inference time, AnalysisBank matches input signals to library entries and applies the retrieved moves to compose the report. A study of Analyses distilled from 550 expert reports reveals a heavy-tailed distribution of 47-52 signal types spanning 13 move types. On two financial benchmarks across four LLM backbones, AnalysisBank increases the proportion of novel, data-grounded insights by 1.7-3.7x over structural-level baselines. Transfer to scientific writing suggests that the distinction generalizes beyond finance. Code and the distilled Analysis library are available at https://github.com/yajingyang/AnalysisBank.
summary: 'A library of expert analysis patterns, distilled from financial reports, that grounds LLM report generation in data-derived insights.'
tags: ["Data-to-text", "Complex Reasoning", "LLMs", "Financial NLP"]
links:
- name: arXiv
  url: https://arxiv.org/abs/2609.00818
url_pdf: 'https://arxiv.org/pdf/2609.00818v1'
url_code: 'https://github.com/yajingyang/AnalysisBank'
# url_slides: ''
projects:
- analytical-reporting
---
