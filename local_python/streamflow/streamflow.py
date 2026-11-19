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
    plt.savefig("provo_streamflow.png", dpi=150, bbox_inches="tight")
    plt.show()


def summarize(dates, flows, sites):
    # AI-assisted code: NumPy finds each gauge's maximum, maximum date, minimum, and average.
    # Excel verification for gauge 10163000: Maximum = 131.0 cfs
    # Excel verification for gauge 10163000: Average = 56.9523611111 cfs
    print("Gauge     Maximum (cfs)  Date/Time of Maximum  Minimum (cfs)  Average (cfs)")
    print("------------------------------------------------------------------------")

    rows = []
    for gauge, site in enumerate(sites):
        column = flows[:, gauge]
        maximum = np.max(column)
        maximum_index = np.argmax(column)
        maximum_date = str(dates[maximum_index]).replace("T", " ")
        minimum = np.min(column)
        average = np.mean(column)
        print(f"{site:<10}{maximum:>8.1f}  {maximum_date:>20}  {minimum:>10.1f}  {average:>12.4f}")
        rows.append([site, maximum, maximum_date, minimum, average])

    np.savetxt(
        "streamflow_summary.csv",
        rows,
        delimiter=",",
        fmt="%s",
        header="Gauge,Maximum (cfs),Date/Time of Maximum,Minimum (cfs),Average (cfs)",
        comments=""
    )


def print_threshold_hours(flows, sites, threshold):
    # AI-assisted code: each 15-minute reading contributes 0.25 hours above the threshold.
    print("\nHours above threshold:")
    for gauge, site in enumerate(sites):
        hours = np.count_nonzero(flows[:, gauge] > threshold) * 0.25
        print(f"{site}: {hours:.2f} hours")


if __name__ == "__main__":
    filename = "June-2021-Provo-River-Streamflow-Rates.csv"
    dates, flows = load_streamflow(filename)
    sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]
    plot_streamflow(dates, flows, sites)
    summarize(dates, flows, sites)
    threshold = float(input("\nEnter a flow threshold in cfs: "))
    print_threshold_hours(flows, sites, threshold)
