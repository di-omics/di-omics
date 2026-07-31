# Di Hu

**full-stack biologist - building autonomous labs**

My work turns protocols, acceptance criteria, and failure responses into gated, auditable
execution across laboratory hardware. This profile is a public portfolio of reusable
automation, omics, robotics, and evaluation systems.

## Capabilities

| | | |
| --- | --- | --- |
| **Autonomous lab** | orchestration, QC gates, provenance, recovery, honest hardware boundaries | [autonomous-lab](https://github.com/di-omics/autonomous-lab) |
| **Robotics** | arm control under PyLabRobot, eye-in-hand vision, instrument reverse engineering | [plr-lab-robot](https://github.com/di-omics/plr-lab-robot) |
| **Computer vision and image analysis** | detection, state, tracking, camera-verified execution, scored blind | [lab-cv](https://github.com/di-omics/lab-cv) |
| **Spatial AI and world models** | action-conditioned prediction, abstention gates, the ceiling of what prediction resolves | `bench-world-model` *(in build)* |
| **ML for biology** | protein design loops, Bayesian assay optimization, conformal QC | [ml-design-loops](https://github.com/di-omics/ml-design-loops) |
| **Benchmarks and evals** | the metric each capability is scored on, and which numbers are still pending | [benchmarks](https://github.com/di-omics/benchmarks) |

Each row states its own evidence boundary. Most of this is simulated, and every repository
says so. A row with no link is a row with nothing to show yet.

## What it is all for

Every layer below exists to serve one number: **how much this lab learns per dollar per
experimental cycle.** Stating that first changes what counts as progress. Throughput is not
the goal, autonomy is not the goal, and neither is a robot that runs overnight. A lab that
runs a thousand plates a day and cannot tell which of them is real has bought motion, not
information.

Three things cap that number, and they are not the ones usually shopped for.

**The ceiling is set by design, not by spend.** If attribution to the unit you are asking
about has been destroyed, a per-unit question is unanswerable at any budget: pool 96 wells
without indexing first and no number of reads recovers which cell produced which molecule.
If every gate that would produce a decision is unevaluable, the cycle yields data and no
decision. Separating "buy more" from "this cannot work" is the most useful thing the stack
computes.

**The discount nobody applies is silent failure.** A campaign with destructive failure modes
that nothing would catch does not yield its nominal information. Some fraction of its output
is confidently wrong, and confidently wrong is worse than missing, because it gets acted on.

**The binding constraint is usually not the one being priced.** Across execution,
measurement, decision, record, detection coverage, instrument durability, and expert
transfer, exactly one of them caps information per dollar at any moment. Computing which one
tells you whether to build orchestration, repair an instrument, run a calibration, or go and
find expertise.

That last point is the procurement argument, and it is why this portfolio builds what it
builds. **Orchestration is buildable.** Scheduling instruments, moving plates, tracking
samples, and holding provenance are engineering with known shapes, and the code here does
them. What is genuinely scarce, and therefore what is worth paying for, is **laboratory
intelligence**: knowing what a result means, what to run next, when a clean-looking plate
should be thrown away, and what a robot must prove before it is trusted with the step. That
is the part that does not come in a box.

## The bet

Autonomous labs are not waiting on a vendor to ship AI-native labware. The instruments
already on benches are enough -- I have been reverse-engineering them into Python one
command set at a time to prove it. What is actually missing is the layer above the
hardware: **a way to encode a domain expert's judgment into autonomous execution, and to
have that expert orchestrate the automation rather than operate it.**

That layer is the hard part, and it is hard for a specific reason. A written protocol is
not what an experienced scientist does; it is the subset that survived being written down.
The rest -- when a result is real, when a sample is still recoverable, when a clean-looking
plate should be thrown away -- lives in one head, gets applied a hundred times a week, and
is exactly what fails to transfer when a lab automates. Buying a better robot does not
touch it.

So the portfolio is built around making that judgment explicit, attributable, and
checkable: thresholds that carry the basis they rest on, gates that refuse to fire when
their input is untrustworthy, failure modes that declare how they would be caught and get
downgraded when that path does not exist, and benchmarks a robot must meet before it is
trusted with a task. An operation nobody has benchmarked is untrusted by default, which is
the opposite of the usual convention and the correct one.

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

## Start here

- **[autonomous-lab](https://github.com/di-omics/autonomous-lab)** -- computes whether a lab
  can close a loop from hypothesis to evidence, across all four legs, and names the one that
  breaks.
- **[plr-mcp](https://github.com/di-omics/plr-mcp)** -- exposes PyLabRobot devices as
  agent-callable tools, simulation by default, with execution gates enforced in code.
- **`plr-tested`** *(private)* -- supervised physical-instrument run cards and observed
  failures, kept as evidence. Private because the work is high stakes, and a reader who
  cannot inspect the evidence should not be shown a claim resting on it.

## Four legs, not one number

Executing a protocol is the leg everyone measures. A lab that executes perfectly and cannot
tell a good plate from a bad one is not running an experiment, it is moving liquid. Closing
a single loop takes four things, and they fail independently:

| Leg | The question | What failure means |
| --- | --- | --- |
| **Execute** | can the machine perform the step? | reverse-engineering work |
| **Measure** | does a result arrive, from the right assay? | an instrument that returns a usable number |
| **Decide** | would anything notice when it goes wrong? | a detection path for failures that destroy material |
| **Record** | could it be proven and replayed afterwards? | barcodes, or an arm that reports its moves |

On the single-cell genomics reference workflow, all four currently break, for four different
reasons. Collapsing that into one autonomy percentage would hide which budget to spend.
`autonomous-lab loop` computes it.

## The stack

An autonomous lab is not one machine, and the pieces fail independently. This is the order
they have to be built in, because each one is what makes the next one meaningful.

**1 / Move it.** Multi-instrument orchestration and the arm that carries plates between
boxes. One plate at a time wastes the instruments, so the moment a second enters, a set of
constraints appears that no single-run report can see: two plates want the same liquid
handler, a human is needed at 2am, a finished plate sits on a deck nobody can clear.
`autonomous-lab schedule` computes what serializes without inventing a single duration --
the serialization point is whichever instrument owns the most steps, which is true at any
speed. It also prices the arm honestly: on the reference protocol a plate mover clears
**5 of 22 stalls and none of the 8 undecoded commands.** Which purchase helps is computable
before the order rather than after it.

**2 / See it, and know what seeing cannot do.** Deploy the best available vision, and be
precise about its ceiling. `vision` sorts conditions into `visible`, `visible_indirect`, and
`invisible` -- and that last boundary is a claim about **physics, not model quality**. No
amount of training data separates a well of active enzyme from one of denatured enzyme,
because the photons are identical.

**3 / Gate what vision cannot reach.** This is the composition that makes the whole thing
work, and it is why the two are one layer rather than two. Where a camera is physically
incapable, an assay is the *only* remaining option -- a plate read, a bioanalyzer trace, a
quantification step. So an invisible failure with no gate behind it is uncovered, and no CV
budget will ever change that. Deploying a newer model has a ceiling, and the ceiling is
computable in advance.

**4 / Close the loop.** Measure, compare, correct. Each of those has a specific way of being
fake, and the load-bearing one is latency: a measurement taken after the material is
consumed cannot steer anything however accurate it is. It is a post-mortem wearing the
costume of a control loop.

**5 / Keep it running.** Instruments wear, calibrations expire, consumables deplete. A
schedule that ignores this is a schedule for the first week. The insurance question is not
"when will it fail" -- predicting that needs reliability data nobody here has -- but *what
is this instrument currently entitled to be trusted with*, and does a planned campaign cross
a service boundary mid-run. Nothing downstream repairs a plate that started before a
calibration expired and finished after.

**6 / Then the intelligence layer.** Once the infrastructure holds, the thing that is
actually missing is the transfer itself: **a scientist demonstrating an operation, and a
machine measured against that demonstration.** That is the step between "the robot executes
the script" and "the robot performs the task as well as the person who taught it."

The honest core of it is that an expert demonstration is *data, not authority*. A scientist
doing something twice is not a specification -- it is two observations with a spread, and
the spread is the information. Most operations have no expert envelope at all, and that list
is the real backlog of an automation programme. Nobody writes it down. This does.

## Repositories

| | |
| --- | --- |
| [autonomous-lab](https://github.com/di-omics/autonomous-lab) | the layer that computes all of the above and names which leg breaks |
| [plr-mcp](https://github.com/di-omics/plr-mcp) | typed, agent-callable lab tools; the arming model is enforced in code, not documented |
| [plr-reverse-engineer](https://github.com/di-omics/plr-reverse-engineer) | capture, decode, guarded replay for no-API instruments; incomplete maps stay blocked from actuation |
| `plr-tested` *(private)* | supervised physical-instrument run cards and observed failures, kept as evidence |
| [plr-lab-robot](https://github.com/di-omics/plr-lab-robot) | a simulation backend for PyLabRobot's arm API, which upstream ships without |
| [lab-cv](https://github.com/di-omics/lab-cv) | detection, state classification, tracking, camera-verified liquid handling, and microscopy image analysis; every demo scored blind against a plant |
| [ml-design-loops](https://github.com/di-omics/ml-design-loops) | ESM-2 protein design, Bayesian assay optimization under a conformal gate, and an agentic design-build-test-learn engine |
| [benchmarks](https://github.com/di-omics/benchmarks) | the evaluation index: what each capability is scored on, and which numbers are still pending |
| [opentrons-drivers](https://github.com/di-omics/opentrons-drivers) | serial GCode for the OT-One Smoothieboard, HTTP for OT-2 and Flex, with a simulator |
| [spatial-flow](https://github.com/di-omics/spatial-flow) | spatial-biology lab operations: specimen lineage and TMA batch-balance planning |
| [awesome-wetlab-cv](https://github.com/di-omics/awesome-wetlab-cv) | curated CV for labs that see, decide, and act -- with CI that checks every link |
| [bay-hack](https://github.com/di-omics/bay-hack) | verified tube access: no verified opening, no pipetting -- enforced in code and in the sealed receipt |
| `bench-world-model` *(in build)* | action-conditioned prediction of a workcell, and the gate that refuses to act when the model cannot predict |

## What is not built yet

Naming this is the same discipline as the rest. The intelligence layer is the newest and
least proven part of the stack, and most of it is simulated. There is no sustained
production evidence here and no wet biological endpoint. The published record does not have
one either: **no cited system demonstrates integrated multi-domain autonomous operation at a
production rate**, and `autonomous-lab evidence` will not return a citation that claims
otherwise.

## About

Oxford PhD / joint first author in *Nature Communications* / wet lab, genomics, automation,
computation, and ML. I opened an upstream PyLabRobot PR for BD FACSMelody support; it is
unmerged and not hardware-validated.

Python / PyLabRobot / MCP and agent harnesses / robotic manipulation and computer vision -
single-cell and low-input NGS.

[LinkedIn](https://www.linkedin.com/in/di-hu-phd-4049401a5/) / [Writing / thesis](https://reinhaudt.com)
