# tiny-chess-01

A chess engine in at most 4,096 bytes of Python (stdlib only), built for the
make.fun tiny-chess-01 bounty: the strongest engine in 4 KB, played against a
fixed gauntlet of eight house engines.

## Engine

- 0x88 board, alpha-beta with iterative deepening (60,000 nodes per move)
- Transposition table (exact and lower-bound entries), one killer per depth,
  MVV-LVA capture ordering, capture-only quiescence
- Evaluation: material plus a shared pawn piece-square table plus a +25 cp
  bishop-pair bonus
- Deterministic: a fixed node count, never a clock

## Run

Set `MAKEFUN_ENV_URL` to the env server and run:

    python3 main.py

## Practice result

Practice trial-0: Elo 1,253 (5 wins, 2 draws, 9 losses, zero time forfeits),
against the house gauntlet (sunfish baseline: 1,360).
