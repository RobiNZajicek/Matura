# 17 - SIMPLE verze: Příprava dat, chyby v datech, korelace vs kauzalita

Zdroj kódu: `C:\Users\Robin\Downloads\scikit.pdf`

Tohle je úplně jednoduchá verze. U zkoušky ukážeš na řádek a řekneš tu jednu větu.

---

## Kód (neměnit)

```python
>>> from sklearn import datasets
>>> iris = datasets.load_iris()
>>> X, y = iris.data[:, :2], iris.target
>>> from sklearn.model_selection import train_test_split
>>> X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
>>> from sklearn.preprocessing import StandardScaler
>>> scaler = StandardScaler().fit(X_train)
>>> standardized_X = scaler.transform(X_train)
>>> standardized_X_test = scaler.transform(X_test)
```

## Co který řádek dělá (jednoduše)

- `from sklearn import datasets` -> načtu si nástroj na hotová data.
- `iris = datasets.load_iris()` -> vezmu si připravená data o květinách.
- `X, y = iris.data[:, :2], iris.target` -> X = vstup (rozměry), y = odpověď (druh).
- `from sklearn.model_selection import train_test_split` -> načtu nástroj na rozdělení dat.
- `train_test_split(...)` -> rozdělím data na učení (train) a zkoušení (test).
- `from sklearn.preprocessing import StandardScaler` -> načtu nástroj na srovnání čísel.
- `StandardScaler().fit(X_train)` -> spočítám, jak čísla srovnat (jen z train dat).
- `scaler.transform(X_train)` -> srovnám trénovací data.
- `scaler.transform(X_test)` -> stejně srovnám i testovací data.

---

## Definice jednoduše (a proč to děláme)

- **X (vstup / features)**: co model dostane. Proč: z toho má hádat. Příklad: věk, výška.
- **y (odpověď / label)**: co má model uhodnout. Proč: to je správný výsledek. Příklad: druh květiny.
- **Train data**: data na učení. Proč: z nich se model učí.
- **Test data**: data na zkoušení. Proč: ověříme, jestli model umí i to, co neviděl.
- **Standardizace**: srovnání čísel na stejnou škálu (průměr 0). Proč: aby velké číslo (plat) nepřebilo malé číslo (počet dětí).
- **Normalizace**: úprava velikosti řádku na délku 1. Proč: když je důležitý směr dat, ne velikost.
- **Kódování kategorií**: převod textu na čísla (M -> 0, F -> 1). Proč: model umí jen čísla.
- **Chybějící hodnoty**: doplnění děr v datech (např. průměrem). Proč: model nesnese prázdná místa.

---

## Chyby v datech a bias (jednoduše)

- **Špatná data = špatný model.** Model věří jen tomu, co dostal.
- **Bias (zaujatost)**: když jsou data jednostranná, model bude taky jednostranný.
- Příklad: když firma brala dřív hlavně muže, model je bude zvýhodňovat.

## Korelace vs kauzalita (jednoduše)

- **Korelace**: dvě věci se mění spolu.
- **Kauzalita**: jedna věc způsobuje druhou.
- Věta: „Korelace není důkaz příčiny.“
- Příklad: zmrzlina a utonutí rostou spolu v létě, ale zmrzlina utonutí nezpůsobuje.
