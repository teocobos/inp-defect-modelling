```markdown
# Project Scope

## Project

InP Defect Modelling

## Primary Aim

Develop a reproducible first-principles framework for investigating the structural, thermodynamic and electronic properties of defects in crystalline indium phosphide.

## Scientific Questions

The project is designed to address the following questions:

1. What are the stable structures of the principal native defects in InP?
2. How do defect formation energies vary with chemical environment and Fermi level?
3. Which charge states are thermodynamically stable?
4. Where are the corresponding thermodynamic charge-transition levels?
5. Which defects introduce electronically active states within the InP band gap?
6. How strongly are electrons or holes localised around native defects?
7. What structural distortions accompany defect formation and charge trapping?
8. Which native defects are sufficiently mobile to contribute to defect redistribution?
9. How do impurities and defect complexes modify the native-defect landscape?
10. How can these atomistic mechanisms influence technologically relevant InP behaviour?

## Materials Scope

### Primary Phase

Zincblende InP.

### Secondary Phases

Alternative InP polymorphs may be used for validation or comparison where scientifically justified, including zincblende InP.

They are not initially part of the production defect dataset.

## Initial Defect Scope

### Vacancies

- `V_In`
- `V_P`

### Antisites

- `In_P`
- `P_In`

### Interstitials

- `In_i`
- `P_i`

### Later Extensions

Potential later extensions include:

- impurities
- dopants
- native-defect complexes
- impurity-defect complexes
- surfaces
- interfaces

These extensions should only be introduced when supported by a clear research question.

## Target Properties

The initial target properties include:

- equilibrium structure
- lattice parameters
- total energies
- band structure
- density of states
- projected density of states
- band gap
- defect formation energies
- charge-transition levels
- local structural distortion
- charge localisation
- spin localisation
- inverse participation ratio where appropriate
- defect migration barriers

## Computational Scope

The repository is designed to support:

- CP2K
- VASP
- AiiDA
- ASE
- pymatgen
- Python-based analysis

The project is method-driven rather than code-dependent.

Results from different electronic-structure packages should only be compared after the relevant numerical and methodological settings have been validated.

## Initially Out of Scope

The following are not initial project objectives:

- exhaustive dopant screening
- full semiconductor-device transport
- device-scale simulation
- large-scale molecular dynamics
- machine-learning interatomic potentials
- extended defects such as dislocations
- grain boundaries
- arbitrary high-throughput screening without prior physical justification

These topics may become later extensions.

## Cross-Material Programme

The InP methodology is intended to form the first template for comparable defect studies of:

- GaAs
- GaSb
- InP

Where scientifically appropriate, common conventions, workflows and analysis methods should be retained across these repositories.

## Success Criteria

The initial InP project will be considered methodologically established when:

1. The reference crystal structure is validated.
2. Numerical convergence has been demonstrated.
3. Pristine InP properties have been benchmarked.
4. A production defect supercell has been justified.
5. Native-defect structures can be generated reproducibly.
6. Charged-defect corrections are validated.
7. Formation-energy diagrams can be reproduced from stored metadata.
8. Charge-transition levels can be calculated consistently.
9. Key results can be independently regenerated from documented inputs and workflows.
```
