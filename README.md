# Quantum Shell Foundation

> **한국어 (정본).** English: [README_EN.md](README_EN.md)

| 항목 | 내용 |
|------|------|
| 버전 | `v0.1.0` |
| 테스트 | `10 passed` |
| 의존성 | 런타임: **stdlib only** · 테스트: `pytest>=8.0` |
| Python | `>=3.10` |
| 라이선스 | MIT |

---

## 한 줄 정의

**전자기 쿨롱 퍼텐셜 위에 쌓이는 양자 껍질 스크리닝 foundation — 수소형 준위, 오비탈 기저·퇴화도, 유효핵전하(Slater 근사), Aufbau 채움, 이온화·길이 스케일 proxy.**

---

## 장기 계층에서의 위치 (A→F)

```text
F  생물 / 인지
E  막 / 경계 생물학
D  복잡 분자 / 자기조립
C  화학 / 결합
B  원자물리 / 양자역학  ← 이 엔진 (Quantum Shell)
A  전자기 / 정전기 경계  ← Electromagnetic_Boundary_Foundation (하위 층)
```

**흐름 정합성**: 고전 **쿨롱 경계·전위**는 A 층에서 다룬다. **전자가 붕괴하지 않고 준위·껍질 구조를 갖는 이유**는 B 층(이 패키지)에서 비고전적으로 스크리닝한다.  
A에서 B로의 점프를 README가 스스로 인정하고, B에서 C(화학 결합)로 가려면 **별도 foundation**이 필요하다.

---

## 레이어 구성 (5)

| 레이어 | 이름 | 물리 | 주요 출력 |
|--------|------|------|---------|
| **L1** | Hydrogenic spectrum | \(E_n = -R_\infty Z_\mathrm{eff}^2/n^2\) | 준위 (eV), 지상태, 보어 반경 |
| **L2** | Orbital basis | \(2(2\ell+1)\) 부분껍질 용량 | 부분껍질 목록, n까지 상태 수 |
| **L3** | Screening proxy | Slater식 근사 차폐 | \(Z_\mathrm{eff}\), 차폐 상수 |
| **L4** | Shell filling | Aufbau 순서 (Z≤118) | 전자 배치 문자열, 원자가 n, 폐곡선 판정 |
| **L5** | Ionization scale | 결합에너지·드브로이 파장 | IP proxy, 열에너지 대비, 길이 비 |

---

## 이것이 다루는 것 / 다루지 않는 것

### 다룸

- 비상대론 수소형 스펙트럼 (무한핵질량 리드버그)
- 오비탈 라벨 (s, p, d, f) 및 스핀 포함 퇴화도
- 단순 차폐·유효핵전하 (사용자 지정 또는 근사식)
- Aufbau 기반 전자 배치 (교과서 순서)
- 이온화 에너지·드브로이 길이의 **순서만** 비교 가능한 proxy

### 다루지 않음

| 영역 | 이유 |
|------|------|
| 상대론·세밀구조·람프 | QED / Dirac 필요 |
| 다전자 정확 스펙트럼 | Hartree–Fock, DFT 등 |
| 분자 오비탈·결합 | MO / 화학 foundation |
| 실제 분광 실험 피팅 | 데이터·장비 별도 |

---

## 하위 층과의 연결

- **`try_em_boundary_bridge()`** — 같은 `_staging` 안의 **Electromagnetic Boundary Foundation**이 있으면, 보어 반경 근처에서 고전 쿨롱 전위·전장 스냅샷을 가져와 맥락을 맞춘다.
- **EM → QM**: `em_boundary.try_quantum_shell_bridge(z_atomic=…)` — A 층에서 B 층으로의 **직접 브리지**.

---

## 사용 예

```python
from quantum_shell import (
    analyze, HydrogenicInput, ShellFillingInput,
    ScreeningInput, IonizationInput,
)

rep = analyze(
    hydrogenic_input=HydrogenicInput(z_effective=1.0, n_max=4),
    filling_input=ShellFillingInput(z_atomic=11),
    screening_input=ScreeningInput(z_atomic=11, inner_electrons=10),
    ionization_input=IonizationInput(z_effective=2.2, n_outer=3),
)
print(rep.omega_overall, rep.verdict.value)
```

---

## 테스트

```bash
pip install -e ".[dev]"
python3 -m pytest tests/ -q            # 10 passed
```

---

## 라이선스

MIT — [LICENSE](LICENSE)
