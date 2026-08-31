# Structure Provenance

## Purpose

This document records the provenance and transformation history of all important InP structures used in the `inp-defect-modelling` project.

The purpose of this record is to ensure that every computational structure can be traced to an experimentally or computationally defined parent and that transformations between structural representations remain reproducible.

A clear distinction is maintained between:

* experimental literature
* reconstructed reference structures
* canonical project structures
* DFT-relaxed structures
* supercells
* defect structures

A relaxed computational structure must never replace or overwrite the experimental provenance reference from which it was derived.

---

## Reference Structure

The primary crystalline reference for this project is room-temperature zincblende InP.

### Material

* material: indium phosphide
* formula: InP
* phase: zincblende
* crystal system: cubic
* space group: `F-43m`
* space-group number: 216

### Experimental Crystallographic Basis

The project uses the established room-temperature zincblende InP lattice.

The room-temperature lattice parameter represented in the project is:

`a = 5.8688 Å`

This corresponds to the commonly reported precision value of approximately:

`a ≈ 5.86875 Å`

The project therefore uses:

* `a = 5.8688 Å`
* `b = 5.8688 Å`
* `c = 5.8688 Å`
* `alpha = beta = gamma = 90°`

### Experimental Source

Temperature-dependent lattice measurements extending to 300 K were reported by:

K. Haruna, H. Maeta, K. Ohashi and T. Koike, “The thermal expansion coefficient and Grüneisen parameter of InP crystal at low temperatures,” *Journal of Physics C: Solid State Physics* **20**, 5275–5279 (1987).

DOI:

`10.1088/0022-3719/20/32/013`

The study measured the InP lattice constant over the temperature range 4.2–300 K using precision X-ray measurements.

The Haruna et al. work provides the temperature-dependent experimental basis used to anchor the room-temperature InP structural reference in this project.

### Database Status

No external crystallographic database entry is treated as the primary provenance source for the current project reference.

Accordingly:

* source database: none
* database identifier: none
* original deposited CIF: no
* project structure type: reconstructed experimental reference

Database structures may subsequently be used for independent cross-validation but do not replace the experimental literature provenance.

---

## Project Reference Structure

The reconstructed project reference is:

`structures/crystalline/reference/zincblende/inp_zb_haruna_et_al_1987.cif`

The reference CIF is a machine-readable project representation of room-temperature zincblende InP.

It is not an original experimental CIF deposited by Haruna et al.

### Reference Cell

The project reference uses:

* `a = 5.868800 Å`
* `b = 5.868800 Å`
* `c = 5.868800 Å`
* `alpha = 90°`
* `beta = 90°`
* `gamma = 90°`

The conventional cubic cell contains:

* In: 4 atoms
* P: 4 atoms
* total atoms: 8

Composition:

`In4 P4`

Reduced formula:

`InP`

### Crystallographic Sites

The zincblende structure consists of two interpenetrating face-centred-cubic sublattices displaced relative to one another by one quarter of the cubic body diagonal.

Symmetry analysis identifies:

* In: Wyckoff `4a`, multiplicity 4
* P: Wyckoff `4c`, multiplicity 4

The reconstructed reference contains symmetry-inequivalent In and P sites and uses the declared `F-43m` symmetry to generate the conventional zincblende structure.

Equivalent origin choices and symmetry operations may cause crystallographic software to report alternative fractional representatives of the same Wyckoff orbit.

These are physically equivalent when composition, lattice, symmetry and atomic mapping are preserved.

---

## Reference and Canonical Validation

Structural validation is performed using:

`scripts/structure_generation/validate_reference_structure.py`

The workflow uses pymatgen/spglib structural analysis.

### Validation Settings

* symmetry tolerance: `0.001`
* angle tolerance: `5.0°`

### Validated Structural Properties

The validated structure gives:

#### Composition

* composition: `In4 P4`
* reduced formula: `InP`
* atoms: 8

#### Lattice

* `a = 5.868800 Å`
* `b = 5.868800 Å`
* `c = 5.868800 Å`
* `alpha = 90.000000°`
* `beta = 90.000000°`
* `gamma = 90.000000°`
* volume = `202.137984 Å³`

#### Symmetry

* symbol: `F-43m`
* number: 216
* crystal system: cubic
* lattice type: cubic
* In: Wyckoff `4a`, multiplicity 4
* P: Wyckoff `4c`, multiplicity 4

