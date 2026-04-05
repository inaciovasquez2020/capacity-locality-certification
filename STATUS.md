# Capacity–Locality Certification Status

## Scope

Certification of claims relating:
- Local refinement processes
- Information/entropy bounds
- Global correctness guarantees

## Certification Model

A claim is **certified** if and only if:
- A concrete witness exists
- A verifier accepts the witness
- Capacity bounds are not violated

## Regimes

- Admissible: local ⇒ global valid under bounded capacity
- Non-admissible: existence of counterexample witness
- Boundary: requires explicit verification

## Pipeline

1. Specify claim
2. Provide witness
3. Run verifier
4. Record outcome

## Status

- Framework: active
- Verification: reproducible
- Certification: conditional on witness completeness
