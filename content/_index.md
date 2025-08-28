---
# Leave the homepage title empty to use the site title
title: WING @ NUS
date: 2022-10-24
type: landing

sections:
  - block: hero
    content:
      title: "Web IR / NLP Group (WING) @ NUS"
      image:
        filename: welcome.jpg
#      text: 
#        The <strong>Web, Information Retrieval / Natural Language Processing Group (WING)</strong> explores the research area of applied language processing and information retrieval to the Web and related technologies. Areas of current interest are question answering, scholarly digital libraries, verb similarity, focused crawling, citation parsing and spidering, web page classification and division, text segmentation, and full text analysis. WING is headed by <A HREF="author/min-yen-kan">Min</a> (A/P Min-Yen KAN). We are based in the Computational Linguistics Laboratory of the <a href="https://www.comp.nus.edu.sg">School of Computing</a> at the National University of Singapore. We often work with the Natural Language Processing Group and the <a href="https://lms.comp.nus.edu.sg/">Lab for Media Search</a>. We are part of the Media Technologies research group umbrella.
  - block: markdown
    content:
      text: 'The **Web, Information Retrieval / Natural Language Processing Group (WING)** explores the research area of applied language processing and information retrieval to the Web and related technologies. Areas of current interest are question answering, scholarly digital libraries, verb similarity, focused crawling, citation parsing and spidering, web page classification and division, text segmentation, and full text analysis. WING is headed by <A HREF="author/min-yen-kan">Min</a> (A/P Min-Yen KAN). We are based in the Computational Linguistics Laboratory of the <a href="https://www.comp.nus.edu.sg">School of Computing</a> at the National University of Singapore. We often work with the Natural Language Processing Group and the <a href="https://lms.comp.nus.edu.sg/">Lab for Media Search</a>. We are part of the Media Technologies research group umbrella.'

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
      title: Latest Conference Publications
      text: ""
      count: 5
      filters:
        folders:
          - publication
        publication_type: 'paper-conference'
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
  - block: markdown
    content:
      title: Sponsors
      subtitle:
      text: |
        <div style="display:flex;flex-wrap:wrap;gap:16px;align-items:center;justify-content:center">
          <a href="https://csidm.sg/" target="_blank" rel="noopener">
            <img src="/assets/media/sponsors/csidmlogo.png" alt="CSIDM" style="height:56px"/>
          </a>
          <a href="https://next.comp.nus.edu.sg/" target="_blank" rel="noopener">
            <img src="/assets/media/sponsors/logo.png" alt="NUS Computing NEXT" style="height:48px"/>
          </a>
          <a href="https://www.crayondata.com/" target="_blank" rel="noopener">
            <img src="/assets/media/sponsors/Screen-Shot-2017-11-10-at-12.11.24-AM.png" alt="Crayon Data" style="height:40px"/>
          </a>
          <a href="https://www.intelllex.com/hello" target="_blank" rel="noopener">
            <img src="/assets/media/sponsors/52750-INTELLLEX-Logo-1.jpg" alt="INTELLLEX" style="height:56px"/>
          </a>
          <a href="https://www.microsoft.com/en-us/research/" target="_blank" rel="noopener">
            <img src="/assets/media/sponsors/MSRLogoDigitalBlack.png" alt="Microsoft Research" style="height:28px"/>
          </a>
          <a href="https://www.nvidia.com/content/global/global.php" target="_blank" rel="noopener">
            <img src="/assets/media/sponsors/1200px-Nvidia_image_logo.svg_.png" alt="NVIDIA" style="height:44px"/>
          </a>
          <a href="https://www.patsnap.com/" target="_blank" rel="noopener">
            <img src="/assets/media/sponsors/PatSnap_Logo_CMYK-1.png" alt="PatSnap" style="height:44px"/>
          </a>
          <a href="https://www.wsg.gov.sg/" target="_blank" rel="noopener">
            <img src="/assets/media/sponsors/WSG.jpg" alt="Workforce Singapore (WSG)" style="height:40px"/>
          </a>
          <a href="https://elsevier.com/" target="_blank" rel="noopener">
            <img src="/assets/media/sponsors/download.jpeg" alt="Elsevier" style="height:48px"/>
          </a>
          <a href="https://www.joinef.com/" target="_blank" rel="noopener">
            <img src="/assets/media/sponsors/EF_Solo_BlackJPG.jpg" alt="Entrepreneur First" style="height:40px"/>
          </a>
          <a href="https://ssi.nus.edu.sg/" target="_blank" rel="noopener">
            <img src="/assets/media/sponsors/ssi.png" alt="NUS Smart Systems Institute" style="height:40px"/>
          </a>
          <a href="https://www.nus.edu.sg/alset" target="_blank" rel="noopener">
            <img src="/assets/media/sponsors/Screen-Shot-2017-11-09-at-11.24.10-PM.png" alt="NUS ALSET" style="height:28px"/>
          </a>
        </div>
    design:
      columns: '1'
    spacing:
      padding: ['20px', '0', '20px', '0']
---
