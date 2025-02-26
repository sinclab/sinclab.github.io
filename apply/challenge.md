---
title: "Challenge"
---
# {% include icon.html icon="fa-solid fa-terminal" %}Python Coding Challenge
**Expected Time: 30 minutes**

Thanks so much for your interest in the Social Interaction & Neural Computation Laboratory! Below, you will find a coding challenge that will mimic a few simple everyday problems we encounter in the lab. This challenge is designed to assess your ability to manipulate and analyze data using Python and relevant libraries (e.g., `pandas`, `numpy`, `matplotlib`). **We will evaluate the code based your coding style, efficiency, and creativity in solving the problems** — it is okay if you do not know how to solve all of the problems, but we will be looking for your thought process and approach to the problems. Please comment your code to explain your thought process.

You are provided with a comma-delimited file (`dyad_neural_data.csv`) and a Python script (`challenge.py`). Your task is to complete the functions within the script by following the prompts below (do not edit anything after `if __name__ == "__main__":` as these will help make sure you are on track). You may use `pandas`, `numpy`, and `matplotlib` (or `seaborn`) to solve the problems. 

Once completed, please email Shawn Rhoads your final script as `LASTNAME_FIRSTNAME_challenge.py`. Before sending, please verify that running the following command works for you:
```{python}
python LASTNAME_FIRSTNAME_challenge.py
```

**Please download the challenge materials here:**
- Data: [`dyad_neural_data.csv`](/apply/dyad_neural_data.csv)
- Script: [`challenge.py`](/apply/challenge.py)

## Dataset Description

The dataset ([`dyad_neural_data.csv`](/apply/dyad_neural_data.csv)) contains mock neural recordings for subjects engaged in dyadic interactions, recorded every second for 60 seconds. Some subjects are matched with more than one partner. See example below.

- `subj_id`: Unique subject identifier  
- `dyad_id`: Identifier for the dyadic interaction  
- `time`: Time in seconds (0-60)
- `power`: Power value of neural activity (relative to a baseline)

<table>
    <thead>
        <tr>
            <th>subj_id</th>
            <th>dyad_id</th>
            <th>time</th>
            <th>power</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>A</td>
            <td>0</td>
            <td>0.349</td>
        </tr>
        <tr>
            <td>1</td>
            <td>A</td>
            <td>1</td>
            <td>0.371</td>
        </tr>
        <tr>
            <td>2</td>
            <td>A</td>
            <td>0</td>
            <td>0.342</td>
        </tr>
        <tr>
            <td>2</td>
            <td>A</td>
            <td>1</td>
            <td>0.364</td>
        </tr>
        <tr>
            <td>3</td>
            <td>B</td>
            <td>0</td>
            <td>0.403</td>
        </tr>
        <tr>
            <td>3</td>
            <td>B</td>
            <td>1</td>
            <td>0.439</td>
        </tr>
        <tr>
            <td>4</td>
            <td>B</td>
            <td>0</td>
            <td>0.366</td>
        </tr>
        <tr>
            <td>4</td>
            <td>B</td>
            <td>1</td>
            <td>0.4</td>
        </tr>
        <tr>
            <td>5</td>
            <td>C</td>
            <td>0</td>
            <td>0.281</td>
        </tr>
        <tr>
            <td>5</td>
            <td>C</td>
            <td>1</td>
            <td>0.261</td>
        </tr>
        <tr>
            <td>6</td>
            <td>C</td>
            <td>0</td>
            <td>0.315</td>
        </tr>
        <tr>
            <td>6</td>
            <td>C</td>
            <td>1</td>
            <td>0.323</td>
        </tr>
        <tr>
            <td>5</td>
            <td>D</td>
            <td>0</td>
            <td>0.261</td>
        </tr>
        <tr>
            <td>5</td>
            <td>D</td>
            <td>1</td>
            <td>0.249</td>
        </tr>
        <tr>
            <td>7</td>
            <td>D</td>
            <td>0</td>
            <td>0.323</td>
        </tr>
        <tr>
            <td>7</td>
            <td>D</td>
            <td>1</td>
            <td>0.331</td>
        </tr>
    </tbody>
</table>

🚨 **Hint**: Subject 5 is in two dyads: Dyad C (with Subject 6) and Dyad D (with Subject 7).

## **Part 1: Data Organization**
**1. Identify Subjects with Multiple Dyad Matches**  
   - Write a function `find_multiple_partners(df)` that returns a list of subjects (`subj_id`) who appear in more than one `dyad_id`.

**2. Filter Specific Time Range**
   - We will often focus only on epochs of the data where there is an event of interest. Filter the data to only include timepoints 24-45 and analyze power during these periods. Write a function `select_timepoints(df, xmin, xmax)` filter the dataframe to include only rows where `time` is between 24 second (`xmin`) and 45 seconds (`xmax`).

## **Part 2: Data Manipulation**
**3. Compute Mean Power**  
   - Write a function `compute_mean_power(df)` that filters the data to only include timepoints 30-70 (using your function from earlier) and returns a new dataframe with the mean `power` for each `subj_id` for this time range.

**4. Standardize Power Values**  
   - Write a function `zscore_power(df)` that adds a new column to the dataframe called `zpower` and standardizes the `power` column over time for each subject by subtracting subjects' mean and dividing by their standard deviation.

**5. Apply a Custom Function to Scale Data**  
   - Write a function `scale_power(df)` that applies a lambda function that scales `power` values by the maximum value in the sample. The new column should be called `scaled_power` and should be added to the dataframe.

## **Part 3: Data Analysis and Visualization**
**6. Detect Dyads with High Variability in Power**  
   - Write a function `detect_high_variability_dyads(df, sigma=.25)` to identify dyads where the standard deviation of `power` across subjects exceeds a threshold (sigma=`0.25`) and print those subjects. 

**7. Extract and Plot Activity as a Function of Time**  
   - Write function `plot_power_x_time(df)` to plot the **z-scored timeseries for all subjects**, color each dyad uniquely and add a legend.
   - ✨ **Bonus:** only plot the timepoints 33-68 using your function from earlier.

**8. Compute and Plot Inter-Subject Correlation**  
   - Write a function `plot_correlation_heatmap(df)` to compute the Pearson *r* correlation of `power` between subjects' timeseries and plot a heatmap of the subject × subject correlation matrix where the color corresponds to the correlation coefficient. Also, mask out the upper triangle.
   - 🚨 **Hint**: The correlation matrix should be a 15 x 15 matrix. Remember that Subject 5 and Subject 7 are also a dyad.
   - ✨ **Bonus:** Draw a border around actual partner pairs (e.g., subject 1 and subject 6 are not partners, but subject 1 and subject 2 are). Annotate these heatmap cells with their respective correlation coefficients. 

