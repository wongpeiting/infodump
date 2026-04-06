# The AI Race's Battle Lines Are Being Redrawn

A [scrollytelling data visualisation](https://wongpeiting.github.io/infodump/) remixing an infodump from this [Information is Beautiful chart on LLM models](https://informationisbeautiful.net/visualizations/the-rise-of-generative-ai-large-language-models-llms-like-chatgpt/). This is part of a class exercise in turning data-dense visualisations into more manageable narratives.

To break down the dense chart, I opened the piece with GPT-2 — OpenAI's last open-weight model before a six-year silence — as an animated character who introduces itself, then shrinks into its place among 258 benchmarked AI models. From there, the reader scrolls through the industry's split into open and closed camps, and watches as both sides cross the line.

The news peg is Alibaba's sudden pivot to closed-source models all of this week ([Bloomberg](https://www.bloomberg.com/news/articles/2026-04-02/alibaba-unveils-third-closed-source-ai-model-in-focus-on-profit)). I attempted to contrast it with OpenAI's move in the opposite direction last year, and flesh out its motivations then.

## Data

- **Source:** [LifeArchitect.ai Models Table](https://docs.google.com/spreadsheets/d/14KzlcYOK6Xj-_6N19T2Iqro4sGaAUOLD2FovSXyefUQ/edit?gid=426115144#gid=426115144) (Google Sheet downloaded as of April 4, 2026)
- **796 models** in the full dataset; **258 with published MMLU scores** shown in the scrolly chart
- **2 estimated entries** (Alibaba's Qwen3.6-Plus and Qwen3.5-Omni-Plus) — flagged in the data as `estimated: true`
- **Open-weight classification** derived from whether the model's playground URL points to HuggingFace (a proxy for downloadable weights)

## Project structure

```
infodump/
├── index.html          # The site (scrolly + article)
├── analysis.ipynb      # Data analysis and chart prototyping (Jupyter)
├── data/
│   ├── *.csv           # Raw source data
│   ├── models_data.json    # Processed (796 models)
│   ├── mmlu_data.json      # MMLU subset (260 models)
│   └── process_data.py     # CSV → JSON processing script
└── charts/
    ├── ai/             # Illustrator source files + ai2html config
    ├── ai2html-output/ # ai2html exports (HTML + PNGs)
    └── svg/            # Matplotlib SVG exports from notebook
```
