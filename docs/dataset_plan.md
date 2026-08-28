# Dataset Plan

## Purpose

This document defines how data generated during the InP defect-modelling project will be organised, retained and prepared for possible publication.

## Dataset Categories

Project data are divided into:

1. reference data
2. generated structures
3. calculation inputs
4. raw calculation outputs
5. processed data
6. figures and tables
7. publication datasets

## Reference Data

Includes:

- experimental structures
- database structures
- literature values
- reference citations

Reference provenance must be recorded.

## Generated Structures

Includes:

- relaxed bulk structures
- supercells
- vacancy structures
- antisite structures
- interstitial structures
- defect complexes
- migration endpoints

Generated structures should be traceable to scripts and parent structures.

## Calculation Inputs

Calculation inputs should generally be retained in version control where licensing permits.

Examples:

- CP2K input files
- VASP INCAR files
- KPOINTS files
- POSCAR structures
- AiiDA workflow inputs

Licensed files such as VASP POTCAR data must not be committed publicly.

## Raw Outputs

Raw outputs may include:

- CP2K output files
- wavefunction restart files
- trajectory files
- VASP OUTCAR files
- WAVECAR files
- CHGCAR files

Large files should generally remain outside Git.

## Processed Data

Processed data should be retained in lightweight machine-readable formats where possible.

Preferred formats include:

- CSV
- JSON
- YAML
- NumPy arrays where justified

Examples:

- convergence summaries
- formation energies
- CTLs
- migration barriers
- structural descriptors

## Figures

Figures should be generated from scripts whenever possible.

Each publication-quality figure should have:

- an analysis script
- an input dataset
- reproducible plotting instructions

## Tables

Tables should be generated from processed data rather than manually transcribed.

## Publication Dataset

A publication dataset may contain:

- validated structures
- calculation inputs
- selected outputs
- processed results
- analysis scripts
- metadata
- citations
- README documentation

## Dataset Freeze

Before publication, create a frozen dataset version.

Record:

- version identifier
- Git commit hash
- creation date
- checksum
- included calculations
- excluded data
- known limitations

## Data Exclusions

The public dataset should exclude:

- licensed software files
- credentials
- commercially sensitive data
- unpublished patent-sensitive material
- raw data subject to restrictions
- unnecessary large restart files

## Future Cross-Material Dataset

The InP dataset schema should remain compatible with corresponding datasets for:

- GaAs
- GaSb
- InP

This will enable later creation of a unified III–V defect dataset.