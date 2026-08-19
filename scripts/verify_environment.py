#!/usr/bin/env python3
"""Smoke tests that verify the LeetCode solutions development environment."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from typing import List

REPO_ROOT = Path(__file__).resolve().parent.parent


def load_leetcode_module(path: Path, module_name: str):
    """Load a LeetCode-style solution module that omits typing imports."""
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load module from {path}")
    module = importlib.util.module_from_spec(spec)
    module.List = List
    spec.loader.exec_module(module)
    return module


def load_module(path: Path, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load module from {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_bubble_sort() -> None:
    module = load_module(
        REPO_ROOT / "arrays" / "sorting" / "bubble_sort.py",
        "bubble_sort",
    )
    result = module.bubble_sort([5, 1, 4, 2, 8])
    assert result == [1, 2, 4, 5, 8], f"unexpected bubble_sort result: {result}"


def test_binary_search() -> None:
    module = load_leetcode_module(
        REPO_ROOT / "arrays" / "searching" / "binary_search.py",
        "binary_search",
    )
    solution = module.Solution()
    assert solution.search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert solution.search([-1, 0, 3, 5, 9, 12], 2) == -1


def test_two_sum() -> None:
    module = load_leetcode_module(
        REPO_ROOT / "arrays" / "two-pointers" / "two_sum.py",
        "two_sum",
    )
    solution = module.Solution()
    result = solution.twoSum([2, 7, 11, 15], 9)
    assert sorted(result) == [0, 1], f"unexpected two_sum result: {result}"


def test_longest_common_prefix() -> None:
    module = load_leetcode_module(
        REPO_ROOT / "strings" / "longest_common_prefix.py",
        "longest_common_prefix",
    )
    solution = module.Solution()
    assert solution.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert solution.longestCommonPrefix(["dog", "racecar", "car"]) == ""


def main() -> int:
    if sys.version_info < (3, 10):
        print(f"Python 3.10+ required, found {sys.version}")
        return 1

    tests = [
        ("bubble_sort", test_bubble_sort),
        ("binary_search", test_binary_search),
        ("two_sum", test_two_sum),
        ("longest_common_prefix", test_longest_common_prefix),
    ]

    for name, test_fn in tests:
        test_fn()
        print(f"PASS {name}")

    print("All environment verification checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
