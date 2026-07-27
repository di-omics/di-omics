# Di Hu

**Building [Clair](https://clair.bio) - the intelligence layer for autonomous labs.**

I am a full-stack biologist working across wet-lab assays, genomics, automation,
instrument control, computer vision, and scientific ML. I turn protocols, acceptance
criteria, and expert failure responses into gated, auditable execution across hardware a
lab already owns.

[Clair](https://clair.bio) | [Portfolio and writing](https://reinhaudt.com) |
[LinkedIn](https://www.linkedin.com/in/di-hu-phd-4049401a5/)

## The thesis

Laboratory autonomy is not a prompt-to-protocol problem. It fails at physical state,
evidence, exception handling, and recovery: whether a sample is recoverable, whether a
QC result is real, and whether the next action is safe or useful.

The bet is that labs do not need to replace every useful instrument with new
"AI-native" hardware. Existing workcells become AI-native through guarded Python
adapters, typed agent tools, computer vision and telemetry, deterministic expert policy,
robot recovery, and a shared operational memory above the hardware already on the bench.

My stack separates proposal, permission, execution, and evidence:

`scientist or model proposes -> reviewed operation contract fixes scope and budgets -> workcell leases custody and resources -> fresh deterministic gates decide -> approved adapter receives an attempt-scoped, expiring permit -> post-operation evidence advances provenance or quarantines uncertainty -> evidence enters the ledger`

A simulator result never becomes a hardware claim by wording alone. Missing evidence
stops the run.

[Read the cross-repository architecture](https://github.com/di-omics/autonomous-lab/blob/agent/closed-loop-intelligence/docs/AI_NATIVE_WORKCELL.md).

## Start here

- **[autonomous-lab](https://github.com/di-omics/autonomous-lab)** - evidence and
  permission for autonomous workflows: fingerprinted expert policies and operation
  contracts loaded into an in-memory approval registry, fresh QC/vision/telemetry gates,
  exact sample-bound evidence, in-process sample/task/resource leases, expiring attempt
  permits, post-operation evidence gates, uncertainty quarantine, throughput, and an
  honest execution boundary.
- **[plr-mcp](https://github.com/di-omics/plr-mcp)** - typed PyLabRobot tools for agents,
  with a process-local run/task/sample context, registered sample links, intent-before-driver
  fsynced JSONL events, typed hash-linked provenance, simulation by default, and an exact
  tool allowlist plus operator confirmation for real mutation.
- **[spatial-flow](https://github.com/di-omics/spatial-flow)** - synthetic spatial-imaging
  QC and release control: expected-versus-observed identity, SHA-256 manifest digests and
  event-chain verification, fail-closed `RELEASE`/`RETRY`/`HOLD` routing, and expert-only
  disposition for identity or provenance failures. It contains no trained CV model or real
  images.
- **[plr-lab-robot](https://github.com/di-omics/plr-lab-robot)** - simulation-validated
  robot workcells with typed labware moves, simulator-state pre/postconditions, at most three
  attempts, halt-and-recheck transient retry, refusal to replay a partial pick, command
  traces, and integrity-checkable JSON outcomes.
- **[plr-tested](https://github.com/di-omics/plr-tested)** - supervised physical-instrument
  run cards, exact confirmation tokens, observed results, and known failures.
- **[plr-reverse-engineer](https://github.com/di-omics/plr-reverse-engineer)** - capture,
  decode, and guarded replay for instruments with no usable API.

Run the public closed-loop prototype:

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

## How the portfolio fits together

| Capability | Primary repositories | What is implemented |
| --- | --- | --- |
| Laboratory intelligence | [autonomous-lab](https://github.com/di-omics/autonomous-lab), [plr-minimum-effective](https://github.com/di-omics/plr-minimum-effective) | Fingerprinted expert policies, exact operation contracts in an in-memory approval registry, source/freshness gates, contract-bound recovery, post-operation evidence gates, uncertainty quarantine, and optimization under acceptance criteria |
| Python control and orchestration | [autonomous-lab](https://github.com/di-omics/autonomous-lab), [plr-mcp](https://github.com/di-omics/plr-mcp), [plr-reverse-engineer](https://github.com/di-omics/plr-reverse-engineer), [ot-flex-automation](https://github.com/di-omics/ot-flex-automation) | Contract-derived resource scope and budgets, in-process sample/task/resource leases, expiring attempt permits, process-local MCP run context, intent-before-driver JSONL, exact hardware mutation allowlists, guarded device backends, no-API command recovery, and explicit off-deck handoffs |
| Sample identity and provenance | [autonomous-lab](https://github.com/di-omics/autonomous-lab), [plr-mcp](https://github.com/di-omics/plr-mcp), [spatial-flow](https://github.com/di-omics/spatial-flow) | In-memory sample lineage, location, consumption, and uncertainty state; registered sample IDs bound to fsynced MCP run events; synthetic specimen/acquisition identity bound to manifest and event hashes |
| Physical execution evidence | [plr-tested](https://github.com/di-omics/plr-tested), [benchmarks](https://github.com/di-omics/benchmarks) | Named run cards, confirmation boundaries, validation status, observed failures, evaluation criteria |
| Spatial and lab computer vision | [spatial-flow](https://github.com/di-omics/spatial-flow), [lab-cv](https://github.com/di-omics/lab-cv), [awesome-wetlab-cv](https://github.com/di-omics/awesome-wetlab-cv) | Synthetic identity-bound imaging release with manifest/event-chain verification, offline lab-video QC, and an eval-first map of wet-lab vision tools |
| Robotics and workcells | [plr-lab-robot](https://github.com/di-omics/plr-lab-robot), [autonomous-lab](https://github.com/di-omics/autonomous-lab), [robotics-devkit](https://github.com/di-omics/robotics-devkit) | Simulation-validated arm and task control, typed move-labware contracts, simulator-state gates, halt-and-recheck bounded retry, partial-pick stop, integrity-checkable outcomes, and contract-derived in-process workcell leasing |
| Omics workflows and analysis | [fullstack-omics](https://github.com/di-omics/fullstack-omics), [omics-demos](https://github.com/di-omics/omics-demos), [ml-bio-eval](https://github.com/di-omics/ml-bio-eval) | Simulator-only scRNA-seq and WGS flows, synthetic ground truth, bioinformatics and closed-loop evals |
| Integrated world-model demos | [bay-hack](https://github.com/di-omics/bay-hack), [robotics-devkit](https://github.com/di-omics/robotics-devkit) | Sim-first composition across planning, tools, robot bridges, testing agents, and project memory |

## Current evidence boundary

Some named STAR, ODTC, HHS, and Tecan operations have been executed on physical
instruments under human supervision. The exact run cards and caveats live in
`plr-tested`; `autonomous-lab doctor` checks their paths and confirmation tokens against
the real checkout.

These slices are compatible, but they are not yet wired into one wet end-to-end runtime.
`plr-mcp` carries registered sample links and policy IDs through tool calls; it does not
evaluate sample-state policy or replace the orchestrator. Most of the portfolio remains
synthetic or simulated: the spatial release-gate evidence uses generated fixtures, and
the robot task benchmarks run against a simulator. They are not real-CV accuracy,
robot-hardware, or clinical-validation claims. There is no customer deployment, no
revenue, and no full wet end-to-end biological endpoint yet. The public genomics
reference flow still stops at its first manual boundary, and its no-API command maps
remain undecoded. That is the point of the ledger: unknowns stay unknown until evidence
clears the next gate.

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
does not disappear between assay, software, and robotics teams.

Python | PyLabRobot | MCP and agent harnesses | robotic manipulation and computer vision |
single-cell and low-input NGS | assay QC and bioinformatics
