"""Bridges to sibling foundations (graceful degradation)."""

from __future__ import annotations

import os
import sys
from typing import Any, Optional

from .contracts import A0_M

_STAGING = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def _add_sibling(name: str) -> bool:
    p = os.path.join(_STAGING, name)
    if not os.path.isdir(p):
        return False
    if p not in sys.path:
        sys.path.insert(0, p)
    return True


def try_em_boundary_bridge(
    *, z_atomic: int = 1, distance_m: Optional[float] = None
) -> Optional[dict[str, Any]]:
    """Coulomb potential scale at Bohr length — classical ↔ QM context."""
    if not _add_sibling("Electromagnetic_Boundary_Foundation"):
        return None
    try:
        from em_boundary import ElectrostaticInput, screen_electrostatic

        r = distance_m if distance_m is not None else A0_M
        q_c = 1.602176634e-19 * max(1, z_atomic)
        es = screen_electrostatic(ElectrostaticInput(charge_c=q_c, distance_m=max(r, 1e-15)))
        return {
            "bridge": "Electromagnetic_Boundary_Foundation",
            "role": "Coulomb V at r~a0 for Z protons (classical screening context)",
            "z_atomic": z_atomic,
            "distance_m": r,
            "potential_v": es.potential_v,
            "electric_field_v_m": es.electric_field_v_m,
            "status": "available",
        }
    except ImportError:
        return None


def try_frequencycore_bridge(*, transition_ev: float = 1.0) -> Optional[dict[str, Any]]:
    """Spectral frequency from ΔE = hν (comparative)."""
    if not _add_sibling("FrequencyCore_Engine"):
        return None
    try:
        from frequency_core import analyze_resonance  # type: ignore

        h_ev_s = 4.135667696e-15
        nu_hz = abs(transition_ev) / h_ev_s if h_ev_s else 0.0
        rep = analyze_resonance(
            signal=[0.0, 1.0, 0.0, -0.5, 0.0],
            natural_freq_hz=max(nu_hz, 1.0),
            excitation_freq_hz=max(nu_hz, 1.0),
        )
        return {
            "bridge": "FrequencyCore_Engine",
            "role": "transition energy → oscillation scale (proxy)",
            "transition_ev": transition_ev,
            "derived_frequency_hz": nu_hz,
            "resonance_state": rep.resonance_state.value,
            "status": "available",
        }
    except ImportError:
        return None
