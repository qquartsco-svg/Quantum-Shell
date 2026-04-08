"""Tests for Quantum Shell Foundation."""

import pytest

from quantum_shell import (
    RY_EV,
    A0_M,
    ReadinessVerdict,
    ShellClosure,
    HydrogenicInput,
    OrbitalBasisInput,
    ScreeningInput,
    ShellFillingInput,
    IonizationInput,
    screen_hydrogenic,
    screen_orbital_basis,
    screen_screening,
    screen_shell_filling,
    screen_ionization,
    analyze,
    try_em_boundary_bridge,
)


def test_hydrogen_ground_state():
    r = screen_hydrogenic(HydrogenicInput(z_effective=1.0, n_principal=1, n_max=4))
    assert r.ground_state_ev == pytest.approx(-RY_EV, rel=1e-5)
    assert r.energies_ev[0] == pytest.approx(-RY_EV, rel=1e-5)
    assert r.energies_ev[1] == pytest.approx(-RY_EV / 4, rel=1e-5)


def test_hydrogenic_z_squared():
    r = screen_hydrogenic(HydrogenicInput(z_effective=2.0, n_principal=1, n_max=2))
    assert r.ground_state_ev == pytest.approx(-4 * RY_EV, rel=1e-5)


def test_bohr_radius_scales_1_over_z():
    r1 = screen_hydrogenic(HydrogenicInput(z_effective=1.0))
    r2 = screen_hydrogenic(HydrogenicInput(z_effective=2.0))
    assert r1.bohr_radius_m == pytest.approx(A0_M, rel=1e-5)
    assert r2.bohr_radius_m == pytest.approx(A0_M / 2, rel=1e-5)


def test_orbital_degeneracy_n3():
    r = screen_orbital_basis(OrbitalBasisInput(n_max=3))
    assert r.total_states_up_to_n_max == 28


def test_screening_override():
    r = screen_screening(ScreeningInput(z_atomic=11, z_effective_override=2.2))
    assert r.z_effective == pytest.approx(2.2)


def test_shell_filling_na():
    r = screen_shell_filling(ShellFillingInput(z_atomic=11))
    assert "3s1" in r.electron_configuration
    assert r.valence_n == 3
    assert r.closure == ShellClosure.OPEN


def test_shell_filling_neon():
    r = screen_shell_filling(ShellFillingInput(z_atomic=10))
    assert r.closure == ShellClosure.NOBLE_LIKE


def test_ionization_hydrogen():
    r = screen_ionization(IonizationInput(z_effective=1.0, n_outer=1))
    assert r.ionization_energy_ev == pytest.approx(RY_EV, rel=1e-5)


def test_analyze_stack():
    rep = analyze(
        hydrogenic_input=HydrogenicInput(),
        orbital_input=OrbitalBasisInput(n_max=3),
        screening_input=ScreeningInput(z_atomic=1, inner_electrons=0),
        filling_input=ShellFillingInput(z_atomic=1),
        ionization_input=IonizationInput(z_effective=1.0, n_outer=1),
    )
    assert rep.layers_executed == 5
    assert 0.0 <= rep.omega_overall <= 1.0
    assert rep.verdict in ReadinessVerdict


def test_em_bridge_graceful():
    r = try_em_boundary_bridge(z_atomic=1)
    assert r is None or r["bridge"] == "Electromagnetic_Boundary_Foundation"
