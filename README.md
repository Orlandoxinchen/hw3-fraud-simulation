# Homework 3

Part 1 is worked below in full. Part 2 is the simulation in
[`fraud_simulation.py`](fraud_simulation.py); its code, output and discussion
are at the end of this page.

---

## Part 1. Analytical Problems

### Question 1. Bayes' theorem — fraud detection

Write $F$ for "the transaction is fraudulent" and $G$ for "the transaction is
flagged". The three given quantities are

$$
P(G \mid F) = 0.98 \quad \text{(sensitivity)}, \qquad
P(\bar G \mid \bar F) = 0.95 \quad \text{(specificity)}, \qquad
P(F) = 0.001 \quad \text{(base rate)} .
$$

Two quantities follow immediately and are the ones actually needed:

$$
P(\bar F) = 1 - 0.001 = 0.999, \qquad
P(G \mid \bar F) = 1 - P(\bar G \mid \bar F) = 1 - 0.95 = 0.05 .
$$

#### (a) Find $P(F \mid G)$

Bayes' theorem, with the denominator expanded by the law of total probability:

$$
P(F \mid G) = \frac{P(G \mid F)\,P(F)}{P(G)}, \qquad
P(G) = P(G \mid F)P(F) + P(G \mid \bar F)P(\bar F) .
$$

Step by step:

1. Numerator — flagged *and* fraudulent:

$$P(G \mid F)\,P(F) = 0.98 \times 0.001 = 0.00098$$

2. Second term of the denominator — flagged *and* legitimate:

$$P(G \mid \bar F)\,P(\bar F) = 0.05 \times 0.999 = 0.04995$$

3. Denominator — flagged, either way:

$$P(G) = 0.00098 + 0.04995 = 0.05093$$

4. Divide:

$$P(F \mid G) = \frac{0.00098}{0.05093} = \frac{98}{5093} = 0.019242\ldots$$

> **Answer (a).** $P(F \mid G) = \dfrac{98}{5093} \approx 0.0192$, i.e. about
> **1.92%**. Fewer than 1 in 50 flagged transactions is actually fraud.

The result is counter-intuitive until one counts cases. Out of a million
transactions, 1,000 are fraudulent and 980 of those are caught, while 999,000
are legitimate and 5% of them — 49,950 — are flagged anyway. False alarms
outnumber true ones more than fifty to one, because the base rate is so small
that a 5% error on the huge legitimate group swamps a 98% success rate on the
tiny fraudulent one.

| Per 1,000,000 transactions | Flagged | Not flagged | Total |
|---|---:|---:|---:|
| Fraudulent | 980 | 20 | 1,000 |
| Legitimate | 49,950 | 949,050 | 999,000 |
| **Total** | **50,930** | **949,070** | **1,000,000** |

#### (b) Specificity raised to 0.99

Now $P(G \mid \bar F) = 1 - 0.99 = 0.01$. The numerator is unchanged —
sensitivity and the base rate have not moved — so only the denominator changes:

$$P(G) = 0.00098 + 0.01 \times 0.999 = 0.00098 + 0.00999 = 0.01097$$

$$P(F \mid G) = \frac{0.00098}{0.01097} = \frac{98}{1097} = 0.089335\ldots$$

> **Answer (b).** $P(F \mid G) = \dfrac{98}{1097} \approx 0.0893$, i.e.
> **8.93%** — up from 1.92%, a **4.6-fold** improvement, achieved without
> catching a single additional fraud.

**Business implication.** Raising specificity from 0.95 to 0.99 cuts false
positives per million transactions from 49,950 to 9,990, a reduction of about
80%. Three consequences follow.

1. **Review cost falls roughly fivefold.** If each flagged transaction costs
   something to investigate, the bill is proportional to the number of flags,
   which drops from 50,930 to 10,970 per million.
2. **Customer friction falls.** Roughly 40,000 fewer legitimate customers per
   million have a payment held or declined, which is where the real revenue
   damage from a fraud system usually sits.
3. **But 91% of flags are still false alarms.** A precision of 8.93% is still
   far too low for automatic blocking; the output remains a triage signal for
   human or secondary review, not a decision. Note also that specificity says
   nothing about missed fraud: 2% of fraudulent transactions still get through
   in both scenarios, so this change improves precision only, not recall.

---

