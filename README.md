# Classical-vs-Quantum-Search-Grover-s-Algorithm-in-Cirq
Classical vs Quantum Search
This project compares: 
  A classical linear search in Python
  Grover’s quantum search algorithm implemented using Cirq
The goal is to demonstrate the quadratic speedup of quantum search:
O(N) → O(√N)

​# Problem Setup
We search for a hidden number in a list of four elements: 
[0, 1, 2, 3]
The target value is <2>.

Classical Approach
- Checks elements sequentially
- Worst-case complexity: O(N)
- Deterministic

Quantum Approach (Grover’s Algorithm)
- Creates superposition over all states
- Uses an oracle to flip the phase of the marked state
- Applies amplitude amplification (diffusion)
- Achieves quadratic speedup: O(√N)

#Results
Classical search requires up to 4 checks.
Grover's algorithm finds the correct state with high probability after one iteration for N=4.

#How to Run
pip install -r requirements.txt
python classical_search.py
python quantum_grover.py

#Why This Matters
Grover’s algorithm demonstrates a fundamental quantum advantage for unstructured search problems. While small examples don’t show practical gains, the asymptotic speedup becomes significant for large N.
