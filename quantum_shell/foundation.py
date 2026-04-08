"""Quantum Shell Foundation — integrator."""

from __future__ import annotations

from typing import Optional

from .contracts import (
    HydrogenicInput,
    OrbitalBasisInput,
    ScreeningInput,
    ShellFillingInput,
    IonizationInput,
    QuantumShellReport,
    ReadinessVerdict,
)
from .hydrogenic import screen_hydrogenic
from .orbitals import screen_orbital_basis
from .screening import screen_screening
from .filling import screen_shell_filling
from .ionization import screen_ionization


def analyze(
    *,
    hydrogenic_input: Optional[HydrogenicInput] = None,
    orbital_input: Optional[OrbitalBasisInput] = None,
    screening_input: Optional[ScreeningInput] = None,
    filling_input: Optional[ShellFillingInput] = None,
    ionization_input: Optional[IonizationInput] = None,
) -> QuantumShellReport:
    omegas: list[float] = []

    h = None
    if hydrogenic_input is not None:
        h = screen_hydrogenic(hydrogenic_input)
        omegas.append(h.omega)

    ob = None
    if orbital_input is not None:
        ob = screen_orbital_basis(orbital_input)
        omegas.append(ob.omega)

    sc = None
    if screening_input is not None:
        sc = screen_screening(screening_input)
        omegas.append(sc.omega)

    fl = None
    if filling_input is not None:
        fl = screen_shell_filling(filling_input)
        omegas.append(fl.omega)

    io = None
    if ionization_input is not None:
        io = screen_ionization(ionization_input)
        omegas.append(io.omega)

    n = len(omegas)
    omega_overall = sum(omegas) / n if n > 0 else 0.0

    if omega_overall >= 0.80:
        verdict = ReadinessVerdict.OPERATIONAL
    elif omega_overall >= 0.55:
        verdict = ReadinessVerdict.FEASIBLE
    elif omega_overall >= 0.30:
        verdict = ReadinessVerdict.EXPERIMENTAL
    else:
        verdict = ReadinessVerdict.NOT_FEASIBLE

    return QuantumShellReport(
        hydrogenic=h,
        orbital_basis=ob,
        screening=sc,
        filling=fl,
        ionization=io,
        omega_overall=omega_overall,
        verdict=verdict,
        layers_executed=n,
    )
