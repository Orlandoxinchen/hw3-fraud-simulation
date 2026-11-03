# Fraud detection simulation — Homework 3, Part 2

Monte Carlo check of the fraud-detection posterior from Part 1: simulate
100,000 transactions, measure P(Fraud | Flagged) empirically, and compare it
with the value Bayes' theorem predicts.

## Assumptions

| Quantity | Value |
|---|---|
| Sensitivity, P(Flagged \| Fraud) | 0.98 |
| Specificity, P(Not flagged \| Legitimate) | 0.95 |
| Base rate, P(Fraud) | 0.001 |
| Transactions simulated | 100,000 (seed 42) |

## Run it

```bash
pip install -r requirements.txt
python3 fraud_simulation.py
```

## Result

```
Empirical   P(Fraud | Flagged) = 0.0200
Theoretical P(Fraud | Flagged) = 0.0192
Absolute difference            = 0.0008

Confusion matrix (counts out of 100,000):
                     Flagged  Not flagged
Actually fraud           100            2
Actually legitimate     4892        95006
```

Precision 0.0200, recall 0.9804, specificity 0.9510.

## Why empirical and theoretical differ

The gap is sampling noise, and it is the size one should expect. The estimate
is a proportion over the 4,992 flagged transactions, so its standard error is

    SE = sqrt(p(1-p)/n_flagged) = sqrt(0.0192 x 0.9808 / 4992) = 0.00194

and the observed difference of 0.0008 is about 0.4 standard errors. The binding
constraint is not the 100,000 transactions but the 102 fraudulent ones among
them: with a base rate of 0.1%, almost none of the sample carries information
about the numerator.

## Raising specificity to 0.99

The script re-runs the same simulation with specificity 0.99:

```
Specificity 0.99 -- empirical 0.0931, theoretical 0.0893
False positives: 4,892 -> 974
```

An 80% reduction in false positives, achieved without catching any additional
fraud — but 91% of flags are still false alarms, so the output remains a triage
signal rather than a decision.
