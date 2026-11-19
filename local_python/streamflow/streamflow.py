"""
CCE 270 - Provo River streamflow Part 3.
"""

# NumPy reads the CSV and Matplotlib creates the gauge plot.
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path


streamflow_file = Path(__file__).resolve().parent / "June-2021-Provo-River-Streamflow-Rates.csv"

streamflow = np.genfromtxt(
    streamflow_file,
    delimiter=",",
    dtype=str,
    skip_header=1,
)

dates = streamflow[:, 0].astype("datetime64[m]")
flows = streamflow[:, 1:6].astype(float)
sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]

plt.figure(figsize=(11, 5))
for gauge in range(flows.shape[1]):
    plt.plot(dates, flows[:, gauge], label=sites[gauge])

plt.title("Provo River Streamflow Data - June 2021")
plt.xlabel("Date")
plt.ylabel("Flowrate (CFS)")
plt.xticks(rotation=45)
plt.legend(title="Site Number")
plt.grid(True)
plt.tight_layout()
plt.show()
