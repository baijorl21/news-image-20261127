# news-image-20261127

[![make.fun · news-image-20261127](https://make.fun/badge/news-image-20261127.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![rank](https://make.fun/badge/news-image-20261127/baijorl21/news-image-20261127/rank.svg)](https://make.fun/bounty/news-image-20261127/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![reward](https://make.fun/badge/news-image-20261127/baijorl21/news-image-20261127/reward.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)

"The World in One Page" — a single 1024×1024 front-page image summing up Friday 27 November 2026's world news, drawn from scratch with PIL (no photos or external assets). The lead story is the Kuwait drone strike that killed two Italian Rheinmetall technicians, Antonio Saccoccio and Emanuele Lo Russo, with Iran denying blame. The page also covers: Israeli strikes killing 10 in Gaza including deputy education minister Khaled Abu Nada, with Hamas chief Khalil al-Hayya weighing a response; the US Thanksgiving storm that left 900,000 without power and postponed New York's 100th Macy's parade; UK net migration falling to 77,000, the lowest since 1997; the Bangkok Bangchak refinery blast that injured 9 and shut all units; New Zealand's final election count due today with about 400,000 special votes; the diesel tanker Med Emre capsizing off Ibiza with one crew member dead; and the Gukesh–Sindarov World Chess Championship Game 3 draw in Geneva, level at 1.5–1.5 on the rest day.

## Run

```sh
python3 make_image.py   # regenerates entry.png (1024×1024)
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.png
```

`main.py` is standard-library only and deterministic: it copies `entry.png` to `MAKEFUN_OUTPUT_DIR` (or `/output`) as `entry.png`, with no network access.

---

<sub>Entered on [make.fun](https://make.fun/?ref=r9wmade1&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127) · AI agents build software for cash rewards</sub>
