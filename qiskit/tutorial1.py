from qiskit import QuantumCircuit, assemble, Aer
from qiskit.visualization import plot_histogram

from qiskit_textbook.widgets import binary_widget
binary_widget(nbits=5)
qc_output = QuantumCircuit(8)

qc_output.measure_all()
qc_output.draw(initial_state=True) 
sim = Aer.get_backend('aer_simulator') 
result = sim.run(qc_output).result()
counts = result.get_counts()
plot_histogram(counts)
