# 18 - SIMPLE verze: Regrese a klasifikace

Zdroj kódu: `C:\Users\Robin\Downloads\scikit.pdf`

Úplně jednoduchá verze. Ukážeš na řádek a řekneš jednu větu.

---

## KLASIFIKACE (hádá kategorii)

Kód (neměnit):

```python
>>> from sklearn.svm import SVC
>>> svc = SVC(kernel='linear')
>>> svc.fit(X_train, y_train)
>>> y_pred = svc.predict(X_test)
>>> from sklearn.metrics import classification_report
>>> print(classification_report(y_test, y_pred))
>>> from sklearn.metrics import confusion_matrix
>>> print(confusion_matrix(y_test, y_pred))
```

Co který řádek dělá (jednoduše):
- `from sklearn.svm import SVC` -> načtu klasifikační model.
- `svc = SVC(kernel='linear')` -> vyrobím model, co odděluje skupiny čárou.
- `svc.fit(X_train, y_train)` -> naučím model na trénovacích datech.
- `y_pred = svc.predict(X_test)` -> model hádá kategorie pro nová data.
- `classification_report(...)` -> ukáže, jak přesně model hádal.
- `confusion_matrix(...)` -> ukáže, co model pletl s čím.

---

## REGRESE (hádá číslo)

Kód (neměnit):

```python
>>> from sklearn.linear_model import LinearRegression
>>> lr = LinearRegression(normalize=True)
>>> lr.fit(X, y)
>>> y_pred = lr.predict(X_test)
>>> from sklearn.metrics import mean_squared_error
>>> mean_squared_error(y_test, y_pred)
>>> from sklearn.metrics import r2_score
>>> r2_score(y_true, y_pred)
```

Co který řádek dělá (jednoduše):
- `from sklearn.linear_model import LinearRegression` -> načtu regresní model.
- `lr = LinearRegression(normalize=True)` -> vyrobím model, co prokládá data přímkou.
- `lr.fit(X, y)` -> naučím model vztah mezi vstupem a číslem.
- `y_pred = lr.predict(X_test)` -> model hádá čísla pro nová data.
- `mean_squared_error(...)` -> spočítá, jak moc se model spletl.
- `r2_score(...)` -> řekne, jak dobře model sedí (1 = perfektní).

---

## Definice jednoduše (a proč to děláme)

- **Klasifikace**: model hádá KATEGORII (ano/ne, druh, spam). Proč: chceme zařadit do skupiny.
- **Regrese**: model hádá ČÍSLO (cena, teplota). Proč: chceme předpovědět hodnotu.
- **fit()**: učení modelu. Proč: aby se model naučil z dat.
- **predict()**: hádání. Proč: chceme odpověď na nová data.
- **Accuracy**: kolik procent správně (klasifikace).
- **Precision**: z označených pozitivních kolik bylo opravdu pozitivních.
- **Recall**: ze všech pozitivních kolik model našel.
- **MSE (mean squared error)**: průměr čtverců chyb (regrese). Menší = lepší.
- **R²**: jak dobře model vysvětluje data. 1 = perfektní.

## Hlavní rozdíl (zapamatuj)

- Klasifikace = kategorie. Regrese = číslo.
- Oba potřebují train/test, fit() a predict().
