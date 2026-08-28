# Validation Strategy

## Purpose

Validation ensures that the computational methodology produces physically meaningful and numerically reliable results before large-scale production calculations are performed.

## Validation Hierarchy

Validation should proceed in the following order:

1. reference structure
2. numerical convergence
3. pristine bulk properties
4. supercell behaviour
5. neutral defect structures
6. charged-defect methodology
7. electronic structure
8. migration pathways

## Structural Validation

The reference zincblende InP structure should be checked against experimental data.

Validate:

- composition
- symmetry
- lattice parameters
- internal coordinates
- In–P bond lengths

## Bulk Validation

The selected DFT methodology should reproduce physically reasonable:

- lattice parameters
- cohesive behaviour
- band structure
- band gap
- band-edge orbital character

Known systematic functional errors should be documented.

## Cross-Code Validation

Where both CP2K and VASP are used, selected benchmark calculations should compare:

- lattice parameters
- relative energies
- band structure
- band gap
- defect relaxation trends

Perfect numerical agreement is not required, but discrepancies should be understood.

## Defect Validation

For representative native defects, verify:

- structural stability
- reproducibility from multiple starting structures
- spin-state stability
- charge localisation
- supercell-size sensitivity

## Charged-Defect Validation

Charged-defect methodology should be validated using:

- supercell-size tests
- correction-magnitude analysis
- potential-alignment consistency
- dielectric properties
- stable formation-energy behaviour

## Charge-Transition Level Validation

CTLs should be checked for:

- numerical convergence
- correct charge-state ordering
- consistency with formation-energy diagrams
- sensitivity to band-edge treatment
- sensitivity to functional choice

## Electronic-State Validation

For defect-induced states, assess:

- localisation
- orbital character
- spin density
- charge density
- dependence on initial electronic state
- dependence on functional

## Migration Validation

Migration pathways should be checked for:

- physically meaningful initial and final states
- continuous atomic motion
- adequate number of images
- converged forces
- absence of unintended intermediate minima

## Literature Comparison

Comparison with published experimental and theoretical values should be used as a validation aid.

Disagreement should not automatically be treated as error.

Instead determine whether the difference arises from:

- methodology
- temperature
- experimental uncertainty
- functional choice
- supercell size
- charge correction
- structural model

## Validation Status

Calculations may be marked:

- `unvalidated`
- `provisionally validated`
- `validated`
- `deprecated`

Only validated results should be used for final conclusions unless explicitly stated otherwise.