import matplotlib.pyplot as plt
import numpy as np

# Generate data for exponential growth chart (number of qubits vs. number of states)
n_qubits = np.arange(1, 11)
n_states = 2 ** n_qubits

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(n_qubits, n_states, marker='o', linestyle='-', color='royalblue')
plt.title('Exponential Growth of Quantum States with Number of Qubits')
plt.xlabel('Number of Qubits (n)')
plt.ylabel('Number of Basis States (2^n)')
plt.grid(True)
plt.xticks(n_qubits)
plt.yscale('log')  # Optional: logarithmic scale to show rapid growth clearly
plt.tight_layout()

plt.show()
