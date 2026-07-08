# Di Hu · building autonomous labs

**Full-stack omics scientist:** wet lab, computation, and automation.

Oxford DPhil (Clarendon Scholar) · joint first author in *Nature Communications* · 11 peer-reviewed papers. Built on the first automation team at **Retro Biosciences**, alongside the creator of PyLabRobot. Methods work spans epigenomics, low-input sequencing, and assay benchmarking.

I automate single-cell omics end to end, from sample intake to interpretation, as a closed loop: QC is measured upfront and gates the run, physical execution is checked (liquid-handling accuracy, computer vision on bench video), and the analysis is scored against known ground truth. Everything here runs in the PyLabRobot simulator with no hardware attached.

Most disease risk is regulatory and cell-type-specific: GWAS loci sit in non-coding DNA whose meaning shifts by cell type. My work maps that layer (transcription-factor binding and non-coding regulation at single-cell resolution) and automates it, so a risk locus becomes a cell-type-specific mechanism and a target.

---

### Selected work

| Repo | What it is | How it is evaluated |
| --- | --- | --- |
| [**fullstack-omics**](https://github.com/di-omics/fullstack-omics) | FLASH-seq scRNA-seq and single-cell WGS, procurement to analysis | Runs end to end in the PyLabRobot simulator; scWGS module at 10/10 tests |
| [**plr-mcp**](https://github.com/di-omics/plr-mcp) | PyLabRobot instruments (liquid handlers, readers, cyclers, shakers) as MCP tools | MCP tool-call round-trip; CI on Python 3.10-3.13 |
| [**omics-demos**](https://github.com/di-omics/omics-demos) | Nine self-contained demos: RNA-seq, UMI dedup, CNV, variant calling, EM-seq, demux, PyLabRobot sim | Each plants known ground truth, runs blind, scores recovery |
| [**plr-minimum-effective**](https://github.com/di-omics/plr-minimum-effective) | Minimal effective reaction search via Bayesian optimization | Cross-validated, held-out recovery |
| [**plr-clarity**](https://github.com/di-omics/plr-clarity) | Automated (sci)TIP-seq on a Hamilton STAR in PyLabRobot | Rhodamine-B validation ladder; plan-text-to-method compiler |
| [**lab-cv**](https://github.com/di-omics/lab-cv) | Offline computer vision for bench video: ROI motion QC and detection | Ground-truth-validated, CPU-only |

### How QC works

Before an assay commits reagents, two readouts gate the run:

- **Rhodamine B on the plate reader** for per-well liquid-handling accuracy and precision (CV%).
- **Qubit or PicoGreen on a small aliquot** for DNA yield and concentration.

Measure first, gate on the number, then run. QC sits at the front, not in the post-mortem.

### How I build

Eval-first: plant known ground truth, run the method blind, score the recovery. Each repo gates its claim on a number rather than a screenshot, and marks where a learned model would earn its keep. Protocol values are sourced, never invented; unknowns stay marked as such. Notes on how each repo is evaluated: [di-omics.github.io/benchmarks](https://di-omics.github.io/benchmarks/).

### More work

| Repo | What it is |
| --- | --- |
| [**blastocyst-if**](https://github.com/di-omics/blastocyst-if) | 3D immunofluorescence for whole-mount preimplantation blastocysts: Cellpose-SAM segmentation, per-nucleus quant, EPI/PE/TE lineage classification. Synthetic data, no GPU. |
| [**ot-flex-automation**](https://github.com/di-omics/ot-flex-automation) | Opentrons Flex genomics library prep: walkaway WGS (ResolveDNA), EM-seq epigenetic clock, low-input TIP-seq. |
| [**awesome-wetlab-cv**](https://github.com/di-omics/awesome-wetlab-cv) | A curated map of computer vision for the wet lab and autonomous science: foundation models, bio-image segmentation, cell tracking, VLA robotics. |

### Focus

Autonomous wet-lab execution · low-input epigenomics · PyLabRobot on Hamilton / Opentrons / Tecan · computer vision for lab video · instruments as agent-accessible tools.

---

[LinkedIn](https://www.linkedin.com/in/di-hu-phd-4049401a5/)
