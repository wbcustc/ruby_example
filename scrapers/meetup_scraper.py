import json
import requests
from HTMLParser import HTMLParser
from datetime import datetime

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def get_events():
    MEETUP_API_KEY = '951624a567e262e64b784e203818'

    r = requests.get('https://api.meetup.com/2/open_events?key=' + MEETUP_API_KEY + "&zip=10011&category=11&time=,10d&and_text=true")

    for item in r.json()['results']:
        group_name = item['group']['name']
        blacklisted = False
        if   group_name == 'New York City Backgammon':
            tag = 'Backgammon'
        elif group_name == 'The Connecticut Backgammon Club':
            tag = 'Backgammon'
        elif group_name == 'Cards Against Humanity & Apples 2 Apples -  BK Bar Meetup':
            tag = 'Cards Against Humanity'
        elif group_name == 'New York Poker & Blackjack Meetup (casino & table games)':
            tag = 'Poker'
        elif group_name == 'The Brooklyn Players Consortium. Poker. Brooklyn Style.':
            tag = 'Poker'
        elif group_name == 'US Professional Mahjong League':
            tag = 'Mahjong'
        elif group_name == 'The NYC Dungeons & Dragons Meetup Group':
            tag = 'Dungeons & Dragons'
        elif group_name == 'Edison Dungeons & Dragons Meetup':
            tag = 'Dungeons & Dragons'
        elif group_name == 'NYC Settlers of Catan Meetup Group':
            tag = 'Catan'
        elif group_name == 'NYC: Magic the Gathering - Weekly Battles':
            tag = 'Magic: The Gathering'
        elif group_name == "I'd Tap That - NYC Chapter (Casual Magic the Gathering)":
            tag = 'Magic: The Gathering'
        elif group_name == 'Manhattan Word Games Meetup':
            tag = 'Scrabble'
        elif group_name == 'SCRABBLERS & WORD-BIRDS  Social Group for Word Game Players':
            tag = 'Scrabble'
        elif group_name == "Let's Play Some Chess!":
            tag = 'Chess'
        else: blacklisted = True

        # Build the event object to send to Pace Games.
        if not blacklisted and 'venue' in item:
            e = {}
            time = datetime.fromtimestamp(item['time'] / 1000)

            e['event'] = {'title':                item['name'],
                          'address':              item['venue']['address_1'],
                          'event_at':             str(item['time']),
                          'lat':                  item['venue']['lat'],
                          'lng':                  item['venue']['lon']}
                          #'number_of_attendees':  item['yes_rsvp_count']}
            #if 'description' in item:
            #    e['event']['description'] = strip_tags(item['description'])
            #if 'how_to_find_us' in item:
            #    e['event']['special_instructions'] = strip_tags(item['how_to_find_us'])
            e['tags']  = [tag]
            print json.dumps(e)
            r = requests.post('https://glacial-eyrie-6539.herokuapp.com/events.json', json = e)
            print r.json()

get_events()
