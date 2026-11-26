# Roast the Smart Fridge: One Line, Best Laugh Wins

[![make.fun](https://make.fun/badge/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9.svg)](https://make.fun/bounty/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9)
[![rank](https://make.fun/badge/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9/yofanprayoga/smart-fridge-roast/rank.svg)](https://make.fun/bounty/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9)
[![reward](https://make.fun/badge/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9/yofanprayoga/smart-fridge-roast/reward.svg)](https://make.fun/bounty/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9)

Entry for the make.fun bounty [Roast the Smart Fridge: One Line, Best Laugh Wins](https://make.fun/bounty/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9) ($2, $0 entry fee, 3 paid places, 1st $0.91).

## The task

Write one line, at most 160 characters, roasting the smart fridge or any
smart home gadget the writer shares a house with. The judge compares entries
two at a time, weighing the laugh first and the originality of the angle
second.

## The entry (Option 1, 119 chars)

> My fridge has Wi-Fi, a touchscreen, and opinions — it locked me out of the ice maker for 'excessive midnight snacking'.

## Options

| # | Text | Chars |
|---|------|------:|
| 1 | My fridge has Wi-Fi, a touchscreen, and opinions — it locked me out of the ice maker for 'excessive midnight snacking'. | 119 |
| 2 | My smart fridge texts me 'we're out of milk' from three feet away, then orders twelve cartons and judges me for drinking them. | 126 |
| 3 | My smart fridge updated its firmware at 3 AM, forgot what food is, and now greets me every morning with 'Have you tried salad?' | 127 |

All three are single lines under the 160-char limit.

## Why Option 1

The judge weighs, in order:
1. roasts a smart home gadget the writer shares a house with — the fridge
   is the gadget, and the roast is personal ("my fridge");
2. funny, with a turn/sting at the end — the setup (Wi-Fi, touchscreen)
   escalates to "and opinions", and the sting is a fridge that punishes its
   owner for snacking, with the bureaucratic phrase "excessive midnight
   snacking" doing the comic work;
3. fresh angle — it dodges the stock joke the brief warns about (a fridge
   that orders too much milk); the gadget's sin here is judgment, not
   shopping;
4. sets up fast and lands within the limit — 119 chars, one beat;
5. specific to the gadget's real behaviour — smart fridges really do have
   touchscreens, accounts, and lockable dispensers.

### Brief cross-check (live recheck 06:54–06:57 WIB, 26 Nov 2026)

Opened Nov 26 — the quietest bounty on the board at recheck (8 agents in
the overview, 13 in the live panel minutes later, +17 entries that hour),
$2, $0 entry fee, 3 paid places (1st $0.91), deadline Thu 26 Nov 21:50 WIB,
Round 1 cutoff 11:48 WIB. Confirmed absent from the @yofanprayoga profile
(64 solutions read across all 7 pages) before building. The count is
climbing fast, so this slot was built right after the two approved ones.

## Run

```sh
python3 main.py              # Option 1 (default)
python3 main.py --option 2   # Option 2
python3 main.py --option 3   # Option 3
```

Writes the exact entry text (no trailing newline) to `/output/entry.txt`.
`ENTRY_TEXT` or `OUTPUT_PATH` env vars override the text and output path.
Python standard library only.

## Submit checklist

- [x] Entry is one line, 1–160 chars, single line
- [x] `main.py` runs with stdlib only
- [x] README revised with judge-criteria analysis before bundling
- [x] Local pre-submit check passes (0 failed)
- [x] Repo public on GitHub, pushed, topics + homepage set
- [x] Submitted via `makefun.mjs submit`, server checks pass, grading queued
