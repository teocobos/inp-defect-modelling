# Convergence Strategy

## Purpose

This document defines how numerical convergence will be established before production InP calculations are performed.

The objective is to ensure that reported physical trends are not dominated by numerical settings.

## General Principle

Only one numerical parameter should be varied at a time unless coupled convergence is explicitly required.

All convergence tests should use a clearly defined reference structure and target observable.

## Target Observables

Possible convergence targets include:

- total energy per atom
- lattice parameters
- forces
- band gap
- band-edge positions
- defect formation energies
- migration barriers

The observable selected for each test must be stated.

## Phase 1 — Pristine Bulk Convergence

Initial convergence testing should use pristine zincblende InP.

The following should be tested:

- basis-set quality
- plane-wave cutoff
- relative cutoff
- k-point sampling
- SCF convergence
- geometry-optimisation thresholds

## Cutoff Convergence

For CP2K, test a sequence of:

- plane-wave cutoffs
- relative cutoffs

The converged value should satisfy the predefined tolerance in the target observable.

The selected production cutoff should include a reasonable margin beyond the minimum converged value.

## Basis-Set Convergence

Where practical, compare multiple basis-set qualities.

At minimum, assess whether the selected basis gives stable:

- total energies
- structural parameters
- band-edge features

A larger basis should be used as a benchmark where computationally feasible.

## k-Point Convergence

Test progressively denser k-point meshes.

For the primitive or conventional cell, monitor:

- total energy per atom
- lattice constants
- band gap
- DOS features where relevant

For supercells, test reduced meshes independently rather than assuming that scaling from the primitive cell is sufficient.

## SCF Convergence

SCF parameters should be tested to ensure stable convergence for:

- pristine cells
- charged cells
- spin-polarised states
- hybrid-functional calculations

Potential issues such as oscillation, charge sloshing or convergence to metastable electronic states must be documented.

## Geometry Convergence

Geometry thresholds should be selected so that further tightening does not materially alter:

- equilibrium bond lengths
- lattice constants
- defect geometries
- defect energetics

## Supercell Convergence

Defect calculations require separate convergence with respect to supercell size.

Candidate cells should be compared using representative defects.

Assess:

- defect-image separation
- formation energy
- local relaxation
- charge localisation
- correction magnitude
- computational cost

## Charged-Defect Convergence

Charged defects require particular attention to:

- supercell size
- dielectric screening
- electrostatic corrections
- potential alignment
- k-point sampling

A correction method should not be considered validated solely because it can be applied numerically.

Its convergence behaviour should also be demonstrated.

## Hybrid-Functional Convergence

Hybrid-functional calculations may require separate convergence testing because:

- exchange interactions are more expensive
- k-point requirements may differ
- localised states may be sensitive to initial conditions
- SCF convergence can be more difficult

The hybrid-functional production settings should therefore be validated independently.

## Migration Convergence

For NEB calculations, convergence should be assessed with respect to:

- number of images
- force threshold
- interpolation quality
- supercell size
- k-point sampling

The calculated migration barrier should not change significantly when these parameters are refined.

## Documentation

Each completed convergence study should record:

- parameter varied
- values tested
- target observable
- convergence tolerance
- selected production value
- justification
- date
- software version

Final values should be transferred to `computational-parameters.md`.