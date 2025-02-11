---
title: Team
nav:
  order: 3
  tooltip: "Who we are"
---

# {% include icon.html icon="fa-solid fa-users" %}Our Team

{% include list.html data="members" component="portrait" filter="role == 'principal-investigator'" %}
{% include list.html data="members" component="portrait" filter="role != 'principal-investigator'" %}

{% include section.html %}

# {% include icon.html icon="fa-solid fa-users" %}Our Collaborators

Abigail A. Marsh, Ph.D. (Georgetown University)

Xiaosi Gu, Ph.D. (Icahn School of Medicine at Mount Sinai)

Ignacio Saez, Ph.D. (Icahn School of Medicine at Mount Sinai)

Salman Qasim, Ph.D. (Rutgers University)

Blair Shevlin, Ph.D. (Icahn School of Medicine at Mount Sinai)

Patricia L. Lockwood, Ph.D. (University of Birmingham)

Jo Cutler, Ph.D. (University of Birmingham)

Mark K. Ho, Ph.D. (New York University)

{% include section.html %}

# {% include icon.html icon="fa-solid fa-users" %}Our Partners

{% capture col1 %}

{%
  include figure.html
  image="images/ccp.jpg"
  caption="Center for Computational Psychiatry"
  link="https://icahn.mssm.edu/research/center-for-computational-psychiatry"
%}

{% endcapture %}

{% capture col2 %}

{%
  include figure.html
  image="images/fbi.jpg"
  caption="Friedman Brain Institute"
  link="https://icahn.mssm.edu/research/friedman"
%}

{% endcapture %}

{% include cols.html col1=col1 col2=col2 %}