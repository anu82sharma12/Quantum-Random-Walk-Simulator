from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import numpy as np

class QuantumWalk:
    def __init__(self, n_qubits=10, steps=100):
        self.n = n_qubits
        self.steps = steps
        self.qc = QuantumCircuit(n_qubits)
        self.backend = AerSimulator(method='statevector')

    def coin(self):
        # Balanced coin: H on all qubits
        self.qc.h(range(self.n))

    def shift(self):
        # Shift operator using increment/decrement gates
        for q in range(self.n-1):
            self.qc.cx(q, q+1)
        self.qc.x(self.n-1)
        for q in reversed(range(self.n-1)):
            self.qc.cx(q, q+1)

    def build(self):
        self.qc.h(range(self.n))  # Initial Hadamard
        for _ in range(self.steps):
            self.coin()
            self.shift()
        self.qc.measure_all()

    def run(self):
        self.build()
        job = self.backend.run(transpile(self.qc, self.backend), shots=1)
        result = job.result()
        statevector = result.get_statevector()
        probs = np.abs(statevector)**2
        return probs / np.sum(probs)  # Normalize
