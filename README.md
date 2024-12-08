Battery Analysis using NASA Battery
Dataset
Submitted by: Shreerang Kolhe
Date: December 8, 2024
Submission for: ThinkClock Battery Labs, London, United Kingdom
1. Introduction
The NASA Battery Dataset consists of data related to the behavior of Lithium-Ion batteries
under various operational profiles. These profiles include charge, discharge, and impedance
measurements conducted at different temperatures. The dataset contains key parameters like
battery impedance, electrolyte resistance (Re), and charge transfer resistance (Rct),
which change as the batteries age during charge/discharge cycles.
The aim of this project is to analyze the changes in battery impedance and resistance
parameters (Re and Rct) over aging cycles to understand how they evolve as the battery
undergoes usage. The analysis is visualized using Plotly, a powerful plotting library in
Python.
2. Methodology
2.1 Data Preprocessing
The analysis starts with loading and exploring the dataset. The dataset consists of a large
number of measurements from different Li-ion batteries. Each measurement contains details
about the battery's impedance, electrolyte resistance, charge transfer resistance, and other
parameters. We focus on three specific parameters for this analysis:
 Battery Impedance (Battery_impedance)
 Electrolyte Resistance (Re)
 Charge Transfer Resistance (Rct)
We perform the following steps to prepare the data for analysis:
1. Data Loading: Load the dataset from a CSV file using pandas.
2. Data Cleaning: Remove any rows containing missing values for the relevant
columns: Battery_impedance, Re, and Rct.
3. Data Filtering: Select only the columns necessary for this analysis, specifically cycle,
Battery_impedance, Re, and Rct.