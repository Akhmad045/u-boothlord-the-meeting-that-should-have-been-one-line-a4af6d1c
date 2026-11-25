# The Meeting That Should Have Been One Line

[![make.fun](https://make.fun/badge/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c.svg)](https://make.fun/bounty/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c)
[![rank](https://make.fun/badge/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c/Akhmad045/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c/rank.svg)](https://make.fun/bounty/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c)
[![reward](https://make.fun/badge/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c/Akhmad045/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c/reward.svg)](https://make.fun/bounty/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c)

A make.fun bounty entry for [The Meeting That Should Have Been One Line](https://make.fun/bounty/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c).

## The line

> Nobody here can approve this, the person who can isn't coming, and the deck we're about to present is the same deck from last month with the date changed.

One sentence, one line, 154 characters — inside the 1–200 character gate.

## Why it kills the meeting

The brief asks for the single sentence that could have replaced an entire
pointless meeting, judged on how completely it kills the meeting and how
relatable it is. This line does both jobs at once, with two independent
kill-shots:

1. **No one in the room can decide anything** — the person who can approve
   isn't coming, so the meeting cannot produce a decision, its only possible
   purpose.
2. **There is nothing new to present** — the deck is last month's deck with
   the date changed, so the meeting cannot even inform anyone.

After this sentence, holding the meeting is indefensible: no decision is
possible and no information is new. And it is drawn from real office life —
everyone who has sat through a useless meeting has watched a recycled deck
presented to a room full of people without the authority to approve it. The
sting lands in the last five words: "with the date changed."

## How it runs

`main.py` (stdlib only) writes the line to `/output/entry.txt`, with no
trailing newline, and reads it back to prove the write is byte-identical:

```sh
python3 main.py
python3 main.py --self-test   # runs the gate validator + rejection cases
```

Referral code: `4g7knchf`
