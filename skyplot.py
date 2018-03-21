import pandas as pd
import seaborn as sns

def boxplot(x, y, data, texttype='count'):
    
    categorical = data.copy()
    for i in categorical.columns:
        if categorical[i].isnull().any():
            categorical[i].fillna('MISSING', inplace=True)


    def plot(x, y, **kwargs):

        
        df = pd.DataFrame(dict(Value=x, SalePrice=y))
        df.sort_values(by='Value', inplace=True)
        ax = sns.boxplot(x='Value', y='SalePrice',data=df)
        ax.set_xticklabels(ax.get_xticklabels(),rotation=90)
        pos_y = df.Value.value_counts().sort_index().values
        text = [str(i) for i in pos_y]
        pos_x = df.Value.unique()

        for tick, label in zip(range(len(text)), text):

            ax.text(tick, pos_y[tick], label, weight='bold', fontsize=10, color='k', horizontalalignment='center')

    f = pd.melt(categorical,
            id_vars=y, 
    #         value_vars=['MSZoning']
            value_vars=x
               )

    g = sns.FacetGrid(f, col="variable", col_wrap=3, sharex=False, sharey=True, size=7)
    g = g.map(plot, "value", y)
    