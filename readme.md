# 🚀 GitPulse

> Turn your GitHub activity into a **clean, shareable developer badge** — fast, minimal, and actually useful.

---

## ⚡ Tech Stack

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-API-000000?style=for-the-badge\&logo=flask)
![Status](https://img.shields.io/badge/🚧_WIP-orange?style=for-the-badge)
![License](https://img.shields.io/badge/MIT-2ea44f?style=for-the-badge)

---

## ✨ Features

* ⭐ GitHub stars tracking
* 📦 Repository count
* 📈 Commit activity tracking
* 🔥 Streak detection
* 🔀 Pull request count
* 🏆 Developer score + grading system
* 🎨 Dynamic SVG badge generation
* ⚡ Fast response (threaded + cached)

---

## 🧠 What is GitPulse?

GitPulse is a lightweight API that transforms raw GitHub data into a **compact, visually clean SVG badge**.

Instead of just showing numbers, it highlights:

* activity
* consistency
* real developer output

---

## 🚀 Quick Start

### 1. Clone

```bash
git clone https://github.com/Dev-Nonsense0909688/GitPulse.git
cd GitPulse
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set GitHub Token

Windows:

```bash
set GITHUB_TOKEN=your_token_here
```

Linux / macOS:

```bash
export GITHUB_TOKEN=your_token_here
```

### 4. Run server

```bash
python app.py
```

### 5. Open in browser

```
http://127.0.0.1:6829/card/<username>
```

---

## 📡 API Usage

Embed directly in your README:

```md
![GitPulse Badge](https://bishop-periodically-arizona-bench.trycloudflare.com/card/<username>)
```

---

## 🧮 Scoring System

GitPulse evaluates developer activity based on:

* stars ⭐
* forks 🍴
* followers 👥
* repositories 📦
* activity 📈

| Score | Grade |
| ----- | ----- |
| 900+  | A+    |
| 800+  | A     |
| 700+  | B     |
| 600+  | C     |
| 500+  | D     |
| <500  | F     |

---

## 🧩 Endpoint

```
GET /card/<username>
```

Returns a dynamically generated SVG badge.

---

## 🖼️ Showcase

![Preview](https://bishop-periodically-arizona-bench.trycloudflare.com/card/openclaw)

![Preview](https://bishop-periodically-arizona-bench.trycloudflare.com/card/anthropics)

![Preview](https://bishop-periodically-arizona-bench.trycloudflare.com/card/auroralabsofficial)

---

## 📁 Project Structure

```
github/
  api.py
  cache.py
  fetch.py
  config.py
  logic.py

templates/
  badge.svg

app.py
```

---

## ⚠️ Notes

* GitHub API rate limits apply
* Pull request count is approximate
* Large organizations may be sampled
* Initial load may take a moment

---

## 🧠 Future Plans

* [ ] Animated SVG badges
* [ ] Contribution heatmap integration
* [ ] Light/Dark themes
* [ ] GraphQL optimization

---

## 🤝 Contributing

Have ideas or improvements?

Open an issue or submit a pull request — contributions of any size are welcome 🚀
