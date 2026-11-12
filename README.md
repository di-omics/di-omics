# Di Hu

**full-stack biologist - building autonomous labs**

My work turns protocols, acceptance criteria, and failure responses into gated, auditable
execution across laboratory hardware. This profile is a public portfolio of reusable
automation, omics, robotics, and evaluation systems.

Oxford PhD / joint first author in *Nature Communications* / wet lab, genomics, automation,
computation, and ML.

[The argument](THESIS.md) / [Benchmarks](https://di-omics.github.io/benchmarks/) /
[LinkedIn](https://www.linkedin.com/in/di-hu-phd-4049401a5/) /
[Writing](https://reinhaudt.com)

## Start here

- **[autonomous-lab](https://github.com/di-omics/autonomous-lab)** -- computes whether a lab
  can close a loop from hypothesis to evidence, across all four legs, and names the one that
  breaks.
- **[plr-mcp](https://github.com/di-omics/plr-mcp)** -- exposes PyLabRobot devices as
  agent-callable tools, simulation by default, with execution gates enforced in code.
- **[plr-lab-robot](https://github.com/di-omics/plr-lab-robot)** -- a simulation backend for
  PyLabRobot's arm API, which upstream ships without.

## Capabilities

| | | |
| --- | --- | --- |
| **Autonomous lab** | orchestration, QC gates, provenance, recovery, honest hardware boundaries | [autonomous-lab](https://github.com/di-omics/autonomous-lab) |
| **Robotics** | arm control under PyLabRobot, eye-in-hand vision, instrument reverse engineering | [plr-lab-robot](https://github.com/di-omics/plr-lab-robot) |
| **Computer vision and image analysis** | detection, state, tracking, camera-verified execution, scored blind | [lab-cv](https://github.com/di-omics/lab-cv) |
| **ML for biology** | protein design loops, Bayesian assay optimization, conformal QC | [ml-design-loops](https://github.com/di-omics/ml-design-loops) |
| **Benchmarks and evals** | the metric each capability is scored on, and which numbers are still pending | [benchmarks](https://github.com/di-omics/benchmarks) |

Each row states its own evidence boundary. Most of this is simulated, and every repository
says so.

## Now: robot learning and evaluation

Started October 2026: learned robot control policies in simulation, and how far to trust the
numbers reported about them. This is early work, and the status column says exactly how
early.

| | The question | Status |
| --- | --- | --- |
| [robot-policy-evals](https://github.com/di-omics/robot-policy-evals) | Is the gain real? A known-truth audit of how robot-policy checkpoints get picked and reported, piloted on Reacher-v5, then on Diffusion Policy / PushT | plan and draft pre-registration committed; nothing run yet beyond environment checks |
| [liquid-policy-robustness](https://github.com/di-omics/liquid-policy-robustness) | Do liquid neural networks control a robot arm better under sensor noise than matched-size MLPs and LSTMs? | teacher, demonstrations, and student training run; the noise sweep has not been run |
| [ml-foundations](https://github.com/di-omics/ml-foundations) | The PyTorch training loop from the inside, on FashionMNIST | warm-up, in progress |

## What it is all for

Every layer here exists to serve one number: **how much a lab learns per dollar per
experimental cycle.** Orchestration is buildable: scheduling instruments, moving plates,
tracking samples, and holding provenance are engineering with known shapes, and the code
here does them. What is genuinely scarce is **laboratory intelligence**: knowing what a
result means, what to run next, when a clean-looking plate should be thrown away, and what a
robot must prove before it is trusted with the step.

So the portfolio is built around making that judgment explicit, attributable, and checkable.
The full argument, the four legs of a closed loop, and the order the stack has to be built
in are in **[THESIS.md](THESIS.md)**.

## Current evidence boundary

Some named operations have been executed on physical instruments under human supervision.
Most of the portfolio remains simulated. There is no customer deployment and no full wet
end-to-end biological endpoint yet. Each repository states its own evidence and validation
boundary, and the language is deliberately narrow:

- **Simulated** -- exercised without attached instruments.
- **Hardware-executed under supervision** -- a named interaction ran on a physical
  instrument and its observed result is recorded.
- **Wet/bio-validated** -- measured biological data met a stated acceptance criterion.

Unknowns stay unknown until evidence clears the next gate. A simulator result never becomes
a hardware or biological claim by wording alone.

The supervised physical-instrument run cards and observed failures live in `plr-tested`
*(private)*. It is private because the work is high stakes, and a reader who cannot inspect
the evidence should not be shown a claim resting on it.

## Repositories

**Autonomous lab**

| | |
| --- | --- |
| [autonomous-lab](https://github.com/di-omics/autonomous-lab) | evidence and permission for autonomous labs: computes whether a loop closes, and names which leg breaks |
| [plr-mcp](https://github.com/di-omics/plr-mcp) | typed, agent-callable lab tools; the arming model is enforced in code, not documented |
| [plr-reverse-engineer](https://github.com/di-omics/plr-reverse-engineer) | capture, decode, guarded replay for no-API instruments; incomplete maps stay blocked from actuation |
| [benchmarks](https://github.com/di-omics/benchmarks) | the evaluation index: what each capability is scored on, and which numbers are still pending |
| `plr-tested` *(private)* | supervised physical-instrument run cards and observed failures, kept as evidence |

**Robotics and vision**

| | |
| --- | --- |
| [plr-lab-robot](https://github.com/di-omics/plr-lab-robot) | a simulation backend for PyLabRobot's arm API, which upstream ships without |
| [lab-cv](https://github.com/di-omics/lab-cv) | detection, state classification, tracking, camera-verified liquid handling, and microscopy image analysis; every demo scored blind against a plant |
| [awesome-wetlab-cv](https://github.com/di-omics/awesome-wetlab-cv) | curated CV for labs that see, decide, and act -- with CI that checks every link |
| [robotics-devkit](https://github.com/di-omics/robotics-devkit) | plugin marketplace and template for the code-to-simulation-to-real-robot ladder, with MCP tools and test agents |

**Instruments and protocols**

| | |
| --- | --- |
| [opentrons-drivers](https://github.com/di-omics/opentrons-drivers) | serial GCode for the OT-One Smoothieboard, HTTP for OT-2 and Flex, with a simulator |
| [ot-flex-automation](https://github.com/di-omics/ot-flex-automation) | Opentrons Flex workflows for whole-genome sequencing, methylation sequencing, and TIP-seq, with explicit off-deck handoffs and validation status |
| [fullstack-omics](https://github.com/di-omics/fullstack-omics) | simulator-only scRNA-seq and whole-genome sequencing workflows, from planning through analysis handoffs |
| [omics-demos](https://github.com/di-omics/omics-demos) | synthetic, ground-truth demos for scRNA-seq, methylation sequencing, and PCR enrichment QC; no wet-lab claims |
| [plr-minimum-effective](https://github.com/di-omics/plr-minimum-effective) | finds the cheapest sequencing library prep that still gives a callable answer: unique reads per dollar, gated on in-process CV |
| [spatial-flow](https://github.com/di-omics/spatial-flow) | spatial-biology lab operations: specimen lineage and TMA batch-balance planning |

**ML**

| | |
| --- | --- |
| [ml-design-loops](https://github.com/di-omics/ml-design-loops) | ESM-2 protein design, Bayesian assay optimization under a conformal gate, and an agentic design-build-test-learn engine |
| [robot-policy-evals](https://github.com/di-omics/robot-policy-evals) | a known-truth audit of how robot-policy checkpoints get picked and reported |
| [liquid-policy-robustness](https://github.com/di-omics/liquid-policy-robustness) | liquid neural networks against matched-size MLPs and LSTMs under sensor noise |
| [ml-foundations](https://github.com/di-omics/ml-foundations) | a first PyTorch training project, kept as a lab notebook |

**Hack days**

| | |
| --- | --- |
| [bay-hack](https://github.com/di-omics/bay-hack) | verified tube access: no verified opening, no pipetting -- enforced in code and in the sealed receipt |
| [someplace](https://github.com/di-omics/someplace) | a voice companion inside a generated world |

## About

Python / PyLabRobot / MCP and agent harnesses / robotic manipulation and computer vision -
single-cell and low-input NGS.

[LinkedIn](https://www.linkedin.com/in/di-hu-phd-4049401a5/) / [Writing / thesis](https://reinhaudt.com)