### Question 2. Two discrete random variables

| Stock A $(X)$ | $-2\%$ | $0\%$ | $3\%$ | $5\%$ |
|---|---:|---:|---:|---:|
| $P(X)$ | 0.1 | 0.3 | 0.4 | 0.2 |

| Stock B $(Y)$ | $3\%$ | $1\%$ | $4\%$ |
|---|---:|---:|---:|
| $P(Y)$ | 0.2 | 0.5 | 0.3 |

#### (a) Expected values

$E[X] = \sum_i x_i p_i$:

$$E[X] = (-2)(0.1) + (0)(0.3) + (3)(0.4) + (5)(0.2) = -0.2 + 0 + 1.2 + 1.0 = \mathbf{2.0\%}$$

$$E[Y] = (3)(0.2) + (1)(0.5) + (4)(0.3) = 0.6 + 0.5 + 1.2 = \mathbf{2.3\%}$$

#### (b) Variances by the shortcut formula

First the second moments $E[X^2] = \sum_i x_i^2 p_i$:

| $x$ | $p$ | $xp$ | $x^2 p$ | | $y$ | $p$ | $yp$ | $y^2 p$ |
|---:|---:|---:|---:|---|---:|---:|---:|---:|
| $-2$ | 0.1 | $-0.2$ | 0.4 | | 3 | 0.2 | 0.6 | 1.8 |
| 0 | 0.3 | 0.0 | 0.0 | | 1 | 0.5 | 0.5 | 0.5 |
| 3 | 0.4 | 1.2 | 3.6 | | 4 | 0.3 | 1.2 | 4.8 |
| 5 | 0.2 | 1.0 | 5.0 | | | | | |
| | **1.0** | **2.0** | **9.0** | | | **1.0** | **2.3** | **7.1** |

$$\mathrm{Var}(X) = E[X^2] - (E[X])^2 = 9.0 - (2.0)^2 = 9.0 - 4.0 = \mathbf{5.0}, \qquad \sigma_X = \sqrt{5.0} = 2.236\%$$

$$\mathrm{Var}(Y) = E[Y^2] - (E[Y])^2 = 7.1 - (2.3)^2 = 7.1 - 5.29 = \mathbf{1.81}, \qquad \sigma_Y = \sqrt{1.81} = 1.345\%$$

Units are percent-squared, since the returns are in percent.

#### (c) The portfolio $R = 0.6X + 0.4Y$

Expectation is linear, and needs no independence assumption:

$$E[R] = 0.6\,E[X] + 0.4\,E[Y] = 0.6(2.0) + 0.4(2.3) = 1.2 + 0.92 = \mathbf{2.12\%}$$

Variance is not linear. In general

$$\mathrm{Var}(aX + bY) = a^2\mathrm{Var}(X) + b^2\mathrm{Var}(Y) + 2ab\,\mathrm{Cov}(X,Y),$$

and here $X$ and $Y$ are independent, so $\mathrm{Cov}(X,Y) = 0$ and the last
term drops:

$$\mathrm{Var}(R) = 0.6^2(5.0) + 0.4^2(1.81) = 0.36(5.0) + 0.16(1.81) = 1.8 + 0.2896 = \mathbf{2.0896}$$

$$\sigma_R = \sqrt{2.0896} = 1.446\%$$

> **Answer (c).** $E[R] = 2.12\%$, $\mathrm{Var}(R) = 2.0896$,
> $\sigma_R = 1.446\%$. Note the point of diversification: the portfolio's
> standard deviation (1.446%) is below Stock A's (2.236%) *and* below the
> weighted average of the two standard deviations
> ($0.6 \times 2.236 + 0.4 \times 1.345 = 1.880\%$), because the two risks are
> independent and partly cancel.

---

### Question 3. A continuous distribution

$$
f(x) = \begin{cases} \tfrac{3}{8}x^2, & 0 \le x \le 2 \\ 0, & \text{otherwise} \end{cases}
$$

#### (a) Is it a valid PDF?

Two conditions must hold.

1. **Non-negativity.** $\tfrac{3}{8}x^2 \ge 0$ for every $x$, since $x^2 \ge 0$
   and $\tfrac{3}{8} > 0$. ✓
2. **Integrates to one.**

