import numpy as np
import time
from payoff import european_call

def classical_walk(paths=1000000, steps=100, S0=100, K=105):
    np.random.seed(42)
    dt = 1.0 / steps
    nudt = (0.01) * dt
    sigdt = 0.02 * np.sqrt(dt)
    start = time.time()
    Z = np.random.normal(0, 1, (paths, steps))
    delta_S = nudt + sigdt * Z
    S = S0 * np.exp(np.cumsum(delta_S, axis=1))
    S = np.concatenate([np.full((paths,1), S0), S], axis=1)
    payoffs = european_call(S[:,-1], K)
    price = np.mean(payoffs)
    duration = time.time() - start
    print(f"Classical: ${price:.2f} in {duration:.1f} sec")

if __name__ == "__main__":
    classical_walk()
