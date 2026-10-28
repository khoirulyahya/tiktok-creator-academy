# 🎓 TikTok Creator Academy — AI Agent Skill

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Verified%20Oct%202026-brightgreen.svg)](#)
[![TikTok Creator Academy](https://img.shields.io/badge/Source-TikTok%20Official-black.svg?logo=tiktok)](https://www.tiktok.com/creator-academy/en/homepage)

> **The First Authoritative AI Agent Skill & Knowledge Base for the official TikTok Creator Academy (`creator-academy/en` & `creator-academy/id`).**

---

## 🌟 Overview

This skill equips any AI Agent (Google Antigravity, Claude Code, Cursor, Codex, Open-WebUI, LangChain, AutoGen) with complete, grounded, and verified knowledge of TikTok's official educational guidelines and monetization ecosystem.

Eliminates hallucinations regarding:
- **Creator Rewards Program (CRP)** eligibility criteria, countries, calculation, and violation rules.
- **TikTok Shop Affiliate & Storefront** discovery paths and best practices.
- **TikTok LIVE Monetization** (Diamonds, Match Power-ups, Gift Gallery, Rankings).
- **Subscription & TikTok One** brand partnerships.
- **Creator Search Insights & TikTok Studio SEO**.
- **Community Guidelines & Account Standing Enforcement**.

---

## 📂 Repository Structure

```
tiktok-creator-academy/
├── SKILL.md                          # Primary AI agent instructions & complete knowledge base
├── README.md                         # Project documentation & integration guide
├── scripts/
│   └── audit_and_sync.py             # Health audit script for checking 111+ live endpoints
└── references/
    └── raw-article-summaries.md      # Ground truth summaries & verbatim data points
```

---

## 🚀 How to Use / Integration

### 1. Google Antigravity
Clone directly into your personal or workspace skills directory:
```bash
git clone https://github.com/khoirulyahya/tiktok-creator-academy.git ~/.gemini/config/skills/tiktok-creator-academy
```
Antigravity automatically discovers `SKILL.md` and activates it whenever you discuss TikTok strategies, monetization, or creator guidelines.

### 2. Claude Code / Cursor / Windsurf
Copy or symlink `SKILL.md` into your project rules or context directory:
- **Cursor:** Add `SKILL.md` to `.cursorrules` or context window.
- **Claude Code:** Place in your prompt template or refer via `@SKILL.md`.

### 3. Custom AI Agents / LangChain / RAG
Load `SKILL.md` or `references/raw-article-summaries.md` directly as system prompt context or document chunks:
```python
with open("SKILL.md", "r") as f:
    tiktok_skill_prompt = f.read()

# Pass tiktok_skill_prompt to your LLM system prompt
```

### 4. Running the Health Audit
Verify that all 111+ TikTok Creator Academy endpoints are alive and responding:
```bash
python3 scripts/audit_and_sync.py
```

---

## 📌 Key Metrics Reference (Quick Glance)

| Metric | Official Requirement |
|---|---|
| Min Followers for CRP | 10,000 |
| Min Video Views (30 Days) | 100,000 |
| Min Duration for CRP | > 1 minute (60 seconds) |
| CRP View Qualification | Minimum 5 seconds watch time |
| Video Appeal Window | 80 days |
| Account Appeal Window | 30 days |
| Subscription Revenue Split | 70% (up to 90% with monthly bonus) |
| Max Upload Duration (TikTok Studio) | 60 minutes (10 GB max, min 720p) |
| Playlist Follower Threshold | 10,000 |

---

## 📄 License

MIT License. Free to use, fork, and integrate into open-source or commercial AI agents.
