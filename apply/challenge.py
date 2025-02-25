import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dyad_neural_data.csv")

# 1. **Identify Subjects with Multiple Dyad Matches**  
def find_multiple_partners(df):
    raise NotImplementedError("Please complete this function.")

# 2. **Filter Specific Time Range**
def select_timepoints(df, xmin, xmax):
    raise NotImplementedError("Please complete this function.")

# 3. **Compute Mean Power**  
def compute_mean_power(df):
    raise NotImplementedError("Please complete this function.")

# 4. **Standardize Power Values** 
def zscore_power(df):
    raise NotImplementedError("Please complete this function.")

# 5. **Apply a Custom Function to Scale Data**  
def scale_power(df):
    raise NotImplementedError("Please complete this function.")

# 6. **Detect Dyads with High Variability in Power**  
def detect_high_variability_dyads(df, sigma=.25):
    raise NotImplementedError("Please complete this function.")

# 7. **Extract and Plot Activity**  
def plot_power_x_time(df):
    raise NotImplementedError("Please complete this function.")

# 8. **Compute and Plot Inter-Subject Correlation Matrix (Subject x Subject)**  
def plot_correlation_heatmap(df):
    raise NotImplementedError("Please complete this function.")

# Run the functions (for testing)
if __name__ == "__main__":
    print('1. Identifying Subjects with Multiple Dyad Matches...')
    multi_dyads = find_multiple_partners(df)
    print(multi_dyads)
    assert 5 in multi_dyads, "Subject 5 should have multiple dyad matches."

    print('Filtering Specific Time Range...')
    filtered_df = select_timepoints(df, 24, 45)
    print(filtered_df.head())
    assert filtered_df['time'].min() == 24, "Minimum time should be 24 seconds."
    assert filtered_df['time'].max() == 45, "Maximum time should be 45 seconds."

    print('Computing Mean Power...')
    print(compute_mean_power(df))

    print('Standardizing Power...')
    zscored_df = zscore_power(df)
    print(zscored_df.head())
    for subj_id in zscored_df['subj_id'].unique():
        subj_data = zscored_df[zscored_df['subj_id'] == subj_id]
        assert np.isclose(subj_data['zpower'].mean(), 0), f"Mean of zpower for subject {subj_id} should be close to 0."
        assert np.isclose(subj_data['zpower'].std(), 1), f"Standard deviation of zpower for subject {subj_id} should be close to 1."

    print('Scaling Power...')
    scale_df = scale_power(df)
    print(scale_df.head())

    print('Detecting Dyads with High Variability in Power...')
    high_variability_dyads = detect_high_variability_dyads(df)
    print(high_variability_dyads)
    assert 'A' in high_variability_dyads, "Dyad A has high variability in power."
    assert 'F' in high_variability_dyads, "Dyad F has high variability in power."
    assert 'H' in high_variability_dyads, "Dyad H has high variability in power."
        
    print('Plotting Activity as a Function of Time...')
    plot_power_x_time(df)

    print('Plotting Inter-Subject Correlation for Real Dyads Only...')
    plot_correlation_heatmap(df)
