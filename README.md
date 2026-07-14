# Di Hu

**Full-stack biologist building autonomous labs.**

Wet lab, automation, computation, ML. I encode expert judgment into autonomous execution so biological R&D runs faster, cheaper, and more reproducibly.

Oxford PhD &middot; joint first author in Nature Communications &middot; contributor to open-source PyLabRobot.

---

### What's here

Open-source autonomous-lab infrastructure built on PyLabRobot: instrument reverse-engineering, end-to-end single-cell omics, epigenomics, robotic manipulation, and an MCP layer so agents can drive the bench. Simulation-first and validated on real hardware, with plant-and-recover checks so the results are honest, not cherry-picked.

### Selected work

- **plr-tested**: PyLabRobot protocols run on real hardware, not just in sim. Hamilton STAR (ResolveDNA PTA/WGA, amplicon-seq), validated on the instrument.
- **plr-reverse-engineer**: playbooks and tooling to bring no-API instruments (BD FACSMelody, Agilent 6530 Q-TOF, Biotage V-10) under PyLabRobot control.
- **fullstack-omics**: full-stack autonomous single-cell omics end to end in the PyLabRobot simulator. scRNA-seq (FLASH-seq UMI) and scWGS (ResolveDNA PTA + NEBNext), with analysis.
- **plr-epigenome**: automated (sci)TIP-seq on a Hamilton STAR. Shared infra, a Rhodamine-B validation ladder, and a statement-of-work compiler (plan text to runnable, validated method).
- **plr-lab-robot**: onboard a robotic arm in the PyLabRobot simulator, then add eye-in-hand computer vision and dexterous manipulation (uncapping). CPU-only, plant-and-recover.
- **plr-mcp**: a Model Context Protocol server for PyLabRobot, so any agent can drive liquid handlers, plate readers, thermocyclers, and heater-shakers.

I also contributed a BD FACSMelody cell-sorter backend to the core PyLabRobot project.

### Stack

Python &middot; PyLabRobot (Hamilton, Opentrons, Tecan) &middot; agent harnesses (PydanticAI, MCP) &middot; robotic manipulation and computer vision &middot; single-cell and low-input NGS.

---

[LinkedIn](https://www.linkedin.com/in/di-hu-phd-4049401a5/)
