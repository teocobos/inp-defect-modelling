from __future__ import annotations

import argparse
from pathlib import Path

from pymatgen.core import Structure
from pymatgen.io.cif import CifWriter
from pymatgen.io.vasp import Poscar
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer


def parse_args():
    parser = argparse.ArgumentParser(
        description=(
            "Generate canonical crystallographic structures from a validated "
            "reference structure."
        )
    )

    parser.add_argument(
        "input_file",
        type=Path,
        help="Validated input structure.",
    )

    parser.add_argument(
        "output_dir",
        type=Path,
        help="Directory in which canonical structures will be written.",
    )

    parser.add_argument(
        "--prefix",
        required=True,
        help="Filename prefix for generated structures.",
    )

    parser.add_argument(
        "--symprec",
        type=float,
        default=1e-3,
        help="Symmetry tolerance used for standardisation.",
    )

    parser.add_argument(
        "--angle-tolerance",
        type=float,
        default=5.0,
        help="Angular tolerance used for symmetry analysis.",
    )

    return parser.parse_args()


def main():
    args = parse_args()

    input_path = args.input_file.expanduser().resolve()
    output_dir = args.output_dir.expanduser().resolve()

    if not input_path.exists():
        raise FileNotFoundError(
            f"Input structure does not exist: {input_path}"
        )

    output_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 70)
    print("CANONICAL STRUCTURE GENERATION")
    print("=" * 70)
    print(f"Input file : {input_path}")
    print(f"Output dir : {output_dir}")
    print(f"symprec    : {args.symprec}")
    print(f"angle tol. : {args.angle_tolerance}°")

    reference = Structure.from_file(input_path)

    analyzer = SpacegroupAnalyzer(
        reference,
        symprec=args.symprec,
        angle_tolerance=args.angle_tolerance,
    )

    canonical = analyzer.get_conventional_standard_structure()

    canonical_analyzer = SpacegroupAnalyzer(
        canonical,
        symprec=args.symprec,
        angle_tolerance=args.angle_tolerance,
    )

    cif_path = output_dir / f"{args.prefix}.cif"
    poscar_path = output_dir / f"{args.prefix}.vasp"

    CifWriter(
        canonical,
        symprec=args.symprec,
    ).write_file(cif_path)

    Poscar(
        canonical,
        comment=(
            f"{canonical.composition.reduced_formula} canonical "
            f"structure generated from {input_path.name}"
        ),
    ).write_file(poscar_path)

    print("\nREFERENCE")
    print("-" * 70)
    print(f"Formula             : {reference.composition.reduced_formula}")
    print(f"Atoms               : {len(reference)}")
    print(
        f"Space group         : "
        f"{analyzer.get_space_group_symbol()} "
        f"({analyzer.get_space_group_number()})"
    )

    print("\nCANONICAL")
    print("-" * 70)
    print(f"Formula             : {canonical.composition.reduced_formula}")
    print(f"Atoms               : {len(canonical)}")
    print(
        f"Space group         : "
        f"{canonical_analyzer.get_space_group_symbol()} "
        f"({canonical_analyzer.get_space_group_number()})"
    )

    print(
        f"a, b, c             : "
        f"{canonical.lattice.a:.6f}, "
        f"{canonical.lattice.b:.6f}, "
        f"{canonical.lattice.c:.6f} Å"
    )

    print(
        f"alpha, beta, gamma  : "
        f"{canonical.lattice.alpha:.6f}, "
        f"{canonical.lattice.beta:.6f}, "
        f"{canonical.lattice.gamma:.6f}°"
    )

    print("\nOUTPUT")
    print("-" * 70)
    print(f"CIF    : {cif_path}")
    print(f"POSCAR : {poscar_path}")

    print("\n" + "=" * 70)
    print("GENERATION COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()