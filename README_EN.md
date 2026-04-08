# Quantum Shell Foundation

> **English.** Korean (정본): [README.md](README.md)

| Item | Details |
|------|---------|
| Version | `v0.1.0` |
| Tests | `10 passed` |
| Deps | Runtime: **stdlib only** · Test: `pytest>=8.0` |
| Python | `>=3.10` |
| License | MIT |

---

## One-liner

**Quantum shell screening on top of the Coulomb potential — hydrogenic levels, orbital degeneracy, effective-Z (Slater-like proxy), Aufbau filling, ionization / length-scale proxies.**

---

## Position in the A→F stack

```
F  Biology / cognition
E  Membrane / boundary biology
D  Complex molecules / self-assembly
C  Chemistry / bonding
B  Atomic / quantum  ← this engine
A  EM / electrostatic boundary  ← Electromagnetic_Boundary_Foundation
```

**Flow consistency:** classical Coulomb boundaries live in **A**. **Why electrons occupy shells instead of collapsing** is screened in **B** (this package). **C** (chemical bonding) requires a separate foundation.

---

## Five layers

| Layer | Name | Physics | Key outputs |
|-------|------|---------|-------------|
| **L1** | Hydrogenic | \(E_n = -R_\infty Z_\mathrm{eff}^2/n^2\) | Levels (eV), ground state, Bohr radius |
| **L2** | Orbital basis | \(2(2\ell+1)\) per subshell | Subshell list, state count to n_max |
| **L3** | Screening | Slater-style proxy | \(Z_\mathrm{eff}\), shielding constant |
| **L4** | Filling | Aufbau (Z ≤ 118) | Config string, valence n, closure class |
| **L5** | Ionization | Binding vs kT, de Broglie λ | IP proxy, thermal ratio, length ratio |

---

## What this is / is not

**Covers:** non-relativistic hydrogenic spectrum, Aufbau, simple screening, order-of-magnitude IP and de Broglie scale.

**Does not cover:** relativistic fine structure, multi-electron accurate spectra, Hartree–Fock/DFT, molecular orbitals, experimental spectroscopy fitting.

---

## Bridges

- `try_em_boundary_bridge()` — Coulomb snapshot at ~Bohr radius when **Electromagnetic_Boundary_Foundation** is sibling-installed.
- From EM upward: `em_boundary.try_quantum_shell_bridge(z_atomic=…)`.

---

## Tests

```bash
pip install -e ".[dev]"
python3 -m pytest tests/ -q            # 10 passed
```

---

## License

MIT — [LICENSE](LICENSE)
