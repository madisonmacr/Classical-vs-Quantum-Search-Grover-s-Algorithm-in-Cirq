import cirq

def run_grover():
    q0, q1 = cirq.LineQubit.range(2)
    circuit = cirq.Circuit()

    # Superposition
    circuit.append([cirq.H(q0), cirq.H(q1)])

    # Oracle for |10>
    circuit.append(cirq.X(q1))
    circuit.append(cirq.CZ(q0, q1))
    circuit.append(cirq.X(q1))

    # Diffusion operator
    circuit.append([cirq.H(q0), cirq.H(q1)])
    circuit.append([cirq.X(q0), cirq.X(q1)])
    circuit.append(cirq.H(q1))
    circuit.append(cirq.CNOT(q0, q1))
    circuit.append(cirq.H(q1))
    circuit.append([cirq.X(q0), cirq.X(q1)])
    circuit.append([cirq.H(q0), cirq.H(q1)])

    # Measurement
    circuit.append(cirq.measure(q0, q1, key='result'))

    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=1000)

    counts = result.histogram(key='result')
    outcomes = {format(k, '02b'): v for k, v in counts.items()}

    print("Quantum Results:", outcomes)

if __name__ == "__main__":
    run_grover()
