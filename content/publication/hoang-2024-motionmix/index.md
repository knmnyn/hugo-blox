---
title: "MotionMix: Weakly-Supervised Diffusion for Controllable Motion Generation"
subtitle: ""
authors:
- nhat
- Kehong Gong
- Chuan Guo
- Michael Bi Mi
author_notes: []
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: '2024-01-24T00:00:00Z'
publication_types: ['paper-conference']

# Publication name and optional abbreviated publication name.
publication: In *The 38th Annual AAAI Conference on Artificial Intelligence*
publication_short: In *AAAI 2024*

abstract: "Controllable generation of 3D human motions becomes an important topic as the world embraces digital transformation. Existing works, though making promising progress with the advent of diffusion models, heavily rely on meticulously captured and annotated (e.g., text) high-quality motion corpus, a resource-intensive endeavor in the real world. This motivates our proposed MotionMix, a simple yet effective weakly-supervised diffusion model that leverages both noisy and unannotated motion sequences. Specifically, we separate the denoising objectives of a diffusion model into two stages: obtaining conditional rough motion approximations in the initial T−T∗ steps by learning the noisy annotated motions, followed by the unconditional refinement of these preliminary motions during the last T∗ steps using unannotated motions. Notably, though learning from two sources of imperfect data, our model does not compromise motion generation quality compared to fully supervised approaches that access gold data. Extensive experiments on several benchmarks demonstrate that our MotionMix, as a versatile framework, consistently achieves state-of-the-art performances on text-to-motion, action-to-motion, and music-to-dance tasks."

# Display this page in the Featured widget?
featured: true

links:
- name: Project Page
  url: https://nhathoang2002.github.io/MotionMix-page/

url_pdf: 'https://arxiv.org/abs/2401.11115'
url_code: 'https://github.com/NhatHoang2002/MotionMix'
url_dataset: ''
url_poster: 'https://nhathoang2002.github.io/MotionMix-page/static/pdfs/MotionMix_poster.pdf'
url_project: ''
url_slides: ''
url_source: ''
url_video: 'https://nhathoang2002.github.io/MotionMix-page/static/videos/demo_vid.mp4'

image:
  caption: "Diffusion model trained with two sources of *imperfect* data while still achieving state-of-the-art performance on different motion generation tasks."
  preview_only: false
---