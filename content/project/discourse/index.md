---
title: Discourse and LLMs

summary: We measure and enhance LLMs' discourse understanding and reasoning faithfulness.
abstract: "While large language models have significantly enhanced the effectiveness of discourse relation classifications, it remains unclear whether their comprehension is faithful and reliable. We provide DiSQ, a new method for evaluating the faithfulness of understanding discourse based on question answering. We first employ in-context learning to annotate the reasoning for discourse comprehension, based on the connections among key events within the discourse. Following this, DiSQ interrogates the model with a sequence of questions to assess its grasp of core event relations, its resilience to counterfactual queries, as well as its consistency to its previous responses. We then evaluate language models with different architectural designs using DiSQ, finding: (1) DiSQ presents a significant challenge for all models, with the top-performing GPT model attaining only 41% of the ideal performance in PDTB; (2) DiSQ is robust to domain shifts and paraphrase variations; (3) Open-source models generally lag behind their closed-source GPT counterparts, with notable exceptions being those enhanced with chat and code/math features; (4) Our analysis validates the effectiveness of explicitly signalled discourse connectives, the role of contextual information, and the benefits of using historical QA data."

tags: ["CL", "Discourse", "NLP", "LLM", "Computational Linguistics"]
year: 2024

date: '2024-08-11' # ACL 24's conference date. 

all_day: true

# Is this a featured project? (true/false)
featured: true
image:
  caption: 'The workflow of Discursive Socratic Questioning (left) and the evaluation results (right).'
  focal_point: Right
url_pdf: 'https://aclanthology.org/2024.acl-long.341/'
url_slides: 'https://yisong.me/publications/acl24-DiSQ-Slides.pdf'
url_code: 'https://github.com/YisongMiao/DiSQ-Score'
# url_video: ''

# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
# slides:

authors: ["yisong", "min"]

---
Yisong, a PhD student at WING, began his research journey by tackling the fundamental question: Do language models truly understand text? Over time, he refined this broad inquiry into the specific challenge of discourse understanding. In his recent work, advised by Prof. Min, they introduced a more precise framework for measuring discourse comprehension from three discourse-specific perspectives, while also contributing insights into broader LLM challenges such as logical consistency. Currently, Yisong and Min are delving deeper into the mechanisms behind how models process and understand discourse.
