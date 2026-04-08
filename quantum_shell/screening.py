"""L3 — Effective nuclear charge proxy (Slater-style simplified)."""

from __future__ import annotations

from .contracts import ScreeningInput, ScreeningResult


def screen_screening(inp: ScreeningInput) -> ScreeningResult:
    if inp.z_effective_override is not None:
        z_eff = max(0.5, min(inp.z_effective_override, 120.0))
        s_const = float(inp.z_atomic) - z_eff
        return ScreeningResult(
            z_effective=z_eff,
            screening_constant=s_const,
            omega=0.85,
            notes="Z_eff from user override",
        )

    z = max(1, inp.z_atomic)
    inner = max(0, inp.inner_electrons)
    same = max(0, inp.same_shell_other)

    # Simplified Slater-like: inner 0.85 each, same-shell others 0.35 each
    shield = 0.85 * inner + 0.35 * same
    z_eff = max(1.0, z - shield)
    z_eff = min(z_eff, float(z))

    omega = 0.5
    if inner + same < z:
        omega += 0.2
    if 1.0 <= z_eff <= z:
        omega += 0.2
    omega = max(0.0, min(1.0, omega))

    return ScreeningResult(
        z_effective=z_eff,
        screening_constant=shield,
        omega=omega,
        notes="simplified screening; not a full Slater table",
    )
