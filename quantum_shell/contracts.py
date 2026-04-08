"""
Quantum Shell Foundation — contracts

Scope: hydrogenic / effective-Z screening / shell filling / ionization proxies.
NOT relativistic QED, NOT full DFT, NOT molecular orbital theory.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Tuple


# Physical constants (CODATA-style, sufficient for screening)
RY_EV: float = 13.605693009  # Rydberg energy (eV), infinite nuclear mass approx
A0_M: float = 5.29177210903e-11  # Bohr radius (m)
EV_TO_J: float = 1.602176634e-19


class ReadinessVerdict(Enum):
    OPERATIONAL = "operational"
    FEASIBLE = "feasible"
    EXPERIMENTAL = "experimental"
    NOT_FEASIBLE = "not_feasible"


class ShellClosure(Enum):
    OPEN = "open"
    NOBLE_LIKE = "noble_like"
    HALF_FILLED = "half_filled"


# ── L1 Hydrogenic spectrum ──────────────────────────────────────────

@dataclass(frozen=True)
class HydrogenicInput:
    z_effective: float = 1.0
    n_principal: int = 1
    n_max: int = 4


@dataclass(frozen=True)
class HydrogenicResult:
    energies_ev: Tuple[float, ...]
    ground_state_ev: float
    bohr_radius_m: float
    r_expect_n1_m: float
    omega: float
    notes: str = ""


# ── L2 Orbital basis & degeneracy ───────────────────────────────────

@dataclass(frozen=True)
class OrbitalBasisInput:
    n_max: int = 4


@dataclass(frozen=True)
class SubshellInfo:
    n: int
    l: int
    label: str
    capacity: int


@dataclass(frozen=True)
class OrbitalBasisResult:
    subshells: Tuple[SubshellInfo, ...]
    total_states_up_to_n_max: int
    degeneracy_per_n: Tuple[Tuple[int, int], ...]
    omega: float
    notes: str = ""


# ── L3 Effective charge / screening proxy ─────────────────────────

@dataclass(frozen=True)
class ScreeningInput:
    z_atomic: int = 11
    inner_electrons: int = 10
    same_shell_other: int = 0
    z_effective_override: Optional[float] = None


@dataclass(frozen=True)
class ScreeningResult:
    z_effective: float
    screening_constant: float
    omega: float
    notes: str = ""


# ── L4 Aufbau filling ───────────────────────────────────────────────

@dataclass(frozen=True)
class ShellFillingInput:
    z_atomic: int = 11


@dataclass(frozen=True)
class ShellFillingResult:
    electron_configuration: str
    valence_n: int
    valence_l: int
    outer_electrons: int
    closure: ShellClosure
    omega: float
    notes: str = ""


# ── L5 Ionization & scale correspondence ────────────────────────────

@dataclass(frozen=True)
class IonizationInput:
    z_effective: float = 1.0
    n_outer: int = 1
    thermal_energy_ev: float = 0.0259


@dataclass(frozen=True)
class IonizationResult:
    ionization_energy_ev: float
    thermal_ratio: float
    de_broglie_m: float
    length_scale_ratio: float
    omega: float
    notes: str = ""


# ── Report ─────────────────────────────────────────────────────────

@dataclass(frozen=True)
class QuantumShellReport:
    hydrogenic: Optional[HydrogenicResult] = None
    orbital_basis: Optional[OrbitalBasisResult] = None
    screening: Optional[ScreeningResult] = None
    filling: Optional[ShellFillingResult] = None
    ionization: Optional[IonizationResult] = None
    omega_overall: float = 0.0
    verdict: ReadinessVerdict = ReadinessVerdict.NOT_FEASIBLE
    layers_executed: int = 0
