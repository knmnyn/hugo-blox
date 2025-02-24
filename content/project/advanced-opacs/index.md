---
title: Re-engineering the OPAC User Interface

summary: Envisioning the Library Catalog in a tabbed, Overview plus Details framework.
abstract: Our solution is to teach the library patron to use advanced query syntax and to formulate more precise queries. However, this solution is both labor-intensive for library staff and time-intensive for patrons.  We have examined how to re-engineer and design the User Interface to better supoort the actual information seeking methods used by library patrons.  

tags: ["NLP", "HCI", "Digital Libraries", "Visualization", "Viz"]
year: 2007-07-01
# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2004-06-04
date_end: '2007-07-01'
all_day: true

# Is this a featured project? (true/false)
featured: true
image:
  caption: 'Image credit: Jesse Gozali Prabawa'
  focal_point: Right
url_code: ''
url_pdf: 'https://wing.comp.nus.edu.sg/publication/10-1145-1255175-1255239/'
url_slides: ''
url_video: ''

# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
# slides:

authors: ["min", "jessegozali", "sirutan", "meichanng", "kalpanakumar", "longqiu"]

---
When library patrons utilize an online public access catalog (OPAC), they tend to type very few query words. Although it has been observed that patrons often have specific information needs, current search engine usability encourages users to underspecify their queries. With an OPAC's fast response times and the difficulty of using more advanced query operators, users are pushed towards a probe-and-browse mode of information seeking. Additionally, patrons have adapted (or forced to adapt) to OPACs and give keywords as their queries, rather than more precise queries. As a consequence, the search results often only approximate the patron's information need, missing crucial resources that may have been phrased differently or offering search results that may be phrased exactly as wanted but which only address the patron's information need tangentially.

One solution is to teach the library patron to use advanced query syntax and to formulate more precise queries. However, this solution is both labor-intensive for library staff and time-intensive for patrons. Furthermore, different OPACs support different levels of advanced capabilities and often represent these operators with different syntax. An alternative solution that we propose is the use of advanced query analysis and query expansion. Rather than change the behavior of the patron, a system can analyze their keyword queries to infer more precise queries that uses advanced operators when appropriate. To make these inferences, the system will not only rely on logic but also will dynamically access both a) historical query logs and b) the library catalog to assess the feasibility of its suggestions.
The proposed research will target three different types of query rewriting/expansion: 1) correction of misspellings, 2) inferring the relationships between a query's noun and noun phrases, and 3) inferring intended advanced query syntax. The realization of these techniques will allow patrons to continue using OPACs by issuing simple keyword searchers while benefiting from more precise querying and alternative search suggestions that would originate from the implemented system.

 In our current work we have examined how to re-engineer and design the User Interface to better supoort the actual information seeking methods used by library patrons.  Jesse has re-engineered the work and has incorporated our own NUS OPAC as well as Colorado State University's OPAC results into his tabbed, overview+details framework.  If you have a library catalog with MARC21 results that can be exported we can wrap our UI around your database.  Contact us for more information.

 In collaboration with Prof. Danny C. C. Poo.
