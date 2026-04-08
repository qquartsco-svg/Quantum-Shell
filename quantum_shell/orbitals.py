"""L2 — Subshell catalog and degeneracy (non-relativistic hydrogenic basis)."""

from __future__ import annotations

from .contracts import OrbitalBasisInput, OrbitalBasisResult, SubshellInfo

_L_LABELS = ("s", "p", "d", "f", "g", "h")


def _capacity(l: int) -> int:
    return 2 * (2 * l + 1)


def _subshells_for_n(n: int) -> tuple[SubshellInfo, ...]:
    out: list[SubshellInfo] = []
    for l in range(n):
        label = _L_LABELS[l] if l < len(_L_LABELS) else f"l{l}"
        out.append(SubshellInfo(n=n, l=l, label=label, capacity=_capacity(l)))
    return tuple(out)


def screen_orbital_basis(inp: OrbitalBasisInput) -> OrbitalBasisResult:
    n_max = max(1, min(inp.n_max, 20))
    all_sub: list[SubshellInfo] = []
    degen_per_n: list[tuple[int, int]] = []

    for n in range(1, n_max + 1):
        subs = _subshells_for_n(n)
        all_sub.extend(subs)
        total_n = sum(s.capacity for s in subs)
        degen_per_n.append((n, total_n))

    total_states = sum(d for _, d in degen_per_n)

    omega = min(1.0, 0.52 + 0.06 * min(n_max, 8))

    return OrbitalBasisResult(
        subshells=tuple(all_sub),
        total_states_up_to_n_max=total_states,
        degeneracy_per_n=tuple(degen_per_n),
        omega=omega,
    )
