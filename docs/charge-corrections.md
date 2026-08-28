# Charge Corrections

## Purpose

Charged-defect calculations in periodic supercells contain finite-size artefacts arising from interaction between periodically repeated charges and compensating backgrounds.

This document defines the strategy for correcting and validating those effects.

## Sources of Finite-Size Error

Potential errors include:

- electrostatic interaction between periodic defect images
- interaction with the compensating background charge
- potential-reference shifts
- elastic interactions
- defect-wavefunction overlap
- band filling

## Correction Framework

The correction methodology should be selected based on:

- supercell geometry
- dielectric properties
- anisotropy
- defect localisation
- software support

Potential approaches may include established schemes such as:

- Makov-Payne-type corrections
- Freysoldt-Neugebauer-Van de Walle corrections
- Kumagai-Oba-type corrections

The final method must be justified and documented.

## Zincblende Anisotropy

Zincblende InP is anisotropic.

Where the correction method permits, dielectric anisotropy should be considered using appropriate parallel and perpendicular dielectric components.

## Dielectric Constants

Record whether the correction uses:

- electronic dielectric constant
- ionic plus electronic static dielectric constant

The appropriate choice depends on the physical quantity and relaxation protocol.

## Potential Alignment

Potential alignment should compare a bulk-like region of the defective supercell with the pristine reference.

The exact quantity used for alignment should be documented.

## Supercell Testing

Correction quality should be tested across multiple supercell sizes where feasible.

A correction method is considered stronger if corrected formation energies converge more rapidly with increasing cell size.

## Band Filling

Shallow defect states that hybridise with host bands may require band-filling corrections.

These should be treated separately from electrostatic corrections.

## Delocalised States

If the added or removed charge is not localised around the defect, a conventional point-charge correction may be physically inappropriate.

Charge density should therefore be inspected for representative states.

## Correction Metadata

For every charged production calculation, record:

- charge state
- correction method
- dielectric parameters
- potential alignment
- correction magnitude
- supercell
- k-point mesh

## Validation

Before publication:

- compare corrected and uncorrected trends
- verify supercell-size convergence
- inspect charge localisation
- confirm stable charge-state ordering
- document residual uncertainties