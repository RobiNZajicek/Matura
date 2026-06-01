	# 17 - Strojové učení: Příprava dat, Chyby v datech a bias, Korelace a kauzalita

Zdroj kódu (nepoužívám žádný jiný kód):
`C:\Users\Robin\Downloads\scikit.pdf` (DataCamp Scikit-Learn Cheat Sheet)

## O čem je tahle otázka

Tahle otázka NENÍ o trénování modelu, ale o všem, co se děje PŘEDTÍM, než model vznikne:
- jak data načíst a dát do správného tvaru,
- jak data rozdělit, aby se model dal poctivě zhodnotit,
- jak data předzpracovat (škálování, normalizace, kódování, chybějící hodnoty),
- jaké chyby a zaujatost (bias) v datech bývají,
- proč korelace neznamená kauzalitu.

Hlavní myšlenka: „Model je jen tak dobrý, jak dobrá jsou data.“ Proto je příprava dat klíčová.

Celý postup této otázky:
načti data -> rozděl na train/test -> předzpracuj -> (až potom by se trénoval model).

---

## KROK 1) Načtení dat

Kód z cheatu (neměnit):

```python
>>> from sklearn import datasets
>>> iris = datasets.load_iris()
>>> X, y = iris.data[:, :2], iris.target
```

Podrobné vysvětlení:

- `from sklearn import datasets`
  - Naimportuje modul s hotovými datovými sadami, které jsou přímo ve scikit-learn.
  - Díky tomu nemusíme stahovat žádný soubor, data jsou hned k dispozici.

- `iris = datasets.load_iris()`
  - Načte dataset Iris: 150 květin, každá má 4 naměřené rozměry a druh.
  - Je to nejznámější ukázkový dataset pro klasifikaci.

- `X, y = iris.data[:, :2], iris.target`
  - `X` jsou vstupní vlastnosti (features) = to, co model dostane na vstup.
    - `iris.data[:, :2]` bere jen první dva sloupce (dva rozměry), aby to bylo jednoduché.
  - `y` je cílová hodnota (label/target) = to, co má model uhodnout (druh květiny jako číslo 0/1/2).

Proč je to důležité:
- Data pro ML musí být ČÍSELNÁ a uložená jako pole (NumPy).
- Vždy musíme jasně oddělit „vstup“ (X) od „správné odpovědi“ (y).

Praktický příklad:
- E-shop: X = věk zákazníka, počet objednávek, průměrná útrata; y = jestli nakoupí znovu (ano/ne).

Častá chyba:
- Nechat v datech text tam, kde model čeká číslo (spadne to). Řeší se to kódováním (krok 3).

---

## KROK 2) Rozdělení na trénovací a testovací data

Kód z cheatu (neměnit):

```python
>>> from sklearn.model_selection import train_test_split
>>> X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
```

Podrobné vysvětlení:

- `from sklearn.model_selection import train_test_split`
  - Naimportuje funkci, která náhodně rozdělí data na dvě části.

- `X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)`
  - `X_train`, `y_train` = trénovací část. Na té se model UČÍ.
  - `X_test`, `y_test` = testovací část. Na té se model HODNOTÍ.
  - `random_state=0` = pevné nastavení náhody, aby rozdělení bylo pokaždé stejné (dá se to znovu zopakovat).

Proč je to důležité:
- Kdyby se model testoval na stejných datech, na kterých se učil, vypadal by skvěle, i kdyby si jen „zapamatoval“ odpovědi.
- Testovací data jsou jako „nové, neviděné“ příklady -> ukážou, jak model funguje v reálu.

Praktický příklad:
- Jako u zkoušení ve škole: učíš se z učebnice (train), ale test je z otázek, které jsi přesně neviděl (test).

Častá chyba:
- „Data leakage“ = když se informace z testovacích dat omylem dostane do trénování. Pak jsou výsledky falešně dobré.

---

## KROK 3) Předzpracování dat (jádro této otázky)

Tady se data „učešou“, aby se s nimi modelu pracovalo dobře.

### 3a) Standardizace (sjednocení škály)

```python
>>> from sklearn.preprocessing import StandardScaler
>>> scaler = StandardScaler().fit(X_train)
>>> standardized_X = scaler.transform(X_train)
>>> standardized_X_test = scaler.transform(X_test)
```

Podrobně:
- `StandardScaler()` převede každou vlastnost tak, aby měla průměr 0 a podobný rozptyl.
- `fit(X_train)` si spočítá průměr a rozptyl JEN z trénovacích dat.
- `transform(...)` ty hodnoty skutečně přepočítá.
- Na test se používá STEJNÉ nastavení z trénovacích dat (proto fit jen na train).

