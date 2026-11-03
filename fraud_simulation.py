"""Homework 3, Part 2 — Monte Carlo check of the fraud-detection posterior.

Simulates 100,000 transactions under the Part 1 assumptions and compares the
empirical P(Fraud | Flagged) with the value Bayes' theorem predicts.

    Sensitivity  P(Flagged | Fraud)      = 0.98
    Specificity  P(Not flagged | Legit)  = 0.95   ->  P(Flagged | Legit) = 0.05
    Base rate    P(Fraud)                = 0.001

    python3 fraud_simulation.py
"""
import numpy as np
import pandas as pd

# Step 1: random seed for reproducibility
np.random.seed(42)

# Step 2: 100,000 transactions
n_transactions = 100000

SENSITIVITY = 0.98      # P(Flagged | Fraud)
SPECIFICITY = 0.95      # P(Not flagged | Legitimate)
BASE_RATE = 0.001       # P(Fraud)

# Step 3: which transactions are fraudulent
is_fraud = np.random.rand(n_transactions) < BASE_RATE

# Step 4: apply the detection system.
# One uniform draw per transaction, compared against that transaction's own
# flagging probability — 0.98 for fraud, 1 - 0.95 = 0.05 for legitimate.
flagged = np.zeros(n_transactions, dtype=bool)
flag_draw = np.random.rand(n_transactions)
flag_prob = np.where(is_fraud, SENSITIVITY, 1 - SPECIFICITY)
flagged = flag_draw < flag_prob

# Step 5: empirical posterior
fraud_and_flagged = np.sum(is_fraud & flagged)
total_flagged = np.sum(flagged)
empirical_prob = fraud_and_flagged / total_flagged

theoretical_prob = (SENSITIVITY * BASE_RATE) / (
    SENSITIVITY * BASE_RATE + (1 - SPECIFICITY) * (1 - BASE_RATE))

print(f"Empirical   P(Fraud | Flagged) = {empirical_prob:.4f}")
print(f"Theoretical P(Fraud | Flagged) = {theoretical_prob:.4f}")
print(f"Absolute difference            = {abs(empirical_prob - theoretical_prob):.4f}")

# Step 6: confusion matrix (counts)
true_positive = int(np.sum(is_fraud & flagged))          # fraud and flagged
false_positive = int(np.sum(~is_fraud & flagged))        # legitimate but flagged
true_negative = int(np.sum(~is_fraud & ~flagged))        # legitimate and not flagged
false_negative = int(np.sum(is_fraud & ~flagged))        # fraud but not flagged

confusion = pd.DataFrame(
    [[true_positive, false_negative], [false_positive, true_negative]],
    index=["Actually fraud", "Actually legitimate"],
    columns=["Flagged", "Not flagged"])

print("\nConfusion matrix (counts out of 100,000):")
print(confusion.to_string())

# The three rates the matrix is there to show
print(f"\nFraudulent transactions simulated : {int(is_fraud.sum()):,}")
print(f"Total flagged                     : {int(total_flagged):,}")
print(f"Precision  TP/(TP+FP)             : {true_positive / (true_positive + false_positive):.4f}")
print(f"Recall     TP/(TP+FN)             : {true_positive / (true_positive + false_negative):.4f}")
print(f"Specificity TN/(TN+FP)            : {true_negative / (true_negative + false_positive):.4f}")

# Part 1(b): the same simulation with specificity raised to 0.99
np.random.seed(42)
is_fraud_b = np.random.rand(n_transactions) < BASE_RATE
flag_prob_b = np.where(is_fraud_b, SENSITIVITY, 1 - 0.99)
flagged_b = np.random.rand(n_transactions) < flag_prob_b
emp_b = np.sum(is_fraud_b & flagged_b) / np.sum(flagged_b)
theo_b = (SENSITIVITY * BASE_RATE) / (SENSITIVITY * BASE_RATE + 0.01 * (1 - BASE_RATE))
print(f"\nSpecificity 0.99 — empirical {emp_b:.4f}, theoretical {theo_b:.4f}")
print(f"False positives: {int(np.sum(~is_fraud & flagged)):,} -> "
      f"{int(np.sum(~is_fraud_b & flagged_b)):,}")
