import pandas as pd
import numpy as np
from numpy.linalg import eig

### PCA function
def PCA(matrix):
    eigenvalues, eigenvectors = eig(matrix)
    
    var_exp = -np.sort(-(eigenvalues / eigenvalues.sum())) #np.sort does not have descending option
    cum_var_exp = var_exp.cumsum()
    df_eigenvalues = pd.DataFrame(np.stack([eigenvalues, var_exp, cum_var_exp], axis=0), 
                index=["Eigenvalue", "Variation Explained", "Cumulative Variation"],
                columns = ["λ"+str(i) for i in range(1, len(eigenvalues)+1)])
    
    df_eigenvectors = pd.DataFrame(eigenvectors, 
            index=matrix.columns,
            columns = ["λ"+str(i) for i in range(1, len(eigenvalues)+1)])
    #df_eigenvectors = df_eigenvectors.reindex(sorted(df_eigenvectors.columns), axis=1)
    return df_eigenvalues, df_eigenvectors