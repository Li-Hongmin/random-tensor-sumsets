# Supplement: Concentration of Random Tensor Sumsets

`check_lemmas.py` (Python 3, standard library only; about one second):

- exact rational enumeration on 1310 small instances (subsets X of {0,1,2}^d, d <= 2, |X| <= 4, nonuniform rational inclusion probabilities including 0 and 1, dilates k in {1,2,-1,-2,3}) of the Key Lemma: the deletion bounds sum_x D_x <= 2Z and D_x <= 2|A|, the covariance bound E[|A|Z] <= (lambda+2)mu, and Var Z <= 4E[|A|Z] <= 4(lambda+2)mu;
- on the 680 instances with |X| <= 3, the Bernoulli Efron–Stein identity E[(Z - E_x Z)^2] = p_x(1-p_x) E[Delta_x^2] for every coordinate and the bound Var Z <= sum_x p_x(1-p_x) E[Delta_x^2];
- b > a (Step 1 of Theorem 1) on random fractional sets of mass greater than one (grid minimization, floating point);
- the values in Example 2, the limit in Remark 3, the k = 0 example of Proposition 7;
- failure of Question 46(1) of Cutler–Pebody–Sarkar on random fractional sets of mass below one.

Expected output: a single line beginning `OK:`. These are numerical sanity checks on small cases, not proofs; the theorem itself rests on the written argument.
