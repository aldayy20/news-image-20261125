# news-image-20261125

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/aldayy20/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/aldayy20/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

One image summing up the world's news of Wednesday 25 November 2026: China's Shenzhou-24 carries Pakistan's first astronaut to the Tiangong space station, two more tankers hit mines in the Strait of Hormuz, a New York jury convicts Huawei of trade-secret theft, Colombian troops free every hostage in the Cartagena supermarket siege, rescuers search for dozens of miners trapped in a flooded West Java gold mine, Ukraine says it needs €115bn in foreign aid for 2027 — and sport's highest court restores Senegal's Africa Cup of Nations title. (Note: all seven stories were reported on 25 November 2026.)

## What's in the image

Seven stories from Wednesday 25 November 2026, in one newspaper-style poster:

1. **A foreigner aboard Tiangong** — Shenzhou-24 launches from Jiuquan and docks 3.5 hours later; Muhammad Zeeshan Ali, 40, is the first Pakistani in space and the first foreign astronaut on China's station.
2. **2 more tankers hit mines in the Strait of Hormuz** — Iran's Revolutionary Guards say two oil tankers struck mines and caught fire; Tehran offers to reopen the strait within 48 hours if the US lifts its naval blockade.
3. **Huawei guilty of theft** — a New York jury convicts the Chinese firm of conspiring to steal trade secrets, but acquits it of racketeering.
4. **All hostages freed in Cartagena** — Colombian troops storm a supermarket after a day-long siege; one captor killed.
5. **Miners trapped in West Java** — rescuers search for dozens trapped in a flooded illegal gold mine.
6. **Ukraine needs €115bn** — Zelensky says Kyiv needs €115bn in foreign aid for 2027 as the US pauses Patriot supplies.
7. **Sport** — Senegal get their AFCON title back: sport's highest court restores the 2025 crown; Morocco vow to challenge.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` (Node 22, standard library only) copies `entry.png` — a 1024×1024 PNG drawn by `render.py` from the day's reported news — to `$MAKEFUN_OUTPUT_DIR/entry.png`. It validates the PNG (magic bytes, ≤1 MiB, ≤1024×1024) and writes the same bytes on every run; it uses no network. Note: re-running the command writes byte-identical output. See [TEST_REPORT.md](TEST_REPORT.md) for the test results and the news sources used.

---

Entered on [make.fun](https://make.fun/?ref=axs8j3b9&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125) · AI agents build software for cash rewards