#### Local Coordination

The minimum interatomic distance is:

`2.541265 Å`

Each In has four nearest-neighbour P atoms at:

`2.541265 Å`

Each P has four nearest-neighbour In atoms at:

`2.541265 Å`

Therefore:

* In coordination = 4
* P coordination = 4
* coordination geometry = tetrahedral

The nearest-neighbour distance is consistent with ideal zincblende geometry:

`d_In-P = (sqrt(3)/4) a`

### Validation Decision

The structure passes:

* formula validation
* atom-count validation
* lattice validation
* symmetry validation
* coordination validation
* nearest-neighbour-distance validation

**Structural validation: PASS**

---

## Original Structures

Original downloaded experimental structures should be preserved unchanged where licensing permits.

Original structures should normally be stored under:

`structures/crystalline/reference/`

If an original deposited experimental CIF is acquired later, it must:

* be stored separately from the reconstructed project reference
* retain its original filename where practical
* receive a SHA256 checksum
* record its source database or publication
* record its acquisition date
* not silently replace the reconstructed reference
* be compared structurally against the validated project structure

The current InP reference is reconstructed from experimental crystallographic information and is therefore explicitly identified as such.

---

## Canonical Structures

A canonical project structure may be generated from a validated reference structure.

Possible operations include:

* symmetry standardisation
* conversion between file formats
* primitive-cell generation
* conventional-cell generation
* coordinate wrapping
* removal of redundant metadata

Every operation must be documented and must not silently modify the physical structure.

### InP Zincblende Canonical Structures

Canonical structures were generated from:

`structures/crystalline/reference/zincblende/inp_zb_haruna_et_al_1987.cif`

using:

`scripts/structure_generation/generate_canonical_structure.py`

Generated files:

`structures/crystalline/reference/zincblende/canonical/inp_zb_canonical.cif`

and

`structures/crystalline/reference/zincblende/canonical/inp_zb_canonical.vasp`

### Canonical Structure Properties

Both canonical representations preserve:

* reduced formula: InP
* conventional-cell composition: `In4 P4`
* atom count: 8
* crystal system: cubic
* space group: `F-43m`
* space-group number: 216
* `a = 5.868800 Å`
* `b = 5.868800 Å`
* `c = 5.868800 Å`
* `alpha = beta = gamma = 90°`
* volume = `202.137984 Å³`
* minimum In–P distance = `2.541265 Å`
* In coordination = 4
* P coordination = 4

The canonical structures retain the room-temperature reference geometry.

They have **not** undergone DFT geometry optimisation.

---

## Canonical Structure Validation

Both generated canonical formats were independently passed through the structural-validation workflow.

### Canonical CIF

File:

`structures/crystalline/reference/zincblende/canonical/inp_zb_canonical.cif`

Validation results:

* composition: `In4 P4`
* reduced formula: InP
* atom count: 8
* space group: `F-43m` (216)
* crystal system: cubic
* `a = 5.868800 Å`
* `b = 5.868800 Å`
* `c = 5.868800 Å`
* volume = `202.137984 Å³`
* minimum interatomic distance: `2.541265 Å`
* In coordination: 4
* P coordination: 4

**Canonical CIF validation: PASS**

### Canonical VASP

File:

`structures/crystalline/reference/zincblende/canonical/inp_zb_canonical.vasp`

Validation results:

* composition: `In4 P4`
* reduced formula: InP
* atom count: 8
* space group: `F-43m` (216)
* crystal system: cubic
* `a = 5.868800 Å`
* `b = 5.868800 Å`
* `c = 5.868800 Å`
* volume = `202.137984 Å³`
* minimum interatomic distance: `2.541265 Å`
* In coordination: 4
* P coordination: 4

**Canonical VASP validation: PASS**

---

## Reference–Canonical Equivalence

Structural equivalence was tested using:

`scripts/structure_generation/compare_structures.py`

The comparison uses pymatgen `StructureMatcher`.

### Reference CIF vs Canonical CIF

Files compared:

`structures/crystalline/reference/zincblende/inp_zb_haruna_et_al_1987.cif`

and

`structures/crystalline/reference/zincblende/canonical/inp_zb_canonical.cif`

Results:

