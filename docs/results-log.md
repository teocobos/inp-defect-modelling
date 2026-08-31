# InP Defect Modelling — Results Log

This document records significant computational results, validation decisions and methodological milestones.

It is not intended to replace raw calculation data.

---

## Phase 0 — Project Foundation

**Status:** Complete

### Repository Initialisation

The `inp-defect-modelling` repository has been established as the master III–V defect-modelling framework.

The repository architecture separates:

* structures
* calculations
* workflows
* scripts
* notebooks
* reports
* documentation
* reusable source code

The repository is version controlled using Git and mirrored to GitHub.

### Research Scope

The initial scientific programme has been defined around:

* crystalline zincblende InP
* pristine bulk properties
* native vacancies
* native antisites
* native interstitials
* charged-defect energetics
* thermodynamic charge-transition levels
* electronic localisation
* structural distortion
* selected migration mechanisms

### Initial Native Defect Set

#### Vacancies

* `V_In`
* `V_P`

#### Antisites

* `In_P`
* `P_In`

#### Interstitials

* `In_i`
* `P_i`

### Computational Framework

The project has been designed as a code-neutral first-principles workflow supporting:

* CP2K
* VASP
* AiiDA
* ASE
* pymatgen
* Python

The production methodology will be selected through numerical convergence and physical validation rather than software availability alone.

### Research Governance

Phase 0 documentation defines:

* computational parameter tracking
* convergence strategy
* structure provenance
* defect naming conventions
* metadata requirements
* reproducibility requirements
* validation criteria
* charged-defect correction strategy
* chemical-potential methodology
* dataset management
* literature-review structure
* IP and publication controls

### Phase 0 Outcome

The repository has a documented research framework capable of supporting reproducible bulk, defect, charged-defect, electronic-structure and migration calculations.

---

## Phase 1 — Crystal Structure

**Status:** Complete

### Objectives

Phase 1 was designed to:

* identify an authoritative zincblende InP reference structure
* establish experimental crystallographic provenance
* construct a project reference structure
* validate composition
* validate lattice parameters
* validate symmetry
* validate local coordination
* generate canonical project structures
* independently validate canonical structures
* establish reference-to-canonical structural equivalence
* record structural metadata and checksums
* establish an approved structural baseline for DFT calculations

### Reference Phase Selection

The primary crystalline phase selected for this project is:

* material: InP
* phase: zincblende
* crystal system: cubic
* space group: `F-43m`
* space-group number: 216

Zincblende InP is therefore used as the primary crystalline reference throughout the project unless another phase is explicitly under investigation.

### Experimental Lattice Reference

The project structure uses the room-temperature cubic lattice parameter:

* `a = 5.8688 Å`
* `b = 5.8688 Å`
* `c = 5.8688 Å`
* `alpha = beta = gamma = 90°`

The project value represents the rounded form of the established room-temperature lattice parameter:

`a ≈ 5.86875 Å`

Temperature-dependent experimental lattice measurements for InP extending to 300 K were reported by Haruna et al.

Experimental reference:

K. Haruna, H. Maeta, K. Ohashi and T. Koike, “The thermal expansion coefficient and Grüneisen parameter of InP crystal at low temperatures,” *Journal of Physics C: Solid State Physics* **20**, 5275–5279 (1987).

DOI:

`10.1088/0022-3719/20/32/013`

Haruna et al. measured the InP lattice constant over the temperature range 4.2–300 K using precision X-ray measurements.

### Reference Structure Construction

A project reference CIF was reconstructed using the established room-temperature zincblende InP crystallography.

Reference file:

`structures/crystalline/reference/zincblende/inp_zb_haruna_et_al_1987.cif`

The structure uses the zincblende `F-43m` crystallographic model with symmetry-inequivalent In and P sites.

The conventional unit cell contains:

* 4 In atoms
* 4 P atoms
* 8 atoms total
* reduced formula: InP
* conventional-cell composition: `In4 P4`

The reference file is a reconstructed project representation.

It is **not** an original deposited experimental CIF.

This distinction preserves the separation between the experimental literature providing the crystallographic basis and the machine-readable structure constructed for the computational workflow.

### Structural Validation

Structural validation was performed using:

`scripts/structure_generation/validate_reference_structure.py`

The same validation methodology is used for the reference and canonical structures.

Validation settings:

* symmetry tolerance: `0.001`
* angle tolerance: `5.0°`

### Validated Structural Properties

The validated InP structure gives:

#### Composition

* composition: `In4 P4`
* reduced formula: `InP`
* number of atoms: 8

#### Lattice

* `a = 5.868800 Å`
* `b = 5.868800 Å`
* `c = 5.868800 Å`
* `alpha = 90.000000°`
* `beta = 90.000000°`
* `gamma = 90.000000°`
* volume = `202.137984 Å³`

#### Symmetry

* space-group symbol: `F-43m`
* space-group number: 216
* crystal system: cubic
* lattice type: cubic

#### Symmetry-Inequivalent Sites

Symmetry analysis identifies:

* In: Wyckoff `4a`, multiplicity 4
* P: Wyckoff `4c`, multiplicity 4

Equivalent crystallographic origins or symmetry operations can lead software to report different fractional representatives of the same Wyckoff orbit. Such differences do not represent different physical structures.

### Local Geometry Validation

The minimum interatomic distance is:

`2.541265 Å`

Every In atom has four nearest-neighbour P atoms:

* In coordination number: 4
* In–P nearest-neighbour distance: `2.541265 Å`

Every P atom has four nearest-neighbour In atoms:

