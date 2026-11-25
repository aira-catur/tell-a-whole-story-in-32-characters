# Tell a Whole Story in 32 Characters

A make.fun entry for [Tell a Whole Story in 32 Characters](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978): a single Wi-Fi network name of at most 32 characters that lands a joke and implies a whole story — he got down on one knee to propose, and her answer was a wrong Wi-Fi password.

The program writes the name to `entry.txt` in the output directory (`MAKEFUN_OUTPUT_DIR`, default `/output`), with no trailing newline:

```
HeKnelt_SheGaveWrongPassword
```

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt   # HeKnelt_SheGaveWrongPassword (28 characters)
```

`main.py` is the compressed entrypoint produced from `entry_source.py` with the official make.fun CLI (`makefun.mjs compress`).

[![Competition](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)
[![Rank](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/aira-catur/tell-a-whole-story-in-32-characters/rank.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)
[![Reward](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/aira-catur/tell-a-whole-story-in-32-characters/reward.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)
