
### `docs/reproducibility.md`

```markdown
# Reproducibility

## Purpose

This project aims to ensure that scientifically significant results can be independently reconstructed from version-controlled inputs, metadata and analysis code.

## Reproducibility Principle

Every reported result should be traceable through the chain:

**reference structure → generated structure → calculation input → calculation output → analysis script → reported result**

## Version Control

Git is used to track:

- documentation
- scripts
- workflows
- calculation inputs
- metadata
- selected lightweight outputs
- analysis code

Large raw outputs may remain outside the repository.

## Software Versions

Production calculations should record software versions for:

- CP2K
- VASP
- Python
- ASE
- pymatgen
- AiiDA
- relevant analysis packages

## Environment Tracking

Python dependencies should be reproducible using one or more of:

- `requirements.txt`
- Conda environment file
- package-lock metadata
- documented installation instructions

## Structure Provenance

Every structure must have a traceable origin.

For reference structures, record:

- database or publication source
- identifier
- citation
- acquisition date

For generated structures, record:

- parent structure
- generation script
- parameters used
- script version or commit

## Calculation Provenance

Each production calculation should record:

- input structure
- input file
- code and version
- parameter set
- charge state
- spin state
- parent calculation where applicable

## Analysis Provenance

Derived quantities should be generated using version-controlled scripts.

Examples include:

- formation energies
- CTLs
- DOS analysis
- localisation metrics
- structural distortion
- migration barriers

Analysis should not depend on undocumented manual editing.

## Raw Data

Large raw outputs may be stored outside Git.

The repository should still retain enough information to identify:

- where the raw data originated
- which calculation produced it
- which analysis used it

## Checksums

Important archival files may use cryptographic checksums.

Examples:

- SHA256 checksum for reference structures
- SHA256 checksum for frozen publication datasets

## Deterministic Structure Generation

Where possible, generated structures should be reproducible from scripts rather than stored only as manually modified files.

For stochastic procedures, record:

- random seed
- software version
- input parameters

## Publication Reproducibility

Before publication:

1. Freeze the computational methodology.
2. Record the Git commit used for production analysis.
3. Re-run key analysis scripts.
4. Verify figures can be regenerated.
5. Verify tables can be regenerated.
6. Check that all published values map to documented calculations.
7. Separate public data from restricted data.

## Repository Integrity

Do not commit:

- temporary editor files
- machine-specific cache files
- large restart files
- licensed pseudopotentials
- proprietary data
- sensitive credentials

## Reproducibility Review

At major milestones, perform a reproducibility review covering:

- structure provenance
- parameter completeness
- software versions
- metadata completeness
- analysis scripts
- raw-data location
- Git status