* P coordination number: 4
* P–In nearest-neighbour distance: `2.541265 Å`

The local environment therefore reproduces the expected tetrahedral coordination of zincblende InP.

For ideal zincblende geometry:

`d_In-P = (sqrt(3)/4) a`

The distance obtained directly from the project structure is consistent with this relationship.

### Validation Decision

The structure passes:

* composition validation
* atom-count validation
* lattice validation
* crystal-system validation
* space-group validation
* local-coordination validation
* nearest-neighbour-distance validation

**Structural validation status: PASS**

### Canonical Structure Generation

Canonical project representations were generated using:

`scripts/structure_generation/generate_canonical_structure.py`

Reference input:

`structures/crystalline/reference/zincblende/inp_zb_haruna_et_al_1987.cif`

Generated structures:

`structures/crystalline/reference/zincblende/canonical/inp_zb_canonical.cif`

and

`structures/crystalline/reference/zincblende/canonical/inp_zb_canonical.vasp`

The canonical generation process preserved:

* formula: InP
* conventional-cell composition: `In4 P4`
* atom count: 8
* space group: `F-43m` (216)
* `a = 5.868800 Å`
* `b = 5.868800 Å`
* `c = 5.868800 Å`
* cubic cell angles

These structures retain the experimental reference geometry.

They are **not DFT-relaxed structures**.

### Canonical CIF Validation

Independent validation of:

`structures/crystalline/reference/zincblende/canonical/inp_zb_canonical.cif`

returned:

* composition: `In4 P4`
* reduced formula: InP
* atoms: 8
* `a = b = c = 5.868800 Å`
* volume: `202.137984 Å³`
* space group: `F-43m`
* space-group number: 216
* crystal system: cubic
* minimum interatomic distance: `2.541265 Å`
* In coordination: 4
* P coordination: 4

**Canonical CIF validation: PASS**

### Canonical VASP Validation

Independent validation of:

`structures/crystalline/reference/zincblende/canonical/inp_zb_canonical.vasp`

returned:

* composition: `In4 P4`
* reduced formula: InP
* atoms: 8
* `a = b = c = 5.868800 Å`
* volume: `202.137984 Å³`
* space group: `F-43m`
* space-group number: 216
* crystal system: cubic
* minimum interatomic distance: `2.541265 Å`
* In coordination: 4
* P coordination: 4

**Canonical VASP validation: PASS**

### Reference–Canonical Equivalence Validation

Structural equivalence was tested using:

`scripts/structure_generation/compare_structures.py`

The comparison uses pymatgen `StructureMatcher` to detect unintended changes introduced during canonicalisation or format conversion.

#### Reference CIF → Canonical CIF

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

**Result: PASS**

#### Reference CIF → Canonical VASP

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

**Result: PASS**

### Structure Checksums

SHA256 checksums recorded following structural generation and validation:

Reference CIF:

`3a3627b1a5935cb15bb8b4b051a185d8fc62c89567776f469e4dae7dd319bcd7`

Canonical CIF:

`34f30ee880fbc90eb60bc48ab4a6d6ee8e323e8c1e08bbef725d89a3c0f5d3e3`

Canonical VASP:

`ec96af6b609c5786140568d33b9492d97e96eab29132ed4c2600703d490cef16`

These checksums correspond to the validated files at the time this result was recorded.

If metadata or comments inside a structural file are subsequently modified, the corresponding checksum must be recalculated even if the underlying atomic geometry remains unchanged.

### Phase 1 Validation Chain

The completed structural workflow is:

```text id="8d8agz"
experimental crystallographic literature
        ↓
room-temperature lattice reference
        ↓
reconstructed project reference CIF
        ↓
composition validation
        ↓
lattice validation
        ↓
symmetry validation
        ↓
local-geometry validation
        ↓
VALIDATED REFERENCE
        ↓
canonical CIF + VASP generation
        ↓
independent canonical validation
        ↓
reference–canonical equivalence testing
        ↓
SHA256 provenance
        ↓
APPROVED CRYSTALLINE BASELINE
```

### Phase 1 Outcome

The following Phase 1 deliverables are complete:

* primary zincblende phase identified
* experimental structural provenance established
* project reference CIF constructed
* composition validated
* lattice validated
* symmetry validated
* tetrahedral coordination validated
* nearest-neighbour distance validated
* canonical CIF generated
* canonical VASP structure generated
* canonical CIF independently validated
* canonical VASP structure independently validated
* reference-to-canonical CIF equivalence verified
* reference-to-canonical VASP equivalence verified
* zero structural displacement confirmed
* SHA256 checksums recorded
* structure approved as the crystalline computational baseline

**Phase 1 status: COMPLETE**

The canonical CIF/VASP structures are approved as starting structural representations for subsequent DFT convergence calculations.

The reconstructed experimental reference CIF remains the provenance reference and must not be replaced by a DFT-relaxed structure.

### Next Milestone

**Phase 2 — DFT Convergence**

Phase 2 will establish and validate the numerical settings required for reliable pristine-bulk and defect calculations, including as appropriate:

* electronic-structure code and version
* exchange-correlation functional strategy
* pseudopotential or PAW dataset selection
* treatment of semicore states
* basis-set or plane-wave cutoff convergence
* k-point convergence
* SCF convergence
* geometry-optimisation thresholds
* equilibrium lattice parameter
* total-energy convergence
* pristine electronic-structure validation
* spin-orbit coupling strategy

No production defect energetics should be interpreted until the relevant Phase 2 convergence criteria have been satisfied.

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
