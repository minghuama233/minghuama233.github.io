# minghuama233.github.io

Personal academic website for **Dr. Minghua Ma**, Senior Researcher at Microsoft.

Pure HTML/CSS/JS — no build step required. Deployed via GitHub Pages.

## Structure

```
index.html             # Single-page site (About, News, Experience, Awards, Teaching, Services, Publications)
data/publications.yml  # All publications data (YAML, loaded client-side via js-yaml)
assets/css/main.css    # Stylesheet
assets/js/main.min.js  # Nav, greedy-nav, theme toggle
assets/js/theme.js     # Dark/light mode persistence
assets/webfonts/       # Font Awesome icons
images/                # Photos, favicon
```

## Adding a Publication

Add a new entry to `data/publications.yml`:

```yaml
- title: "Your Paper Title"
  topic: AI Agents
  authors: "Author One, Minghua Ma*"
  category: conference
  venue: "ICSE'26"
  paper: "https://arxiv.org/abs/..."
  code: "https://github.com/..."
  homepage: "https://project-page.github.io/"
  bibtex: |-
    @inproceedings{key2026,
      title={Your Paper Title},
      author={...},
      booktitle={...},
      year={2026}
    }
```

Fields (`*` = required):

| Field | Description |
|-------|-------------|
| `title`* | Paper title |
| `authors`* | Author string; use `*` for corresponding author (e.g. `Minghua Ma*`). `Minghua Ma` is auto-bolded in rendering |
| `category`* | `conference` \| `journal` \| `workshop` \| `preprint` |
| `topic`* | Research topic, used for grouping (e.g. `incident management`, `AI Agents`, `Survey/Benchmark`, `anomaly detection`) |
| `venue` | Short venue label, e.g. `FSE'26` |
| `paper` | URL to paper PDF / preprint |
| `code` | URL to code repository |
| `dataset` | URL to dataset |
| `homepage` | URL to project homepage |
| `bibtex` | BibTeX citation (multiline with `\|-`) |
| `award` | Award text, shown highlighted |


