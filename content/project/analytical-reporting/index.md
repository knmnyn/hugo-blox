---
title: "Analytical Report Generation with LLMs"

summary: A challenging dataset for compositional reasoning and claim verification on scientific tables.
abstract: "We introduce DATATALES, a novel benchmark designed to assess the proficiency of language models in data narration, a task crucial for transforming complex tabular data into accessible narratives. Existing benchmarks often fall short in capturing the requisite analytical complexity for practical applications. DATATALES addresses this gap by offering 4.9k financial reports paired with corresponding market data, showcasing the demand for models to create clear narratives and analyze large datasets while understanding specialized terminology in the field. Our findings highlight the significant challenge that language models face in achieving the necessary precision and analytical depth for proficient data narration, suggesting promising avenues for future model development and evaluation methodologies."

tags: ["Data-to-text", "Tables", "Complex Reasoning", "LLMs"]
year: 2024

date: '2024-11-12'  # EMNLP 2024 conference date.

all_day: true

# Is this a featured project? (true/false)
featured: true
image:
  caption: 'DATATALES example featuring a report and tabular data on 28 equity market entities, with 7 columns.'
  focal_point: Right
url_pdf: 'https://aclanthology.org/2024.emnlp-main.601/'
# url_slides: ''
url_code: 'https://github.com/yajingyang/DataTales/'

# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
# slides:

authors: ["yajing", "qian", "yunshan", "min"]

---
While LLMs excel in language understanding and can pass professional financial examinations, they struggle to generate expert-level analytical reasoning from real data. In this project, we explore analytical report generation using LLMs, turning complex market data and corporate disclosures into actionable, decision-relevant narratives. We first develop DataTales (EMNLP 2024), a benchmark pairing 4.9k financial market data tables with human reports to diagnose the exact gap between LLM generation and human creation. Secondly, we propose KAHAN (Findings of EMNLP 2025), a knowledge-augmented hierarchical analysis framework that coordinates analysis from entity metrics to market-wide patterns using executable code. Thirdly, we introduce AnalysisBank (EMNLP 2026), a distilled library of over 5,300 expert analysis patterns that conditions reasoning directly on observed data signals to generate novel, data-specific insights.

Yajing, a PhD student at WING and a Senior Data Scientist at Rio Tinto, started her research driven by the real-world business need for timely daily market reports. While working alongside market professionals, she observed how human commentary takes hours to draft while existing automation defaults to shallow summaries. Advised by Prof. Min-Yen Kan, she formalized this industry pain point into a systematic study of execution failures in generative models. Together with their collaborators, they developed structured methodologies to decouple calculation from composition and condition reasoning moves directly on observed data patterns. Their work demonstrates that grounded analytical depth can be systematically achieved across financial modalities and transferred to domains like medical diagnostics and scientific writing.
