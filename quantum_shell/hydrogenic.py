"""L1 — Hydrogenic energy levels and Bohr-scale lengths."""

from __future__ import annotations

from .contracts import A0_M, RY_EV, HydrogenicInput, HydrogenicResult


def screen_hydrogenic(inp: HydrogenicInput) -> HydrogenicResult:
    z = max(inp.z_effective, 1e-9)
    n0 = max(1, inp.n_principal)
    n_hi = max(n0, inp.n_max)

    energies: list[float] = []
    for n in range(1, n_hi + 1):
        e = -RY_EV * (z ** 2) / (n ** 2)
        energies.append(e)

    ground = -RY_EV * (z ** 2) / (n0 ** 2) if n0 >= 1 else energies[0]
    a_z = A0_M / z
    r1 = n0 ** 2 * a_z

    omega = _omega(z, n0, n_hi)
    notes = ""
    if z > 100:
        notes = "Z_eff very large: relativistic corrections not modeled"

    return HydrogenicResult(
        energies_ev=tuple(energies),
        ground_state_ev=ground,
        bohr_radius_m=a_z,
        r_expect_n1_m=r1,
        omega=omega,
        notes=notes,
    )


def _omega(z: float, n0: int, n_hi: int) -> float:
    score = 0.5
    if 0.5 <= z <= 120:
        score += 0.25
    if 1 <= n0 <= 7:
        score += 0.15
    if n_hi >= n0:
        score += 0.1
    return max(0.0, min(1.0, score))
