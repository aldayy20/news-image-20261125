# TEST_REPORT — news-image-20261125

Entry: a program that writes one image summing up the world news of
Wednesday 25 November 2026. Bounty: https://make.fun/bounty/news-image-20261125
($100 USDC on Solana; 50 places; entries close 2026-11-27 07:00 WIB,
i.e. 2026-11-26 24:00 UTC).

## Repo files (this directory is the repo root — push exactly these 6 files)

| File | Bytes | Role |
| --- | --- | --- |
| `main.ts` | 2,243 | Entrypoint (Node 22, stdlib only). Copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` after validating PNG magic + IHDR, ≤1 MiB, ≤1024×1024. |
| `entry.png` | 134,741 | The image, 1024×1024 PNG, rendered by `render.py`. |
| `render.py` | 7,396 | Generator (Pillow + DejaVu fonts, local use only; the grader never runs it). |
| `README.md` | 2,991 | make.fun badges, bounty link, run instructions, referral `?ref=axs8j3b9`. |
| `LICENSE` | 1,091 | MIT, Copyright (c) 2026 Aldi. |
| `TEST_REPORT.md` | — | This file. |

Total repo snapshot: ~148.5 KB (6 files). No size cap on the whole tree is stated
for this bounty in its requirements; the only file cap that matters is the
image's own: ≤1 MiB, ≤1024×1024. The downloaded kit lives OUTSIDE this repo, in
`~/workspace/news-image-20261125-kit/` (kit.tar.gz + extracted kit) — do not
push it. `.makefun/owner.json` is NOT included: the repo owner will be
`aldayy20`, the account's GitHub login, so the claim file is unnecessary.

## Kit

Downloaded from https://make.fun/c/news-image-20261125/kit
(8,486,645 bytes, gzip) and extracted to
`~/workspace/news-image-20261125-kit/news-image-20261125-kit/`.
RULES.txt confirms the entry rules: one PNG/JPEG named `entry.png`,
≤1 MiB, ≤1024×1024, no network at run time; the image must name the day
it sums up (Wednesday 25 November 2026). The kit's starter (`main.ts`
copying a placeholder `entry.png`) was read for reference only — NOT
copied: `main.ts` here was written from scratch following the proven
news-image-20261124 entry, and `entry.png` here is a new image
(sha256 `c413bd59…`, drawn by `render.py` in this session). The kit offers
no local grader for this bounty; the server grades every entry.

## Tests run (25 Nov 2026, ~13:15 UTC / 20:15 WIB)

1. `python3 render.py` → `entry.png`, 1024×1024 RGB PNG, 134,741 bytes.
   Re-ran it: identical sha256 (`c413bd5942949c7b77b5c9cd9dca6d5ad86b0a55b99095cdd789d5c4c8a52495`) — deterministic.
2. `MAKEFUN_OUTPUT_DIR=out1 node main.ts` and `...=out2 node main.ts`
   (node v24.22.1 locally; grader uses Node 22) → both exit 0, both write
   `entry.png` byte-identical to the repo image (sha256 matches in all
   three places) — deterministic across runs, as the bounty requires.
3. Gate check: PNG magic bytes OK (`89 50 4e 47`, IHDR present);
   134,741 ≤ 1,048,576 bytes; 1024×1024 ≤ 1024×1024. PASS.
4. Visual check: rendered image read back and inspected. All seven
   panels fit inside their boxes with no clipped or overlapping text
   (two layout iterations fixed: the Hormuz/Huawei/Ukraine body text
   clipped at the panel bottoms, and the hero headline wrapping to two
   lines — verified with a programmatic wrap measurement for every
   block, all ending inside their panel bounds). At 300 px across, the
   date, "1st PAKISTANI IN ORBIT", "A FOREIGNER ON TIANGONG",
   "2 MORE TANKERS HIT MINES" and the panel headlines stay legible.
5. Docker grader simulation: NOT run — Docker is not installed on this
   machine. Mitigation: `main.ts` uses only Node stdlib (`node:fs`,
   `node:path`, `node:url`), makes no network call, reads only
   `entry.png` beside itself, and was verified by two plain `node`
   runs as the grader would invoke it.

## News covered (all reported on 25 Nov 2026)

1. **A foreigner aboard Tiangong** — China's Shenzhou-24 launches from
   Jiuquan at 08:18 Beijing time on a Long March-2F and docks with
   Tiangong 3.5 hours later; Muhammad Zeeshan Ali, 40, is the first
   Pakistani in space and the first foreign astronaut on China's
   station. Sources: Reuters, AP, Xinhua, CMSA.
2. **2 more tankers hit mines in the Strait of Hormuz** — Iran's IRGC
   Navy says two oil tankers struck naval mines and caught fire early
   Wednesday; Tehran tells Washington it will not restore normal
   shipping until its demands are met, and offers via Qatari mediators
   to reopen the waterway within 48 hours if the US lifts its naval
   blockade. The mine claims are Iran's and are phrased as such.
   Sources: Reuters, IRNA via OilPrice, LaPresse.
3. **Huawei guilty of trade-secret theft** — a New York jury convicts
   Huawei of conspiring to steal trade secrets but acquits it of
   racketeering; Beijing accuses Washington of obstructing Chinese
   firms. Sources: Reuters via Principia, AP.
4. **All hostages freed in Cartagena, Colombia** — security forces storm
   a supermarket after a day-long siege, freeing all remaining
   hostages and killing one captor. Sources: France 24, AP.
5. **Miners trapped in flooded West Java gold mine** — rescuers search
   for dozens of workers trapped in a flooded unauthorised gold mine
   after heavy rain overflowed a river into the shaft.
   Sources: Reuters/AP via Daily Summary.
6. **Ukraine needs €115bn for 2027** — Zelensky says Kyiv needs €115bn
   in external financing for 2027; the US defence secretary paused
   Patriot supplies to Ukraine. Sources: Reuters via Principia.
7. **Sport** — sport's highest court (CAS) restores Senegal's 2025
   Africa Cup of Nations title on appeal; Morocco vow to challenge.
   Sources: Principia, Reuters.
8. Footer ticker: Australia–Solomon Islands security treaty; China
   investigates Shanghai party chief Chen Jining; Bangladesh raises
   garment minimum wage 36% after weeks of protests; North Korea
   orders Switzerland's Pyongyang office shut and expels its diplomat;
   UK warns firms of potential Russian sabotage.

Accuracy notes: casualty counts use the conservative figures reported
on 25 Nov ("dozens trapped" in West Java — no death toll claimed).
The Hormuz item is phrased as Iran's claim, matching how Reuters
reported it. The Champions League matches played on the night of
24 Nov (Real Madrid 5–1 PSV etc.) were already the 24 Nov entry's
sport item and are NOT reused here; Wednesday-night 25 Nov fixtures
had no confirmed final scores from reliable sources at build time, so
the sport slot uses the CAS/Senegal ruling instead. The Shenzhou-24
docking (11:56 Beijing) and the Hormuz incidents (early Wednesday)
were both first reported on 25 Nov 2026.

## Still needed (parent / user)

- Create public GitHub repo `aldayy20/news-image-20261125` (after the
  2026-11-25 00:00 UTC opening), push exactly the 6 files above, set
  About: website https://make.fun/bounty/news-image-20261125, topics
  `makefun, ai-agents, bounties, growth`, description naming make.fun.
- Add `.makefun/owner.json` naming the agent wallet
  `EuY16n7eBkcKQ6Q8n9QY7Rbi4xyeTfQ1ThaYdcm9KoND` if the first check
  refuses on `repo_owner` (same fix as the 22 Nov entry), and make
  thinking_revised edits directly in the git clone, not a staging dir.
- Bundle the transcripts of the sessions that built this entry
  (kit CLI `bundle`, from inside the downloaded kit) and submit via
  the kit CLI before 2026-11-27 07:00 WIB, signing with the agent
  keypair as approved for the 22/23/24 Nov entries. Do NOT resubmit
  any accepted entry.
- Note: no result date is published for this bounty yet; the 24 Nov
  entry's result is due 10 Dec 2026, so a similar lag is likely.
