import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
from pathlib import Path
import base64

def create_graph(population,locus,positions):
    matrix = f"{Path(__file__).resolve().parent.parent}/data/{population}.ALD.matrix.csv"
    matrix_df = pd.read_csv(matrix, index_col='Loc-Pos')

    saved_pos = [f"{locus}-{pos}" for pos in positions]
    matrix = matrix_df.loc[saved_pos,saved_pos]
    
    #plt.rcParams["figure.figsize"] = (200,200)
    #f, ax = plt.subplots(figsize=(200,200))
    f, ax = plt.subplots(figsize=(10,10))
    ax.set_title('Multiallelic Asymmetric Linkage Disequilibrium (ALD)')
    #ax.set_ylabel('Wx|y', fontsize=100)
    #ax.set_xlabel('Wy|x', fontsize=100)
    ax.xaxis.set_ticks_position('top')
    ax.xaxis.set_label_position('top')
    plt.yticks(np.arange(0.5,len(matrix.index),1), matrix.index, rotation=90)
    plt.xticks(np.arange(0.5,len(matrix.columns),1), matrix.columns, rotation=270)
    sns.heatmap(matrix, annot=False, cmap=sns.cm.icefire)
    plt.ylabel('Wx|y')
    plt.xlabel('Wy|x')
    plot_file = BytesIO()
    plt.savefig(plot_file, format='png')
    encoded_file = base64.b64encode(plot_file.getvalue())
    
    return encoded_file