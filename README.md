# Di Hu

**full-stack biologist • building autonomous labs**

My work turns protocols, acceptance criteria, and failure responses into gated, auditable execution across laboratory hardware. This profile is a public portfolio of reusable automation, omics, robotics, and evaluation systems.

## Current evidence boundary

Some named operations have been executed on physical instruments under human supervision. Most of the portfolio remains simulated. There is no customer deployment and no full wet end-to-end biological endpoint yet. Each repository states its own evidence and validation boundary.

## Start here

- **[autonomous-lab](https://github.com/di-omics/autonomous-lab)** — computes what a reference workflow can actually automate, supervise, block, or break, and stops at unsupported steps.
- **[plr-mcp](https://github.com/di-omics/plr-mcp)** — exposes PyLabRobot devices as agent-callable tools, with simulation by default and explicit execution gates.
- **[plr-tested](https://github.com/di-omics/plr-tested)** — keeps supervised physical-instrument run cards and observed failures as evidence.

## How the stack fits together

`protocol + acceptance criteria → execution gates → MCP/device backend → measurements → run and decision ledger`

| Layer | Repository | Current role |
| --- | --- | --- |
| Evidence ledger | [autonomous-lab](https://github.com/di-omics/autonomous-lab) | Computes the real autonomy boundary and the next blocking gate. |
| Agent execution | [plr-mcp](https://github.com/di-omics/plr-mcp) | Gives agents typed, discoverable laboratory tools. |
| Physical evidence | [plr-tested](https://github.com/di-omics/plr-tested) | Records named hardware operations run under supervision. |
| Instrument expansion | [plr-reverse-engineer](https://github.com/di-omics/plr-reverse-engineer) | Captures, decodes, and guarded-replays no-API instrument commands. |
| Omics workflows | [fullstack-omics](https://github.com/di-omics/fullstack-omics) | Simulator-only scRNA-seq and whole-genome sequencing workflows. |
| Evaluation | [omics-demos](https://github.com/di-omics/omics-demos) | Synthetic, ground-truth demos that run blind and score recovery. |

## How to read validation claims

- **Simulated** — exercised without attached instruments.
- **Hardware-executed under supervision** — a named interaction ran on a physical instrument and its observed result is recorded.
- **Wet/bio-validated** — measured biological data met a stated acceptance criterion.

Unknowns remain unknown until evidence clears the next gate. A simulator result never becomes a hardware or biological claim by wording alone.

## About

Oxford PhD · joint first author in *Nature Communications* · wet lab, genomics, automation, computation, and ML. I opened an upstream PyLabRobot PR for BD FACSMelody support; it is unmerged and not hardware-validated.

Python · PyLabRobot · MCP and agent harnesses · robotic manipulation and computer vision · single-cell and low-input NGS.

[LinkedIn](https://www.linkedin.com/in/di-hu-phd-4049401a5/) · [Writing / thesis](https://reinhaudt.com)
