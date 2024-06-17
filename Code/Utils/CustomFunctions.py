import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import kendalltau, spearmanr, pearsonr

# Function to calculate slope using linear regression
def calculate_slope(y):
    x = np.arange(len(y))
    slope, _ = np.polyfit(x, y, 1)
    return slope

# Functions for correlations
def kendall_pval(x,y):
        return kendalltau(x,y)[1]
    
def pearsonr_pval(x,y):
        return pearsonr(x,y)[1]
    
def spearmanr_pval(x,y):
        return spearmanr(x,y)[1]

def correlation_test(water_dataset, drought_dataset, drought_indice, lag,test_dataset):
    output = ""
    columns = water_dataset.columns
    column_list = water_dataset.columns.tolist()
    
    output += "Results for "+test_dataset+":\n"
    output += 'Kendall Correlation coefficient\n'
    for i in column_list:
        output += ' ' + str(i) + ':\n'
        df1 = water_dataset[i]
        df2 = drought_dataset[drought_indice].shift(lag)
        output += '  tau = ' + str(round(df1.corr(df2, method='kendall'), 3)) + '\n'
        output += '  pval = ' + str(round(df1.corr(df2, method=kendall_pval), 4)) + '\n'
    
    output += 'Spearman Correlation coefficient\n'
    for i in column_list:
        output += ' ' + str(i) + ':\n'
        df1 = water_dataset[i]
        df2 = drought_dataset[drought_indice].shift(lag)
        output += '  rho = ' + str(round(df1.corr(df2, method='spearman'), 3)) + '\n'
        output += '  pval = ' + str(round(df1.corr(df2, method=spearmanr_pval), 4)) + '\n'
    
    output += 'Pearson Correlation coefficient\n'
    for i in column_list:
        output += ' ' + str(i) + ':\n'
        df1 = water_dataset[i]
        df2 = drought_dataset[drought_indice].shift(lag)
        r = df1.corr(df2, method='pearson')
        output += '  rsq = ' + str(round(r * r, 3)) + '\n'
        output += '  pval = ' + str(round(df1.corr(df2, method=pearsonr_pval), 4)) + '\n'
    
    return output

def correlation_test_2y(water_dataset1, water_dataset2, drought_dataset, drought_indice, lag,
                        test_dataset_name1, test_dataset_name2,y1label,y2label,color1,color2):
    output = ""
    columns = water_dataset1.columns
    column_list = water_dataset1.columns.tolist()
    columns2 = water_dataset2.columns
    column_list2 = water_dataset2.columns.tolist()
    betterlabels = [y1label] 
    betterlabels2 = [y2label] 
    
    output += "Results for "+test_dataset_name1+":\n"
    output += 'Kendall Correlation coefficient\n'
    for i in column_list:
        output += ' ' + str(i) + ':\n'
        df1 = water_dataset1[i]
        df2 = drought_dataset[drought_indice].shift(lag)
        output += '  tau = ' + str(round(df1.corr(df2, method='kendall'), 3)) + '\n'
        output += '  pval = ' + str(round(df1.corr(df2, method=kendall_pval), 4)) + '\n'
    
    output += 'Spearman Correlation coefficient\n'
    for i in column_list:
        output += ' ' + str(i) + ':\n'
        df1 = water_dataset1[i]
        df2 = drought_dataset[drought_indice].shift(lag)
        output += '  rho = ' + str(round(df1.corr(df2, method='spearman'), 3)) + '\n'
        output += '  pval = ' + str(round(df1.corr(df2, method=spearmanr_pval), 4)) + '\n'
    
    output += 'Pearson Correlation coefficient\n'
    for i in column_list:
        output += ' ' + str(i) + ':\n'
        df1 = water_dataset1[i]
        df2 = drought_dataset[drought_indice].shift(lag)
        r = df1.corr(df2, method='pearson')
        output += '  rsq = ' + str(round(r * r, 3)) + '\n'
        output += '  pval = ' + str(round(df1.corr(df2, method=pearsonr_pval), 4)) + '\n'
    
    output += ""
    output += "Results for "+test_dataset_name2+":\n"
    output += 'Kendall Correlation coefficient\n'
    for i in column_list2:
        output += ' ' + str(i) + ':\n'
        df1 = water_dataset2[i]
        df2 = drought_dataset[drought_indice].shift(lag)
        output += '  tau = ' + str(round(df1.corr(df2, method='kendall'), 3)) + '\n'
        output += '  pval = ' + str(round(df1.corr(df2, method=kendall_pval), 4)) + '\n'
    
    output += 'Spearman Correlation coefficient\n'
    for i in column_list2:
        output += ' ' + str(i) + ':\n'
        df1 = water_dataset2[i]
        df2 = drought_dataset[drought_indice].shift(lag)
        output += '  rho = ' + str(round(df1.corr(df2, method='spearman'), 3)) + '\n'
        output += '  pval = ' + str(round(df1.corr(df2, method=spearmanr_pval), 4)) + '\n'
    
    output += 'Pearson Correlation coefficient\n'
    for i in column_list2:
        output += ' ' + str(i) + ':\n'
        df1 = water_dataset2[i]
        df2 = drought_dataset[drought_indice].shift(lag)
        r = df1.corr(df2, method='pearson')
        output += '  rsq = ' + str(round(r * r, 3)) + '\n'
        output += '  pval = ' + str(round(df1.corr(df2, method=pearsonr_pval), 4)) + '\n'
    
    # Scatterplot of correlation values
    fig, ax = plt.subplots(figsize=(7, 5))

    x = drought_dataset[drought_indice]
    x2 = drought_dataset[drought_indice]

    # AZ Wells
    for i, j in zip(column_list2, betterlabels2):
        y2 = water_dataset2[i]
        ax.scatter(x2, y2, label=j, color=color2, marker='x')  # Using marker='x' for differentiation
        z = np.polyfit(x2, y2, 1)
        p = np.poly1d(z)
        ax.plot(x2, p(x2), '-', color=color2)  # Using '--' for differentiation

    # Create a secondary y-axis
    ax2 = ax.twinx()

    # GRACE
    for i, j in zip(column_list, betterlabels):
        y = water_dataset1[i]
        ax2.scatter(x, y, label=j, color=color1)
        z = np.polyfit(x, y, 1)
        p = np.poly1d(z)
        plt.plot(x, p(x), '-', color=color1)

    # Reverse the order of the secondary y-axis
    ax.set_ylim(ax.get_ylim()[::-1])

    ax.set_xlabel(drought_indice)
    ax2.set_ylabel('LWE Anomalies (cm)')
    ax.set_ylabel('DTW Anomalies (ft)')  # Set label for the secondary axis
    ax.set_title('Comparing ' + drought_indice + ' with DTW and GRACE Anomalies', loc='center')
    fig.set_dpi(600)

    # Combine legends for both axes
    lines, labels = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax.legend(lines + lines2, labels + labels2, loc='lower right')

    plt.show()
    return output