$$\int_{-\infty}^{\infty} f(x)\,dx = \int_0^2 \frac{3}{8}x^2\,dx = \frac{3}{8}\left[\frac{x^3}{3}\right]_0^2 = \frac{1}{8}\Big[x^3\Big]_0^2 = \frac{8}{8} = 1 \quad ✓$$

> **Answer (a).** Both conditions hold, so $f$ is a valid probability density
> function.

#### (b) The CDF

For $0 \le x \le 2$,

$$F(x) = P(X \le x) = \int_0^x \frac{3}{8}t^2\,dt = \frac{3}{8}\left[\frac{t^3}{3}\right]_0^x = \frac{x^3}{8}$$

> **Answer (b).**
>
> $$F(x) = \begin{cases} 0, & x < 0 \\ \dfrac{x^3}{8}, & 0 \le x \le 2 \\ 1, & x > 2 \end{cases}$$
>
> A check: $F(0) = 0$ and $F(2) = 8/8 = 1$, as a CDF requires.

#### (c) Three probabilities

With the CDF in hand these are subtractions rather than integrals.

$$P(X \le 1) = F(1) = \frac{1^3}{8} = \frac{1}{8} = \mathbf{0.125}$$

$$P(0.5 \le X \le 1.5) = F(1.5) - F(0.5) = \frac{3.375}{8} - \frac{0.125}{8} = \frac{3.25}{8} = \frac{13}{32} = \mathbf{0.40625}$$

$$P(X > 1.5) = 1 - F(1.5) = 1 - \frac{3.375}{8} = 1 - 0.421875 = \frac{37}{64} = \mathbf{0.578125}$$

For a continuous variable the endpoints carry no probability, so $\le$ and $<$
are interchangeable throughout.

---

### Question 4. Binomial versus hypergeometric

#### (a) Binomial

Ten users see the ad independently, each clicking with probability 0.2, so
$X \sim \mathrm{Binomial}(n = 10,\, p = 0.2)$ and

$$P(X = k) = \binom{n}{k}p^k(1-p)^{n-k} .$$

With $k = 3$:

$$P(X = 3) = \binom{10}{3}(0.2)^3(0.8)^7 = 120 \times 0.008 \times 0.2097152 = \mathbf{0.2013}$$

where $\binom{10}{3} = \dfrac{10!}{3!\,7!} = 120$, $(0.2)^3 = 0.008$ and
$(0.8)^7 = 0.2097152$.

#### (b) Hypergeometric

Here the five products are drawn **without replacement** from a finite batch, so
the draws are not independent and the binomial does not apply. With $N = 20$
products, $K = 4$ defective and $n = 5$ drawn,
$Y \sim \mathrm{Hypergeometric}(N, K, n)$ and

$$P(Y = k) = \frac{\binom{K}{k}\binom{N-K}{n-k}}{\binom{N}{n}} .$$

With $k = 1$:

$$P(Y = 1) = \frac{\binom{4}{1}\binom{16}{4}}{\binom{20}{5}} = \frac{4 \times 1820}{15504} = \frac{7280}{15504} = \frac{455}{969} = \mathbf{0.4696}$$

**Why the two models differ.** Both count "successes in $n$ trials", but the
binomial assumes the success probability stays fixed, which requires
replacement or an effectively infinite population. Drawing 5 from 20 removes a
quarter of the batch, so each draw changes the composition of what is left:
after pulling one defective, the chance the next is defective falls from
$4/20$ to $3/19$. The binomial approximation
$\binom{5}{1}(0.2)^1(0.8)^4 = 0.4096$ is noticeably below the exact 0.4696 for
exactly that reason; it would be adequate only if the batch were large relative
to the sample.

---

## Part 2. Coding Problem

Monte Carlo check of the Question 1 posterior: simulate 100,000 transactions,
measure $P(F \mid G)$ empirically, and compare it with Bayes' theorem.

### Assumptions

| Quantity | Value |
|---|---|
| Sensitivity, $P(\text{Flagged} \mid \text{Fraud})$ | 0.98 |
| Specificity, $P(\text{Not flagged} \mid \text{Legitimate})$ | 0.95 |
| Base rate, $P(\text{Fraud})$ | 0.001 |
| Transactions simulated | 100,000 (seed 42) |

### Run it

```bash
pip install -r requirements.txt
python3 fraud_simulation.py
```

### The code

