import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Data from your CSV
data = {
    "Frequency (Hz)": [100, 200, 400, 800, 1000, 2000, 4000, 8000, 10000, 20000, 40000, 80000, 100000],
    "Amplitude Vin (mV)": [576, 535.6, 607, 608, 616, 728, 872, 940, 966, 997.4, 999.4, 966.1, 873],
    "Amplitude Vout (mV)": [496.1, 454.1, 488, 488, 488, 440, 336, 171, 141.7, 79.37, 45.3, 30, 28.44],
    "Phase Shift (degrees)": [0.9912, 4.401, 9.46, 19.76, 23.45, 45.05, 61.92, 72.2, 74.17, 78.11, 80.49, 84.4, 90.2],
    "Gain (dB)": [-1.297, -1.434, -1.895, -1.910, -2.023, -4.374, -8.284, -14.803, -16.672, -21.984, -26.873, -30.158, -29.742]
}

df = pd.DataFrame(data)

# Create figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Plot 1: Gain vs Frequency (Bode Magnitude Plot)
ax1.semilogx(df["Frequency (Hz)"], df["Gain (dB)"], 'bo-', linewidth=1.5, markersize=6, label='Measured Gain')
ax1.set_title('Low-Pass Filter Frequency Response', fontsize=14)
ax1.set_ylabel('Gain (dB)', fontsize=12)
ax1.grid(True, which="both", linestyle="--", alpha=0.5)
ax1.legend()

# Add -3dB cutoff line and label
ax1.axhline(-3, color='r', linestyle=':', linewidth=1)
ax1.annotate('-3 dB Cutoff', (1000, -2.5), color='r')

# Plot 2: Phase Shift vs Frequency (Bode Phase Plot)
ax2.semilogx(df["Frequency (Hz)"], df["Phase Shift (degrees)"], 'rs-', linewidth=1.5, markersize=6, label='Phase Shift')
ax2.set_xlabel('Frequency (Hz)', fontsize=12)
ax2.set_ylabel('Phase (degrees)', fontsize=12)
ax2.grid(True, which="both", linestyle="--", alpha=0.5)
ax2.legend()

# Add 45° phase shift reference
ax2.axhline(45, color='b', linestyle=':', linewidth=1)
ax2.annotate('45°', (1000, 47), color='b')

plt.tight_layout()
plt.show()