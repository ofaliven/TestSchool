"""Given dataframe, generate EDA of object data"""
def EDA_object (df, hue=None):
    
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
           
    # Plot count distribution of object-based data
    for col in df.select_dtypes(include='object').columns:
        unique_count = df[col].nunique()
        # plot histograms
        if unique_count < 50:
            fig = sns.catplot(x=col, kind="count", data=df)
            fig.set_xticklabels(rotation=90)
            plt.show()