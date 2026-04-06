import csv
import json
import re
from datetime import datetime

models = []
month_map = {
    'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
    'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
}

with open('2026 LifeArchitect.ai data (shared) - NEW - Models Table.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    rows = list(reader)

# Data starts at row 10 (0-indexed), after multi-line header
for row in rows[10:]:
    if len(row) < 17:
        continue

    model = row[0].strip()
    lab = row[1].strip()

    # Skip empty or header rows
    if not model or model == 'About this sheet' or not lab:
        continue

    # Parse parameters
    params_str = row[3].strip().replace(',', '')
    try:
        params = float(params_str) if params_str else None
    except ValueError:
        params = None

    # Parse tokens
    tokens_str = row[4].strip().replace(',', '')
    try:
        tokens = float(tokens_str) if tokens_str else None
    except ValueError:
        tokens = None

    # Parse ALScore
    alscore_str = row[6].strip()
    try:
        alscore = float(alscore_str) if alscore_str else None
    except ValueError:
        alscore = None

    # Parse date
    date_str = row[12].strip() if len(row) > 12 else ''
    date_val = None
    if date_str and date_str != 'TBA':
        match = re.match(r'(\w{3})/(\d{4})', date_str)
        if match:
            m, y = match.groups()
            if m in month_map:
                date_val = f"{y}-{month_map[m]:02d}-01"

    if not date_val:
        continue  # Skip models without dates

    # Public
    public = row[13].strip() if len(row) > 13 else ''

    # Architecture
    arch = row[15].strip() if len(row) > 15 else ''

    # Tags
    tags = row[16].strip() if len(row) > 16 else ''

    # Normalize lab names for coloring
    lab_clean = lab
    if 'Google' in lab or 'DeepMind' in lab:
        lab_clean = 'Google'
    elif 'OpenAI' in lab:
        lab_clean = 'OpenAI'
    elif 'Meta' in lab or 'Facebook' in lab:
        lab_clean = 'Meta'
    elif 'Anthropic' in lab:
        lab_clean = 'Anthropic'
    elif 'Microsoft' in lab:
        lab_clean = 'Microsoft'
    elif 'Alibaba' in lab or 'Qwen' in lab:
        lab_clean = 'Alibaba'
    elif 'DeepSeek' in lab:
        lab_clean = 'DeepSeek'
    elif 'xAI' in lab:
        lab_clean = 'xAI'
    elif 'NVIDIA' in lab:
        lab_clean = 'NVIDIA'
    elif 'Mistral' in lab:
        lab_clean = 'Mistral'
    elif 'Baidu' in lab:
        lab_clean = 'Baidu'
    elif 'Amazon' in lab:
        lab_clean = 'Amazon'
    elif 'Tencent' in lab or 'Wechat' in lab:
        lab_clean = 'Tencent'
    elif 'Apple' in lab:
        lab_clean = 'Apple'
    elif 'Samsung' in lab or 'SK ' in lab or 'LG' in lab:
        lab_clean = 'Korean'
    elif 'Xiaomi' in lab:
        lab_clean = 'Xiaomi'
    elif 'AI21' in lab:
        lab_clean = 'AI21'
    elif 'Cohere' in lab:
        lab_clean = 'Cohere'
    elif 'Allen AI' in lab:
        lab_clean = 'Allen AI'
    elif 'IBM' in lab:
        lab_clean = 'IBM'
    elif 'Huawei' in lab:
        lab_clean = 'Huawei'
    elif 'Tsinghua' in lab or 'Z.AI' in lab or 'Zhipu' in lab:
        lab_clean = 'Zhipu/Tsinghua'
    elif 'Moonshot' in lab:
        lab_clean = 'Moonshot'
    elif 'MiniMax' in lab:
        lab_clean = 'MiniMax'
    elif 'EleutherAI' in lab:
        lab_clean = 'EleutherAI'
    elif 'BigScience' in lab:
        lab_clean = 'BigScience'
    elif 'Stability' in lab:
        lab_clean = 'Stability AI'

    # Determine if reasoning tag
    is_reasoning = 'Reasoning' in tags
    is_sota = 'SOTA' in tags
    is_moe = arch == 'MoE'

    models.append({
        'model': model,
        'lab': lab,
        'lab_group': lab_clean,
        'params': params,
        'tokens': tokens,
        'alscore': alscore,
        'date': date_val,
        'public': public,
        'arch': arch if arch else 'Unknown',
        'reasoning': is_reasoning,
        'sota': is_sota,
        'moe': is_moe,
        'tags': tags
    })

# Sort by date
models.sort(key=lambda x: x['date'])

print(f"Total models: {len(models)}")
print(f"Date range: {models[0]['date']} to {models[-1]['date']}")
print(f"Labs: {len(set(m['lab_group'] for m in models))}")

# Count by year
from collections import Counter
year_counts = Counter(m['date'][:4] for m in models)
for y in sorted(year_counts):
    print(f"  {y}: {year_counts[y]} models")

with open('models_data.json', 'w') as f:
    json.dump(models, f, indent=2)

print("\nSaved to models_data.json")
