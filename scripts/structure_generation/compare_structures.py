from __future__ import annotations

import argparse
from pathlib import Path

from pymatgen.analysis.structure_matcher import StructureMatcher
from pymatgen.core import Structure


def parse_args():
    parser = argparse.ArgumentParser(
        description="Compare two structures for crystallographic equivalence."
    )

    parser.add_argument("structure_a", type=Path)
    parser.add_argument("structure_b", type=Path)

    return parser.parse_args()


def main():
    args = parse_args()

    path_a = args.structure_a.expanduser().resolve()
    path_b = args.structure_b.expanduser().resolve()

    structure_a = Structure.from_file(path_a)
    structure_b = Structure.from_file(path_b)

    matcher = StructureMatcher(
        ltol=0.2,
        stol=0.3,
        angle_tol=5.0,
        primitive_cell=False,
        scale=False,
        attempt_supercell=False,
    )

    equivalent = matcher.fit(structure_a, structure_b)

    print("=" * 70)
    print("STRUCTURE EQUIVALENCE TEST")
    print("=" * 70)

    print(f"Structure A : {path_a}")
    print(f"Structure B : {path_b}")

    print("\nCOMPOSITION")
    print("-" * 70)
    print(f"A : {structure_a.composition}")
    print(f"B : {structure_b.composition}")

    print("\nATOM COUNT")
    print("-" * 70)
    print(f"A : {len(structure_a)}")
    print(f"B : {len(structure_b)}")

    print("\nLATTICE")
    print("-" * 70)

    print(
        f"A : {structure_a.lattice.a:.6f} "
        f"{structure_a.lattice.b:.6f} "
        f"{structure_a.lattice.c:.6f} Å"
    )

    print(
        f"B : {structure_b.lattice.a:.6f} "
        f"{structure_b.lattice.b:.6f} "
        f"{structure_b.lattice.c:.6f} Å"
    )

    print("\nSTRUCTURE MATCHER")
    print("-" * 70)
    print(f"Equivalent : {equivalent}")

    if equivalent:
        rms = matcher.get_rms_dist(structure_a, structure_b)

        if rms is not None:
            print(f"Normalized RMS displacement : {rms[0]:.8f}")
            print(f"Maximum displacement        : {rms[1]:.8f}")

    print("\n" + "=" * 70)

    if equivalent:
        print("RESULT: PASS")
    else:
        print("RESULT: FAIL")

    print("=" * 70)


if __name__ == "__main__":
    main()