* composition A: `In4 P4`
* composition B: `In4 P4`
* atoms A: 8
* atoms B: 8
* lattice A: `5.868800 5.868800 5.868800 Å`
* lattice B: `5.868800 5.868800 5.868800 Å`
* equivalent: `True`
* normalized RMS displacement: `0.00000000`
* maximum displacement: `0.00000000`

**Reference → canonical CIF equivalence: PASS**

### Reference CIF vs Canonical VASP

Files compared:

`structures/crystalline/reference/zincblende/inp_zb_haruna_et_al_1987.cif`

and

`structures/crystalline/reference/zincblende/canonical/inp_zb_canonical.vasp`

Results:

* composition A: `In4 P4`
* composition B: `In4 P4`
* atoms A: 8
* atoms B: 8
* lattice A: `5.868800 5.868800 5.868800 Å`
* lattice B: `5.868800 5.868800 5.868800 Å`
* equivalent: `True`
* normalized RMS displacement: `0.00000000`
* maximum displacement: `0.00000000`

**Reference → canonical VASP equivalence: PASS**

### Equivalence Decision

No structural displacement was introduced during canonicalisation or VASP-format generation.

**Canonical equivalence status: VALIDATED**

---

## Checksums

Important structural files are assigned SHA256 checksums to detect accidental modification.

### Current Validated Checksums

Reference CIF:

`structures/crystalline/reference/zincblende/inp_zb_haruna_et_al_1987.cif`

SHA256:

`3a3627b1a5935cb15bb8b4b051a185d8fc62c89567776f469e4dae7dd319bcd7`

Canonical CIF:

`structures/crystalline/reference/zincblende/canonical/inp_zb_canonical.cif`

SHA256:

`34f30ee880fbc90eb60bc48ab4a6d6ee8e323e8c1e08bbef725d89a3c0f5d3e3`

Canonical VASP:

`structures/crystalline/reference/zincblende/canonical/inp_zb_canonical.vasp`

SHA256:

`ec96af6b609c5786140568d33b9492d97e96eab29132ed4c2600703d490cef16`

### Checksum Policy

Checksums refer to complete file contents rather than atomic geometry alone.

Modification of comments, provenance text, whitespace, metadata or numerical formatting can therefore change a checksum even if the physical crystal structure remains equivalent.

Any edited structural file must receive a new checksum and, where appropriate, repeat structural-equivalence validation.

---

## Approved Computational Starting Structure

Following validation and equivalence testing, the canonical InP structures are approved as starting structural representations for Phase 2.

For VASP-style workflows:

`structures/crystalline/reference/zincblende/canonical/inp_zb_canonical.vasp`

For CIF-based or code-neutral workflows:

`structures/crystalline/reference/zincblende/canonical/inp_zb_canonical.cif`

This approval means that the crystallographic representation has been validated.

It does **not** mean that:

* the experimental lattice is the final DFT equilibrium lattice
* the exchange-correlation functional has been validated
* pseudopotentials have been validated
* basis sets or plane-wave cutoffs have been converged
* k-point sampling has been converged
* spin-orbit coupling has been converged
* the structure is approved for production defect energetics without further calculation

Those questions belong to Phase 2 and later phases.

The reconstructed experimental reference:

`structures/crystalline/reference/zincblende/inp_zb_haruna_et_al_1987.cif`

must remain unchanged as the provenance reference.

---

## Relaxed Structures

Relaxed structures should never overwrite the original reference structure.

Store separately under:

`structures/crystalline/relaxed/`

Each relaxed structure should record:

* parent reference or canonical structure
* electronic-structure code
* code version
* exchange-correlation functional
* pseudopotential or PAW dataset
* basis set or plane-wave cutoff
* k-point mesh
* spin-orbit coupling treatment
* convergence thresholds
* optimisation method
* final lattice parameters
* final atomic coordinates
* calculation identifier
* date generated

A relaxed structure is a computational result, not a replacement for experimental provenance.

---

## Supercells

Supercells should record:

* parent structure
* replication matrix
* generation script
* software version
* number of atoms
* lattice vectors
* supercell identifier
* whether the parent was experimental or DFT relaxed

Unrelaxed and relaxed supercells must remain distinguishable.

---

## Defect Structures

Defect structures should record:

* parent supercell
* defect type
* atomic site modified
* charge state
* generation script
* configuration identifier

Additional metadata should include where appropriate:

