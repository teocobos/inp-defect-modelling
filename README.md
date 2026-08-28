````markdown
# InP Defect Modelling

Computational investigation of native defects, electronic structure, charge states, carrier localisation and defect migration in crystalline indium phosphide (InP).

## Project Overview

Indium phosphide is a wide-band-gap III–V semiconductor used extensively in power electronics, radio-frequency devices, optoelectronics and high-field applications.

The properties and performance of InP can be strongly influenced by native point defects, impurities and defect complexes. Understanding their thermodynamic stability, electronic structure, charge states and migration behaviour is therefore important for connecting atomistic defect physics with experimentally relevant material behaviour.

This repository provides a reproducible computational framework for first-principles investigation of defects in InP.

## Research Objectives

The project aims to:

1. Establish a validated first-principles description of pristine crystalline InP.
2. Characterise native vacancies, antisites and interstitials.
3. Calculate defect formation energies under relevant chemical-potential conditions.
4. Determine thermodynamic charge-transition levels.
5. Investigate defect-induced electronic states and carrier localisation.
6. Characterise structural distortions associated with defects and trapped charge.
7. Investigate selected defect migration mechanisms.
8. Extend the framework to selected impurities and defect complexes.
9. Develop reproducible workflows suitable for comparison with other III–V semiconductors.

## Initial Defect Space

### Vacancies

- In vacancy: `V_In`
- P vacancy: `V_P`

### Antisites

- In on P site: `In_P`
- P on In site: `P_In`

### Interstitials

- In interstitial: `In_i`
- P interstitial: `P_i`

Impurities and defect complexes will be introduced in later phases based on literature evidence and results from the native-defect calculations.

## Computational Methods

The project is designed to support calculations using:

- CP2K
- VASP
- AiiDA
- ASE
- pymatgen
- Python

Density-functional theory will be used for structural optimisation, energetics and electronic-structure calculations.

Hybrid-functional calculations will be used where required for improved treatment of the InP band gap, defect levels and carrier localisation.

Charged-defect calculations will explicitly consider:

- finite-size corrections
- potential alignment
- chemical potentials
- Fermi-level dependence
- band-edge references
- supercell convergence

## Repository Structure

```text
calculations/    Calculation inputs and organised calculation directories
docs/            Methodology, provenance and project documentation
notebooks/       Interactive analysis and exploratory calculations
reports/         Figures, tables and research summaries
scripts/         Structure generation, automation and analysis scripts
src/             Reusable project source code
structures/      Reference, relaxed, supercell and defect structures
workflows/       CP2K, VASP and AiiDA workflows
````

Large production outputs, restart files and licensed or proprietary files are not intended for version control.

## Research Workflow

The project follows the general sequence:

1. Project foundation
2. Literature review
3. Crystal-structure selection and validation
4. DFT convergence
5. Pristine bulk validation
6. Supercell convergence
7. Native-defect enumeration
8. Charged-defect calculations
9. Formation energies and charge-transition levels
10. Electronic-structure and localisation analysis
11. Defect migration
12. Impurities and defect complexes
13. Device-relevant interpretation
14. Publication dataset and reproducibility validation

## Related Projects

This project forms part of a broader computational investigation of technologically relevant semiconductor materials, including:

* IGZO
* InP
* GaAs
* GaSb
* InP

A consistent repository architecture and computational methodology will enable systematic cross-material comparison.

## Project Status

Current stage: **Phase 0 — Project Foundation**

See:

* `docs/project_roadmap.md`
* `docs/results-log.md`

for current progress.

## Reproducibility

Calculation parameters, structural provenance, software versions, naming conventions and analysis procedures are documented within `docs/`.

Key files include:

* `docs/computational-parameters.md`
* `docs/metadata_schema.md`
* `docs/naming_conventions.md`
* `docs/reproducibility.md`
* `docs/validation.md`

## Data and Intellectual Property

Only material appropriate for public release should be committed to this repository.

Raw production data, unpublished commercially sensitive results, licensed software files and other restricted material should remain outside the public repository unless explicitly approved for release.

See:

* `docs/ip-and-publication-policy.md`

## Author

Dr Teofilo Cobos Freire

```
```
