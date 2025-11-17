---
title: Team
seo_title: "Social Interaction & Neural Computation Lab Members"
nav:
  order: 3
  tooltip: "Who we are"
---

# {% include icon.html icon="fa-solid fa-users" %}Our Team

{% include list.html data="team" component="portrait" filter="role == 'principal-investigator'" %}
{% include list.html data="team" component="portrait" filter="role == 'laboratory-manager'" %}
{% include list.html data="team" component="portrait" filter="role == 'research-assistant'" %}

{% include section.html %}

# {% include icon.html icon="fa-solid fa-users" %}Our Collaborators

[Abigail A. Marsh, Ph.D.](https://abigailmarsh.com/) (Georgetown University)

[Xiaosi Gu, Ph.D.](https://www.neurocpu.org/) (Icahn School of Medicine at Mount Sinai)

[Ignacio Saez, Ph.D.](https://www.thesaezlab.com/) (Icahn School of Medicine at Mount Sinai)

[Salman Qasim, Ph.D.](https://sites.rutgers.edu/qasim-lab/) (Rutgers University)

[Blair Shevlin, Ph.D.](https://blairshevlin.github.io/) (Icahn School of Medicine at Mount Sinai)

[Patricia L. Lockwood, Ph.D.](https://www.sdn-lab.org/) (University of Birmingham)

[Jo Cutler, Ph.D.](https://www.jocutler.com/) (University of Birmingham)

[Mark K. Ho, Ph.D.](https://codec-lab.github.io/) (New York University)

[Marla Dressel]() (Georgetown University)

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