# Structure Provenance

## Purpose

This document records the provenance and transformation history of all important InP structures.

## Reference Structure

The primary reference structure will be experimental zincblende InP.

The following must be recorded:

- database
- database identifier
- publication
- authors
- journal
- year
- DOI
- lattice parameters
- space group
- atomic coordinates
- acquisition date
- original file name
- repository file name

## Original Structures

Original downloaded structures should be preserved unchanged where licensing permits.

Store under:

`structures/crystalline/reference/`

## Canonical Structures

A canonical project structure may be generated from the reference file.

Possible operations include:

- symmetry standardisation
- conversion between file formats
- primitive-cell generation
- conventional-cell generation
- coordinate wrapping
- removal of redundant metadata

Every operation must be documented.

## Relaxed Structures

Relaxed structures should never overwrite the original reference structure.

Store separately under:

`structures/crystalline/relaxed/`

## Supercells

Supercells should record:

- parent structure
- replication matrix
- generation script
- software version
- number of atoms

## Defect Structures

Defect structures should record:

- parent supercell
- defect type
- atomic site modified
- charge state
- generation script
- configuration identifier

## Format Conversions

File conversion should not silently alter:

- lattice vectors
- fractional coordinates
- atom ordering
- species labels

Conversion scripts should be version controlled where possible.

## Validation

Reference structures should be checked using tools such as:

- pymatgen
- ASE
- spglib

Validate:

- composition
- atom count
- symmetry
- lattice parameters
- minimum interatomic distances

## Checksums

Important reference structures may be assigned SHA256 checksums to detect accidental modification.

## Provenance Record Template

For each reference structure, record:

```yaml
material: InP
phase: zincblende
source_database: null
database_id: null
citation: null
doi: null
download_date: null
original_filename: null
repository_filename: null
sha256: null
modifications: none