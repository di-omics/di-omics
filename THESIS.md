# The argument behind the work

The long form of what the [profile](README.md) summarizes: what an autonomous lab is for,
what is actually scarce, and the order the pieces have to be built in.

## The short version

An AI score in biology is a readout, and I validate it the way a wet lab validates an assay:
controls that must separate, traps that must fail, repeats that must agree.
[drugdev-gym](https://github.com/di-omics/drugdev-gym) does this for the rewards of 10
drug-development environments, [sc-zprime](https://github.com/di-omics/sc-zprime) for 2
published agent benchmarks in single-cell and spatial biology, and
[robot-lab-handling](https://github.com/di-omics/robot-lab-handling) for 19 robot lab chores.
The same discipline decides what an autonomous lab can be trusted to do, which is the rest of
this page.

## What it is all for

Every layer below exists to serve a single number: **how much a lab learns per dollar per
experimental cycle.** Throughput and autonomy only count when they raise that number. A lab
that runs 1,000 plates a day and cannot tell which of them is real has bought motion, not
information.

3 things cap that number, and they are not the ones usually shopped for.

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
transfer, exactly 1 of them caps information per dollar at any moment. Computing which one
tells you whether to build orchestration, repair an instrument, run a calibration, or go and
find expertise.

That last point is why the work here is built the way it is. **Orchestration is
buildable.** Scheduling instruments, moving plates, tracking samples, and holding provenance
are engineering with known shapes, and the code here models them. What is genuinely scarce, and therefore what is worth paying for, is **laboratory
intelligence**: knowing what a result means, what to run next, when a clean-looking plate
should be thrown away, and what a robot must prove before it is trusted with the step. That
is the part that does not come in a box.

## The bet

Autonomous labs are not waiting on a vendor to ship AI-native labware. The instruments
already on benches are enough, and
[plr-reverse-engineer](https://github.com/di-omics/plr-reverse-engineer) is how I test that,
with playbooks for 5 instruments that have no published automation API. What is actually missing is the layer above the
hardware: **a way to encode a domain expert's judgment into autonomous execution, and to
have that expert orchestrate the automation rather than operate it.**

That layer is the hard part, and it is hard for a specific reason. A written protocol is
not what an experienced scientist does; it is the subset that survived being written down.
The rest -- when a result is real, when a sample is still recoverable, when a clean-looking
plate should be thrown away -- lives in 1 person's head, gets applied 100 times a week, and
is exactly what fails to transfer when a lab automates. Buying a better robot does not
touch it.

So the work is built around making that judgment explicit, attributable, and
checkable: thresholds that carry the basis they rest on, gates that refuse to fire when
their input is untrustworthy, failure modes that declare how they would be caught and get
downgraded when that path does not exist, and benchmarks a robot must meet before it is
trusted with a task. An operation nobody has benchmarked is untrusted by default.

## 4 stages, not 1 number

Executing a protocol is the stage everyone measures. A lab that executes perfectly and cannot
tell a good plate from a bad one is not running an experiment, it is moving liquid. Closing
a single loop takes 4 things, and they fail independently:

| Stage | The question | What failure means |
| --- | --- | --- |
| **Execute** | can the machine perform the step? | reverse-engineering work |
| **Measure** | does a result arrive, from the right assay? | an instrument that returns a usable number |
| **Decide** | would anything notice when it goes wrong? | a detection path for failures that destroy material |
| **Record** | could it be proven and replayed afterwards? | barcodes, or an arm that reports its moves |

On the single-cell genomics reference workflow, all 4 currently break, for 4 different
reasons. Collapsing that into a single autonomy percentage would hide which budget to spend.
`autonomous-lab loop` computes it.

## The stack

An autonomous lab is not a single machine, and the pieces fail independently. This is the order
they have to be built in, because each one is what makes the next one meaningful.

**1 / Move it.** Multi-instrument orchestration and the arm that carries plates between
boxes. Running 1 plate at a time wastes the instruments, so the moment a second enters, a set of
constraints appears that no single-run report can see: 2 plates want the same liquid
handler, a human is needed at 2am, a finished plate sits on a deck nobody can clear.
With plates in flight, the busiest instrument sets the cycle time, and
`autonomous-lab throughput` will not quote plates per day until every step has been timed.
The arm can be priced the same way: on the reference protocol, `autonomous-lab ledger` finds
**5 plate hops that only a plate mover removes, and 8 steps blocked on undecoded commands
that no arm helps.** Which purchase helps is computable before the order rather than after
it.

**2 / See it, and know what seeing cannot do.** Deploy the best available vision, and be
precise about its ceiling. `vision` sorts conditions into `visible`, `visible_indirect`, and
`invisible` -- and that last boundary is a claim about **physics, not model quality**. No
amount of training data separates a well of active enzyme from one of denatured enzyme,
because the photons are identical.

**3 / Gate what vision cannot reach.** This is the composition that makes the whole thing
work, and it is why seeing and gating are one layer. Where a camera is physically
incapable, an assay is the *only* remaining option -- a plate read, a bioanalyzer trace, a
quantification step. So an invisible failure with no gate behind it is uncovered, and no CV
budget will ever change that. Deploying a newer model has a ceiling, and the ceiling is
computable in advance.

**4 / Close the loop.** Measure, compare, correct. Each of those has a specific way of being
fake, and the load-bearing one is latency: a measurement taken after the material is
consumed cannot steer anything however accurate it is. It is a post-mortem, not a
control loop.

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

An expert demonstration is *data, not authority*. A scientist doing something twice is not a
specification: it is 2 observations with a spread, and the spread is the information. Most
operations have no expert envelope at all, and that list is the real backlog of an automation
programme. Nobody writes it down. `autonomous-lab knowledge` keeps it: today it holds 8 expert
judgments, 4 of them validated, and 7 robot benchmarks, 2 of them met.

## What is not built yet

The intelligence layer is the newest and least proven part of the stack, and most of it is
simulated. There is no sustained production evidence here and no wet biological endpoint
yet.
