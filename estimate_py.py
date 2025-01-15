def estimate_pi(terms):
    result = 0.0
    sign = 1.0
    for n in range(terms):
        result += sign/(2.0*n+1.0)
        sign = -sign
    return 4*result

....

>>> estimate_pi(100)
3.1315929035585537
>>> estimate_pi(1000)
3.140592653839794
