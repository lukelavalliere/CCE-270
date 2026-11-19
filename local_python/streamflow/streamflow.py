"""CCE 270 - Provo River streamflow data."""

# AI-assisted code comment: NumPy reads the CSV and Matplotlib plots all gauge columns.
import matplotlib.pyplot as plt
import numpy as np


def load_streamflow(filename):
    # AI-assisted code: genfromtxt reads the relative CSV and separates dates from flows.
    streamflow = np.genfromtxt(filename, delimiter=",", dtype=str, skip_header=1)
    dates = streamflow[:, 0].astype("datetime64[m]")
    flows = streamflow[:, 1:6].astype(float)
    return dates, flows


def plot_streamflow(dates, flows, sites):
    # AI-assisted code: this loop draws each gauge and configures the Part 3 plot.
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


if __name__ == "__main__":
    filename = "June-2021-Provo-River-Streamflow-Rates.csv"
    dates, flows = load_streamflow(filename)
    sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]
    plot_streamflow(dates, flows, sites)
