# Imports
import json
import logging
from pathlib import Path
from typing import Any, Text, Dict, List


from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase
from rasa_sdk.events import SlotSet, AllSlotsReset


# Funktion zum Auslesen und Anzeigen der Sonderangebote
class SonderAngebote(Action):
    def name(self) -> Text:
        return "action_show_special_offers"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        def auslesen():
            # Datei öffnen
            with open('data/db/specialoffer.json') as file:
                # Datei wird geladen und Inhalt in data gespeichert
                data = json.load(file)
                logging.info('specialoffer.json loaded successfully')

                # Array zum Speichern der For Loop Daten
                array = []

                # Auf die Struktur zugreifen und pro JSON Objekt an das Array anhängen
                for offer in data['specialoffer']:
                    array.append(str(offer['id'] + ": " + offer['name'] +
                                     " für " + str(offer['price']) + "€"))

            # Array zurückgeben, damit der Dispatcher außerhalb der Funktion darauf zugreifen kann.
            return array

        # Daten der JSON sollen in Variable angebot abgespeichert werden
        angebot = auslesen()

        return dispatcher.utter_message(
            f"Das sind unsere Sonderangebote für heute:\n{angebot[0]}\n{angebot[1]}\n{angebot[2]}")


# Funktion zum Setzen der Kuchen/Tortenbeschriftung
class Message(Action):
    def name(self) -> Text:
        return "action_set_slot_message"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = tracker.latest_message['text']
        print(message)
        return [SlotSet("message", message)]


# Funktion um nach einem Bestellvorgang die Slots zurückzusetzen
class SlotReset(Action):

    def name(self) -> Text:
        return "action_reset_slots"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [AllSlotsReset()]


# Slots der Bestellung in DB schreiben
class OrderToDB(Action):

    def name(self) -> Text:
        return "action_save_order_to_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        def writetodb(orderdata):
            print(orderdata)
            with open('data/db/order.json', 'r') as db:
                dbdata = json.load(db)
                print(dbdata)
                dbdata.append(orderdata)

            with open('data/db/order.json', 'w') as db:
                json.dump(dbdata, db)

            return []

        # return um zu verhindern, dass die Funktion ausgeführt wird die nicht funktioniert
        return []

        slot_value = tracker.get_slot('product')
        slot_value = slot_value.lower()
        if slot_value == 'muffins':
            slot_value == 'muffin'
        if slot_value == 'muffin':
            slot_quantity = tracker.get_slot('quantity')
            slot_ingredients = tracker.get_slot('ingredients')
            slot_allergens = tracker.get_slot('allergens')
            dict = {
                "id": slot_value,
                "quantity": int(slot_quantity),
                "ingredients": slot_ingredients,
                "allergens": slot_allergens
            }

            orderdata = json.dumps(dict, indent=2)
            writetodb(orderdata)

        if slot_value == 'kuchen':
            slot_ingredients = tracker.get_slot('ingredients')
            slot_allergens = tracker.get_slot('allergens')
            slot_special_occasion = tracker.get_slot('special_occasion')
            slot_message = tracker.get_slot('message')
            orderdata = {"id": slot_value, "ingredients": slot_ingredients, "allergens": slot_allergens,
                         "special_occasion": slot_special_occasion, "message": slot_message}
            writetodb(orderdata)

        if slot_value == 'torte':
            slot_ingredients = tracker.get_slot('ingredients')
            slot_allergens = tracker.get_slot('allergens')
            slot_special_occasion = tracker.get_slot('special_occasion')
            slot_message = tracker.get_slot('message')
            orderdata = {"id": slot_value, "ingredients": slot_ingredients, "allergens": slot_allergens,
                         "special_occasion": slot_special_occasion, "message": slot_message}
            writetodb(orderdata)

        writetodb(orderdata)

        return []
