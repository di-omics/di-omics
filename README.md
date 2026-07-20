# Di Hu

**Full-stack biologist building autonomous labs.**

Wet lab, automation, computation, ML. I encode expert judgment into autonomous execution so biological R&D runs faster, cheaper, and more reproducibly.

Oxford PhD &middot; joint first author in Nature Communications &middot; contributor to open-source PyLabRobot.

---

## What I build

Open-source autonomous-lab infrastructure built on PyLabRobot: instrument reverse-engineering, end-to-end single-cell omics, epigenomics, robotic manipulation, and an MCP layer so agents can drive the bench. Simulation-first and validated on real hardware, with plant-and-recover checks so the results are honest, not cherry-picked.

## Start here

- **[Let an agent run a simulated lab](https://github.com/di-omics/plr-mcp)** - an MCP server that exposes liquid handlers, readers, thermocyclers, and heater-shakers as safe, discoverable tools.
- **[See what has actually touched hardware](https://github.com/di-omics/plr-tested)** - Hamilton STAR and instrument-integration run cards, with the observed result as the source of truth.
- **[See the honest autonomy ledger](https://github.com/di-omics/autonomous-lab)** - a step-by-step account of what an end-to-end protocol can run unattended, and exactly what blocks the rest.
- **[Run a self-contained demo](https://github.com/di-omics/omics-demos)** - synthetic-data omics and lab-automation demos that plant ground truth, recover it blind, and score the result.

## Portfolio map

| Area | Repositories | What to expect |
| --- | --- | --- |
| **Core platform** | [plr-mcp](https://github.com/di-omics/plr-mcp), [plr-lab-robot](https://github.com/di-omics/plr-lab-robot), [plr-reverse-engineer](https://github.com/di-omics/plr-reverse-engineer) | Agent tools, robotic manipulation, and guarded paths for onboarding no-API instruments. |
| **Hardware evidence** | [plr-tested](https://github.com/di-omics/plr-tested), [autonomous-lab](https://github.com/di-omics/autonomous-lab), [lab-cv](https://github.com/di-omics/lab-cv) | Run cards, capability accounting, and physical-AI QC. |
| **Assay automation** | [plr-epigenome](https://github.com/di-omics/plr-epigenome), [fullstack-omics](https://github.com/di-omics/fullstack-omics), [ot-flex-automation](https://github.com/di-omics/ot-flex-automation) | Reusable protocols and end-to-end single-cell/genomics workflows. |
| **Evaluation and demos** | [omics-demos](https://github.com/di-omics/omics-demos), [ml-bio-eval](https://github.com/di-omics/ml-bio-eval), [plr-minimum-effective](https://github.com/di-omics/plr-minimum-effective), [benchmarks](https://github.com/di-omics/benchmarks), [blastocyst-if](https://github.com/di-omics/blastocyst-if) | Ground-truth recovery, optimization, capability metrics, and analysis examples. |
| **Community and tooling** | [awesome-wetlab-cv](https://github.com/di-omics/awesome-wetlab-cv), [robotics-devkit](https://github.com/di-omics/robotics-devkit), [bay-hack](https://github.com/di-omics/bay-hack) | Curation, reusable development tooling, and current experimental integrations. |

## How to read validation claims

- **Simulation** - exercised end to end without attached instruments.
- **Hardware-tested** - a named instrument interaction has been run and its result is recorded.
- **Bio-validated** - a wet-lab acceptance criterion has been met with measured data.

Every project should name its current tier, its last evidence, and the next gate required for promotion. Unknowns remain unknown until data clears the gate.

## Selected work

- **plr-mcp**: an MCP server for PyLabRobot, with simulation-first tools and CI across Python 3.10-3.13.
- **plr-tested**: physical-instrument run cards for the Hamilton STAR and linked instruments, with observed outcomes retained as evidence.
- **autonomous-lab**: a computed ledger of the real autonomy boundary, including the reverse-engineering queue that would move it.
- **fullstack-omics**: end-to-end autonomous scRNA-seq and scWGS in the PyLabRobot simulator, from procurement through analysis.
- **plr-reverse-engineer**: capture, decode, and guarded-replay tools for instruments with no published automation API.
- **omics-demos**: portable demonstrations that make an expected recovery result visible and testable.

I also contributed a BD FACSMelody cell-sorter backend to the core PyLabRobot project.

### Stack

Python &middot; PyLabRobot (Hamilton, Opentrons, Tecan) &middot; agent harnesses (PydanticAI, MCP) &middot; robotic manipulation and computer vision &middot; single-cell and low-input NGS.

---

[LinkedIn](https://www.linkedin.com/in/di-hu-phd-4049401a5/)
