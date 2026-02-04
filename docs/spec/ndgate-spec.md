# NDGate — Admissible New Data Gate

## Purpose
Block predictions when local evidence is insufficient.

## Input
- observation history x_{0:t}
- locality radius R
- capacity budget C

## Output
- ADMISSIBLE or REJECT
- reason code

## Rule
REJECT if the next prediction requires global information not inferable from x_{0:t}
within R and C.

## Action
When REJECT: abstain, slow down, or request new sensing.

