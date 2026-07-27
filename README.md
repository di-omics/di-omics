# Di Hu

**full-stack biologist • building autonomous labs**

My work turns protocols, acceptance criteria, and failure responses into gated, auditable
execution across laboratory hardware. This profile is a public portfolio of reusable
automation, omics, robotics, and evaluation systems.

## The bet

Autonomous labs are not waiting on a vendor to ship AI-native labware. The instruments
already on benches are enough — I have been reverse-engineering them into Python one
command set at a time to prove it. What is actually missing is the layer above the
hardware: **a way to encode a domain expert's judgment into autonomous execution, and to
have that expert orchestrate the automation rather than operate it.**

That layer is the hard part, and it is hard for a specific reason. A written protocol is
not what an experienced scientist does; it is the subset that survived being written down.
The rest — when a result is real, when a sample is still recoverable, when a clean-looking
plate should be thrown away — lives in one head, gets applied a hundred times a week, and
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

- **Simulated** — exercised without attached instruments.
- **Hardware-executed under supervision** — a named interaction ran on a physical
  instrument and its observed result is recorded.
- **Wet/bio-validated** — measured biological data met a stated acceptance criterion.

Unknowns stay unknown until evidence clears the next gate. A simulator result never becomes
a hardware or biological claim by wording alone.

## Start here

- **[autonomous-lab](https://github.com/di-omics/autonomous-lab)** — computes whether a lab
  can close a loop from hypothesis to evidence, across all four legs, and names the one that
  breaks.
- **[plr-mcp](https://github.com/di-omics/plr-mcp)** — exposes PyLabRobot devices as
  agent-callable tools, simulation by default, with execution gates enforced in code.
- **[plr-tested](https://github.com/di-omics/plr-tested)** — supervised physical-instrument
  run cards and observed failures, kept as evidence.

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

## Three capability areas

### 1. Seeing — computer vision for the bench

What a camera can verify, and the hard boundary of what no camera ever will. That boundary
is a claim about physics rather than model quality: no amount of training data separates a
well of active enzyme from one of denatured enzyme, because the photons are identical. Four
of the reference lab's six silent failures sit on that side of the line, so **buying cameras
would not fix them** — and a plan that budgets for cameras to solve them is spending on the
wrong sensor.

- [lab-cv](https://github.com/di-omics/lab-cv) — plate/well detection, well-state
  classification, ROI tracking, and camera-verified liquid handling. Classical baselines
  scored against planted ground truth on synthetic renders, CPU-only. The learned-model
  seams (RF-DETR, SAM 2, VLM backends) are declared interfaces, not shipped weights.
- [spatial-flow](https://github.com/di-omics/spatial-flow) — operations platform for a
  high-throughput spatial-biology lab: specimen→core→placement→slide lineage, and a TMA
  randomization planner that spreads each patient across slides to suppress batch effects.
  Synthetic data throughout.
- [awesome-wetlab-cv](https://github.com/di-omics/awesome-wetlab-cv) — curated models,
  trackers, and robot stacks for labs that see, decide, and act.

### 2. Acting — arms, skills, and workcells

- [plr-lab-robot](https://github.com/di-omics/plr-lab-robot) — a simulation backend for
  PyLabRobot's arm API, which upstream ships without one, so the arm interface can be
  exercised with no physical robot. Eye-in-hand calibration, vision-guided pick correction,
  and a decap/recap skill that models thread-following as discrete rotation plus lift.
- [robotics-devkit](https://github.com/di-omics/robotics-devkit) — the code → simulation →
  real-robot ladder as a reusable plugin and per-repo template.
- [bay-hack](https://github.com/di-omics/bay-hack) — verified tube access: a robot uncaps a
  tube, independently verifies the cap is off, presents it for pipetting, recaps, and
  verifies closure. Ambiguity triggers recovery or a safe stop. The rule is enforced in
  code and in the sealed receipt: no verified opening, no pipetting.

### 3. Knowing — orchestration, sample identity, and provenance

- [autonomous-lab](https://github.com/di-omics/autonomous-lab) — the loop-closure layer.
  Costs every step against the real state of the code, computes which QC gates can even be
  evaluated, which failures nothing would notice, and what could be proven afterwards.
- **Sample identity** (`autonomous-lab lineage`) — every other layer tracks *containers*;
  no experiment's conclusion is about a plate. This tracks the claim the science actually
  makes. The two graphs come apart at pooling: pool 96 wells without indexing first and no
  barcode reader, no camera, and no amount of decoding recovers which cell produced which
  read. It also finds that the reference protocol's only quantification happens *after*
  pooling, so a failure confined to one well moves the number by a ninety-sixth and fails
  no gate.
- [plr-reverse-engineer](https://github.com/di-omics/plr-reverse-engineer) — capture,
  decode, and guarded replay for no-API instruments. Incomplete maps stay blocked from
  actuation.
- [plr-mcp](https://github.com/di-omics/plr-mcp) — typed, discoverable lab tools for agents,
  with the arming model enforced rather than documented.

## What is not built yet

Naming this is the same discipline as the rest of the portfolio. **Multi-instrument workcell
orchestration does not exist in any of these repos.** Plate movers, incubator and reader
handoffs, resource contention, and concurrent scheduling appear in prose and in coordinate
names; none of them is modeled in code. `autonomous-lab throughput` contains a real
pipelined scheduling model and correctly refuses to produce a plates-per-day number,
because 18 of 18 steps have never been timed. That refusal is the honest state, and closing
it is the next substantial piece of work.

## About

Oxford PhD · joint first author in *Nature Communications* · wet lab, genomics, automation,
computation, and ML. I opened an upstream PyLabRobot PR for BD FACSMelody support; it is
unmerged and not hardware-validated.

Python · PyLabRobot · MCP and agent harnesses · robotic manipulation and computer vision ·
single-cell and low-input NGS.

[LinkedIn](https://www.linkedin.com/in/di-hu-phd-4049401a5/) · [Writing / thesis](https://reinhaudt.com)
