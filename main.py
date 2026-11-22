#!/usr/bin/env python3
"""The plan make.fun will carry out in public.

Writes one short plan (264 Unicode code points) to /output/entry.txt.
Deterministic: the same bytes on every run. No network, no randomness.

The plan: sell $49 one-page sites to US plumbers with no website,
found on Google Maps — 300 outreach emails a day, 1% buy, $147 a day,
compounding from $400 in week 1 to $3,000+ by day 30. The edge is speed
and price: agencies charge $500 and take a week; the agent delivers in
minutes, 24/7, with no human in the loop.
"""

import os

ENTRY = (
    "Day 1: find 300 US plumbers with no website on Google Maps. "
    "Build each a $49 1-page site in 20min, email preview + Stripe link. "
    "300/day, 1% buy = $147/day. "
    "Week 1 $400, W3 $1,500, day 30 $3,000+. "
    "Edge: agencies charge $500, take a week; I deliver in minutes, 24/7."
)


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 280, f"entry is {len(text)} code points"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
