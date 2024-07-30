---
title: Data Augmentation Using Corner CutMix and an Auxiliary Self-Supervised Loss
subtitle: ""
authors:
- Fen Fang
- nhat
- Qianli Xu
- Joo-Hwee Lim

author_notes: []
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: '2023-10-08T17:06:11.943Z'
publication_types: ['1']

# Publication name and optional abbreviated publication name.
publication: In *2023 IEEE International Conference on Image Processing*
publication_short: In *ICIP 2023*

abstract: Deep convolutional neural networks (CNNs) have achieved remarkable success in computer vision tasks, but their training is susceptible to overfitting when the training sample size is insufficient. In this paper, we introduce Corner CutMix, a novel data augmentation technique for CNN training. During training, Corner CutMix randomly selects a region from one of four corner areas in an image and replaces it with a randomly chosen region from a distractor image. Additionally, we design an auxiliary self-supervised loss function to learn the position of the selected corner region, thereby improving the transferability and generalizability of the learned representation. Corner CutMix is easy to implement, adding little computational overhead, and can be combined with other augmentation methods such as random cropping, color distortion, and flipping. Our extensive classification task experiments in self-supervised learning on public datasets (e.g., CIFAR10, CIFAR100, and STL10) demonstrate the effectiveness of Corner CutMix, which consistently outperforms strong baselines such as CutOut and CutMix.

# Display this page in the Featured widget?
featured: true

url_pdf: 'https://doi.org/10.1109/ICIP49359.2023.10222009'
image:
  caption: "Visualization examples of Corner CutMix (CCM). The CCM can be directly applied to original images as well as combined with other augmentation methods including crop- ping, flipping and color distortion."
  preview_only: false
---