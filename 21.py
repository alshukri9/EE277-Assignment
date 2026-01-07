def bayesian_diagnosis(prior, sensitivity, specificity):
    """
    Calculates posterior probability using Bayes' Theorem.
    
    prior: P(D) - Probability of disease in population
    sensitivity: P(+|D) - True positive rate
    specificity: P(-|not D) - True negative rate
    """
    # 1. Probability of NOT having the disease
    prior_no_disease = 1 - prior
    
    # 2. False Positive Rate: P(+|not D)
    false_positive_rate = 1 - specificity
    
    # 3. Total Probability of Testing Positive: P(+)
    # P(+) = [P(+|D) * P(D)] + [P(+|not D) * P(not D)]
    prob_positive_test = (sensitivity * prior) + (false_positive_rate * prior_no_disease)
    
    # 4. Posterior Probability: P(D|+)
    posterior_positive = (sensitivity * prior) / prob_positive_test
    
    # 5. Probability of testing negative: P(-)
    prob_negative_test = 1 - prob_positive_test
    
    # 6. Posterior Probability: P(D|-) 
    # (Probability you have the disease even if you test negative)
    false_negative_rate = 1 - sensitivity
    posterior_negative = (false_negative_rate * prior) / prob_negative_test
    
    return posterior_positive, posterior_negative

# Scenario Parameters
disease_prevalence = 0.01   # 1% of the population has the disease
test_sensitivity = 0.95     # 95% chance to catch the disease
test_specificity = 0.90     # 90% chance to correctly identify a healthy person

pos, neg = bayesian_diagnosis(disease_prevalence, test_sensitivity, test_specificity)

print(f"--- Medical Diagnosis Report ---")
print(f"Prior Probability (Prevalence): {disease_prevalence:.2%}")
print(f"Posterior P(Disease | Positive Test): {pos:.2%}")
print(f"Posterior P(Disease | Negative Test): {neg:.2%}")