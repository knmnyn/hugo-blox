---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: hero
    content:
      title: |
        Web IR / NLP Group (WING) @ NUS
      image:
        filename: welcome.jpg
      text: |
        The <strong>Web, Information Retrieval / Natural Language Processing Group (WING)</strong> explores the research area of applied language processing and information retrieval to the Web and related technologies. Areas of current interest are question answering, scholarly digital libraries, verb similarity, focused crawling, citation parsing and spidering, web page classification and division, text segmentation, and full text analysis. WING is headed by <A HREF="author/min-yen-kan">Min</a> (A/P Min-Yen KAN). We are based in the Computational Linguistics Laboratory of the <a href="https://www.comp.nus.edu.sg">School of Computing</a> at the National University of Singapore. We often work with the Natural Language Processing Group and the <a href="https://lms.comp.nus.edu.sg/">Lab for Media Search</a>. We are part of the Media Technologies research group umbrella.
  
  - block: collection
    content:
      title: Latest News
      subtitle:
      text:
      count: 5
      filters:
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: ''
      offset: 0
      order: desc
      page_type: post
    design:
      view: card
      columns: '1'
  
  - block: markdown
    content:
      title:
      subtitle: ''
      text:
    design:
      columns: '1'
      background:
        image: 
          filename: acl24.jpg
          filters:
            brightness: 1
          parallax: false
          position: center
          size: cover
          text_color_light: true
      spacing:
        padding: ['20px', '0', '20px', '0']
      css_class: fullscreen

  - block: collection
    content:
      title: Latest Preprints
      text: ""
      count: 5
      filters:
        folders:
          - publication
        publication_type: 'article'
    design:
      view: citation
      columns: '1'

  - block: markdown
    content:
      title:
      subtitle:
      text: |
        {{% cta cta_link="./people/" %}}
    design:
      columns: '1'
---
