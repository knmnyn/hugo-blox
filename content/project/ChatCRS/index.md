---
title: ChatCRS:Incorporating External Knowledge and Goal Guidance for LLM-based Conversational Recommender Systems

summary: We incoporate external knowledge and gols for better CRS. 
abstract: "This paper aims to efficiently enable large language models (LLMs) to use external knowledge and goal guidance in conversa- tional recommender system (CRS) tasks. Advanced LLMs (e.g., ChatGPT) are limited in domain-specific CRS tasks for 1) generating grounded responses with recommendation- oriented knowledge, or 2) proactively leading the conversations through different dialogue goals. In this work, we first analyze those limitations through a comprehensive evaluation, showing the necessity of external knowledge and goal guidance which contribute sig- nificantly to the recommendation accuracy and language quality. In light of this finding, we propose a novel ChatCRS framework to decompose the complex CRS task into several sub-tasks through the implementation of 1) a knowledge retrieval agent using a tool-augmented approach to reason over external knowledge bases and 2) a goal-planning agent for dialogue goal prediction. Incorporating those external inputs, LLMs proactively plan interactions and generate outputs with rich information. Experiments on two multi-goal CRS datasets reveal that ChatCRS sets new state-of-the-art benchmarks, improving language quality of informativeness by 17% and proactivity by 27%, with tenfold recommendation accuracy enhancement"

tags: [ "NLP", "LLM", "Conversational Recommendation"]
year: 2025

date: '2025-05-01' # LREC-COLING 24's conference date. 

all_day: true

# Is this a featured project? (true/false)
featured: true
image:
  caption: 'Overall framework of ChatCRS'
  focal_point: Right
url_pdf: 'https://arxiv.org/abs/2405.01868'
url_code: 'https://github.com/lichuangnus/ChatCRS'

# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
# slides:

authors: ["victor", "hengchang", "min"]

---

