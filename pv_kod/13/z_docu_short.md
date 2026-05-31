# 13 - Navrhove vzory / pipeline z docu

Zdroj v docu:
`C:\Users\Robin\Downloads\doc (1)\doc\Výběr z scikit-learn.org\scikit-learn-docs\_downloads\ba89a400c6902f85c10199ff86947d23\plot_digits_pipe.py`

Pouzitelne u maturity:
- Otazka 13: navrhove vzory.
- Otazka 18: klasifikace.
- Otazka 22: paralelismus pres `n_jobs=2`.

Pozor: v `doc` jsem nenasel kratky klasicky GoF priklad typu Singleton/Factory/Command/Facade. Tohle je nejlepsi kratka ukazka z docu pro princip **Pipeline**: skladani vice kroku za sebe.

Co rict:
- Pipeline znamena, ze data postupne prochazi pres kroky.
- Tady je krok `scaler`, potom `pca`, potom `logistic`.
- Je to ciste a udrzitelne, protoze kazdy krok ma jednu odpovednost.
- `GridSearchCV` zkousi ruzne parametry a `n_jobs=2` pouzije paralelni vyhodnocovani.

Kod z docu, nemenit:

```python
import matplotlib.pyplot as plt
import numpy as np
import polars as pl

from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# Define a pipeline to search for the best combination of PCA truncation
# and classifier regularization.
pca = PCA()
# Define a Standard Scaler to normalize inputs
scaler = StandardScaler()

# set the tolerance to a large value to make the example faster
logistic = LogisticRegression(max_iter=10000, tol=0.1)
pipe = Pipeline(steps=[("scaler", scaler), ("pca", pca), ("logistic", logistic)])

X_digits, y_digits = datasets.load_digits(return_X_y=True)
# Parameters of pipelines can be set using '__' separated parameter names:
param_grid = {
    "pca__n_components": [5, 15, 30, 45, 60],
    "logistic__C": np.logspace(-4, 4, 4),
}
search = GridSearchCV(pipe, param_grid, n_jobs=2)
search.fit(X_digits, y_digits)
print("Best parameter (CV score=%0.3f):" % search.best_score_)
print(search.best_params_)
```
