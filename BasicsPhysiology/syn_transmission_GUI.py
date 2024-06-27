import sys
import os
import numpy as np
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QSlider, QLabel
from PyQt6.QtCore import Qt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

# Create QApplication instance first
app = QApplication(sys.argv)

# Now set the library path
plugin_path = os.path.join(os.path.dirname(sys.executable), 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

class SynapticTransmissionGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Synaptic Transmission Simulator (EPSPs)")
        self.setGeometry(100, 100, 1000, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)

        # Left side: controls
        control_layout = QVBoxLayout()
        main_layout.addLayout(control_layout)

        # EPSP Amplitude slider
        self.amplitude_slider = self.create_slider("EPSP Amplitude", 1, 100, 50)
        control_layout.addWidget(self.amplitude_slider)

        # Presynaptic Engagement slider
        self.frequency_slider = self.create_slider("Presynaptic Engagement (Hz)", 1, 20, 7)
        control_layout.addWidget(self.frequency_slider)

        # Right side: plots
        plot_layout = QVBoxLayout()
        main_layout.addLayout(plot_layout)

        # EPSP plot
        self.epsp_figure, self.epsp_ax = plt.subplots(figsize=(6, 4))
        self.epsp_canvas = FigureCanvas(self.epsp_figure)
        plot_layout.addWidget(self.epsp_canvas)

        # Circuit diagram plot
        self.circuit_figure, self.circuit_ax = plt.subplots(figsize=(6, 4))
        self.circuit_canvas = FigureCanvas(self.circuit_figure)
        plot_layout.addWidget(self.circuit_canvas)

        # Initial plot
        self.update_plots()

    def create_slider(self, name, min_val, max_val, default_val):
        layout = QVBoxLayout()
        label = QLabel(name)
        layout.addWidget(label)

        slider = QSlider(Qt.Orientation.Horizontal)
        slider.setMinimum(min_val)
        slider.setMaximum(max_val)
        slider.setValue(default_val)
        slider.valueChanged.connect(self.update_plots)
        layout.addWidget(slider)

        container = QWidget()
        container.setLayout(layout)
        return container

    def update_plots(self):
        amplitude = self.amplitude_slider.findChild(QSlider).value() / 50  # Scale to 0-2 mV range
        frequency = self.frequency_slider.findChild(QSlider).value()

        # Update EPSP plot
        self.epsp_ax.clear()
        t = np.linspace(0, 2000, 10000)
        epsp = np.zeros_like(t)
        
        for i in range(int(2 * frequency)):
            onset = i * (1000 / frequency)
            epsp += amplitude * np.exp(-(t - onset) / 10) * (t > onset)

        self.epsp_ax.plot(t, epsp)
        self.epsp_ax.set_title("Excitatory Postsynaptic Potentials (EPSPs)")
        self.epsp_ax.set_xlabel("Time (ms)")
        self.epsp_ax.set_ylabel("Membrane Potential (mV)")
        self.epsp_ax.set_ylim(0, 2)
        self.epsp_canvas.draw()

        # Update circuit diagram
        self.circuit_ax.clear()
        self.circuit_ax.axis('off')
        self.circuit_ax.set_aspect('equal')
        
        # Presynaptic neuron
        self.circuit_ax.add_patch(plt.Circle((0.2, 0.5), 0.15, fill=False))
        self.circuit_ax.text(0.2, 0.7, "Presynaptic", ha='center', va='center')
        
        # Postsynaptic neuron
        self.circuit_ax.add_patch(plt.Circle((0.8, 0.5), 0.15, fill=False))
        self.circuit_ax.text(0.8, 0.7, "Postsynaptic", ha='center', va='center')
        
        # Synapse (arrow size changes with frequency)
        arrow_width = 0.02 + (frequency / 20) * 0.03  # Scale arrow width with frequency
        self.circuit_ax.arrow(0.35, 0.5, 0.25, 0, head_width=arrow_width, head_length=0.03, fc='blue', ec='blue', width=arrow_width/3)
        self.circuit_ax.text(0.475, 0.53, "Input", ha='center', va='bottom')
        
        # Variable resistance (gi)
        resistance_size = 0.1 - (amplitude * 0.05)  # Size changes with amplitude
        self.draw_variable_resistor(0.62, 0.5, resistance_size, 0.04)
        self.circuit_ax.text(0.7, 0.44, "gi", ha='center', va='top')
        
        conductance = amplitude  # Simplified conductance calculation
        self.circuit_ax.text(0.5, 0.58, f"gi = {conductance:.2f} mS", ha='center', va='center')
        self.circuit_ax.text(0.5, 0.45, f"Frequency = {frequency:.2f} Hz", ha='center', va='center')
        
        self.circuit_canvas.draw()

    def draw_variable_resistor(self, x, y, width, height):
        self.circuit_ax.plot([x, x+width], [y, y], 'k-')
        self.circuit_ax.add_patch(plt.Polygon([[x, y], [x+width/2, y-height], [x+width, y]], fill=False))

if __name__ == "__main__":
    window = SynapticTransmissionGUI()
    window.show()
    sys.exit(app.exec())