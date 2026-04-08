"""L4 — Aufbau filling (non-relativistic order, Z ≤ 118)."""

from __future__ import annotations

from .contracts import ShellClosure, ShellFillingInput, ShellFillingResult

_LAB = ("s", "p", "d", "f", "g", "h")

# (n, l, capacity) — Madelung / Aufbau order
_AUFBAU: tuple[tuple[int, int, int], ...] = (
    (1, 0, 2),
    (2, 0, 2),
    (2, 1, 6),
    (3, 0, 2),
    (3, 1, 6),
    (4, 0, 2),
    (3, 2, 10),
    (4, 1, 6),
    (5, 0, 2),
    (4, 2, 10),
    (5, 1, 6),
    (6, 0, 2),
    (4, 3, 14),
    (5, 2, 10),
    (6, 1, 6),
    (7, 0, 2),
    (5, 3, 14),
    (6, 2, 10),
    (7, 1, 6),
)

_NOBLE_Z = frozenset({2, 10, 18, 36, 54, 86, 118})


def screen_shell_filling(inp: ShellFillingInput) -> ShellFillingResult:
    z = max(1, min(inp.z_atomic, 118))
    remaining = z
    chunks: list[str] = []
    val_n, val_l = 1, 0
    outer = 0
    last_cap = 2

    for n, l, cap in _AUFBAU:
        if remaining <= 0:
            break
        take = min(remaining, cap)
        if take > 0:
            label = _LAB[l] if l < len(_LAB) else f"l{l}"
            chunks.append(f"{n}{label}{take}")
            remaining -= take
            val_n, val_l = n, l
            outer = take
            last_cap = cap

    config = " ".join(chunks)

    if z in _NOBLE_Z:
        closure = ShellClosure.NOBLE_LIKE
    elif last_cap > 2 and outer * 2 == last_cap:
        closure = ShellClosure.HALF_FILLED
    else:
        closure = ShellClosure.OPEN

    omega = 0.55 if z <= 118 else 0.2
    if z in _NOBLE_Z:
        omega += 0.15
    omega = max(0.0, min(1.0, omega))

    notes = ""
    if inp.z_atomic > 118:
        notes = "Z > 118: Aufbau list truncated; not physical for superheavy"

    return ShellFillingResult(
        electron_configuration=config,
        valence_n=val_n,
        valence_l=val_l,
        outer_electrons=outer,
        closure=closure,
        omega=omega,
        notes=notes,
    )
