# 19 - Strojove uceni: umele neuronove site

Zdroj v docu:
`C:\Users\Robin\Downloads\doc (1)\doc\Výběr z scikit-learn.org\scikit-learn-docs\_downloads\7534058b2748ca58f7594203b7723a0e\plot_mnist_filters.py`

Pouzitelne u maturity:
- Otazka 19: neuronove site.
- Otazka 18: klasifikace obrazku/cifer.
- Otazka 17: priprava dat a train/test split.

Co rict:
- Neuronova sit je model slozeny z vrstev a vah.
- `MLPClassifier` je vicevrstva neuronova sit pro klasifikaci.
- MNIST jsou obrazky cislic 28x28 pixelu.
- `X = X / 255.0` normalizuje pixely na rozsah 0-1.
- `hidden_layer_sizes=(40,)` znamena jednu skrytou vrstvu se 40 neurony.
- `fit()` trenuje vahu site, `score()` meri presnost.

Poznamka: Keras/TensorFlow jsem v tom `doc` baliku nenasel jako kratky Python zdroj. Tohle je kratka scikit-learn neuronova sit z dokumentace.

Kod z docu, nemenit:

```python
import warnings

import matplotlib.pyplot as plt

from sklearn.datasets import fetch_openml
from sklearn.exceptions import ConvergenceWarning
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

# Load data from https://www.openml.org/d/554
X, y = fetch_openml("mnist_784", version=1, return_X_y=True, as_frame=False)
X = X / 255.0

# Split data into train partition and test partition
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size=0.7)

mlp = MLPClassifier(
    hidden_layer_sizes=(40,),
    max_iter=8,
    alpha=1e-4,
    solver="sgd",
    verbose=10,
    random_state=1,
    learning_rate_init=0.2,
)

# this example won't converge because of resource usage constraints on
# our Continuous Integration infrastructure, so we catch the warning and
# ignore it here
with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=ConvergenceWarning, module="sklearn")
    mlp.fit(X_train, y_train)

print("Training set score: %f" % mlp.score(X_train, y_train))
print("Test set score: %f" % mlp.score(X_test, y_test))
```
