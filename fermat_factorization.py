from sympy.ntheory.primetest import is_square
import math

def fermat_factorization(N_str):
    # Convert modulus N from hexadecimal string to integer
    N = int(N_str, 16)

    # Compute initial values
    a = math.isqrt(N)
    b_sq = a * a - N

    print("Trying values for a:")

    while not is_square(b_sq):
        print(f"Trying a = {a}")
        a += 1
        b_sq = a * a - N

    b = math.isqrt(b_sq)
    p_pred = a - b
    q_pred = a + b

    return p_pred, q_pred

if __name__ == "__main__":
    # Example modulus_N as string (replace with your actual modulus)
    modulus_N = "876af4c18470ebf7fec711836ba81ed20f23d143b20bd1e970ee3fd7e9297c703281d626f3cb35b42c7d7a442dbb0ad733d2f006888dd4918e6c1d587dd4c93459b8decb6bff6e596ef29986aad2618d92ab681e12df1dedc555e6c5364d92bb1cfbf6a17bb2030d3b725a336e75d10c3ba8c2f87d004190cf407d209a1f4023435e644ffe902b4ddc6547a108240b8e04bd74887b7c0d42e6b403aa35ae21b513bd905674fa9e86e49d2d6ce43bac619f43c3070f1067d8d98918360569c6ce111a8bf8aa816f3ce82308dea72dcbf693cd83a8a940ff375ec0beb15c743cdf31288e1ea0df453589de48d595eafb103568624e38f05dcfcd5b89f5e4df3"

    # Call the function with modulus_N as string
    p, q = fermat_factorization(modulus_N)
    print(f"p = {p}, q = {q}")
