# Naming Conventions

## Purpose

This document defines naming conventions for structures, calculations, defects, scripts and results.

Consistent naming is essential for automation, reproducibility and cross-material comparison.

## Material Identifier

Use:

`inp`

for indium phosphide.

## Crystal Phase

Use:

- `zb` for zincblende
- `zb` for zincblende

Example:

`inp_zb_reference.cif`

## Structure Categories

Recommended names include:

- `reference`
- `relaxed`
- `primitive`
- `conventional`
- `supercell`
- `defect`

Examples:

`inp_zb_reference.cif`

`inp_zb_relaxed.xyz`

`inp_zb_primitive.cif`

`inp_zb_supercell_4x4x2.xyz`

## Supercells

Use:

`inp_zb_supercell_<a>x<b>x<c>`

Example:

`inp_zb_supercell_4x4x2`

If multiple geometrically distinct cells have the same replication dimensions, append an identifier.

Example:

`inp_zb_supercell_4x4x2_001`

## Defect Names

Use standard defect notation.

### Vacancies

- `V_In`
- `V_P`

### Antisites

- `In_P`
- `P_In`

### Interstitials

- `In_i`
- `P_i`

## Defect Charge States

Use:

- `q-3`
- `q-2`
- `q-1`
- `q0`
- `q+1`
- `q+2`
- `q+3`

Example directory:

`V_In/q-3/`

## Multiple Defect Configurations

When multiple geometrically distinct configurations exist, use a three-digit index.

Examples:

`In_i_001`

`In_i_002`

`P_i_001`

For multiple relaxed minima originating from the same initial configuration:

`In_i_001_relaxed_001`

## Calculation Type

Recommended identifiers include:

- `sp` for single point
- `geo_opt` for geometry optimisation
- `cell_opt` for cell optimisation
- `dos`
- `pdos`
- `bands`
- `neb`
- `charge_density`
- `spin_density`

Example:

`inp_zb_V_In_q-3_geo_opt`

## Code Identifier

Where useful, append:

- `cp2k`
- `vasp`

Example:

`inp_zb_bulk_geo_opt_cp2k`

## Functional Identifier

Use concise functional names where needed:

- `pbe`
- `scan`
- `pbe0`
- `hse06`

Example:

`inp_zb_bulk_hse06_vasp`

## File Naming

Avoid spaces.

Use lowercase for general file names and preserve standard chemical notation within defect identifiers where practical.

Preferred:

`inp_zb_bulk_geo_opt.inp`

Avoid:

`InP Final Geometry optimisation new.inp`

## Scripts

Use descriptive snake_case names.

Examples:

`generate_supercells.py`

`generate_native_defects.py`

`analyse_coordination.py`

`plot_formation_energies.py`

`calculate_ctls.py`

## Results

Generated tables should use descriptive names.

Examples:

`bulk_convergence_summary.csv`

`native_defect_energies.csv`

`charge_transition_levels.csv`

`migration_barriers.csv`

## Figures

Figures should use descriptive names that correspond to analysis scripts.

Examples:

`inp_band_structure.png`

`inp_native_defect_formation_energies.png`

`V_In_charge_density.png`

## Metadata

Metadata files should use the same base identifier as the associated calculation where possible.

Example:

`inp_zb_V_In_q-3_geo_opt.yaml`

## General Rules

1. Do not use spaces.
2. Avoid ambiguous abbreviations.
3. Use fixed-width numeric identifiers where multiple configurations exist.
4. Preserve consistent defect notation across all scripts and datasets.
5. Do not silently rename production calculations.
6. Record renaming operations in Git history where they affect reproducibility.