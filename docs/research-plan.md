```markdown
# InP Research Plan

## Research Strategy

The project follows a staged workflow in which each computational level is validated before proceeding to more expensive defect calculations.

The guiding principle is:

**structure → convergence → pristine material → supercell → native defects → charged defects → electronic structure → kinetics**

## Stage 1 — Reference Structure

Identify an authoritative experimental zincblende InP structure.

Record:

- source
- citation
- database identifier
- lattice parameters
- symmetry
- atomic coordinates
- acquisition date
- any modifications

The original reference structure must be preserved separately from generated or relaxed structures.

## Stage 2 — Numerical Convergence

Establish convergence with respect to the numerical parameters relevant to each electronic-structure code.

Potential variables include:

- plane-wave cutoff
- auxiliary cutoff
- basis set
- pseudopotential
- k-point mesh
- SCF thresholds
- smearing
- geometry-optimisation criteria

Convergence criteria must be defined before production calculations.

## Stage 3 — Pristine InP

Optimise and characterise pristine InP.

Target properties include:

- lattice constants
- internal structural parameters
- In–P bond lengths
- total energy
- band structure
- DOS
- PDOS
- band gap
- orbital character of the valence-band edge
- orbital character of the conduction-band edge

Comparison with experiment and high-quality theoretical literature should be documented.

## Stage 4 — Supercell Validation

Generate candidate InP supercells and assess their suitability for defect calculations.

Tests should consider:

- number of atoms
- minimum defect-image separation
- k-point sampling
- computational cost
- structural relaxation around defects
- electrostatic finite-size effects for charged calculations

A production supercell must be selected based on evidence rather than convenience.

## Stage 5 — Native Defects

Generate and relax:

- `V_In`
- `V_P`
- `In_P`
- `P_In`
- `In_i`
- `P_i`

Multiple interstitial starting configurations should be considered where appropriate.

Symmetry-equivalent configurations should be identified to avoid redundant calculations.

## Stage 6 — Charged Defects

For relevant defects:

1. Identify candidate charge states.
2. Perform charged calculations.
3. Evaluate finite-size corrections.
4. Reference energies consistently to host band edges.
5. Determine formation energies as a function of Fermi level.
6. Calculate thermodynamic charge-transition levels.

Both In-rich and P-rich limits should be considered, together with any required competing-phase constraints.

## Stage 7 — Electronic Structure

Characterise electronically active defects using quantities including:

- DOS
- PDOS
- defect-state charge density
- spin density
- localisation metrics
- IPR
- local coordination
- bond lengths
- bond angles
- defect-induced structural distortion

Hybrid-functional calculations should be used where semilocal DFT is insufficient to describe the relevant electronic state.

## Stage 8 — Migration

Migration calculations should focus on defects identified as physically relevant from earlier stages.

For selected mechanisms:

1. Construct initial and final states.
2. Generate migration pathways.
3. Perform NEB calculations.
4. Identify transition states.
5. Determine migration barriers.
6. Investigate charge-state dependence where appropriate.

## Stage 9 — Impurities and Complexes

Only after the native-defect framework is established should the project expand to selected impurities and defect complexes.

Selection should be motivated by:

- experimental relevance
- semiconductor processing
- compensation
- carrier trapping
- reliability
- existing literature
- industrial relevance

## Stage 10 — Cross-Material Comparison

Validated methodology should subsequently be transferred to GaAs, GaSb and InP.

Cross-material analysis may consider:

- vacancy energetics
- antisite behaviour
- interstitial stability
- charge-transition levels
- carrier localisation
- migration barriers
- trends across III–V chemistry

## Stage 11 — Publication Dataset

Before publication:

- critical calculations should be independently checked
- computational parameters should be frozen
- provenance should be complete
- analysis scripts should be version controlled
- figures should be reproducible
- uncertainties and methodological limitations should be documented
- public and non-public data should be clearly separated
```
