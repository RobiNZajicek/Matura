# 18 - Strojové učení: regrese a klasifikace (workflow z cheatu)

Zdroj kódu (nepoužívám žádný jiný kód):
`C:\Users\Robin\Downloads\scikit.pdf` (DataCamp Scikit-Learn Cheat Sheet)

## O čem je tahle otázka

Regrese a klasifikace jsou dva hlavní druhy učení s učitelem (máme vstup X i správnou odpověď y).
Workflow je u obou stejný: načti data -> rozděl -> natrénuj model -> predikuj -> zhodnoť.
Liší se jen TYP modelu a METRIKA.

## Jaké otázky to zodpovídá

- Otázka 18: regrese a klasifikace.
- Otázka 17: příprava dat, train/test split (sdílené kroky).

---

## Část A: KLASIFIKACE (predikuje kategorii)

Kód z cheatu (neměnit):

```python
>>> from sklearn.model_selection import train_test_split
>>> X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
>>> from sklearn.svm import SVC
>>> svc = SVC(kernel='linear')
>>> svc.fit(X_train, y_train)
>>> y_pred = svc.predict(X_test)
>>> from sklearn.metrics import classification_report
>>> print(classification_report(y_test, y_pred))
>>> from sklearn.metrics import confusion_matrix
>>> print(confusion_matrix(y_test, y_pred))
```

Podrobné vysvětlení řádek po řádku:

1. `from sklearn.model_selection import train_test_split`
   - Naimportuje funkci na rozdělení dat na trénovací a testovací část.

2. `X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)`
   - Rozdělí data. Na `_train` se model učí, na `_test` se hodnotí.
   - `random_state=0` zajistí stejné rozdělení pokaždé.

3. `from sklearn.svm import SVC`
   - Naimportuje model Support Vector Classifier (klasifikátor).

4. `svc = SVC(kernel='linear')`
   - Vytvoří klasifikační model s lineárním jádrem (rozděluje třídy přímkou/rovinou).

5. `svc.fit(X_train, y_train)`
   - Natrénuje model na trénovacích datech (najde hranici mezi třídami).

6. `y_pred = svc.predict(X_test)`
   - Model predikuje třídy pro testovací data, která neviděl.

7. `from sklearn.metrics import classification_report`
   - Naimportuje souhrnný report metrik.

8. `print(classification_report(y_test, y_pred))`
   - Vypíše precision, recall a f1-score (jak dobře model klasifikuje).

9. `from sklearn.metrics import confusion_matrix`
   - Naimportuje matici záměn.

10. `print(confusion_matrix(y_test, y_pred))`
    - Ukáže, co model pletl s čím (kolik správně, kolik zaměnil).

Klasifikace = výstup je KATEGORIE (např. druh květiny, spam/nespam, schválit/zamítnout).

Metriky klasifikace:
- Accuracy = kolik procent celkem správně.
- Precision = z těch, co model označil za pozitivní, kolik bylo opravdu pozitivních.
- Recall = z těch, co byly opravdu pozitivní, kolik model našel.
- F1-score = kombinace precision a recall.

---

## Část B: REGRESE (predikuje číslo)

Kód z cheatu (neměnit):

```python
>>> from sklearn.linear_model import LinearRegression
>>> lr = LinearRegression(normalize=True)
>>> lr.fit(X, y)
>>> y_pred = lr.predict(X_test)
>>> from sklearn.metrics import mean_absolute_error
>>> y_true = [3, -0.5, 2]
>>> mean_absolute_error(y_true, y_pred)
>>> from sklearn.metrics import mean_squared_error
>>> mean_squared_error(y_test, y_pred)
>>> from sklearn.metrics import r2_score
>>> r2_score(y_true, y_pred)
```

Podrobné vysvětlení řádek po řádku:

1. `from sklearn.linear_model import LinearRegression`
   - Naimportuje lineární regresi.

2. `lr = LinearRegression(normalize=True)`
   - Vytvoří model lineární regrese.

3. `lr.fit(X, y)`
   - Natrénuje model: proloží daty přímku, která nejlíp popisuje vztah mezi X a y.

4. `y_pred = lr.predict(X_test)`
   - Model predikuje číselné hodnoty pro testovací data.

5. `from sklearn.metrics import mean_absolute_error`
   - Naimportuje průměrnou absolutní chybu (MAE).

6. `y_true = [3, -0.5, 2]`
   - Skutečné (správné) hodnoty pro porovnání.

7. `mean_absolute_error(y_true, y_pred)`
   - Průměr absolutních rozdílů mezi pravdou a predikcí (čím menší, tím lepší).

8. `from sklearn.metrics import mean_squared_error`
   - Naimportuje střední kvadratickou chybu (MSE).

9. `mean_squared_error(y_test, y_pred)`
   - Průměr čtverců chyb. Velké chyby trestá víc než MAE.

10. `from sklearn.metrics import r2_score`
    - Naimportuje koeficient determinace R².

11. `r2_score(y_true, y_pred)`
    - Jak dobře model vysvětluje data (1.0 = perfektní, 0 = nic nevysvětluje).

Regrese = výstup je ČÍSLO (např. cena bytu, teplota, věk, plat).

---

## Hlavní rozdíl k zapamatování

- Klasifikace: predikuje třídu. Metriky: accuracy, precision, recall, f1, confusion matrix.
- Regrese: predikuje číslo. Metriky: MAE, MSE, R².
- Společné: oba potřebují train/test split, `fit()` a `predict()`.

## Pozor (zastaralé v cheatu)

- `LinearRegression(normalize=True)` už v nových verzích není; dnes se škáluje zvlášť přes `StandardScaler`.
- Princip ale zůstává stejný a na vysvětlení je to v pořádku.
