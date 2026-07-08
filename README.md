# Di Hu · building autonomous labs

**Full-stack omics scientist:** wet lab, computation, and automation, the three layers usually split across three people.

Oxford DPhil (Clarendon Scholar) · joint first author in *Nature Communications* · 11 peer-reviewed papers. Built on the first automation team at **Retro Biosciences**, alongside the creator of PyLabRobot. Methods work spans epigenomics, low-input sequencing, and assay benchmarking.

> **I build autonomous, senior-scientist omics: any sample, from intake to interpretation, at the principal bar.** Every assay runs as a closed loop. QC is baked in upfront, execution is verified from video, and the result is scored against a number a senior scientist would sign off on. One scientist, the full stack, reproducible at scale.

Most disease risk is regulatory and cell-type-specific: GWAS loci sit in non-coding DNA whose meaning shifts by cell type. My through-line is mapping that layer (transcription-factor binding and non-coding regulation at single-cell resolution) and automating it, so a risk locus becomes a cell-type-specific mechanism and a target.

---

### Two bars, both high

Every repo here has to clear a benchmark on **both** axes at once:

- **The bio bar** is a number a senior scientist recognizes, and it covers both halves: the physical biology and chemistry ran (liquid-handling CV%, yield, verified not assumed) and the bioinformatics recovers ground truth (recovery, coverage, lineage-call accuracy), scored on a statistical framework fixed before the run.
- **The AI bar** is the eval that makes it an environment an agent can be trained and graded in: blind method runs, instruments driven as tools, physical-AI QC baked in, closed-loop feedback with agentic correction, spatial verification of physical execution from video.

| Capability | Bio bar (a scientist checks) | AI bar (the eval) | Graded by | Human / expert in loop |
| --- | --- | --- | --- | --- |
| [**fullstack-omics**](https://github.com/di-omics/fullstack-omics) · FLASH-seq scRNA + scWGS | UMI molecule counts, low-input recovery, coverage | end to end in the PyLabRobot simulator (scWGS 10/10 tests) | scanpy result · BJ-WGS variant concordance | 1 approval before purchase, operator at the deck |
| [**plr-mcp**](https://github.com/di-omics/plr-mcp) · instruments as agent tools | actions execute on liquid handler / reader / cycler | MCP tool-call round-trip, CI green on 3.10-3.13 | simulator + hardware handshake | agent proposes, operator confirms |
| [**omics-demos**](https://github.com/di-omics/omics-demos) · nine scored demos | method recovery vs. planted ground truth | blind run, recovery score per assay | recovery score, not a screenshot | none (fully automated eval) |
| [**plr-minimum-effective**](https://github.com/di-omics/plr-minimum-effective) · minimal recipe search | yield held at reduced reagent | Bayesian optimization, held-out recovery | cross-validated recovery | expert sets the acceptance floor |
| [**plr-clarity**](https://github.com/di-omics/plr-clarity) · (sci)TIP-seq on Hamilton STAR | Rhodamine-B validation ladder, real deck | plan text compiled into a runnable method | validation tier reached | expert signs off each tier |
| [**lab-cv**](https://github.com/di-omics/lab-cv) · spatial AI on bench video | wells filled / empty, pipetting correct | ROI motion QC, detection on protocol video | ground-truth-validated, CPU-only | reviewer adjudicates edge cases |

**[Live benchmark scoreboard](https://di-omics.github.io/benchmarks/)**: the two bars, the infra that proves them, and the anti-fooling guardrails. Hard numbers get pushed up one green cell at a time.

---

### QC is baked in upfront, and it fails closed

Before any assay commits reagents, two cheap readouts gate the run:

- **Rhodamine B on the plate reader** for liquid-handling accuracy and precision (per-well CV%). READY or NEEDS_CALIBRATION.
- **Qubit or PicoGreen on a small aliquot** for DNA yield and concentration, so a bad input never propagates downstream.

Same pattern everywhere: measure first, gate on the number, only then run. QC sits at the front, not in the post-mortem.

---

### More work

| Repo | What it is |
| --- | --- |
| [**blastocyst-if**](https://github.com/di-omics/blastocyst-if) | 3D immunofluorescence for whole-mount preimplantation blastocysts: Cellpose-SAM nuclear segmentation, per-nucleus marker quant, EPI/PE/TE lineage classification. Synthetic data, no GPU. |
| [**ot-flex-automation**](https://github.com/di-omics/ot-flex-automation) | Opentrons Flex genomics library prep: walkaway WGS (ResolveDNA), EM-seq epigenetic clock, low-input TIP-seq. |
| [**awesome-wetlab-cv**](https://github.com/di-omics/awesome-wetlab-cv) | A curated map of computer vision for the wet lab and autonomous science: foundation models, bio-image segmentation, cell tracking, VLA robotics, and the eval stack to compose them. |

### How I build

**Eval-first.** Plant known ground truth, run the method blind, score the recovery. Every repo gates its claim on a number, not a screenshot, and shows the seam where a learned model earns its keep. The lab is the environment, a benchmark is the reward, and a senior scientist is the grader.

### Focus

Autonomous wet-lab execution · low-input epigenomics · PyLabRobot on Hamilton / Opentrons / Tecan · spatial AI for lab video · instruments as agent-accessible tools.

---

[LinkedIn](https://www.linkedin.com/in/di-hu-phd-4049401a5/)
