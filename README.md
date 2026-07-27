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

My stack separates proposal from permission:

`scientist or model proposes -> deterministic evidence gates decide -> controller executes -> measurements and decisions enter an audit ledger`

A simulator result never becomes a hardware claim by wording alone. Missing evidence
stops the run.

[Read the cross-repository architecture](https://github.com/di-omics/autonomous-lab/blob/main/docs/AI_NATIVE_WORKCELL.md).

## Start here

- **[autonomous-lab](https://github.com/di-omics/autonomous-lab)** - evidence and
  permission for autonomous workflows: QC and vision gates, recovery decisions, sample
  provenance, atomic workcell resource leases, throughput, and an honest step-by-step
  execution boundary.
- **[plr-mcp](https://github.com/di-omics/plr-mcp)** - typed PyLabRobot tools for agents,
  with simulation by default, confirmation gates, and opt-in hardware backends.
- **[plr-tested](https://github.com/di-omics/plr-tested)** - supervised physical-instrument
  run cards, exact confirmation tokens, observed results, and known failures.
- **[plr-reverse-engineer](https://github.com/di-omics/plr-reverse-engineer)** - capture,
  decode, and guarded replay for instruments with no usable API.

Run the public closed-loop prototype:

```bash
pip install 'autonomous-lab @ git+https://github.com/di-omics/autonomous-lab'
autonomous-lab loop --scenario pass
autonomous-lab loop --scenario vision_error
autonomous-lab loop --scenario missing_evidence
autonomous-lab orchestrate --scenario vision_recovery
autonomous-lab orchestrate --scenario resource_busy
autonomous-lab throughput --samples 96
```

The failing scenarios return non-zero on purpose. They select a versioned recovery or
stop with the sample still at the prior station, then verify the hash-chained run record.
All bundled observations, acceptance ranges, and timings are labeled synthetic or
assumed.

## How the portfolio fits together

| Capability | Primary repositories | What is implemented |
| --- | --- | --- |
| Laboratory intelligence | [autonomous-lab](https://github.com/di-omics/autonomous-lab), [plr-minimum-effective](https://github.com/di-omics/plr-minimum-effective) | Versioned expert gates, assay-QC decisions, bounded recovery, optimization under acceptance criteria |
| Python control and orchestration | [autonomous-lab](https://github.com/di-omics/autonomous-lab), [plr-mcp](https://github.com/di-omics/plr-mcp), [plr-reverse-engineer](https://github.com/di-omics/plr-reverse-engineer), [ot-flex-automation](https://github.com/di-omics/ot-flex-automation) | In-process atomic multi-resource tasks, typed tools, guarded device backends, no-API command recovery, explicit off-deck handoffs |
| Physical execution evidence | [plr-tested](https://github.com/di-omics/plr-tested), [benchmarks](https://github.com/di-omics/benchmarks) | Named run cards, confirmation boundaries, validation status, observed failures, evaluation criteria |
| Computer vision and robot recovery | [lab-cv](https://github.com/di-omics/lab-cv), [plr-lab-robot](https://github.com/di-omics/plr-lab-robot), [awesome-wetlab-cv](https://github.com/di-omics/awesome-wetlab-cv) | Offline lab-video QC, synthetic hand-eye and recovery benchmarks, an eval-first map of wet-lab vision tools |
| Omics workflows and analysis | [fullstack-omics](https://github.com/di-omics/fullstack-omics), [omics-demos](https://github.com/di-omics/omics-demos), [ml-bio-eval](https://github.com/di-omics/ml-bio-eval) | Simulator-only scRNA-seq and WGS flows, synthetic ground truth, bioinformatics and closed-loop evals |
| Integrated world-model demos | [bay-hack](https://github.com/di-omics/bay-hack), [robotics-devkit](https://github.com/di-omics/robotics-devkit) | Sim-first composition across planning, tools, robot bridges, testing agents, and project memory |

## Current evidence boundary

Some named STAR, ODTC, HHS, and Tecan operations have been executed on physical
instruments under human supervision. The exact run cards and caveats live in
`plr-tested`; `autonomous-lab doctor` checks their paths and confirmation tokens against
the real checkout.

Most of the portfolio remains simulated. There is no customer deployment, no revenue,
and no full wet end-to-end biological endpoint yet. The public genomics reference flow
still stops at its first manual boundary, and its no-API command maps remain undecoded.
That is the point of the ledger: unknowns stay unknown until evidence clears the next
gate.

Validation labels used across the portfolio:

- **Simulated** - exercised without attached instruments.
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
