---
title: WING Events

# Listing view
view: compact

# Optional header image (relative to `assets/media/` folder).
banner:
  caption: 'COM3 at Imagination Ridge, NUS'
  image: 'com3.jpg'

type: landing

sections:
  - block: slider
    content:
      slides:
      - title: ACL'24 @ Thailand
        content: "Current WING and alumni at ACL '24 in Thailand!"
        align: center
        background:
          image:
            filename: acl24.jpg
            filters:
              brightness: 0.7
          position: center
          color: '#666'
      - title: IT:U Austria Summer School
        content: "Min's invited talk on prompting at the IT:U Austria NLP Summer School"
        align: center
        background:
          image:
            filename: acl24-banner.jpg
            filters:
              brightness: 0.7
          position: center
          color: '#666'
      - title: WING Group Events
        content: "We had a fun BBQ at Yajing's condo!"
        align: center
        background:
          image:
            filename: com3.jpg
            filters:
              brightness: 0.7
          position: center
          color: '#666'
    design:
      slide_height: '400px'
      is_fullscreen: false
      loop: true
      interval: 3000

  - block: markdown
    content:
      title:
      subtitle: ''
      text: |
        WING members hosts, organises and participate in events related to natural language processing, information retrieval, digital libraries and Web research. Take a look at what's in store and the past events we've helped to host and organise.
    design:
      columns: '1'
      background:
        color: '#f8f9fa'
      spacing:
        padding: ['20px', '0', '20px', '0']

  - block: collection
    content:
      title: Featured Events
      text: ""
      count: 6
      filters:
        folders:
          - event
        featured: true
    design:
      view: card
      columns: '2'
