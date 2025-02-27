---
title: TART – An Open-Source Tool-Augmented Framework for Explainable Table-Based Reasoning

summary: A framework integrating LLMs with external tools to enhance explainability and accuracy in table-based reasoning tasks.
abstract: "Large Language Models (LLMs) often struggle with table structures and precise numerical reasoning, which are crucial for tasks such as table question answering (TableQA) and table-based fact verification (TableFV). To address these limitations, we introduce the **Tool-Augmented Reasoning framework for Tables (TART)**, which integrates LLMs with specialized tools to enhance explainability and reasoning accuracy. TART consists of three components: (1) a **Table Formatter** to ensure structured table representation, (2) a **Tool Maker** to generate task-specific computational functions, and (3) an **Explanation Generator** to maintain human-interpretable reasoning. Additionally, we introduce **TOOLTAB**, a new dataset benchmark tailored for training LLMs in table–tool integration. Our results demonstrate that TART achieves significant improvements over standard Chain-of-Thought (CoT) prompting, achieving near-parity with GPT-3.5-turbo when paired with **CodeLlama**."

tags: ["Table Reasoning", "Explainability", "LLMs", "Fact-Checking", "Tool Learning"]
year: 2025

date: '2025-04-29'  # NAACL 2025 conference date.

all_day: true

# Is this a featured project? (true/false)
featured: true
image:
  caption: 'Overview of the TART framework showing Table Formatter, Tool Maker, and Explanation Generator.'
  focal_point: Right
url_pdf: 'https://arxiv.org/abs/2409.11724'
url_slides: 'https://drive.google.com/file/d/1QrLCPdd0qxljgXnssCI8bsungjYXhCu8/view'
url_code: 'https://github.com/XinyuanLu00/TART'

# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
# slides:

authors: ["xinyuan", "liangming", "Yubo Ma", "Preslav Nakov","min"]

---
TART is designed to overcome the **limitations of LLMs in table reasoning** by combining **structured table processing, precise tool execution, and explainability**. The key components of TART are:

1. **Table Formatter**: Prepares tables by formatting, aligning, and cleaning the data for structured input.
2. **Tool Maker**: Dynamically generates tools (Python functions) tailored for complex table operations.
3. **Explanation Generator**: Integrates structured reasoning steps and tool outputs into human-readable explanations.

TART is evaluated on **nine table-based reasoning benchmarks**, including **SCITAB, TabFact, FinQA, and HybridQA**. The framework consistently outperforms Chain-of-Thought (CoT) prompting by integrating structured tool-assisted reasoning.

TART has received the **Best Paper Runner-Up Award** at the [3rd Table Representation Learning Workshop](https://table-representation-learning.github.io/NeurIPS2024/) at NeurIPS 2024 and has been accepted at **NAACL 2025**. Its code and dataset are publicly available for further research. Researchers working on LLM explainability, table reasoning, and AI-assisted fact-checking are encouraged to contribute.
