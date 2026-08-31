from __future__ import annotations

import argparse
from pathlib import Path

from pymatgen.core import Structure
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer


def parse_args():
    parser = argparse.ArgumentParser(
        description="Validate a crystalline reference structure."
    )
    parser.add_argument(
        "structure_file",
        type=Path,
        help="Path to CIF/POSCAR/structure file.",
    )
    parser.add_argument(
        "--symprec",
        type=float,
        default=1e-3,
        help="Symmetry tolerance passed to pymatgen/spglib.",
    )
    parser.add_argument(
        "--angle-tolerance",
        type=float,
        default=5.0,
        help="Angular tolerance for symmetry analysis.",
    )
    return parser.parse_args()


def minimum_distance(structure: Structure):
    distance_matrix = structure.distance_matrix.copy()

    nonzero = distance_matrix[distance_matrix > 1e-8]

    if len(nonzero) == 0:
        return None

    return float(nonzero.min())


def print_lattice(structure: Structure):
    lattice = structure.lattice

    print("\nLATTICE")
    print("-" * 60)
    print(f"a      = {lattice.a:.6f} Å")
    print(f"b      = {lattice.b:.6f} Å")
    print(f"c      = {lattice.c:.6f} Å")
    print(f"alpha  = {lattice.alpha:.6f}°")
    print(f"beta   = {lattice.beta:.6f}°")
    print(f"gamma  = {lattice.gamma:.6f}°")
    print(f"volume = {lattice.volume:.6f} Å^3")


def print_composition(structure: Structure):
    print("\nCOMPOSITION")
    print("-" * 60)
    print(f"Composition      : {structure.composition}")
    print(f"Reduced formula  : {structure.composition.reduced_formula}")
    print(f"Number of atoms  : {len(structure)}")


def print_symmetry(structure: Structure, symprec: float, angle_tolerance: float):
    analyzer = SpacegroupAnalyzer(
        structure,
        symprec=symprec,
        angle_tolerance=angle_tolerance,
    )

    print("\nSYMMETRY")
    print("-" * 60)
    print(f"Space-group symbol : {analyzer.get_space_group_symbol()}")
    print(f"Space-group number : {analyzer.get_space_group_number()}")
    print(f"Crystal system     : {analyzer.get_crystal_system()}")
    print(f"Lattice type       : {analyzer.get_lattice_type()}")

    symm_structure = analyzer.get_symmetrized_structure()

    print("\nSYMMETRY-INEQUIVALENT SITES")
    print("-" * 60)

    for i, equivalent_sites in enumerate(symm_structure.equivalent_sites, start=1):
        site = equivalent_sites[0]
        wyckoff = symm_structure.wyckoff_symbols[i - 1]

        print(
            f"{i:3d}  "
            f"{site.specie!s:4s}  "
            f"Wyckoff={wyckoff:4s}  "
            f"multiplicity={len(equivalent_sites):2d}  "
            f"frac=({site.frac_coords[0]:.6f}, "
            f"{site.frac_coords[1]:.6f}, "
            f"{site.frac_coords[2]:.6f})"
        )


def print_nearest_neighbours(structure: Structure):
    print("\nNEAREST-NEIGHBOUR ENVIRONMENTS")
    print("-" * 60)

    for i, site in enumerate(structure):
        neighbours = structure.get_neighbors(site, r=3.0)

        if not neighbours:
            print(f"{i:3d} {site.specie}: no neighbours within 3.0 Å")
            continue

        neighbours = sorted(neighbours, key=lambda x: x.nn_distance)

        closest_distance = neighbours[0].nn_distance

        first_shell = [
            neighbour
            for neighbour in neighbours
            if neighbour.nn_distance <= closest_distance + 0.20
        ]

        print(
            f"{i:3d} {site.specie:4s} "
            f"coordination≈{len(first_shell):2d} "
            f"nearest={closest_distance:.6f} Å"
        )

        for neighbour in first_shell:
            print(
                f"      -> {neighbour.specie:4s} "
                f"{neighbour.nn_distance:.6f} Å"
            )


def main():
    args = parse_args()

    path = args.structure_file.expanduser().resolve()

    if not path.exists():
        raise FileNotFoundError(f"Structure file not found: {path}")

    print("=" * 60)
    print("REFERENCE STRUCTURE VALIDATION")
    print("=" * 60)
    print(f"File: {path}")
    print(f"symprec: {args.symprec}")
    print(f"angle tolerance: {args.angle_tolerance}°")

    structure = Structure.from_file(path)

    print_composition(structure)
    print_lattice(structure)
    print_symmetry(
        structure,
        symprec=args.symprec,
        angle_tolerance=args.angle_tolerance,
    )

    dmin = minimum_distance(structure)

    print("\nGEOMETRY")
    print("-" * 60)

    if dmin is None:
        print("Minimum distance: unavailable")
    else:
        print(f"Minimum interatomic distance: {dmin:.6f} Å")

    print_nearest_neighbours(structure)

    print("\n" + "=" * 60)
    print("VALIDATION COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()