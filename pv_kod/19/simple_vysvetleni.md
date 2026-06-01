# 19 - SIMPLE verze: Neuronové sítě

Zdroj kódu: `C:\Users\Robin\Downloads\scikit.pdf`

Pozor: cheat NEMÁ kód neuronové sítě. Tady ukážu, že postup je stejný jako u jiných modelů, a jako síť bych vyměnil jen krok modelu. (Reálný kód sítě je v `19/z_docu_short.md`.)

---

## Kód z cheatu (neměnit)

```python
>>> from sklearn.model_selection import train_test_split
>>> X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
>>> from sklearn.preprocessing import StandardScaler
>>> scaler = StandardScaler().fit(X_train)
>>> standardized_X = scaler.transform(X_train)
>>> standardized_X_test = scaler.transform(X_test)
>>> knn.fit(X_train, y_train)
>>> y_pred = knn.predict(X_test)
>>> from sklearn.metrics import accuracy_score
>>> accuracy_score(y_test, y_pred)
```

## Co který řádek dělá (jednoduše)

- `train_test_split(...)` -> rozdělím data na učení a zkoušení.
- `from sklearn.preprocessing import StandardScaler` -> načtu nástroj na srovnání čísel.
- `StandardScaler().fit(X_train)` -> spočítám srovnání z trénovacích dat.
- `scaler.transform(X_train)` -> srovnám trénovací data.
- `scaler.transform(X_test)` -> srovnám testovací data.
- `knn.fit(X_train, y_train)` -> naučím model. (U sítě by tu bylo `mlp.fit(...)`.)
- `knn.predict(X_test)` -> model hádá. (U sítě by tu bylo `mlp.predict(...)`.)
- `accuracy_score(...)` -> spočítám, kolik model uhodl.

---

## Definice jednoduše (a proč)

- **Neuronová síť**: model složený z vrstev „neuronů“. Proč: umí se naučit i složité vztahy.
- **Neuron**: malý počítací prvek. Vezme vstupy, vynásobí je váhami, sečte a pustí dál.
- **Váha**: číslo, které říká, jak důležitý je vstup. Proč: učením se mění, aby síť hádala líp.
- **Bias**: posunutí výsledku neuronu. Proč: dává síti víc volnosti.
- **Aktivační funkce**: rozhodne, jestli neuron „vystřelí“. Proč: umožní síti učit se nelineární vztahy.
- **Forward pass**: data jdou sítí dopředu a vyjde odhad.
- **Loss (chyba)**: jak moc se síť spletla. Proč: podle ní se síť opravuje.
- **Backpropagation**: chyba se vrací zpět a upraví váhy. Proč: aby síť byla příště lepší.
- **Overfitting**: síť se naučí data nazpaměť. Proč je to špatně: pak selže na nových datech.

## Klíčová věta

„Neuronová síť je jen další typ modelu. Postup je stejný (rozděl, srovnej, nauč, zhodnoť), jen se učí úpravou vah přes backpropagation.“
