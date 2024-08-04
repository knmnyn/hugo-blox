---
title: 'The ELCo Dataset: Bridging Emoji and Lexical Composition'
# Zi Yun Yang, Ziqing Zhang, and Yisong Miao (2024) The ELCo Dataset: Bridging Emoji and Lexical Composition. In Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING '24).

authors:
  - ziyun
  - Ziqing Zhang
  - yisong

date: '2024-05-20T00:00:00Z'
doi: ''

# Schedule page publish date (NOT publication's date).
publishDate: '2017-01-01T00:00:00Z'
publication_types: ['paper-conference']

# Publication name and optional abbreviated publication name.
publication: In *In Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation*
publication_short: In *LREC-COLING 2024*

abstract: Can emojis be composed to convey intricate meanings like English phrases? As a pioneering study, we present the Emoji-Lexical Composition (ELCo) dataset, a new resource that offers parallel annotations of emoji sequences corresponding to English phrases. Our dataset contains 1,655 instances, spanning 209 diverse concepts from tangible ones like {``}right man{''} (✔️👨) to abstract ones such as {``}full attention{''} (🧐✍️, illustrating a metaphoric composition of a focusing face and writing hand). ELCo enables the analysis of the patterns shared between emoji and lexical composition. Through a corpus study, we discovered that simple strategies like direct representation and reduplication are sufficient for conveying certain concepts, but a richer, metaphorical strategy is essential for expressing more abstract ideas. We further introduce an evaluative task, Emoji-based Textual Entailment (EmoTE), to assess the proficiency of NLP models in comprehending emoji compositions. Our findings reveals the challenge of understanding emoji composition in a zero-shot setting for current models, including ChatGPT. Our analysis indicates that the intricacy of metaphorical compositions contributes to this challenge. Encouragingly, models show marked improvement when fine-tuned on the ELCo dataset, with larger models excelling in deciphering nuanced metaphorical compositions.

# Summary. An optional shortened abstract.
summary: Can emojis convey intricate meanings like English phrases? We present the Emoji-Lexical Composition (ELCo) dataset with 1,655 instances spanning 209 concepts, from tangible to abstract ideas. ELCo enables analysis of emoji and lexical composition. Our Emoji-based Textual Entailment (EmoTE) task reveals challenges for current models, but fine-tuning improves performance significantly.

tags: ["ELCo", "Emoji", "Natural Langauge Processing", "2024"]

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_pdf: 'https://aclanthology.org/2024.lrec-main.1381'
url_code: 'https://github.com/WING-NUS/ELCo'

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'A summary of the ELCo project. The ELCo dataset is comprised of 1,655 annotations of 209 EN phrases 45 adjectives and 77 attributes. Our corpus study reveals five structures to compose emoji compositions, and we show metaphorical structures use more diverse emojis. Our new EmoTE task is challenging for all models, but fine-tuning on ELCo helps to learn useful emoji composition skills. '
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects:
  - example

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
# slides: example
---
