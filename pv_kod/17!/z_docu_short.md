# 17 - Strojove uceni: priprava dat, bias, korelace a kauzalita

Zdroj v docu pro scaling:
`C:\Users\Robin\Downloads\doc (1)\doc\Výběr z scikit-learn.org\scikit-learn-docs\_downloads\4ef6a0e5e8f2fe6463d63928373e5f91\plot_scaling_importance.py`

Zdroj v docu pro korelaci/kauzalitu:
`C:\Users\Robin\Downloads\doc (1)\doc\Výběr z scikit-learn.org\scikit-learn-docs\_downloads\521b554adefca348463adbbe047d7e99\plot_linear_model_coefficient_interpretation.py`

Pouzitelne u maturity:
- Otazka 17: priprava dat, chyby v datech, bias, korelace a kauzalita.
- Otazka 18: predzpracovani pred regresi/klasifikaci.
- Otazka 19: predzpracovani pred neuronovou siti.

Co rict:
- Model se neuci z reality, ale z dat. Kdyz jsou data spatna nebo zaujata, model bude spatny.
- `train_test_split` oddeli trenovaci a testovaci data, aby se model nehodnotil na tom, co uz videl.
- `StandardScaler` prevede ruzne veliciny na podobnou skalu.
- Korelace neznamena kauzalitu: model muze najit souvislost, ale to nedokazuje pricinu.

Kod z docu, nemenit:

```python
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X, y = load_wine(return_X_y=True, as_frame=True)
scaler = StandardScaler().set_output(transform="pandas")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42
)
scaled_X_train = scaler.fit_transform(X_train)
```

Teorie z docu ke kauzalite, nemenit:

```python
# Interpreting coefficients: being cautious about causality
# ---------------------------------------------------------
#
# Linear models are a great tool for measuring statistical association, but we
# should be cautious when making statements about causality, after all
# correlation doesn't always imply causation. This is particularly difficult in
# the social sciences because the variables we observe only function as proxies
# for the underlying causal process.
#
# In our particular case we can think of the EDUCATION of an individual as a
# proxy for their professional aptitude, the real variable we're interested in
# but can't observe. We'd certainly like to think that staying in school for
# longer would increase technical competency, but it's also quite possible that
# causality goes the other way too. That is, those who are technically
# competent tend to stay in school for longer.
#
# An employer is unlikely to care which case it is (or if it's a mix of both),
# as long as they remain convinced that a person with more EDUCATION is better
# suited for the job, they will be happy to pay out a higher WAGE.
#
# This confounding of effects becomes problematic when thinking about some
# form of intervention e.g. government subsidies of university degrees or
# promotional material encouraging individuals to take up higher education.
# The usefulness of these measures could end up being overstated, especially if
# the degree of confounding is strong. Our model predicts a :math:`0.054699`
# increase in hourly wage for each year of education. The actual causal effect
# might be lower because of this confounding.
```
