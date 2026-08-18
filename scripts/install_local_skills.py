#!/usr/bin/env python3
"""Install repository skills into a local Agent skill directory."""

from __future__ import annotations

import argparse
import os
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT / "custom_skills"
DEFAULT_TARGET = Path.home() / ".agents" / "skills"


def packages() -> list[Path]:
    return sorted(
        directory
        for directory in SOURCE_ROOT.iterdir()
        if directory.is_dir()
        and (directory / "SKILL.md").is_file()
        and (directory / "manifest.json").is_file()
    )


def install(target: Path, force: bool) -> int:
    target = target.expanduser()
    target.mkdir(parents=True, exist_ok=True)
    installed = 0
    for source in packages():
        destination = target / source.name
        if destination.exists() or destination.is_symlink():
            if destination.is_symlink() and destination.resolve() == source.resolve():
                installed += 1
                continue
            if not force:
                raise SystemExit(
                    f"refusing to replace existing path: {destination}; "
                    "use --force only after reviewing it"
                )
            if destination.is_dir() and not destination.is_symlink():
                raise SystemExit(f"refusing to remove existing directory: {destination}")
            destination.unlink()
        os.symlink(source, destination, target_is_directory=True)
        installed += 1
    print(f"installed={installed}")
    print(f"target={target}")
    print(f"mode=symlink")
    return installed


def uninstall(target: Path) -> int:
    target = target.expanduser()
    if not target.exists() and not target.is_symlink():
        print(f"removed=0")
        print(f"target={target}")
        return 0
    removed = 0
    source_root = SOURCE_ROOT.resolve()
    for source in packages():
        destination = target / source.name
        if not destination.is_symlink():
            continue
        try:
            resolves_to = destination.resolve()
        except OSError:
            continue
        if resolves_to == source.resolve() or source_root in resolves_to.parents:
            destination.unlink()
            removed += 1
    print(f"removed={removed}")
    print(f"target={target}")
    return removed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", type=Path, default=DEFAULT_TARGET)
    parser.add_argument("--force", action="store_true", help="replace existing symlinks only")
    parser.add_argument("--uninstall", action="store_true", help="remove only links managed by this repository")
    args = parser.parse_args()
    if args.uninstall:
        uninstall(args.target)
    else:
        install(args.target, args.force)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