Full file: [`fraud_simulation.py`](fraud_simulation.py)

```python
import numpy as np
import pandas as pd

# Step 1: random seed for reproducibility
np.random.seed(42)

# Step 2: 100,000 transactions
n_transactions = 100000

SENSITIVITY = 0.98      # P(Flagged | Fraud)
SPECIFICITY = 0.95      # P(Not flagged | Legitimate)
BASE_RATE   = 0.001     # P(Fraud)

# Step 3: which transactions are fraudulent
is_fraud = np.random.rand(n_transactions) < BASE_RATE

# Step 4: apply the detection system.
# One uniform draw per transaction, compared against that transaction's own
# flagging probability -- 0.98 for fraud, 1 - 0.95 = 0.05 for legitimate.
flagged   = np.zeros(n_transactions, dtype=bool)
flag_draw = np.random.rand(n_transactions)
flag_prob = np.where(is_fraud, SENSITIVITY, 1 - SPECIFICITY)
flagged   = flag_draw < flag_prob

# Step 5: empirical posterior
fraud_and_flagged = np.sum(is_fraud & flagged)
total_flagged     = np.sum(flagged)
empirical_prob    = fraud_and_flagged / total_flagged

theoretical_prob = (SENSITIVITY * BASE_RATE) / (
    SENSITIVITY * BASE_RATE + (1 - SPECIFICITY) * (1 - BASE_RATE))

print(f"Empirical   P(Fraud | Flagged) = {empirical_prob:.4f}")
print(f"Theoretical P(Fraud | Flagged) = {theoretical_prob:.4f}")

# Step 6: confusion matrix (counts)
true_positive  = int(np.sum( is_fraud &  flagged))   # fraud and flagged
false_positive = int(np.sum(~is_fraud &  flagged))   # legitimate but flagged
true_negative  = int(np.sum(~is_fraud & ~flagged))   # legitimate, not flagged
false_negative = int(np.sum( is_fraud & ~flagged))   # fraud but not flagged

confusion = pd.DataFrame(
    [[true_positive, false_negative], [false_positive, true_negative]],
    index=["Actually fraud", "Actually legitimate"],
    columns=["Flagged", "Not flagged"])
print(confusion.to_string())
```

### Output

```
Empirical   P(Fraud | Flagged) = 0.0200
Theoretical P(Fraud | Flagged) = 0.0192
Absolute difference            = 0.0008

Confusion matrix (counts out of 100,000):
                     Flagged  Not flagged
Actually fraud           100            2
Actually legitimate     4892        95006

Fraudulent transactions simulated : 102
Total flagged                     : 4,992
Precision  TP/(TP+FP)             : 0.0200
Recall     TP/(TP+FN)             : 0.9804
Specificity TN/(TN+FP)            : 0.9510

Specificity 0.99 -- empirical 0.0931, theoretical 0.0893
False positives: 4,892 -> 974
```

### Discussion

**The simulation agrees with Question 1(a).** The empirical posterior is 0.0200
against the theoretical 0.0192, a difference of 0.0008. That gap is sampling
noise, and it is the size one should expect: the estimate is a proportion
computed from the 4,992 flagged transactions, so its standard error is

$$\mathrm{SE} = \sqrt{\frac{p(1-p)}{n_{\text{flagged}}}} = \sqrt{\frac{0.0192 \times 0.9808}{4992}} = 0.00194,$$

and the observed discrepancy is $0.0008 / 0.00194 \approx 0.4$ standard errors —
well inside ordinary variation. The binding constraint is not the 100,000
transactions but the **102** fraudulent ones among them; with a base rate of
0.1%, almost all of the sample carries no information about the numerator.

**The confusion matrix shows the same story as the table in 1(a).** Of 4,992
flags, only 100 are real fraud and 4,892 are false alarms. Recall is excellent
(0.9804, essentially the 0.98 sensitivity) and specificity comes out at 0.9510,
matching the assumed 0.95 — the model is behaving exactly as specified.
Precision is nevertheless 2%. A classifier can be simultaneously accurate on
both of its conditional error rates and nearly useless as a standalone decision
rule, whenever the event it looks for is rare.

**Raising specificity.** Re-running with specificity 0.99 gives an empirical
0.0931 against the theoretical 0.0893, and false positives fall from 4,892 to
974 — the 80% reduction predicted in 1(b).
