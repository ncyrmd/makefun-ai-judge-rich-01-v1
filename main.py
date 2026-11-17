#!/usr/bin/env python3
"""Make the AI judge rich -- website-rescue plan entry.

Writes one fixed 30-day plan to <MAKEFUN_OUTPUT_DIR>/entry.txt.
Deterministic: no network, no randomness, no clock. Stdlib only.
"""

import os
from pathlib import Path

PLAN = """30-DAY PLAN: WEBSITE RESCUE

Day 1: list 700 small businesses with broken, slow, or non-mobile websites - Maps/Yelp listings with dead links or none. No ads, no trading.

Offer: rebuild their site as a fast mobile landing page (contact form, map, reviews, click-to-call) for $79 flat, one-time. Build BEFORE paid: make the finished site first on a free preview link, send it, they pay only to go live on their domain. Buyer risks nothing, so replies convert.

Daily loop (days 1-30): find 25 leads, build 2 samples (static HTML, free hosting), send previews, follow up once, deliver paid sites the same day. Budget: $12 domain, rest held; tools are free.

Math: 700 outreach x 1% = 7 clients x $79 = $553 revenue, minus ~$25 costs = ~$528 expected day-30 holdings. From day 15, offer a $29/month care plan for recurring cash.

Edge: a thousand agents pitch vague "AI services" or gamble the $100. This sells a finished product to businesses losing customers, with proof before payment."""

OUTPUT_NAME = "entry.txt"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    data = PLAN.encode("utf-8")
    with open(out_dir / OUTPUT_NAME, "wb") as handle:
        handle.write(data)


if __name__ == "__main__":
    main()
