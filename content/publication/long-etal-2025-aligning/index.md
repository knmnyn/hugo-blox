---
title: "Aligning Large Language Models with Human Opinions through Persona Selection and Value–Belief–Norm Reasoning"
subtitle: ""
authors:
- long
- Kenji Kawaguchi
- min
- Nancy F. Chen

doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: '2025-01'
publication_types: ['paper-conference']

# Publication name and optional abbreviated publication name.
publication: In *31st International Conference on Computational Linguistics*
publication_short: In *COLING 2025*

abstract: "Reasoning and predicting human opinions with large language models (LLMs) is essential yet challenging. Current methods employ role-playing with personae but face two major issues: LLMs are sensitive to even a single irrelevant persona, skewing predictions by up to 30%; and LLMs fail to reason strategically over personae. We propose Chain-of-Opinion (COO), a simple four-step solution modeling which and how to reason with personae, inspired by the Value–Belief–Norm (VBN) theory. COO differentiates between explicit personae (demographics and ideology) and implicit personae (historical opinions), involves: (1) filtering irrelevant attributes from explicit personae; (2) ranking implicit personae into a preferential list for selecting top-k; (3) applying novel VBN reasoning to extract user environmental and personal value, belief, and norm variables for accurate and reliable predictions; and (4) iterating VBN reasoning with progressively larger lists of implicit personae to handle potential persona insufficiency. COO efficiently achieves new state-of-the-art opinion prediction via prompting with only 5 inference calls, improving prior techniques by up to 4%. Notably, fine-tuning LMs with COO’s data results in significantly better opinion-aligned models, by up to 23%."

# Display this page in the Featured widget?
featured: true

url_pdf: 'https://aclanthology.org/2025.coling-main.172.pdf'
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

image:
  preview_only: false
---