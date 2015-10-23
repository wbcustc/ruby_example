import io
import itertools as IT
import json
import re
import requests
import time
import xml.etree.ElementTree as ET
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
    categories = ['111', '74'] # D&D, Magic
    #for category in categories:

    r = requests.get('https://www.uncommonsnyc.com/events/?pno=1&action=search_events&category=111')
    content = r.content.replace('class=event', 'class="event')
    m = re.search(r'(<div class=\'css-events-list\'.*</p>\n</td>\n<td>\n</td>\n</tr>\n</tbody>\n</table>\n</div>)', content, re.DOTALL)
    content = m.group(0)
    content = content.replace('<p>', '')
    content = content.replace('</p>', '')
    tree = ET.fromstring(content)
    data = tree.findall(".//td")
    for i in range(len(data)/4):
        date, name = data[i*4].text.strip(), data[i*4+2].text.strip()

        # Build the event object to send to Pace Games.
        e = {}
        t = time.mktime(datetime.strptime(date, "%m/%d/%Y").replace(hour=19, minute=0).timetuple())*1000

        e['event'] = {'title':                name,
                      'address':              '230 Thompson St',
                      'event_at':             str(t),
                      'lat':                  40.730162,
                      'lng':                  -73.998687}
                      #'number_of_attendees':  item['yes_rsvp_count']}
        e['event']['description'] = 'New! The latest 5th edition Dungeons & Dragons adventure, Out of the Abyss. Available here a week before the wide release!'
        #if 'how_to_find_us' in item:
        #    e['event']['special_instructions'] = strip_tags(item['how_to_find_us'])
        e['tags']  = ['Dungeons & Dragons']
        print json.dumps(e)
        r = requests.post('https://glacial-eyrie-6539.herokuapp.com/events.json', json = e)

    for i in range(1,3):
        r = requests.get('https://www.uncommonsnyc.com/events/?pno='+str(i)+'&action=search_events&category=74')
        content = r.content.replace('class=event', 'class="event')
        m = re.search(r'(<tbody>.*</td>.*</tr>.*</tbody>)', content, re.DOTALL)
        content = m.group(0)
        content = content.replace('<p>', '')
        content = content.replace('</p>', '')
        tree = ET.fromstring(content)
        data = tree.findall(".//td")
        for i in range(len(data)/4):
            date, name = data[i*4].text.strip(), data[i*4+2].text.strip()

            # Build the event object to send to Pace Games.
            e = {}
            if 'Friday Night Magic' in name or 'Magic: Drafts' in name:
                t = time.mktime(datetime.strptime(date, "%m/%d/%Y").replace(hour=15, minute=30).timetuple())*1000
            if 'Battle for Zendikar Game Day' in name:
                t = time.mktime(datetime.strptime(date, "%m/%d/%Y").replace(hour=10, minute=0).timetuple())*1000
            else:
                t = time.mktime(datetime.strptime(date, "%m/%d/%Y").replace(hour=19, minute=0).timetuple())*1000

            e['event'] = {'title':                name,
                          'address':              '230 Thompson St',
                          'event_at':             str(t),
                          'lat':                  40.730162,
                          'lng':                  -73.998687}
                          #'number_of_attendees':  item['yes_rsvp_count']}
            e['event']['description'] = 'The Uncommons is one of the biggest and best places to play and purchase Magic: The Gathering in New York City. We run regular Magic NYC events four nights a week. Eight-person pods start when full! Prizes are based on a two pack per person payout.'
            #if 'description' in item:
            #    e['event']['description'] = strip_tags(item['description'])
            #if 'how_to_find_us' in item:
            #    e['event']['special_instructions'] = strip_tags(item['how_to_find_us'])
            e['tags']  = ['Magic: The Gathering']
            print json.dumps(e)
            r = requests.post('https://glacial-eyrie-6539.herokuapp.com/events.json', json = e)

get_events()
