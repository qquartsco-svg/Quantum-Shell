"""Quantum Shell Foundation — public API."""

from .contracts import (
    RY_EV,
    A0_M,
    EV_TO_J,
    ReadinessVerdict,
    ShellClosure,
    HydrogenicInput,
    HydrogenicResult,
    OrbitalBasisInput,
    OrbitalBasisResult,
    SubshellInfo,
    ScreeningInput,
    ScreeningResult,
    ShellFillingInput,
    ShellFillingResult,
    IonizationInput,
    IonizationResult,
    QuantumShellReport,
)
from .hydrogenic import screen_hydrogenic
from .orbitals import screen_orbital_basis
from .screening import screen_screening
from .filling import screen_shell_filling
from .ionization import screen_ionization
from .foundation import analyze
from .ecosystem_bridges import try_em_boundary_bridge, try_frequencycore_bridge

__all__ = [
    "RY_EV", "A0_M", "EV_TO_J",
    "ReadinessVerdict", "ShellClosure",
    "HydrogenicInput", "HydrogenicResult",
    "OrbitalBasisInput", "OrbitalBasisResult", "SubshellInfo",
    "ScreeningInput", "ScreeningResult",
    "ShellFillingInput", "ShellFillingResult",
    "IonizationInput", "IonizationResult",
    "QuantumShellReport",
    "screen_hydrogenic", "screen_orbital_basis", "screen_screening",
    "screen_shell_filling", "screen_ionization", "analyze",
    "try_em_boundary_bridge", "try_frequencycore_bridge",
]
