# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []


class ActionTellNumber(Action):

    def name(self) -> Text:
        return "action_calculate_numbers"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # remember to check for other value of get_latest_entity_value
        number1 = next(tracker.get_latest_entity_values("number", "number1"), None)
        number2 = next(tracker.get_latest_entity_values("number", "number2"), None)

        if not number1 or not number2:
            msg = "Please give me a number!"
            dispatcher.utter_message(text=msg)

        msg = f"What do you want from number {number1} and {number2}"
        dispatcher.utter_message(text=msg,
                                 buttons=[
                                     {"payload": "/plus_numbers", "title": "plus"},
                                     {"payload": "/multiple_numbers", "title": "multiple"},
                                 ])
        return []


class ActionPlusNumber(Action):

    def name(self) -> Text:
        return "action_plus_numbers"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        number1 = tracker.get_slot("number1")
        number2 = tracker.get_slot("number2")

        if not number1 or not number2:
            msg = "Please give me a number!"
            dispatcher.utter_message(text=msg)

        result = int(number1) + int(number2)
        msg = f"Plus result is:  {result}"
        dispatcher.utter_message(text=msg)

        return []


class ActionMultipleNumber(Action):

    def name(self) -> Text:
        return "action_multiple_numbers"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        number1 = tracker.get_slot("number1")
        number2 = tracker.get_slot("number2")

        if not number1 or not number2:
            msg = "Please give me a number!"
            dispatcher.utter_message(text=msg)

        result = int(number1) * int(number2)
        msg = f"Multiple result is:  {result}"
        dispatcher.utter_message(text=msg)

        return []

