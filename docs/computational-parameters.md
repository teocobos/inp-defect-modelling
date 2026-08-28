# Computational Parameters

## Purpose

This document records the computational settings used throughout the InP defect-modelling project.

All production calculations should be traceable to a defined and version-controlled parameter set.

## General Principles

Computational parameters should be selected through numerical convergence and physical validation rather than convenience.

Separate parameter sets may be required for:

- pristine bulk calculations
- supercell calculations
- charged-defect calculations
- hybrid-functional calculations
- electronic-structure calculations
- migration calculations

Any parameter change that affects comparability with earlier results must be documented.

## Electronic-Structure Codes

The project is designed to support:

- CP2K
- VASP

The final production workflow may use one or both codes.

Results generated using different codes should only be compared after confirming that the relevant physical and numerical approximations are consistent.

## Exchange-Correlation Functional

Initial calculations may use a semilocal exchange-correlation functional for:

- convergence testing
- structure optimisation
- workflow development
- exploratory calculations

Hybrid-functional calculations should be considered for:

- band-gap validation
- defect-state energies
- charge-transition levels
- localised carrier states
- final benchmark calculations

The selected functional must be recorded for each calculation.

## CP2K Parameters

The following must be recorded for every CP2K calculation:

- CP2K version
- basis-set file
- basis set for each element
- pseudopotential file
- pseudopotential for each element
- exchange-correlation functional
- plane-wave cutoff
- relative cutoff
- k-point mesh
- SCF convergence threshold
- maximum SCF iterations
- smearing method where applicable
- electronic temperature where applicable
- geometry-optimisation thresholds
- Poisson solver settings
- periodic boundary conditions
- spin settings
- total charge
- ADMM settings where applicable

## VASP Parameters

The following must be recorded for every VASP calculation:

- VASP version
- PAW datasets
- exchange-correlation functional
- plane-wave cutoff
- k-point mesh
- smearing method
- smearing width
- electronic convergence threshold
- ionic convergence threshold
- spin settings
- total charge treatment
- hybrid-functional settings where applicable
- symmetry settings
- dipole corrections where applicable

Licensed pseudopotential or PAW data must not be committed to the public repository.

## Structural Optimisation

Structural optimisation settings should include:

- whether the cell is fixed or relaxed
- force threshold
- total-energy threshold
- maximum number of geometry steps
- stress threshold where applicable
- optimisation algorithm

Pristine bulk calculations may allow cell relaxation.

Defect calculations should generally use a previously validated host supercell unless a different protocol is explicitly justified.

## k-Point Sampling

k-point meshes must be selected through convergence testing.

The target quantity for convergence should be stated, such as:

- total energy per atom
- lattice parameters
- band gap
- defect formation energy
- force components

Large supercells may justify reduced k-point meshes or Γ-point-only sampling, but this must be demonstrated rather than assumed.

## Plane-Wave or Grid Convergence

Relevant quantities should be converged with respect to:

- plane-wave cutoff
- relative cutoff
- auxiliary grid settings
- basis-set size

Convergence thresholds should be documented in `convergence-strategy.md`.

## Spin Polarisation

Spin-polarised calculations should be used when unpaired electrons or holes may be present.

The initial magnetic state should be documented for each defect charge state.

Multiple initial spin configurations may need to be tested where competing electronic states are possible.

## Charged Cells

Charged-defect calculations must record:

- nominal defect charge state
- total supercell charge
- correction methodology
- potential-alignment method
- dielectric constants used
- reference potential
- band-edge alignment procedure

## Migration Calculations

NEB or equivalent migration calculations should record:

- initial structure
- final structure
- number of intermediate images
- interpolation method
- spring constant
- force convergence
- climbing-image settings
- charge state
- supercell size
- k-point sampling

## Software Versions

Software versions must be recorded for production calculations.

Where possible, include:

- CP2K version
- VASP version
- Python version
- ASE version
- pymatgen version
- AiiDA version
- analysis-script commit hash

## Production Parameter Freeze

Before generation of a publication dataset, the validated production parameter set should be frozen.

Any later change should trigger:

1. documentation of the reason
2. revalidation
3. identification of affected calculations
4. selective recalculation where required