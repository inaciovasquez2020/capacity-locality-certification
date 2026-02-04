(prediction set, certificate), where the certificate records the regime (liquid vs frozen) and
mandatory abstention conditions when prediction is structurally unreliable.

## Setup (informal)
A predictor observes a local history x_{0:t} and emits a proposal set T_t.
The certification layer emits Cert_t containing (R, C, regime, abstain flag).

## Certification outputs
- Locality radius: R
- Capacity / transcript budget: C
- Regime tag: liquid or frozen
- Abstention condition: when local evidence is insufficient for reliable global inference

## Core guarantee (ceiling form)
Improvements of refinement-based predictors saturate under bounded capacity and locality:
the effective reduction in uncertainty per update is bounded as a function of (R, C).

## Corollary (engineering interpretation)
In the frozen regime (OOD, occlusion, rare events), producing “plausible” futures without
admissible new data is structurally unsafe; abstention is the correct certified behavior.

## Scope
This note is a structural discipline layer. It does not propose a new generator architecture.
GANs, diffusion, flows are treated as interchangeable within the same ceiling constraints.
