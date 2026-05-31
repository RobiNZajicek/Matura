# 22 - Vlakna, multiprocessing, paralelni zpracovani

Zdroj v docu:
`C:\Users\Robin\Downloads\doc (1)\doc\Výběr z scikit-learn.org\scikit-learn-docs\_sources\computing\parallelism.rst.txt`

Dalsi kratky kod s `n_jobs=2`:
`C:\Users\Robin\Downloads\doc (1)\doc\Výběr z scikit-learn.org\scikit-learn-docs\_downloads\091282551e0bf11fedc96b869dfa8408\plot_grid_search_text_feature_extraction.py`

Pouzitelne u maturity:
- Otazka 22: vlakna, paralelni programovani, asynchronni metody, concurrent patterns.
- Otazka 18: paralelni hledani parametru modelu.
- Otazka 13: pipeline a skladani kroku.

Co rict:
- V tomhle docu neni kratky klasicky Python priklad `threading.Thread` nebo `multiprocessing.Process`.
- Je tam ale vysvetleni paralelismu ve scikit-learn: `joblib`, `OpenMP`, `BLAS`.
- `n_jobs` ridi, kolik workeru scikit-learn pouzije.
- `loky` je multiprocessing backend.
- `threading` backend pouziva vlakna.
- Pozor na oversubscription: moc vlaken/procesu muze program zpomalit.

Teorie z docu, nemenit:

```text
Joblib is able to support both multi-processing and multi-threading. Whether
joblib chooses to spawn a thread or a process depends on the **backend**
that it's using.

scikit-learn generally relies on the ``loky`` backend, which is joblib's
default backend. Loky is a multi-processing backend. When doing
multi-processing, in order to avoid duplicating the memory in each process
(which isn't reasonable with big datasets), joblib will create a `memmap
<https://docs.scipy.org/doc/numpy/reference/generated/numpy.memmap.html>`_
that all processes can share, when the data is bigger than 1MB.

In some specific cases (when the code that is run in parallel releases the
GIL), scikit-learn will indicate to ``joblib`` that a multi-threading
backend is preferable.

As a user, you may control the backend that joblib will use (regardless of
what scikit-learn recommends) by using a context manager::

    from joblib import parallel_backend

    with parallel_backend('threading', n_jobs=2):
        # Your scikit-learn code here
```

Kod z docu s paralelnim hledanim parametru, nemenit:

```python
parameter_grid = {
    "vect__max_df": (0.2, 0.4, 0.6, 0.8, 1.0),
    "vect__min_df": (1, 3, 5, 10),
    "vect__ngram_range": ((1, 1), (1, 2)),  # unigrams or bigrams
    "vect__norm": ("l1", "l2"),
    "clf__alpha": np.logspace(-6, 6, 13),
}

# %%
# In this case `n_iter=40` is not an exhaustive search of the hyperparameters'
# grid. In practice it would be interesting to increase the parameter `n_iter`
# to get a more informative analysis. As a consequence, the computional time
# increases. We can reduce it by taking advantage of the parallelisation over
# the parameter combinations evaluation by increasing the number of CPUs used
# via the parameter `n_jobs`.

from pprint import pprint

from sklearn.model_selection import RandomizedSearchCV

random_search = RandomizedSearchCV(
    estimator=pipeline,
    param_distributions=parameter_grid,
    n_iter=40,
    random_state=0,
    n_jobs=2,
    verbose=1,
)
```
