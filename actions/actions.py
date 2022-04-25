# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import requests
import json
import feedparser
from urllib.request import urlopen

class Action_get_lottery(Action):
    def name(self) -> Text:
        return "action_get_lottery"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Khai bao dia chi luu tru ket qua so xo. O day lam vi du nen minh lay ket qua SX Mien Bac
        url = 'https://xskt.com.vn/rss-feed/mien-bac-xsmb.rss'
        # Tien hanh lay thong tin tu URL
        feed_cnt = feedparser.parse(url)
        # Lay ket qua so xo moi nhat
        first_node = feed_cnt['entries']
        # Lay thong tin ve ngay va chi tiet cac giai
        return_msg = first_node[0]['title'] + "\n" + first_node[0]['description']
        # Tra ve cho nguoi dung
        dispatcher.utter_message(return_msg)
        print("lottery result")

        return []

class Action_get_weather(Action):
    def name(self) -> Text:
        return "action_get_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        url = "https://wttr.in/Hanoi?format=j1"
        response = urlopen(url)
        data_json = json.loads(response.read())
        weather = data_json['current_condition'][0]['weatherDesc'][0]['value']
        FeelsLikeC = data_json['current_condition'][0]['FeelsLikeC']
        do_am = data_json['current_condition'][0]['humidity']
        gio_km = data_json['current_condition'][0]['windspeedKmph']
        result = "Thời tiết hôm nay là " + weather + ", nhiệt độ là " + FeelsLikeC + " độ C, độ ẩm là " + do_am + " phần trăm và tốc độ gió là " + gio_km + " km/h"
        dispatcher.utter_message(text=result)
        print("weather result")

        return []