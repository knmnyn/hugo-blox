---

title: A Comparative Analysis of Representation Flow in State-Space and Transformer Architectures

summary: We study the feature flow across layers in state-space models compared to Transformers.
abstract: State-space models (SSMs) have emerged as promising alternatives to Transformers, particularly for long-context tasks, due to their efficiency in modeling long-range dependencies through structured state transitions. While prior work has focused on interpreting final-layer outputs, this study investigates the feature flow across layers in SSMs. By comparing this behavior to Transformers, we show fundamental differences in how contextual information is encoded and propagated. Our analysis reveals trade-offs in efficiency and expressivity, offering a deeper understanding of learning dynamics in both architectures. This work not only advances our understanding of SSMs but also lays the foundation for designing hybrid models that combine the strengths of both paradigms.


tags: ["NLP", "State Space Model", "Interpretability"]
year: 2025  
# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with #.
date: '2025-01-01'
#date_end: '2004-12-31'
all_day: true

# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. slides = "example-slides" references content/slides/example-slides.md.
#   Otherwise, set slides = "".
# slides:

# authors: ["nhat", "long", "min", "Luu Anh Tuan"]
authors: 
- nhat
- long
- Anh Tuan Luu
- min

---
State-space models (SSMs) have emerged as promising alternatives to Transformers, particularly for long-context tasks, due to their efficiency in modeling long-range dependencies through structured state transitions. While prior work has focused on interpreting final-layer outputs, this study investigates the feature flow across layers in SSMs. By comparing this behavior to Transformers, we show fundamental differences in how contextual information is encoded and propagated. Our analysis reveals trade-offs in efficiency and expressivity, offering a deeper understanding of learning dynamics in both architectures. This work not only advances our understanding of SSMs but also lays the foundation for designing hybrid models that combine the strengths of both paradigms.
