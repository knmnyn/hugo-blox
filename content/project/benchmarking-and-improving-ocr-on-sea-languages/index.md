---
title: Benchmarking and Improving OCR Systems for Southeast Asian Languages

summary: We benchmark and improve modern OCR systems on Southeast Asian languages.
abstract: While Optical Character Recognition (OCR) has been widely studied for high-resource languages such as English and Chinese, its performance on Southeast Asian (SEA) languages remains largely unexplored. This study addresses this gap by evaluating three OCR tools — EasyOCR, Tesseract, and the transformer-based General OCR Theory (GOT) — on English, Indonesian, Vietnamese, and Thai. We introduce a reusable pipeline for collecting textual data from Wikipedia and benchmarking OCR tools. Contrary to popular belief, our results show that OCR tools perform well on complex scripts like Vietnamese and Thai, with most errors arising from misclassifying characters outside the target language. Additionally, we demonstrate the effectiveness of fine-tuning GOT with limited training data, yielding notable improvements on Vietnamese and Thai.

tags: ["OCR", "SEA Languages", "NLP"]
year: 2024
# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: "2024-08-01"
date_end: "2025-05-01"
all_day: true

# Is this a featured project? (true/false)
featured: false
#image:
#  caption: 'Image credit: Jesse Gozali Prabawa'
#  focal_point: Right
url_pdf: "https://github.com/jasonqiu212/ocr-benchmarking-on-sea-languages/blob/main/docs/final-report/final-report.pdf"
url_slides: "https://github.com/jasonqiu212/ocr-benchmarking-on-sea-languages/blob/main/docs/slide-deck.pdf"
url_code: "https://github.com/jasonqiu212/ocr-benchmarking-on-sea-languages"

# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
# slides:

authors: ["jason", "tongyao", "min"]
---

While Optical Character Recognition (OCR) has been widely studied for high-resource languages such as English and Chinese, its performance on Southeast Asian (SEA) languages remains largely unexplored. This study addresses this gap by evaluating three OCR tools — EasyOCR, Tesseract, and the transformer-based General OCR Theory (GOT) — on English, Indonesian, Vietnamese, and Thai. We introduce a reusable pipeline for collecting textual data from Wikipedia and benchmarking OCR tools. Contrary to popular belief, our results show that OCR tools perform well on complex scripts like Vietnamese and Thai, with most errors arising from misclassifying characters outside the target language. Additionally, we demonstrate the effectiveness of fine-tuning GOT with limited training data, yielding notable improvements on Vietnamese and Thai.
