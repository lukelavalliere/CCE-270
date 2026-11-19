"""
CCE 270 - HW Matplotlib
Standalone Python version completed from the BYU CCE 270 homework instructions.

AI assistance note:
ChatGPT helped organize the code, verify the CSV formats, and add comments
explaining the equations and plotting steps.
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

BASE_DIR = Path(__file__).resolve().parent


def find_file(base_name):
    """
    Look for the normal assignment filename first.
    If the browser downloaded a duplicate such as '(1)', use that instead.
    """
    normal = BASE_DIR / base_name
    if normal.exists():
        return normal

    stem = Path(base_name).stem
    suffix = Path(base_name).suffix
    matches = sorted(BASE_DIR.glob(f"{stem}(*){suffix}"))
    if matches:
        return matches[0]

    raise FileNotFoundError(
        f"Could not find {base_name}. Put the CSV in the same folder as this .py file."
    )


# ============================================================
# PART 1a - SHEAR DIAGRAM
# ============================================================

L = 6          # beam length, ft
R_A = 170      # reaction at A, lb
R_B = 410      # reaction at B, lb
P_1 = 100      # point load, lb
q_1 = 120      # distributed load, lb/ft
q_2 = 120      # distributed load, lb/ft

x = np.linspace(0, L, 500)
V = np.zeros_like(x)

# Evaluate the provided piecewise shear equations.
for i in range(len(x)):
    if x[i] < 2:
        V[i] = R_A - (q_1 * x[i])
    elif x[i] < 4:
        V[i] = R_A - (q_1 * 2) - P_1
    else:
        V[i] = R_A - (q_1 * 2) - P_1 + R_B - (q_2 * (x[i] - 4))

plt.figure(figsize=(8, 4))
plt.plot(x, V, color="green", linewidth=2)
plt.fill_between(x, V, 0, color="lightgreen", alpha=0.6)
plt.axhline(0, color="black", linewidth=1)
plt.xlim(0, L)
plt.title("Shear Diagram")
plt.xlabel("Distance Along Beam, x (ft)")
plt.ylabel("Shear, V (lb)")
plt.grid(True)
plt.tight_layout()
plt.show()


# ============================================================
# PART 1b - MOMENT DIAGRAM
# ============================================================

x = np.linspace(0, L, 500)
M = np.zeros_like(x)

# Evaluate the provided piecewise moment equations.
for i in range(len(x)):
    if x[i] < 2:
        M[i] = (R_A * x[i]) - (q_1 * x[i]**2 / 2)
    elif x[i] < 4:
        M[i] = (
            (R_A * x[i])
            - (q_1 * 2 * (x[i] - 1))
            - (P_1 * (x[i] - 2))
        )
    else:
        M[i] = (
            (R_A * x[i])
            - (q_1 * 2 * (x[i] - 1))
            - (P_1 * (x[i] - 2))
            + (R_B * (x[i] - 4))
            - (q_2 * (x[i] - 4) * ((x[i] - 4) / 2))
        )

plt.figure(figsize=(8, 4))
plt.plot(x, M, color="red", linewidth=2)
plt.fill_between(x, M, 0, color="lightcoral", alpha=0.6)
plt.axhline(0, color="black", linewidth=1)
plt.xlim(0, L)
plt.title("Moment Diagram")
plt.xlabel("Distance Along Beam, x (ft)")
plt.ylabel("Moment, M (lb-ft)")
plt.grid(True)
plt.tight_layout()
plt.show()


# ============================================================
# PART 2 - PASADENA TEMPERATURE DATA
# ============================================================

pasadena_file = find_file("2013-2014-Pasadena-Temperature-Data.csv")

pasadena = np.genfromtxt(
    pasadena_file,
    delimiter=",",
    dtype=str,
    skip_header=1
)

dates = pasadena[:, 0].astype("datetime64[D]")
high_temp = pasadena[:, 1].astype(float)
low_temp = pasadena[:, 2].astype(float)

plt.figure(figsize=(10, 5))
plt.plot(dates, high_temp, label="High Temperature", color="red")
plt.plot(dates, low_temp, label="Low Temperature", color="blue")
plt.title("Pasadena Temperature Data 2013-2014")
plt.xlabel("Date")
plt.ylabel("Temperature (°F)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# ============================================================
# PART 3 - PROVO RIVER STREAMFLOW DATA
# ============================================================

streamflow_file = find_file("June-2021-Provo-River-Streamflow-Rates.csv")

streamflow = np.genfromtxt(
    streamflow_file,
    delimiter=",",
    dtype=str,
    skip_header=1
)

dates = streamflow[:, 0].astype("datetime64[m]")
site_10163000 = streamflow[:, 1].astype(float)
site_10155200 = streamflow[:, 2].astype(float)
site_10155500 = streamflow[:, 3].astype(float)
site_10154200 = streamflow[:, 4].astype(float)
site_10155000 = streamflow[:, 5].astype(float)

plt.figure(figsize=(11, 5))
plt.plot(dates, site_10163000, label="10163000")
plt.plot(dates, site_10155200, label="10155200")
plt.plot(dates, site_10155500, label="10155500")
plt.plot(dates, site_10154200, label="10154200")
plt.plot(dates, site_10155000, label="10155000")
plt.title("Provo River Streamflow Data - June 2021")
plt.xlabel("Date")
plt.ylabel("Flowrate (CFS)")
plt.xticks(rotation=45)
plt.legend(title="Site Number")
plt.grid(True)
plt.tight_layout()
plt.show()


# ============================================================
# PART 4 - FREMONT BRIDGE BICYCLE COUNT DATA
# ============================================================

bicycle_file = find_file("Fremont-Bridge-Bicycle-Count.csv")

bicycle = np.genfromtxt(
    bicycle_file,
    delimiter=",",
    dtype=str,
    skip_header=1
)

dates = bicycle[:, 0].astype("datetime64[h]")
bridge_total = bicycle[:, 1].astype(float)
east_sidewalk = bicycle[:, 2].astype(float)
west_sidewalk = bicycle[:, 3].astype(float)

plt.figure(figsize=(11, 5))
plt.plot(dates, bridge_total, label="Fremont Bridge Total", color="black")
plt.plot(dates, east_sidewalk, label="Fremont Bridge East Sidewalk", color="blue")
plt.plot(dates, west_sidewalk, label="Fremont Bridge West Sidewalk", color="orange")
plt.title("Fremont Bridge Bicycle Count")
plt.xlabel("Date")
plt.ylabel("Bicycle Count")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# The bike count in later years may be lower because commuting and travel
# patterns changed during and after the COVID-19 pandemic.


# ============================================================
# PART 5 - AVERAGE U.S. DAILY BIRTH DATA
# ============================================================

birth_file = find_file("2012-US-Birth-Rates.csv")

births = np.genfromtxt(
    birth_file,
    delimiter=",",
    dtype=str,
    skip_header=1
)

dates = births[:, 0].astype("datetime64[D]")
birth_count = births[:, 1].astype(float)

plt.figure(figsize=(12, 4))
plt.plot(dates, birth_count, color="steelblue")
plt.title("Average U.S. Daily Birth Data")
plt.xlabel("Date")
plt.ylabel("Births")
plt.grid(True)

# The homework graph labels these five holidays.
holiday_labels = [
    ("New Year's Day", "2012-01-01", "2012-02-01", -250),
    ("4th of July", "2012-07-04", "2012-07-24", 250),
    ("Halloween", "2012-10-31", "2012-09-20", 250),
    ("Thanksgiving", "2012-11-22", "2012-10-20", -250),
    ("Christmas", "2012-12-25", "2012-11-20", -250),
]

for label, holiday, text_date, offset in holiday_labels:
    holiday_date = np.datetime64(holiday)
    index = np.argmin(np.abs(dates - holiday_date))

    plt.annotate(
        label,
        xy=(dates[index], birth_count[index]),
        xytext=(np.datetime64(text_date), birth_count[index] + offset),
        arrowprops=dict(
            arrowstyle="->",
            connectionstyle="arc3,rad=0.25"
        )
    )

plt.tight_layout()
plt.show()

# Birth rates may drop on major holidays because fewer inductions,
# C-sections, and other planned deliveries are scheduled on holidays.
