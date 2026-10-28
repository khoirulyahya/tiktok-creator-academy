#!/usr/bin/env python3
"""
TikTok Creator Academy — Sync & Health Audit Tool
Verifies live endpoint availability across locales (/en and /id) using curl subprocess.
"""

import subprocess
import sys
from pathlib import Path

SLUGS = [
    "creator-rewards-program", "monetizing-your-content", "subscription",
    "creator-monetization-center", "tiktok-shop", "tiktok-shop-affiliate",
    "shop-affiliate", "affiliate-program", "tiktok-one", "creator-marketplace",
    "brand-partnership", "brand-collaborations", "work-with-artists",
    "creator-fund", "creator-program", "video-gifts", "virtual-gifts",
    "diamonds", "coins", "withdrawal", "taxes", "finding-creator-rewards-success",
    "subscription-or-super-fan", "getting-first-10-subscribers", "tiktok-ads",
    "branded-content", "going-live", "live-monetization", "live-gifts",
    "live-gifts-monetization", "live-match", "live-match-powerups", "gift-gallery",
    "gift-points", "gift-vote", "live-rankings", "live-campaigns", "live-shopping",
    "live-gaming", "guessing-game", "live-streaming-tips", "live-setup",
    "live-audience", "live-growth", "live-moderation", "live-subscription",
    "super-fan", "high-quality-videos", "8-tips-for-creators", "video-creation",
    "video-editing", "editing-tips", "video-upload", "video-length", "aspect-ratio",
    "vertical-video", "horizontal-video", "hooks", "captions", "hashtags",
    "sounds-library", "trending-sounds", "copyright", "duet", "stitch",
    "photo-mode", "series", "series-feature", "playlists", "collabs",
    "creator-collab", "q-and-a", "ar-effects", "effect-house",
    "effect-house-creator-rewards", "effect-house-rewards", "analytics",
    "creator-search-insights", "watch-time", "follower-growth", "posting-schedule",
    "content-calendar", "content-strategy", "finding-your-niche", "tiktok-search",
    "getting-started", "account-setup", "profile-optimization", "tiktok-studio",
    "for-you-page", "fyp-algorithm", "algorithm", "notifications", "inbox",
    "direct-messages", "comment-management", "community-guidelines",
    "creator-code-of-conduct", "account-safety", "account-violation",
    "content-violation", "appeal", "shadowban", "restricted-mode",
    "restricted-videos", "age-restriction", "privacy-settings", "safety-toolkit",
    "digital-wellbeing", "screen-time", "family-pairing"
]

def check_url_curl(url: str) -> int:
    try:
        res = subprocess.run(
            ["curl", "-o", "/dev/null", "-s", "-w", "%{http_code}", "--max-time", "5", url],
            capture_output=True,
            text=True,
            check=False
        )
        code_str = res.stdout.strip()
        return int(code_str) if code_str.isdigit() else 0
    except Exception:
        return 0

def run_audit(sample_size: int = 15):
    print(f"🚀 Starting TikTok Creator Academy Health Audit (sample {sample_size} of {len(SLUGS)} slugs)...")
    
    en_home = check_url_curl("https://www.tiktok.com/creator-academy/en/homepage")
    id_home = check_url_curl("https://www.tiktok.com/creator-academy/id/homepage")
    print(f"[*] EN Homepage Status: HTTP {en_home}")
    print(f"[*] ID Homepage Status: HTTP {id_home}")
    
    success_count = 0
    fail_count = 0
    
    for slug in SLUGS[:sample_size]:
        url = f"https://www.tiktok.com/creator-academy/en/article/{slug}"
        code = check_url_curl(url)
        if code == 200:
            success_count += 1
            print(f"  [OK 200] {slug}")
        else:
            fail_count += 1
            print(f"  [FAIL {code}] {slug}")

    print(f"\n📊 Audit Complete: {success_count} OK, {fail_count} Failed.")

if __name__ == "__main__":
    run_audit()
