#!/usr/bin/python3

import json
import os.path

with open(os.path.dirname(__file__) + '/../challenges.json', 'r') as file_challenges, open(os.path.dirname(__file__) + '/../README.md', 'w') as fout:
  fout.write('HackerRank Solutions in Python3\n======\n')
  json_root = json.loads(file_challenges.read())
  for track in json_root['tracks']:
    fout.write(track['title'] + '\n------\n$')
    for chapter in track['chapters']:
      for challenge in chapter['challenges']:
        path_to_challenge = '/../solution/practice/' + track['name'] + '/' + chapter['name'] + '/' + challenge['name']
