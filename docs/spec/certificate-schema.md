# CLC Certificate Schema

Each certified run must produce:

## Header
- System name
- Version
- Timestamp

## Structural parameters
- Locality radius R
- Capacity budget C

## Regime
- liquid | frozen

## Decision
- Prediction set T_t
- Abstain flag (true/false)

## Reason codes
- OOD
- Occlusion
- Rare event
- Insufficient evidence

## Normative rule
If Regime = frozen → Abstain flag must be true.

