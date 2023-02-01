import requests
import json
import pandas as pd

production_Bugs_and_Issues_ID = "5cb598afa1818b308f701c28"
L3_requirement_and_activity_tracker_ID = "61135c658e97a87597b4a4d3"
neostark_corporate_tracker_ID = "635cdcde7466b3002aa33c6c"

url = f'https://api.trello.com/1/boards/{L3_requirement_and_activity_tracker_ID}/lists?key=e172c18d735be6e5f5151f60fa1e4a5f&token=5b22bd5251c88ff639e0c7db34ec6e595270b8f12e2294bd74bf883064a239b3'
response = requests.get(url).text
json_object = json.loads(response)
total_list_entries = []
for element in json_object:
    total_lists = {"list_id": element["id"],
                     "list_name": element["name"]}
    total_list_entries.append(total_lists)
total_cards_entries = []
for list in total_list_entries:
    list_name = list["list_name"]
    print(list_name)
    list_id = list["list_id"]
    url = f'https://api.trello.com/1/lists/{list_id}/cards?key=e172c18d735be6e5f5151f60fa1e4a5f&token=5b22bd5251c88ff639e0c7db34ec6e595270b8f12e2294bd74bf883064a239b3'
    response = requests.get(url).text
    json_object = json.loads(response)
    for card in json_object:
        try:
            label = card['labels'][0]['name']
        except:
            label = None
        try:
            due = card['due'][0:10]
        except:
            due = None
        try:
            last_activity = card['dateLastActivity'][0:10]
        except:
            last_activity = None
        total_cards = {"URL": card['url'],
                       "Name": card["name"],
                       "Due Date": due,
                       "Last Activity Date": last_activity,
                        "Label": label,
                       "List Name": list_name }
        total_cards_entries.append(total_cards)
    df = pd.DataFrame(total_cards_entries)
    df.to_excel("L3 Requirement and Activity Tracker.xlsx", sheet_name="Cards_Details", index=False)
