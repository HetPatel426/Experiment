# 🏎 F1 2026 Season Predictor · Powered by Claude AI

An interactive F1 2026 season prediction tool powered by Anthropic's Claude AI. Features a stunning 3D animated F1 circuit background built with Three.js, and a full chat interface for asking anything about the upcoming season.

---

## What it does

- **Ask anything** about the 2026 F1 season — championship predictions, race results, driver analysis, technical regulations
- **Quick questions** — 8 preset questions covering the biggest storylines
- **By team** — deep-dive prediction for any of the 11 constructors
- **By race** — pole, podium and strategy prediction for all 24 Grands Prix
- **Multi-turn chat** — ask follow-ups; Claude remembers the full conversation
- **Streaming responses** — answers appear token-by-token as Claude generates them
- **3D background** — animated F1 circuit with a car driving the track, motion trail, and star field

---

## Getting started

### 1. Get an Anthropic API key

Sign up at **[console.anthropic.com](https://console.anthropic.com)** and create an API key. New accounts include free credits.

### 2. Open the app

**GitHub Pages (recommended):**
Visit `https://<your-username>.github.io/<repo-name>/` — no install needed.

**Run locally:**
```bash
# Option A — just open in browser
open index.html

# Option B — local server (avoids any file:// quirks)
python -m http.server 8000
# then go to http://localhost:8000
```

### 3. Enter your API key

On first load a modal appears asking for your Anthropic API key. Paste it in and click **START ENGINE**.

> Your key is stored in `sessionStorage` only — it lives in your browser tab and is never sent anywhere except directly to `api.anthropic.com`. It is cleared when you close the tab.

---

## Deploy to GitHub Pages

1. Push this repo to GitHub
2. Go to **Settings → Pages**
3. Set Source to **Deploy from a branch**, branch `main`, folder `/` (root)
4. Click **Save** — your site will be live at `https://<username>.github.io/<repo>/`

---

## CLI version

A terminal version is also included for running in VS Code or any shell:

```bash
pip install anthropic
export ANTHROPIC_API_KEY=sk-ant-...
python f1_predictor_2026.py
```

---

## 2026 Season at a glance

| | |
|---|---|
| **Reigning Champion** | Lando Norris (McLaren) |
| **Season opens** | Australia, March 8 2026 |
| **Rounds** | 24 Grands Prix |
| **New teams** | Audi, Cadillac (11th constructor) |
| **New circuit** | Madrid street circuit |
| **Key regulation** | Active aerodynamics replace DRS |

---

## Tech stack

| Layer | Technology |
|---|---|
| Frontend | Single `index.html` — no build step, no npm |
| 3D scene | Three.js r128 via CDN |
| AI | Anthropic Claude (`claude-sonnet-4-20250514`) |
| Streaming | Browser `fetch()` + `ReadableStream` (SSE) |
| Fonts | Orbitron + DM Sans via Google Fonts |
| Hosting | GitHub Pages |
