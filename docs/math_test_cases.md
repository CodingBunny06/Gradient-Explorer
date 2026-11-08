
# Mathematical Test Cases

## Gradient Explorer

**Purpose:** Define the expected mathematical results used to verify the gradient calculation engine.

These test cases cover partial derivatives, gradient vectors, gradient magnitude, unit gradient vectors and special cases.

---

## 1. Core Mathematical Test Cases

| ID | Function f(x,y) | Evaluation Point (x,y) | Expected Gradient |
|---|---|---|---|
| M01 | x² + y² | (1, 2) | (2, 4) |
| M02 | 3x + 4y | (1, 1) | (3, 4) |
| M03 | xy | (3, 2) | (2, 3) |
| M04 | x² - y² | (2, 1) | (4, -2) |
| M05 | x² + y² | (0, 0) | (0, 0) |

## 2. Expected Partial Derivatives

| ID | ∂f/∂x | ∂f/∂y |
|---|---|---|
| M01 | 2x | 2y |
| M02 | 3 | 4 |
| M03 | y | x |
| M04 | 2x | -2y |
| M05 | 2x | 2y |

## 3. Expected Gradient Magnitudes

The magnitude of a gradient vector is:

|∇f| = √((∂f/∂x)² + (∂f/∂y)²)

| ID | Expected Magnitude |
|---|---|
| M01 | √20 ≈ 4.4721 |
| M02 | 5 |
| M03 | √13 ≈ 3.6056 |
| M04 | √20 ≈ 4.4721 |
| M05 | 0 |

## 4. Expected Unit Gradient Vectors

The unit gradient vector is obtained by dividing the gradient by its magnitude.

| ID | Expected Unit Gradient |
|---|---|
| M01 | (1/√5, 2/√5) |
| M02 | (3/5, 4/5) |
| M03 | (2/√13, 3/√13) |
| M04 | (2/√5, -1/√5) |
| M05 | Undefined (zero gradient) |

A zero gradient has no defined unit gradient vector because division by zero is undefined.

## 5. Edge Cases

| ID | Scenario | Expected Behaviour |
|---|---|---|
| E01 | Zero gradient | Magnitude is zero; unit vector is undefined |
| E02 | Negative coordinates | Derivatives and numerical values are calculated correctly |
| E03 | Fractional coordinates | Numerical evaluation is supported |
| E04 | 1/x evaluated at x = 0 | Undefined result is reported |
| E05 | log(x) evaluated at x = -1 | Non-real result is reported |
| E06 | Large valid coordinates | Results retain sufficient numerical precision |

## 6. Acceptance Criteria

The gradient calculation engine should satisfy the following:

1. Calculate both partial derivatives correctly.
2. Evaluate gradient components at the selected coordinates.
3. Calculate gradient magnitude correctly.
4. Calculate a unit gradient vector when the gradient is non-zero.
5. Handle zero gradients without division by zero.
6. Detect undefined and non-real numerical results.
7. Preserve sufficient precision in numerical calculations.

## 7. Scope

These test cases define the mathematical expectations for the Gradient Explorer calculation engine.

They serve as a reference for implementation, unit testing and verification.
