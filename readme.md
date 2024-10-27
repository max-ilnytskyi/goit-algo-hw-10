## Monte Carlo Method results summary

task2 explores numerical integration using the Monte Carlo method, comparing it with the analytical solution for the definite integral of the function \( f(x) = x^2 \) over the interval [0, 2].

### Key Findings

- **Monte Carlo Integration Result:** Approx. 2.656 (using 10,000 random samples)
- **Analytical Integration Result:** 2.667 (computed using SciPy's `quad` function)
- **Error Estimation (Analytical):** ~2.96e-14

### Conclusion

The Monte Carlo method provides a reasonable approximation for integrals, particularly useful for more complex or high-dimensional functions. In this case, with a simple function like \( f(x) = x^2 \), the analytical method (e.g., using SciPy's `quad` function) is more accurate and efficient. 

The accuracy of the Monte Carlo method is influenced by the number of random samples:

- **Increased Sample Size:** Leads to a more accurate approximation, as it reduces the variance and brings the estimate closer to the true integral value.
- **Decreased Sample Size:** Results in less accuracy and higher variance, causing larger deviations from the analytical solution.

This trade-off between computational cost and accuracy is a key consideration when using the Monte Carlo method for integration.
