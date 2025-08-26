---
title: "Self-Improving and Self-Adapting Agents"

summary: "We study test-time methods for self‑improving and self‑adapting agents which represent an emerging frontier of artificial intelligence in which autonomous systems can not only perform tasks but also learn from interactions, refine their own behaviors, and even modify their own code or learning processes over time."
abstract: "As large language models (LLMs) are increasingly deployed in open-ended settings, understanding and improving their behavior through test-time methods has become a central challenge. In this work, we examine how LLMs can self-adapt and self-improve without additional training through structured test-time interventions. First, we propose a human- and property-centric evaluation framework grounded in a meta-analysis of over 150 papers, identifying 21 core properties of natural language prompts and analyzing their underexplored influence across models and tasks. Building on these insights, we introduce LongGuide, a method that automatically generates dual-stream guidelines to steer generation toward desired language and output distributions. We further present the first systematic study of format bias in LLMs and propose actionable strategies to reduce over-reliance on superficial input formats. To enhance reasoning and robustness, we propose Multi-expert input modeling, which simulates collaborative agent decision-making, and Adversarial In-Context Learning, a competitive setup that iteratively refines inputs through generator–discriminator interactions. Across 20+ tasks, these methods significantly outperform strong baselines in truthfulness, generalization, and robustness. Our findings offer a comprehensive foundation for building adaptable LLM agents that improve through interaction, feedback, and structure-aware test-time methods—without reliance on additional gradient-based training."

tags: ["Multi-Agent System", "Evolution", "LLM", "Machine Learning"]
year: 2025
date: '2025-08-01' 

all_day: true

# Is this a featured project? (true/false)
featured: true
# image:
#   caption: 'The workflow of Discursive Socratic Questioning (left) and the evaluation results (right).'
#   focal_point: Right
url_pdf: 'https://arxiv.org/abs/2506.06950'  # Replace with actual publication URL
# url_slides: 'https://your-slides-url.pdf'  # Optional: link to presentation slides
# url_video: ''

# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
# slides:

authors: ["long", "hai", "duy", "trong", "wangyiwen", "anhnguyen", "min"]

---

We study test-time methods for self‑improving and self‑adapting agents which represent an emerging frontier of artificial intelligence in which autonomous systems can not only perform tasks but also learn from interactions, refine their own behaviors, and even modify their own code or learning processes over time.

As large language models (LLMs) are increasingly deployed in open-ended settings, understanding and improving their behavior through test-time methods has become a central challenge. In this work, we examine how LLMs can self-adapt and self-improve without additional training through structured test-time interventions. First, we propose a human- and property-centric evaluation framework grounded in a meta-analysis of over 150 papers, identifying 21 core properties of natural language prompts and analyzing their underexplored influence across models and tasks. Building on these insights, we introduce LongGuide, a method that automatically generates dual-stream guidelines to steer generation toward desired language and output distributions. We further present the first systematic study of format bias in LLMs and propose actionable strategies to reduce over-reliance on superficial input formats. To enhance reasoning and robustness, we propose Multi-expert input modeling, which simulates collaborative agent decision-making, and Adversarial In-Context Learning, a competitive setup that iteratively refines inputs through generator–discriminator interactions. Across 20+ tasks, these methods significantly outperform strong baselines in truthfulness, generalization, and robustness. Our findings offer a comprehensive foundation for building adaptable LLM agents that improve through interaction, feedback, and structure-aware test-time methods—without reliance on additional gradient-based training.