import pandas as pd
import seaborn as sns

def boxplot(x, y, data, texttype='count', showdatapts=False, includemissing=True):
    
    categorical = data.copy()
    
    if includemissing==True:
        for i in categorical.columns:
            if categorical[i].isnull().any():
                categorical[i].fillna('MISSING', inplace=True)


    def plot(x, y, **kwargs):

        
        df = pd.DataFrame(dict(Value=x, Target=y))
        df.sort_values(by='Value', inplace=True)
        
        # Plotting boxplot
        ax = sns.boxplot(x='Value', y='Target',data=df)
        ax.set_xticklabels(ax.get_xticklabels(),rotation=90)
        
        # Showing data points incase 'showdatapts' is TRUE
        if showdatapts == True:
            ax = sns.swarmplot(x='Value', y='Target',data=df, color='0.25', size=8)
        
        # Defining text type
        if texttype=='count':
            pos_y = df.Value.value_counts().sort_index().values
        elif textype=='median':
            pos_y = df.groupby('Value').Target.median().values
        elif textype=='mean':
            pos_y = df.groupby('Value').Target.mean().values
            
        text = [str(i) for i in pos_y]
        pos_x = df.Value.unique()
        
        # Print info of dimension on x-axis
        for tick, label in zip(range(len(text)), text):

            ax.text(tick, 0, label, weight='bold', fontsize=10, color='k', horizontalalignment='center')

    f = pd.melt(categorical,
            id_vars=y, 
    #         value_vars=['MSZoning']
            value_vars=x
               )

    g = sns.FacetGrid(f, col="variable", col_wrap=2, sharex=False, sharey=True, size=7)
    g = g.map(plot, "value", y)
    