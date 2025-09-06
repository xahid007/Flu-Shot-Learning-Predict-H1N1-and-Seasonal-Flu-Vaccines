# utils/plotting.py
import matplotlib.pyplot as plt

def annotate_bars(decimals=2):
    """
    Annotate bars in the current seaborn/matplotlib bar plot with their values.
    
    Parameters:
        decimals (int): Number of decimal places to display.
    """
    ax = plt.gca()
    for p in ax.patches:
        height = p.get_height()
        if not height or height <= 0:
            continue  # skip bars with zero or negative height
        ax.annotate(f'{height:.{decimals}f}',
                    (p.get_x() + p.get_width() / 2., height),
                    ha='center', va='bottom',
                    xytext=(0, 1), textcoords='offset points', fontsize=9)