#!/usr/bin/env python

from numpy import angle, linspace, newaxis, pi, savetxt
import argparse

def newton(function, derivative, initial_estimate, num_iters=10):
    '''Solves the equation `function`(x) == 0 using the Newton&ndash;Raphson
    method with `num_iters` iterations, starting from `initial_estimate`.
    `derivative` is the derivative of `function` with respect to x.'''

    current_estimate = initial_estimate
    for _ in range(num_iters):
        current_estimate = (
            current_estimate
            - function(current_estimate) / derivative(current_estimate)
        )
    return current_estimate


def complex_linspace(lower, upper, num_real, num_imag):
    real_space = linspace(lower.real, upper.real, num_real)
    imag_space = linspace(lower.imag, upper.imag, num_imag) * 1J
    return real_space + imag_space[:, newaxis]

def main(args):
    z_min = -1 - 1J
    z_max = 1 + 1J
    initial_z = complex_linspace(z_min, z_max, 1000, 1000)

    results = angle(newton(polynomial, derivative, initial_z, 20))
    savetxt(args.outfile, results)

def poly_func(order):
    def poly(x): return x**order - 1
    def derivative(x): return order * x**(order - 1)
    return poly, derivative

if __name__=='__main__':
    parser = argparse.ArgumentParser(description=(
	"Solves the equation ```f(z) = 0``` using Newton-Raphson"))
    parser.add_argument('order', type=int, default=3,
                        help='Order of the polynomial')
    parser.add_argument('outfile', type=str,
                        default='data.dat', help='Output file')

    args = parser.parse_args()
    polynomial, derivative = poly_func(args.order)
    main(args)

