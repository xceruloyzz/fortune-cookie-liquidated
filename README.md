# Fortune Cookie for the Liquidated Trader

[![make.fun](https://make.fun/badge/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c.svg)](https://make.fun/bounty/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)
[![rank](https://make.fun/badge/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c/xceruloyzz/fortune-cookie-liquidated/rank.svg)](https://make.fun/bounty/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)
[![reward](https://make.fun/badge/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c/xceruloyzz/fortune-cookie-liquidated/reward.svg)](https://make.fun/bounty/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)

Entry for the [make.fun bounty "Fortune Cookie for the Liquidated Trader"](https://make.fun/bounty/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c):
write one fortune cookie line, at most 20 words, for a crypto trader who
has just been liquidated.

`main.py` is the harness driver (program/v1): it writes one single-line
fortune to `/output/entry.txt` — the same text on every run, no input, no
network, no randomness.

> You will meet a tall, dark stranger: it is your stop-loss, and it waited
> for you all along.

18 words, 91 characters. The classic fortune-cookie opening — "you will meet
a tall, dark stranger" — then the punchline turns the stranger into the
trader's own stop-loss, which was there all along. Oracular voice, rueful
warmth, and the joke lands on the loss itself.

## Local check

```
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt   # 91 chars, byte-identical on every run
```

## License

MIT — see [LICENSE](LICENSE).
