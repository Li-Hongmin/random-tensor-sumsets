"""Exact rational checks of the finite statements in 'Concentration of random
tensor sumsets' on small instances. These are numerical sanity checks, not proofs."""
from fractions import Fraction as F
from itertools import product, combinations
import math, random

def subsets_with_prob(X, q):
    for bits in product((0, 1), repeat=len(X)):
        p = F(1)
        for b, x in zip(bits, X):
            p *= q[x] if b else 1 - q[x]
        yield frozenset(x for b, x in zip(bits, X) if b), p

def img(A, k):
    return {tuple(r + k * t for r, t in zip(a, b)) for a in A for b in A}

def check_key_lemma(X, q, k):
    lam = sum(q.values()); mu = E2 = EAZ = F(0)
    for A, w in subsets_with_prob(X, q):
        z = len(img(A, k))
        mu += w * z; E2 += w * z * z; EAZ += w * len(A) * z
        D = [z - len(img(A - {x}, k)) for x in A]
        assert sum(D) <= 2 * z and all(0 <= d <= 2 * len(A) for d in D)
        assert sum(d * d for d in D) <= 4 * len(A) * z
    var = E2 - mu * mu
    assert EAZ <= (lam + 2) * mu, (X, q, k)          # covariance bound
    assert var <= 4 * EAZ <= 4 * (lam + 2) * mu, (X, q, k)

def check_efron_stein(X, q, k):
    """Bernoulli Efron-Stein form: E[(Z-E_xZ)^2] = p(1-p)E[Delta^2], Var Z <= sum."""
    ps = [q[x] for x in X]
    val = {}; w = {}
    for bits in product((0, 1), repeat=len(X)):
        pr = F(1)
        for b, pi in zip(bits, ps): pr *= pi if b else 1 - pi
        w[bits] = pr; val[bits] = len(img([x for x, b in zip(X, bits) if b], k))
    mean = sum(w[b] * val[b] for b in w)
    var = sum(w[b] * (val[b] - mean) ** 2 for b in w)
    total = F(0)
    for i, pi in enumerate(ps):
        lhs = rhs = F(0)
        for b in w:
            b1 = b[:i] + (1,) + b[i+1:]; b0 = b[:i] + (0,) + b[i+1:]
            Ei = pi * val[b1] + (1 - pi) * val[b0]; delta = val[b1] - val[b0]
            lhs += w[b] * (val[b] - Ei) ** 2; rhs += w[b] * pi * (1 - pi) * delta ** 2
        assert lhs == rhs; total += rhs
    assert var <= total

def conv(a, b, k):
    out = {}
    for u, x in a.items():
        for v, y in b.items():
            out[u + k * v] = out.get(u + k * v, 0) + x * y
    return out

def size(g, grid=4000):  # min over p in [0,1] of sum g^p (float, grid + endpoints)
    vals = [float(v) for v in g.values() if v > 0]
    return min(sum(v ** (j / grid) for v in vals) for j in range(grid + 1))

random.seed(1)
probs = [F(0), F(1), F(1, 2), F(1, 3), F(2, 3), F(3, 4), F(1, 5)]
n_inst = n_es = 0
for dim in (1, 2):
    pts = list(product(range(3), repeat=dim))
    for sz in (1, 2, 3, 4):
        for X in combinations(pts, sz):
            for k in (1, 2, -1, -2, 3):
                q = {x: random.choice(probs) for x in X}
                check_key_lemma(list(X), q, k); n_inst += 1
                if sz <= 3:
                    check_efron_stein(list(X), q, k); n_es += 1
# Step 1: b > a on random fractional sets of mass > 1 (lower bound a^{p+1} on a grid, plus p=0)
n_ba = 0
for _ in range(300):
    al = {i: F(random.randint(1, 100), 100) for i in random.sample(range(-5, 6), random.randint(2, 5))}
    a = sum(al.values())
    if a <= 1: continue
    k = random.choice([1, 2, 3, -1, -2])
    assert size(conv(al, al, k)) > float(a); n_ba += 1
# Example 2
r = F(49, 64); al = {0: F(7, 8), 1: F(7, 8)}
assert sorted(conv(al, al, 1).values()) == [r, r, 2 * r]
assert 2 * r ** 3 == F(235298, 262144) < 1 and 2 * r ** 2 == F(4802, 4096) > 1
ps = math.log2(-2 * math.log(r) / math.log(2 * r)); b = float(r) ** ps * (2 + 2 ** ps)
assert abs(ps - 0.32604) < 1e-5 and abs(b - 2.98225) < 1e-5 and b < 3 and abs(size(conv(al, al, 1), 100000) - b) < 1e-6
# Remark 3: (1-2^-n)^(2^n) -> e^-1
assert abs((1 - 2.0 ** -30) ** (2 ** 30) - math.exp(-1)) < 1e-6
# Proposition 7 (k = 0 boundary)
a7 = {0: F(3, 5), 1: F(3, 5)}
assert sum(a7.values()) == F(6, 5) and sum(conv(a7, a7, 0).values()) == F(36, 25) and max(conv(a7, a7, 0).values()) <= 1
# Question 46(1) fails below mass one
for _ in range(200):
    a = {i: F(random.randint(1, 30), 100) for i in random.sample(range(-4, 5), random.randint(1, 3))}
    m = sum(a.values())
    if not (0 < m < 1): continue
    s, d = sum(conv(a, a, 1).values()), sum(conv(a, a, 2).values())
    assert s == d == m * m and m * d > s * s
print(f"OK: {n_inst} exact instances of the Key Lemma (deletion, covariance, variance bounds); {n_es} exact Bernoulli Efron-Stein instances; b>a on {n_ba} random fractional sets; Example 2; Remark 3; Proposition 7; Q46(1) mass<1 failures")
