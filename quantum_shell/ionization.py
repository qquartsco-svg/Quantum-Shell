"""L5 — Ionization energy proxy & de Broglie length scale (order-of-magnitude)."""

from __future__ import annotations

import math

from .contracts import A0_M, EV_TO_J, RY_EV, IonizationInput, IonizationResult

M_E_KG = 9.1093837015e-31
H_SI = 6.62607015e-34  # Planck constant (J·s)


def screen_ionization(inp: IonizationInput) -> IonizationResult:
    z = max(inp.z_effective, 1e-9)
    n = max(1, inp.n_outer)
    e_bind_ev = -RY_EV * (z ** 2) / (n ** 2)
    ip_ev = abs(e_bind_ev)

    kT = max(inp.thermal_energy_ev, 1e-9)
    ratio = ip_ev / kT

    # de Broglie λ = h / p,  p = sqrt(2 m E), E in J
    e_j = ip_ev * EV_TO_J
    if e_j <= 0:
        lam = float("inf")
        scale_ratio = 0.0
    else:
        p = math.sqrt(2.0 * M_E_KG * e_j)
        lam = H_SI / p if p > 0 else float("inf")
        scale_ratio = lam / (2.0 * math.pi * A0_M) if lam < 1e10 else 0.0

    omega = 0.45
    if ip_ev > kT:
        omega += 0.25
    if 0.1 <= scale_ratio <= 100.0:
        omega += 0.2
    omega = max(0.0, min(1.0, omega))

    return IonizationResult(
        ionization_energy_ev=ip_ev,
        thermal_ratio=ratio,
        de_broglie_m=lam if lam < 1e10 else 0.0,
        length_scale_ratio=scale_ratio,
        omega=omega,
        notes="IP from hydrogenic binding; gas-phase thermal comparison only",
    )
