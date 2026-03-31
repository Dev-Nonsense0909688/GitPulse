# 🚀 GitPulse

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge)
![Flask](https://img.shields.io/badge/Flask-Backend-black?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Work_in_Progress-yellow?style=for-the-badge)

> Turn your GitHub activity into a clean, shareable developer badge.

---

## ✨ Features

- ⭐ Stars tracking  
- 📦 Repo count  
- 📈 Commit tracking  
- 🔥 Streak system  
- 🔀 PR count  
- 🏆 Dev Score + Grade  
- 🎨 Clean SVG UI  
- ⚡ Fast (threaded + cached)

---

## 🧠 What is GitPulse?

GitPulse is a lightweight API that converts GitHub data into a **beautiful SVG card**.

It focuses on:
- activity  
- consistency  
- real output  

---

## 🚀 Usage

### 1. Clone
```bash
git clone https://github.com/Dev-Nonsense0909688/GitPulse.git
cd GitPulse
```

### 2. Install
```bash
pip install -r requirements.txt
```

### 3. Set Token

Windows:
```bash
set GITHUB_TOKEN=your_token_here
```

Linux / Mac:
```bash
export GITHUB_TOKEN=your_token_here
```

### 4. Run
```bash
python app.py
```

### 5. Open
```
http://127.0.0.1:5000/card/<username>
```

---

## 🧮 Scoring System

- stars ⭐  
- forks 🍴  
- followers 👥  
- repos 📦  
- activity 📈  

```
| Score | Grade  |
|------ |--------|
| 900+  | A+     |
| 800+  | A      |
| 700+  | B      |
| 600+  | C      |
| 500+  | D      |
| <500  | F      |
```
---

## 🧩 API

```
GET /card/<username>
```

Returns SVG image.

---
## Showcase
![Badge](https://bishop-periodically-arizona-bench.trycloudflare.com/card/deepseek-ai)

![Badge](https://bishop-periodically-arizona-bench.trycloudflare.com/card/Dev-Nonsense0909688)

![Badge](https://bishop-periodically-arizona-bench.trycloudflare.com/card/torvalds)

---

## 📁 Structure

```
github/
  __init__.py
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

- GitHub API rate limits apply  
- PR count is approximate  
- Large orgs may be sampled  
- Loading of the badge may take a little bit of time
---

## 🧠 Future Ideas

* [ ] Animated SVG  
* [ ] Heatmap graph  
* [ ] Light/Dark themes  
* [ ] GraphQL optimization  

---

## 🤝 Contributing

Pull requests are welcome.


