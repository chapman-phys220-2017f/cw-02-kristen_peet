#!/bin/bash/ env python3         ### Should be #!/usr/bin/env python3


def compute_sum(tol):
    k = 1
    conv_sum = 0
    term = (1/k**2)
    while tol < term:
        term = (1/k**2)
        conv_sum += term
        k += 1
        return conv_sum          ### This return breaks the while loop immediately
                                 ### It should be unindented to be outside the while loop

if __name__=="__main__":
    convergence = compute_sum(tol=1e-2)
    print("If tol is 1e-2, sum converges at", convergence)
    smaller_tol = (compute_sum(tol=1e-10))
    print("If tol is 1e-10, sum converges at", smaller_tol)