Proč: když má jedna vlastnost hodnoty v tisících (plat) a jiná v jednotkách (počet dětí), model by tu velkou bral nesprávně jako důležitější. Standardizace to srovná.

Kdy v praxi: skoro vždy u modelů, které počítají vzdálenosti nebo váhy (KNN, SVM, neuronové sítě).

### 3b) Normalizace

```python
>>> from sklearn.preprocessing import Normalizer
>>> scaler = Normalizer().fit(X_train)
>>> normalized_X = scaler.transform(X_train)
>>> normalized_X_test = scaler.transform(X_test)
```

Podrobně:
- Normalizace upraví každý ŘÁDEK (jeden vzorek) tak, aby měl jednotnou velikost (délku 1).
- Rozdíl oproti standardizaci: standardizace řeší sloupce (vlastnosti), normalizace řeší řádky (vzorky).

Kdy v praxi: když záleží na „směru“ dat víc než na absolutní velikosti (např. textová data, vektory).

### 3c) Binarizace

```python
>>> from sklearn.preprocessing import Binarizer
>>> binarizer = Binarizer(threshold=0.0).fit(X)
>>> binary_X = binarizer.transform(X)
```

Podrobně:
- Převede čísla na 0 nebo 1 podle prahu (`threshold`).
- Vše nad prahem = 1, vše pod (nebo rovno) = 0.

Kdy v praxi: když nás zajímá jen „ano/ne“ místo přesného čísla (např. „utratil víc než 1000 Kč“ -> 1).

### 3d) Kódování kategorií

```python
>>> from sklearn.preprocessing import LabelEncoder
>>> enc = LabelEncoder()
>>> y = enc.fit_transform(y)
```

Podrobně:
- `LabelEncoder` převede textové kategorie na čísla.
- Např. „M“ -> 0, „F“ -> 1.
- `fit_transform` znamená „nauč se kategorie a rovnou je převeď“.

Proč: model umí počítat jen s čísly, ne s textem.

Kdy v praxi: kdykoli máš sloupec jako pohlaví, země, barva, kategorie produktu.

### 3e) Doplnění chybějících hodnot

```python
>>> from sklearn.preprocessing import Imputer
>>> imp = Imputer(missing_values=0, strategy='mean', axis=0)
>>> imp.fit_transform(X_train)
```

Podrobně:
- `Imputer` doplní chybějící hodnoty místo toho, aby se řádek zahodil.
- `missing_values=0` určuje, co se považuje za chybějící.
- `strategy='mean'` doplní průměrem sloupce (jde i mediánem nebo nejčastější hodnotou).
- `axis=0` znamená počítat po sloupcích.

Proč: chybějící data jsou běžná chyba a model je neumí zpracovat, když chybí.

Pozor: v nových verzích scikit-learn se to jmenuje `SimpleImputer`. Na vysvětlení principu to ale stačí.

---

## KROK 4) Chyby v datech a bias

- Model se neučí z reality, ale jen z DAT, která mu dáme. Špatná data = špatný model.
- Bias (zaujatost) = když data nezachycují realitu spravedlivě, model převezme stejnou zaujatost.
- Typické chyby v datech:
  - chybějící hodnoty,
  - překlepy a nekonzistence (např. „Praha“ vs „praha“),
  - nevyvážené třídy (jedné kategorie je 95 %, druhé 5 %),
  - stará/neaktuální data,
  - příliš málo dat.
- Příklad biasu: když model na přijímání lidí trénuješ na datech, kde firma dříve brala hlavně muže, model bude zvýhodňovat muže.

Proto je krok 3 (příprava dat) tak důležitý - čistí a srovnává data.

---

## KROK 5) Korelace vs kauzalita

- Korelace = dvě věci se mění spolu (když roste jedna, mění se i druhá).
- Kauzalita = jedna věc je PŘÍČINOU druhé.
- Model umí najít korelaci, ale to NEDOKAZUJE příčinu.
- Příklad: v létě roste prodej zmrzliny i počet utonutí. Korelují spolu, ale zmrzlina nezpůsobuje utonutí. Skrytá příčina je teplo/léto.
- Pro maturitu stačí věta: „Korelace není důkaz kauzality.“

---

## Klíčová věta k otázce

„Kvalita modelu záleží hlavně na datech. Data se musí načíst do číselného tvaru, rozdělit na trénovací a testovací část a předzpracovat (škálování, normalizace, kódování kategorií, doplnění chybějících hodnot). Musíme dávat pozor na chyby a bias v datech a pamatovat, že korelace není důkaz kauzality.“
