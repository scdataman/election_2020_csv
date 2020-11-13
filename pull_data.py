import pandas as pd
import requests


states = [
        'Alaska',
        'Alabama',
        'Arizona',
        'Arkansas',
        'California',
        'Colorado',
        'Connecticut',
        'Delaware',
        'Florida',
        'Georgia',
        'Hawaii',
        'Idaho',
        'Illinois',
        'Indiana',
        'Iowa',
        'Kansas',
        'Kentucky',
        'Louisiana',
        'Maine',
        'Maryland',
        'Massachusetts',
        'Michigan',
        'Minnesota',
        'Missouri',
        'Mississippi',
        'Montana',
        'North-Carolina',
        'North-Dakota',
        'Nebraska',
        'New-Hampshire',
        'New-Jersey',
        'New-Mexico',
        'Nevada',
        'New-York',
        'Ohio',
        'Oklahoma',
        'Oregon',
        'Pennsylvania',
        'Rhode-Island',
        'South-Carolina',
        'South-Dakota',
        'Tennessee',
        'Texas',
        'Utah',
        'Vermont',
        'Virginia',
        'Washington',
        'West-Virginia',
        'Wisconsin',
        'Wyoming'
]


def downloadStates():
    for state in states:
        state = state.lower()
        print('downloading ' + state)
        downloadState(state)


def downloadState(state):
    js = getStateJson(state)
    counts = getStateCounts(js)
    saveStateCounts(counts, state)


def getStateJson(state):
    return requests.get(f'https://static01.nyt.com/elections-assets/2020/data/api/2020-11-03/race-page/{state}/president.json')


def getStateCounts(state_json):
    races = state_json.json()['data']['races'][0]['timeseries']

    ret = pd.DataFrame(races)
    ret['biden'] = [v['bidenj'] for v in ret['vote_shares']]
    ret['trump'] = [v['trumpd'] for v in ret['vote_shares']]

    del ret['vote_shares']

    return ret


def saveStateCounts(state_times, state_name):
    state_times.to_csv(f'data/{state_name}.csv', index = None)
