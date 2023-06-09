import json


def second_assignment():

    with open("2nd assignment\ex5.json","r") as f:
        ex5=json.load(f)

        for x in ex5:
            if x['name'] == 'Old Fashioned' and x['type'] == 'donut':
                z=x['batters']['batter']

                z.append({'id': '1003', 'type': 'Coffee'})

    with open("2nd assignment\ex5.json","w") as out:
        json.dump(ex5,out,indent=4)

second_assignment()