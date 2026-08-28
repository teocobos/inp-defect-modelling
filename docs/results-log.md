# InP Defect Modelling — Results Log

This document records significant computational results, validation decisions and methodological milestones.

It is not intended to replace raw calculation data.

---

## Phase 0 — Project Foundation

**Status:** Complete

### Repository Initialisation

The `inp-defect-modelling` repository has been established as the master III–V defect-modelling framework.

The repository architecture separates:

- structures
- calculations
- workflows
- scripts
- notebooks
- reports
- documentation
- reusable source code

The repository is version controlled using Git and mirrored to GitHub.

### Research Scope

The initial scientific programme has been defined around:

- crystalline zincblende InP
- pristine bulk properties
- native vacancies
- native antisites
- native interstitials
- charged-defect energetics
- thermodynamic charge-transition levels
- electronic localisation
- structural distortion
- selected migration mechanisms

### Initial Native Defect Set

#### Vacancies

- `V_In`
- `V_P`

#### Antisites

- `In_P`
- `P_In`

#### Interstitials

- `In_i`
- `P_i`

### Computational Framework

The project has been designed as a code-neutral first-principles workflow supporting:

- CP2K
- VASP
- AiiDA
- ASE
- pymatgen
- Python

The production methodology will be selected through numerical convergence and physical validation rather than software availability alone.

### Research Governance

Phase 0 documentation now defines:

- computational parameter tracking
- convergence strategy
- structure provenance
- defect naming conventions
- metadata requirements
- reproducibility requirements
- validation criteria
- charged-defect correction strategy
- chemical-potential methodology
- dataset management
- literature-review structure
- IP and publication controls

### Phase 0 Outcome

The repository now has a documented research framework capable of supporting reproducible bulk, defect, charged-defect, electronic-structure and migration calculations.

### Next Milestone

Begin:

**Phase 1 — Reference zincblende InP crystal structure acquisition and validation.**

---

## Phase 1 — Crystal Structure

**Status:** In progress

### Objectives

- identify an authoritative zincblende InP reference structure
- record bibliographic and database provenance
- preserve the original structure
- validate composition
- validate lattice parameters
- validate symmetry
- validate atomic coordinates
- generate canonical project structures
- record structural metadata

### Results

No computational results recorded yet.

---

## Phase 2 — DFT Convergence

**Status:** Not started

---

## Phase 3 — Pristine InP

**Status:** Not started

---

## Phase 4 — Defect Supercell

**Status:** Not started

---

## Phase 5 — Native Defects

**Status:** Not started

---

## Phase 6 — Charged Defects

**Status:** Not started

---

## Phase 7 — Electronic Structure

**Status:** Not started

---

## Phase 8 — Migration

**Status:** Not started