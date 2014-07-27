import json

json_data=open('lineup_2014.json')

lineups = json.load(json_data)
json_data.close()

for lineup in lineups:
    del lineup['ids']
    for show in lineup['shows']:
        show['time_start'], show['time_end'] = str(show['time']).split(" - ")
        show['time_start'] = "".join([str(12+int(time)) if len(time) == 1 else time for time in show['time_start'].split(":")])
        show['time_end'] = "".join([str(12+int(time)) if len(time) == 1 else time for time in show['time_end'].split(":")])
        print show['time_start'], show['time_end']

out = open('../lineup_2014_new.json', 'w')
print >> out, json.dumps(lineups, indent=4)
out.close()