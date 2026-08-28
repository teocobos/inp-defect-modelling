# Chemical Potentials

## Purpose

This document defines the chemical-potential framework used for InP defect formation energies.

## Defect Formation Energy

The defect formation energy is written as:

\[
E_f(D^q)
=
E_{\mathrm{tot}}(D^q)
-
E_{\mathrm{tot}}(\mathrm{host})
-
\sum_i n_i\mu_i
+
q(E_F + E_{\mathrm{VBM}})
+
E_{\mathrm{corr}}
\]

The chemical potentials \(\mu_i\) represent the energetic reservoirs of atoms exchanged with the host.

## InP Stability Condition

For equilibrium with bulk InP:

\[
\mu_{\mathrm{In}} + \mu_{\mathrm{P}}
=
\mu_{\mathrm{InP}}
\]

Chemical potentials should normally be expressed relative to elemental reference states.

## Relative Chemical Potentials

Define:

\[
\mu_{\mathrm{In}}
=
\mu_{\mathrm{In}}^0
+
\Delta \mu_{\mathrm{In}}
\]

\[
\mu_{\mathrm{P}}
=
\mu_{\mathrm{P}}^0
+
\Delta \mu_{\mathrm{P}}
\]

where:

\[
\Delta \mu_{\mathrm{In}} \leq 0
\]

and:

\[
\Delta \mu_{\mathrm{P}} \leq 0
\]

to avoid precipitation of elemental phases.

## In-Rich Limit

Under In-rich conditions:

\[
\Delta \mu_{\mathrm{In}} = 0
\]

and the phosphorus chemical potential is determined from the InP formation enthalpy.

## P-Rich Limit

Under P-rich conditions:

\[
\Delta \mu_{\mathrm{P}} = 0
\]

and the indium chemical potential is determined from the InP formation enthalpy.

## Elemental Reference States

Reference phases must be explicitly defined.

The thermodynamically appropriate elemental reference structures for In and P must be identified and calculated consistently.

Reference-state treatment should be validated carefully because elemental phases can respond differently to exchange-correlation approximations.

## Competing Phases

If impurities or multicomponent defect chemistry are introduced later, competing phases must be considered.

The allowed chemical-potential region should satisfy the stability constraints of all relevant phases.

## Consistency

All chemical potentials used in defect calculations must be derived using the same computational methodology as the host and defect calculations unless a correction scheme is explicitly justified.

## Required Metadata

Record:

- reference phase
- structure
- functional
- code
- basis or pseudopotential
- total energy
- correction applied
- final chemical potential

## Formation-Energy Diagrams

Formation-energy diagrams should clearly state the chemical-potential condition used.

At minimum, plot:

- In-rich
- P-rich

conditions separately unless there is a specific reason to show another point within the stability region.
