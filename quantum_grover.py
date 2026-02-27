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

    # Measure
    circuit.append(cirq.measure(q0, q1, key='result'))

    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=1000)

    # Get most common result
    counts = result.histogram(key='result')
    most_common = max(counts, key=counts.get)

    # Convert binary to decimal
    found_value = int(format(most_common, '02b'), 2)

    print(f"Found target {found_value} in 1 iteration (quantum Grover search)")

if __name__ == "__main__":
    run_grover()
