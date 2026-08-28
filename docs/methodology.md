# Methodology

## General Philosophy

The project uses a validation-first computational strategy.

No production defect dataset should be generated until the underlying pristine-material methodology and defect-supercell methodology have been demonstrated to be numerically reliable.

## Electronic-Structure Methods

Density-functional theory is the primary electronic-structure framework.

Calculations may be performed using:

- CP2K
- VASP

The repository is intentionally code-neutral.

Results generated using different packages should not be assumed equivalent unless relevant numerical settings and physical approximations have been compared.

## Exchange-Correlation Treatment

Semilocal DFT may be used for:

- initial convergence
- structure optimisation
- workflow development
- exploratory calculations

Hybrid-functional calculations may be required for:

- accurate band-gap description
- defect-level positions
- charge-transition levels
- carrier localisation
- polaronic states
- final benchmark calculations

The final functional choice must be justified through validation.

## Structural Optimisation

Geometry optimisation should continue until documented force and energy thresholds are satisfied.

For bulk calculations, optimisation of lattice parameters and internal coordinates should be distinguished from fixed-cell defect relaxations.

## Defect Formation Energies

Defect formation energies will be evaluated using the general formalism:

\[
E_f(D^q)
=
E_{\mathrm{tot}}(D^q)
-
E_{\mathrm{tot}}(\mathrm{host})
-
\sum_i n_i\mu_i
+
q(E_F + E_{\mathrm{VBM}})
+
E_{\mathrm{corr}}
\]

where:

- \(D\) is the defect
- \(q\) is its charge state
- \(E_{\mathrm{tot}}(D^q)\) is the defective-cell total energy
- \(E_{\mathrm{tot}}(\mathrm{host})\) is the pristine-cell total energy
- \(n_i\) describes atoms added or removed
- \(\mu_i\) is the relevant chemical potential
- \(E_F\) is the Fermi level
- \(E_{\mathrm{VBM}}\) is the valence-band reference
- \(E_{\mathrm{corr}}\) accounts for finite-size and electrostatic corrections

The exact implementation must be documented before production calculations.

## Chemical Potentials

In and P chemical potentials must satisfy equilibrium with InP and appropriate competing-phase constraints.

At minimum, the project will consider:

- In-rich conditions
- P-rich conditions

The exact reference phases and calculated chemical potentials must be recorded.

## Charged Defects

Charged supercell calculations require explicit treatment of:

- periodic-image interactions
- electrostatic finite-size effects
- potential alignment
- band-edge references
- supercell convergence

The selected correction methodology must be validated and documented.

## Charge-Transition Levels

Thermodynamic charge-transition levels will be calculated from formation-energy differences between stable charge states.

CTLs should only be reported after:

- structural relaxation
- charge correction
- band-edge referencing
- charge-state stability analysis

have been completed consistently.

## Electronic-Structure Analysis

Depending on the defect, analysis may include:

- band structure
- DOS
- PDOS
- charge density
- spin density
- localisation metrics
- inverse participation ratio
- local coordination
- bond lengths
- bond angles
- defect-induced structural distortion

## Migration

Selected migration mechanisms will be investigated using nudged elastic band methods or equivalent transition-state techniques.

Migration studies should only be performed for mechanisms supported by prior thermodynamic or experimental evidence.

## Automation

Where practical, repetitive tasks should be automated using:

- Python
- ASE
- pymatgen
- AiiDA
- shell scripting

Automation scripts must preserve sufficient metadata to reconstruct each calculation.

## Reproducibility

Every result intended for scientific interpretation should be traceable to:

1. an input structure
2. computational parameters
3. software and version information
4. calculation outputs
5. analysis code
6. provenance metadata

See:

- `reproducibility.md`
- `metadata_schema.md`