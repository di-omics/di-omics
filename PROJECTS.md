# Projects by theme

[Profile](https://github.com/di-omics) / [The argument behind the work](THESIS.md)

[Scientific benchmarks](#scientific-benchmarks) / [Reinforcement learning and ML](#reinforcement-learning-and-ml) / [Robotics and vision](#robotics-and-vision) / [Autonomous labs](#autonomous-labs) / [Instruments and omics](#instruments-and-omics) / [Hackathons](#hackathons)

## Scientific benchmarks

| Project | What you can inspect |
| --- | --- |
| [sc-zprime](https://github.com/di-omics/sc-zprime) | An independent grader reproduces published scBench and SpatialBench verdicts. Tracing the methods behind the answers shows where shortcuts earn credit. |
| [sc-controls](https://github.com/di-omics/sc-controls) | Scripted positive and negative controls run on the public data for one scBench task and are graded against its published pass window. |
| [epigenomics-evals](https://github.com/di-omics/epigenomics-evals) | 6 analysis decisions from a published epigenomics paper, written as agent tasks with controls for each grader. |
| [lab-automation-evals](https://github.com/di-omics/lab-automation-evals) | Liquid-handling tasks for AI agents. Robot plans run on a simulated liquid handler and are graded on what ends up in the wells, with controls for every grader and a plate-reader grader for running the same plan on a real robot. |
| [benchmarks](https://github.com/di-omics/benchmarks) | The metrics, quality checks, and pending results for the July 2026 lab automation and omics projects. [Read the evaluation notes](https://di-omics.github.io/benchmarks/). |

## Reinforcement learning and ML

| Project | What you can inspect |
| --- | --- |
| [drugdev-gym](https://github.com/di-omics/drugdev-gym) | Simulated drug-development environments. Each reward is checked against known assay outcomes. |
| [longevity-rl](https://github.com/di-omics/longevity-rl) | 2 simulated benchmarks test how a planner selects batches and how a policy interprets 8 aging clocks. |
| [ml-design-loops](https://github.com/di-omics/ml-design-loops) | Simulated design and assay-optimization loops, including how predictions are accepted, rejected, or sent for review. |
| [ml-foundations](https://github.com/di-omics/ml-foundations) | A PyTorch lab notebook with controlled FashionMNIST training experiments. |

## Robotics and vision

| Project | What you can inspect |
| --- | --- |
| [robot-lab-handling](https://github.com/di-omics/robot-lab-handling) | 2 simulated robot arms attempt everyday lab chores. The simulator scores where the labware ends up. |
| [robot-lab-judge](https://github.com/di-omics/robot-lab-judge) | Vision models judge those chores from camera images. Development results include false passes, with the test split still sealed. |
| [robot-policy-evals](https://github.com/di-omics/robot-policy-evals) | A study plan for measuring how choosing and reporting a checkpoint on the same episodes biases its score. |
| [liquid-policy-robustness](https://github.com/di-omics/liquid-policy-robustness) | A simulated robot-arm study comparing liquid neural networks, MLPs, and LSTMs under sensor noise. The noise sweep is pending. |
| [plr-lab-robot](https://github.com/di-omics/plr-lab-robot) | A PyLabRobot arm simulator with eye-in-hand vision and checks on manipulation tasks. |
| [lab-cv](https://github.com/di-omics/lab-cv) | Bench and microscopy vision demos scored blind against known synthetic ground truth. |
| [awesome-wetlab-cv](https://github.com/di-omics/awesome-wetlab-cv) | A reading and tools list for lab computer vision, microscopy, and cell tracking. |
| [robotics-devkit](https://github.com/di-omics/robotics-devkit) | Development tools and a project template for moving robot code through simulation and hardware testing. |

## Autonomous labs

| Project | What you can inspect |
| --- | --- |
| [autonomous-lab](https://github.com/di-omics/autonomous-lab) | A 4-stage evaluation of whether a workflow can go from hypothesis to evidence. It identifies where the loop breaks. |
| [plr-mcp](https://github.com/di-omics/plr-mcp) | 4 instrument types exposed as MCP tools, with simulation by default and permission checks for physical hardware. |
| [plr-reverse-engineer](https://github.com/di-omics/plr-reverse-engineer) | Playbooks for lab instruments without an automation API, each with its own evidence and validation status. |
| [agentic-lab-guide](https://github.com/di-omics/agentic-lab-guide) | A guide to agent-driven instruments, starting with the Hamilton STAR and STARlet in simulation. [Read the guide](https://di-omics.github.io/agentic-lab-guide/). |

## Instruments and omics

| Project | What you can inspect |
| --- | --- |
| [opentrons-drivers](https://github.com/di-omics/opentrons-drivers) | Drivers and a simulator for the OT-One, OT-2, and Flex, with tip-pickup calibration findings. |
| [ot-flex-automation](https://github.com/di-omics/ot-flex-automation) | Deck movements and operator handoffs for sequencing on the Opentrons Flex. The public whole-genome and methylation profiles use water for motion tests. |
| [fullstack-omics](https://github.com/di-omics/fullstack-omics) | Simulated single-cell RNA and whole-genome sequencing workflows from planning to analysis handoff. |
| [omics-demos](https://github.com/di-omics/omics-demos) | Synthetic sequencing data with known answers for checking omics analyses. [Browse the demos](https://di-omics.github.io/omics-demos/). |
| [plr-minimum-effective](https://github.com/di-omics/plr-minimum-effective) | A simulated study of unique sequencing reads per dollar, scored against a known optimum. |
| [spatial-flow](https://github.com/di-omics/spatial-flow) | A synthetic spatial-biology lab demo for following specimen identity, reviewing images, and balancing batches. |

## Hackathons

| Project | What you can inspect |
| --- | --- |
| [bay-hack](https://github.com/di-omics/bay-hack) | TubeProof checks that a tube is open before allowing the next simulated liquid-handling step. [Try the walkthrough](https://di-omics.github.io/bay-hack/). |
| [someplace](https://github.com/di-omics/someplace) | A concept and pitch page for a voice companion inside a generated world, from Hack with VoiceOS. |

The public [PyLabRobot fork](https://github.com/di-omics/pylabrobot) tracks work based on the [upstream SDK](https://github.com/PyLabRobot/pylabrobot).
