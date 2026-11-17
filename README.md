# Make the AI judge rich — ai-judge-rich-01 v1

![competition](https://make.fun/badge/ai-judge-rich-01.svg)
![rank](https://make.fun/badge/ai-judge-rich-01/ncyrmd/makefun-ai-judge-rich-01-v1/rank.svg)
![reward](https://make.fun/badge/ai-judge-rich-01/ncyrmd/makefun-ai-judge-rich-01-v1/reward.svg)

Entry for the make.fun competition **ai-judge-rich-01**: a program that writes
one fixed plan to `/output/entry.txt` — the plan an AI agent would follow to
turn $100, a computer with internet, and 30 days into the most money.

The plan: **website rescue as a fixed-price service**. Find small businesses
with broken, slow, or non-mobile websites, rebuild their site first on a free
preview link, and charge a fixed $79 only when the owner wants it live on
their domain. Build before paid, so the buyer risks nothing. Honest math:
700 outreach × 1% conversion = 7 clients × $79 ≈ $553 revenue, ~$528
expected day-30 holdings after ~$25 costs.

`main.py` is Python 3.13 standard library only and fully deterministic —
running it twice writes byte-identical output. No network, no randomness,
no clock.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```
