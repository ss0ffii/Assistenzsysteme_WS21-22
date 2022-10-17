# Rasa Chatbot

## The Confectionist

Erstellt von:<br>
Matrikelnummer: 00819789, Name: Gutoranska, Sofia<br>
Matrikelnummer: 00751738, Name: Ring, Daniel<br>

### Installation

#### Rasa Open Source
Installation der aktuellsten Rasa Open Source 2.0 Version.<br>
[Guide](https://rasa.com/docs/rasa/2.x/installation#step-by-step-installation-guide)

Danach prüfen, ob alle Dependencies unserer Rasa Installation installiert sind mit der Datei requirements.txt<br>
```pip install -r requirements.txt```

#### Rasa X

Zum Testen hatten wir Rasa X im Local Mode installiert.<br>
[Guide](https://rasa.com/docs/rasa-x/installation-and-setup/install/local-mode) <br>
```pip3 install rasa-x --extra-index-url https://pypi.rasa.com/simple```<br>
Bei uns hat nur die Rasa Version 1.0.0 funktioniert.


### Beschreibung der Dateien

- config.yml: Sprache wurde auf Deutsch umgestellt. Und Standardwerte für pipeline und policies aktiviert.<br>
- credentials.yml: Für die Verwendung von Rasa X.<br>
- domain.yml: Auflistung aller verwendeten Intents, Entities, Slots, Actions und Forms.<br>
- endpoints.yml: Für die Aktivierung der URL zum Action Server (rasa run actions).<br>
- requirements.txt: Enthält alle benötigten Abhängigkeiten (Dependencies) unserer Rasa Open Source Installation.

#### actions

- actions.py: Beinhaltet alle custom actions, die von uns entwickelt wurden.<br>

#### data

- lookups.yml: Lookup Datei für die möglichen Eingaben von Slots und Entities.<br>
- nlu.yml: Alle User Inputs mit mehreren Arten von Ausdrucksweisen.<br>
- responses.yml: Antworten des Sprachassistenten.<br>
- rules.yml: Spezifische Reihenfolgen der Konversation mit intents und actions. Außerdem sind die Forms hier definiert, damit der Bot bei einer Bestellung alle Slots abfragt.<br>
- stories.yml: Einige Stories mit Variationen von verschiedenen Gesprächsrichtungen.<br>

##### db
- order.json: Hier sollen die getätigten Bestellungen hinterlegt werden.<br>
- specialoffer.json: Datenbankdatei für das Aufrufen der täglichen Sonderangebote.<br>