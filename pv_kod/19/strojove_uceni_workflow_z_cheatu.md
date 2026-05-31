# 19 - Strojové učení: umělé neuronové sítě (a co k tomu dá cheat)

Zdroj kódu (nepoužívám žádný jiný kód):
`C:\Users\Robin\Downloads\scikit.pdf` (DataCamp Scikit-Learn Cheat Sheet)

## Důležité upozornění

V tomhle cheatu NENÍ žádný kód neuronové sítě (žádný MLPClassifier, žádný Keras/TensorFlow).
Cheat obsahuje jen: KNN, LinearRegression, SVC, GaussianNB (učení s učitelem) a KMeans, PCA (bez učitele).

Takže pro otázku 19 můžu z cheatu poctivě ukázat jen:
- že workflow neuronové sítě je STEJNÝ jako u jiných modelů,
- a jako neuronovou síť bys nahradil pouze krok „vyber + natrénuj model“.

(Pokud chceš reálný kód neuronové sítě, mám ho v poznámce `19/z_docu_short.md` - to je MLPClassifier ze scikit-learn dokumentace, ne z tohohle cheatu.)

## Jaké otázky to zodpovídá

- Otázka 19: neuronové sítě (workflow + zařazení do postupu ML).
- Otázka 18: klasifikace (stejný postup, jiný model).
- Otázka 17: příprava dat a train/test split.

## Workflow z cheatu, který platí i pro neuronovou síť

Kód z cheatu (neměnit):

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

Podrobné vysvětlení řádek po řádku:

1. `from sklearn.model_selection import train_test_split`
   - Naimportuje funkci na rozdělení dat.

2. `X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)`
   - Rozdělí data na trénovací a testovací část.

3. `from sklearn.preprocessing import StandardScaler`
   - Naimportuje škálování.

4. `scaler = StandardScaler().fit(X_train)`
   - Spočítá škálu z trénovacích dat. U neuronových sítí je škálování obzvlášť důležité, jinak se síť učí pomalu nebo špatně.

5. `standardized_X = scaler.transform(X_train)`
   - Naškáluje trénovací data.

6. `standardized_X_test = scaler.transform(X_test)`
   - Stejně naškáluje testovací data.

7. `knn.fit(X_train, y_train)`
   - Tady se trénuje model. PRO NEURONOVOU SÍŤ by tady bylo `mlp.fit(...)`.

8. `y_pred = knn.predict(X_test)`
   - Model predikuje. U sítě by to bylo `mlp.predict(...)`.

9. `from sklearn.metrics import accuracy_score`
   - Naimportuje přesnost.

10. `accuracy_score(y_test, y_pred)`
    - Změří, kolik model uhodl správně.

## Co říct o neuronové síti (teorie)

- Neuronová síť se skládá z vrstev neuronů (vstupní, skryté, výstupní).
- Každý neuron má váhy a bias, sečte vstupy a pustí je přes aktivační funkci.
- Forward pass: data tečou sítí dopředu a vznikne predikce.
- Loss funkce změří chybu predikce (jak moc se síť spletla).
- Backpropagation: chyba se vrací zpět a upraví váhy, aby byla síť příště lepší.
- Více vrstev a neuronů = síť umí složitější vztahy, ale hrozí overfitting (naučí se data nazpaměť místo obecného pravidla).

## Klíčová věta k otázce

„Neuronová síť je další typ modelu. Celý postup ML zůstává stejný (načti, rozděl, naškáluj, natrénuj, zhodnoť), jen místo KNN/SVC použiju neuronovou síť, která se učí úpravou vah přes backpropagation.“