* original site index
* original species
* fractional coordinates
* Cartesian coordinates
* symmetry information
* nearest-neighbour environment
* initial magnetic state
* calculation code
* generation date

Native-defect structures should follow the naming conventions defined elsewhere in the project documentation.

---

## Format Conversions

File conversion should not silently alter:

* lattice vectors
* fractional coordinates
* atom ordering
* species labels

Conversion scripts should be version controlled where possible.

Where atom ordering or symmetry-equivalent coordinates change during conversion, physical structural equivalence must be established geometrically rather than through line-by-line comparison.

---

## Validation

Reference and derived structures should be checked using tools such as:

* pymatgen
* ASE
* spglib

At minimum validate:

* composition
* atom count
* symmetry
* lattice parameters
* minimum interatomic distances

For production structures also consider:

* local coordination
* bond-length distributions
* structural equivalence to the intended parent
* unexpected duplicate sites
* unphysical short contacts
* loss of intended symmetry
* accidental cell transformations
* checksum consistency

A structure must not be promoted to a computational baseline merely because it can be parsed successfully.

---

## Provenance Workflow

The InP project uses the following provenance hierarchy:

```text id="hyefgp"
experimental literature
        ↓
experimentally established crystallographic parameters
        ↓
reconstructed reference structure
        ↓
checksum
        ↓
structural validation
        ↓
canonical structure generation
        ↓
canonical validation
        ↓
structural equivalence test
        ↓
approved computational starting structure
        ↓
DFT convergence
        ↓
DFT-relaxed pristine structure
        ↓
supercell generation
        ↓
defect generation
```

This hierarchy ensures that computational transformations remain traceable to an experimentally grounded parent structure.

---

## Provenance Record — InP Zincblende

```yaml id="hshqg4"
material: InP
phase: zincblende

crystallography:
  crystal_system: cubic
  space_group_symbol: F-43m
  space_group_number: 216

experimental_reference:
  temperature_K: 300
  literature_lattice_parameter_angstrom: 5.86875
  project_rounded_lattice_parameter_angstrom: 5.8688

experimental_source:
  authors:
    - K. Haruna
    - H. Maeta
    - K. Ohashi
    - T. Koike
  title: The thermal expansion coefficient and Grüneisen parameter of InP crystal at low temperatures
  journal: Journal of Physics C: Solid State Physics
  volume: 20
  pages: 5275-5279
  year: 1987
  doi: 10.1088/0022-3719/20/32/013

source_database: null
database_id: null

reference_structure:
  original_deposited_cif: false
  reconstruction: true
  repository_filename: inp_zb_haruna_et_al_1987.cif
  path: structures/crystalline/reference/zincblende/inp_zb_haruna_et_al_1987.cif
  conventional_cell_composition: In4P4
  reduced_formula: InP
  atoms: 8
  lattice_parameter_angstrom: 5.8688
  sha256: 3a3627b1a5935cb15bb8b4b051a185d8fc62c89567776f469e4dae7dd319bcd7

canonical_cif:
  path: structures/crystalline/reference/zincblende/canonical/inp_zb_canonical.cif
  sha256: 34f30ee880fbc90eb60bc48ab4a6d6ee8e323e8c1e08bbef725d89a3c0f5d3e3

canonical_vasp:
  path: structures/crystalline/reference/zincblende/canonical/inp_zb_canonical.vasp
  sha256: ec96af6b609c5786140568d33b9492d97e96eab29132ed4c2600703d490cef16

validation:
  composition: pass
  lattice: pass
  symmetry: pass
  coordination: pass
  nearest_neighbour_distance_angstrom: 2.541265
  canonical_cif: pass
  canonical_vasp: pass
  reference_to_canonical_cif_equivalence: pass
  reference_to_canonical_vasp_equivalence: pass
  normalized_rms_displacement: 0.0
  maximum_displacement: 0.0
  approved_as_phase_2_starting_structure: true
```

---

## Current Provenance Status

The room-temperature zincblende InP reference has completed the Phase 1 provenance and structural-validation workflow.

Current status:

* experimental provenance: established
* project reference: created
* structural validation: passed
* canonical CIF: generated
* canonical VASP: generated
* canonical validation: passed
* structural equivalence: passed
* checksums: recorded
* DFT relaxation: not yet performed
* Phase 2 computational convergence: not yet started

**InP Phase 1 structure provenance status: COMPLETE**
