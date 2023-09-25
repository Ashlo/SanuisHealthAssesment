import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages

def save_report(heart_rate_path, temp_variability_path, act_intensity_path):
    try:
        heart_rate_df = pd.read_csv(heart_rate_path)
        temp_var_df = pd.read_csv(temp_variability_path)
        act_intensity_df = pd.read_csv(act_intensity_path)
        create_visualisation(heart_rate_df,temp_var_df,act_intensity_df)
    except Exception as e:
        print(e)
        raise

def create_visualisation(heart_rate_df, temp_var_df, act_intensity_df):

    with PdfPages('Visualization_Report.pdf') as pdf:
        # Set up the plotting environment
        sns.set(style="whitegrid")

        sns.barplot(x='activityID', y='avg(hand_intensity)', data=act_intensity_df)
        plt.title('Average Hand Intensity by Activity')
        pdf.savefig()

        # Plotting for avg(chest_intensity)
        sns.barplot(x='activityID', y='avg(chest_intensity)', data=act_intensity_df)
        plt.title('Average Chest Intensity by Activity')
        pdf.savefig()

        # Plotting for avg(ankle_intensity)
        sns.barplot(x='activityID', y='avg(ankle_intensity)', data=act_intensity_df)
        plt.title('Average Ankle Intensity by Activity')
        pdf.savefig()

        sns.barplot(x='activityID', y='avg(heart_rate)', data=heart_rate_df)
        plt.title('Average Heart Rate by Activity')
        pdf.savefig()

