# Di Hu

**Building [Clair](https://clair.bio) - the intelligence layer for autonomous labs.**

I am a full-stack biologist working across wet-lab assays, genomics, automation,
instrument control, computer vision, and scientific ML. I turn protocols, acceptance
criteria, and expert failure responses into gated, auditable execution across hardware a
lab already owns.

[Clair](https://clair.bio) | [Portfolio and writing](https://reinhaudt.com) |
[LinkedIn](https://www.linkedin.com/in/di-hu-phd-4049401a5/)

## The bet

Autonomous labs are not waiting on a vendor to ship AI-native labware. The instruments
already on benches are enough; I have been reverse-engineering them into guarded Python
interfaces one command set at a time. What is missing is the layer above the hardware: a
way to encode a domain expert's judgment into autonomous execution, so that the expert
orchestrates the automation rather than operating every instrument.

That layer is hard for a specific reason. A written protocol is not what an experienced
scientist does; it is the subset that survived being written down. The rest - when a result
is real, when a sample is still recoverable, when a clean-looking plate should be rejected
- lives in one head and is exactly what fails to transfer when a lab automates. Buying a
better robot does not solve it.

The portfolio makes that judgment explicit, attributable, and checkable: thresholds carry
their basis, gates refuse to fire on stale or untrustworthy evidence, failures declare how
they would be detected, and robot tasks remain untrusted until they meet a benchmark.

## The system

Laboratory autonomy is not a prompt-to-protocol problem. It fails at physical state,
evidence, exception handling, and recovery. My stack separates proposal, permission,
execution, and evidence:

`scientist or model proposes -> reviewed contract fixes scope and budgets -> workcell leases sample custody and resources -> fresh deterministic gates decide -> approved adapter receives an expiring attempt permit -> post-operation evidence advances provenance or quarantines uncertainty -> evidence enters the ledger`

The current public draft binds evidence to the exact sample and leased resources, derives
scope and retry budgets from an approved operation contract, and fails closed when evidence
is missing or stale. A simulator result never becomes a hardware claim by wording alone.

[Read the cross-repository architecture](https://github.com/di-omics/autonomous-lab/blob/agent/closed-loop-intelligence/docs/AI_NATIVE_WORKCELL.md).

### Four legs, not one number

Executing a protocol is the leg everyone measures. A lab that executes perfectly and
cannot tell a good plate from a bad one is not running an experiment; it is moving liquid.
Closing one scientific loop takes four things, and they fail independently:

| Leg | The question | What failure means |
| --- | --- | --- |
| **Execute** | Can the machine perform the step? | Instrument control or reverse-engineering work |
| **Measure** | Does the right result arrive from the right assay? | A missing or unusable measurement path |
| **Decide** | Would anything notice when it goes wrong? | A missing detection or expert-policy gate |
| **Record** | Could the action and evidence be attributed and replayed? | Missing identity, lineage, or provenance |

On the single-cell genomics reference workflow, the legs currently break for different
reasons. Collapsing that into one autonomy percentage would hide which budget to spend.
`autonomous-lab loop` names the blocking leg instead.

## Start here

- **[autonomous-lab](https://github.com/di-omics/autonomous-lab)** - the loop-closure and
  policy-gated workcell layer. Its current draft uses exact contract fingerprints in an
  in-memory approval registry, sample-bound fresh evidence, a process-wide resource
  namespace, expiring attempt permits, bounded recovery, post-operation gates, a
  hash-chained ledger, and uncertainty quarantine.
- **[plr-mcp](https://github.com/di-omics/plr-mcp)** - typed PyLabRobot tools for agents,
  with process-local run/task/sample context, registered sample links, intent recorded to
  fsynced JSONL before driver calls, typed hash-linked provenance, simulation by default,
  and an exact tool allowlist plus operator confirmation for real mutation. It carries
  policy identifiers but is not a policy engine.
- **[spatial-flow](https://github.com/di-omics/spatial-flow)** - synthetic spatial-imaging
  release control: expected-versus-observed identity, SHA-256 manifest digests and
  event-chain verification, fail-closed `RELEASE`/`RETRY`/`HOLD` routing, and expert-only
  disposition for identity or provenance failures. It ships no trained CV model or real
  image dataset.
- **[plr-lab-robot](https://github.com/di-omics/plr-lab-robot)** - simulation-only robot
  workcell tasks with typed labware moves, simulator-visible pre/postconditions, no more
  than three attempts, halt-and-recheck transient retry, refusal to replay a partial pick,
  command traces, and integrity-checkable outcomes.
- **[plr-tested](https://github.com/di-omics/plr-tested)** - supervised
  physical-instrument run cards, exact confirmation tokens, observed results, and known
  failures.
- **[plr-reverse-engineer](https://github.com/di-omics/plr-reverse-engineer)** - capture,
  decode, and guarded replay for instruments with no usable API. Incomplete command maps
  stay blocked from actuation.

Run the branch-pinned closed-loop prototype:

```bash
pip install 'autonomous-lab @ git+https://github.com/di-omics/autonomous-lab@agent/closed-loop-intelligence'
autonomous-lab loop --scenario pass
autonomous-lab loop --scenario vision_error
autonomous-lab loop --scenario missing_evidence
autonomous-lab orchestrate --scenario vision_recovery
autonomous-lab orchestrate --scenario resource_busy
autonomous-lab orchestrate --scenario ambiguous_driver_timeout
autonomous-lab throughput --samples 96
```

Scenarios that stop or quarantine return non-zero on purpose, and recovery stays bounded.
An ambiguous driver timeout marks the sample state uncertain, retains its last confirmed
location, records the possible destination, and verifies the hash-chained run record. All
bundled observations, acceptance ranges, and timings are labeled synthetic or assumed.

## Three capability areas

### 1. Seeing - spatial and laboratory computer vision

The first question is not only what a camera can verify, but what it cannot. Some failures
are physically invisible: no amount of training data can distinguish active enzyme from
denatured enzyme when the observable signal is identical. Those cases require another
sensor or assay, not a stronger vision claim.

- [spatial-flow](https://github.com/di-omics/spatial-flow) binds synthetic
  specimen/acquisition identity to manifest and event hashes before an imaging result can
  be released. The release-gate fixtures are generated; this is not a trained-model or
  real-image accuracy claim.
- [lab-cv](https://github.com/di-omics/lab-cv) evaluates plate/well detection, well-state
  classification, ROI tracking, and camera-verifiable liquid handling against planted
  ground truth on synthetic renders. Learned-model seams are interfaces, not shipped
  weights.
- [awesome-wetlab-cv](https://github.com/di-omics/awesome-wetlab-cv) maps models, trackers,
  and robot stacks for labs that see, decide, and act.

### 2. Acting - robot arms, skills, and workcells

- [plr-lab-robot](https://github.com/di-omics/plr-lab-robot) makes typed labware moves
  testable in simulation and records the precondition, command trace, retry decision, and
  integrity-linked outcome. The draft does not claim robot-hardware validation.
- [robotics-devkit](https://github.com/di-omics/robotics-devkit) packages the code-to-
  simulation-to-real-robot validation ladder as a reusable plugin and repository template.
- [bay-hack](https://github.com/di-omics/bay-hack) demonstrates the safety shape of a tube
  access task: opening must be independently verified before pipetting, and ambiguity
  routes to recovery or a safe stop.

The `autonomous-lab` draft now supplies in-memory policy-gated orchestration above those
task adapters: exact approved contracts, sample and resource binding, process-wide
namespace leases, bounded recovery, and post-operation evidence. That is a real software
slice, not yet a durable or deployed workcell.

### 3. Knowing - expert policy, sample identity, and provenance

- [autonomous-lab](https://github.com/di-omics/autonomous-lab) computes which legs of a
  scientific loop can close, evaluates deterministic evidence gates, and records proposed,
  permitted, attempted, observed, and quarantined states separately.
- **Sample identity** (`autonomous-lab lineage`) tracks the scientific claim, not only the
  container. The sample and container graphs can diverge at pooling: pool wells without
  preserving identity first, and no barcode reader, camera, or later decoding can recover
  which source produced which result.
- [plr-mcp](https://github.com/di-omics/plr-mcp) carries registered sample links and policy
  IDs into process-local tool context and records intent before invoking a driver. It does
  not evaluate sample-state policy or replace the orchestrator.
- [plr-tested](https://github.com/di-omics/plr-tested) anchors named supervised physical
  runs, while [plr-reverse-engineer](https://github.com/di-omics/plr-reverse-engineer)
  turns captured no-API traffic into guarded Python operations.

## Repository map

| Capability | Primary repositories | Implemented boundary |
| --- | --- | --- |
| Laboratory intelligence | [autonomous-lab](https://github.com/di-omics/autonomous-lab), [plr-minimum-effective](https://github.com/di-omics/plr-minimum-effective) | Fingerprinted expert policy, exact approved contracts, source/freshness gates, bounded recovery, uncertainty quarantine, and optimization under acceptance criteria |
| Python control | [plr-mcp](https://github.com/di-omics/plr-mcp), [plr-reverse-engineer](https://github.com/di-omics/plr-reverse-engineer), [ot-flex-automation](https://github.com/di-omics/ot-flex-automation) | Typed tool context, intent-before-driver events, exact hardware-mutation allowlists, guarded device backends, no-API command recovery, and explicit off-deck handoffs |
| Sample identity and provenance | [autonomous-lab](https://github.com/di-omics/autonomous-lab), [plr-mcp](https://github.com/di-omics/plr-mcp), [spatial-flow](https://github.com/di-omics/spatial-flow) | In-memory lineage/location/uncertainty state, registered sample links in fsynced events, and synthetic acquisition identity bound to manifest and event hashes |
| Physical execution evidence | [plr-tested](https://github.com/di-omics/plr-tested), [benchmarks](https://github.com/di-omics/benchmarks) | Named run cards, confirmation boundaries, validation status, observed failures, and evaluation criteria |
| Spatial/lab CV | [spatial-flow](https://github.com/di-omics/spatial-flow), [lab-cv](https://github.com/di-omics/lab-cv), [awesome-wetlab-cv](https://github.com/di-omics/awesome-wetlab-cv) | Synthetic identity-bound release gates, offline/synthetic vision evaluation, and an eval-first map of wet-lab vision tools |
| Robotics/workcells | [plr-lab-robot](https://github.com/di-omics/plr-lab-robot), [autonomous-lab](https://github.com/di-omics/autonomous-lab), [robotics-devkit](https://github.com/di-omics/robotics-devkit) | Simulation-validated typed moves plus in-memory contract, lease, permit, recovery, and quarantine machinery |
| Omics workflows and analysis | [fullstack-omics](https://github.com/di-omics/fullstack-omics), [omics-demos](https://github.com/di-omics/omics-demos), [ml-bio-eval](https://github.com/di-omics/ml-bio-eval) | Simulator-only scRNA-seq and WGS flows, synthetic ground truth, bioinformatics, and closed-loop evaluations |
| Integrated world-model demos | [bay-hack](https://github.com/di-omics/bay-hack), [robotics-devkit](https://github.com/di-omics/robotics-devkit) | Sim-first composition across planning, tools, robot bridges, testing agents, and project memory |

## Current evidence boundary

Evidence is federated rather than laundered into one portfolio-wide claim: each repository
states what its own code and artifacts support. Some named STAR, ODTC, HHS, and Tecan
operations have been executed on physical instruments under human supervision; their run
cards and caveats live in `plr-tested`. `autonomous-lab doctor` checks those paths and
confirmation tokens against a real checkout.

The software slices are compatible, but they are not yet wired into one wet end-to-end
runtime. The new multi-instrument workcell orchestrator exists as an in-memory,
policy-gated draft: it models task claims, sample custody, resource contention, bounded
recovery, and uncertainty. Durable cross-process coordination, crash-atomic external
storage, persistent adapter-side idempotency, instrument-driver integration, and one wet
deployed runtime remain unbuilt.

Most repositories remain synthetic or simulated. `spatial-flow` uses generated fixtures;
`plr-lab-robot` runs against a simulator. These are not real-CV accuracy, robot-hardware,
clinical-validation, customer-deployment, or revenue claims. The public genomics reference
flow still stops at its first manual boundary, and its no-API command maps remain
incomplete. Unknowns stay unknown until evidence clears the next gate.

Validation labels used across the portfolio:

- **Synthetic** - generated fixtures or data with no device control.
- **Simulated** - real control code exercised against a simulator.
- **Dry-run on hardware** - motion or control path ran without the full wet assay.
- **Hardware-executed under supervision** - a named physical interaction ran and its
  observed result is recorded.
- **Wet/bio-validated** - measured biological data met a stated acceptance criterion.
- **Independently reproduced** - a bounded workflow passed outside the development setup.

## About

Oxford PhD; joint first author in *Nature Communications*. I have built wet-lab assays,
omics analysis, and automation across aging biology, genomics, and scientific tooling.
I now write the instrument and orchestration layers myself so tacit scientific judgment
does not disappear between assay, software, and robotics teams. I opened an upstream
PyLabRobot PR for BD FACSMelody support; it remains unmerged and is not hardware-validated.

Python | PyLabRobot | MCP and agent harnesses | robotic manipulation and computer vision |
single-cell and low-input NGS | assay QC and bioinformatics
