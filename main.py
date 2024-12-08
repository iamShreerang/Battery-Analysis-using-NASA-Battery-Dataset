import os
import pandas as pd
import plotly.express as px

# Define paths
data_folder = r"cleaned_dataset\data"  # Update as per your dataset location
metadata_path = r"cleaned_dataset\metadata.csv"  # Update with the metadata file path

# Load metadata
metadata = pd.read_csv(metadata_path)

# Filter for "impedance" data type
impedance_data = metadata[metadata['type'] == 'impedance']

# Initialize a list to store data
combined_data = []

# Loop through the CSV files listed in metadata
for _, row in impedance_data.iterrows():
    file_path = os.path.join(data_folder, row['filename'])
    if os.path.exists(file_path):
        # Load the data
        temp_data = pd.read_csv(file_path)
        # Add metadata columns to the data
        temp_data['test_id'] = row['test_id']
        temp_data['battery_id'] = row['battery_id']
        temp_data['ambient_temperature'] = row['ambient_temperature']
        temp_data['Re'] = row['Re']
        temp_data['Rct'] = row['Rct']
        temp_data['Battery_impedance'] = temp_data['Battery_impedance']  # Ensure battery impedance is included
        combined_data.append(temp_data)

# Combine all data into a single DataFrame
if combined_data:
    combined_df = pd.concat(combined_data, ignore_index=True)
else:
    raise ValueError("No valid data files were loaded.")

# Display sample of the combined data
print("Combined Data Sample:")
print(combined_df.head())

# Drop rows where `Battery_impedance`, `Re`, or `Rct` is NaN
filtered_data = combined_df.dropna(subset=['Battery_impedance', 'Re', 'Rct'])

# Plot `Battery_impedance` vs. aging cycles
fig_impedance = px.scatter(filtered_data, x='test_id', y='Battery_impedance', color='battery_id',
                           title='Battery Impedance vs. Aging Cycles',
                           labels={'test_id': 'Aging Cycles (Test ID)', 'Battery_impedance': 'Battery Impedance (Ohms)'})
fig_impedance.show()

# Plot `Re` vs. aging cycles
fig_re = px.scatter(filtered_data, x='test_id', y='Re', color='battery_id',
                    title='Electrolyte Resistance (Re) vs. Aging Cycles',
                    labels={'test_id': 'Aging Cycles (Test ID)', 'Re': 'Electrolyte Resistance (Ohms)'})
fig_re.show()

# Plot `Rct` vs. aging cycles
fig_rct = px.scatter(filtered_data, x='test_id', y='Rct', color='battery_id',
                     title='Charge Transfer Resistance (Rct) vs. Aging Cycles',
                     labels={'test_id': 'Aging Cycles (Test ID)', 'Rct': 'Charge Transfer Resistance (Ohms)'})
fig_rct.show()
