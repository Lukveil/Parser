import re
from datetime import datetime
import bd
with open('3monthslo.txt', 'r', encoding='UTF-8') as f:
    list_log = f.read().split("\n")



count_day = 1
version = 0
project = 0
test = 0
time_day = 'PM'
new_time_day = 'PM'

for id_list in list_log:
    if id_list != 'Cloud bot':
        if re.search(r"APP\s+(\d{1,2}:\d{2}\s+(PM|AM))", id_list) or re.search(r"\s+(\d{1,2}:\d{2}\s+(PM|AM))", id_list):
            name_time = id_list.split(' ')
            time_ob = datetime.strptime(name_time[2], "%H:%M").time()
            time_day = name_time[3]
            print(time_ob)
            continue
        elif re.search(r"\d{1,2}:\d{2}", id_list):
            time_ob = datetime.strptime(id_list, "%H:%M").time()
            print(time_ob)
            continue
        if time_day == 'PM':
            new_time_day = time_day

        if time_day == 'AM' and new_time_day == 'PM':
            count_day += 1
            new_time_day = time_day

        else:
            new_list = id_list.split(' ')

            if 'user' in new_list:
                try:
                    user = int(new_list[new_list.index('user') + 1])
                except:
                    user = 0
                    text = ' '.join(new_list[new_list.index('user') + 2:])

            if 'team' in new_list:
                try:
                    team = int(new_list[new_list.index('team') + 1])
                    text = ' '.join(new_list[new_list.index('team') + 2:])
                except:
                    try:
                        team = int(new_list[new_list.index('team') + 2])
                        text = ' '.join(new_list[new_list.index('team') + 3:])
                    except:
                        team = 0

            if 'test' in new_list:
                test = int(new_list[new_list.index('test') + 1])
                text = ' '.join(new_list[new_list.index('test') + 2:])

            if 'project' in new_list:
                    project = int(new_list[new_list.index('project') + 1][:-1])
                    text = ' '.join(new_list[new_list.index('project') + 2:])

            if 'version' in new_list:
                version = int(new_list[new_list.index('version') + 1])
                text = ' '.join(new_list[new_list.index('version') + 2:])


            full_date = datetime.strptime(f"{count_day} {time_ob}", "%d %H:%M:%S").isoformat()
            new_bd = bd.User(day=count_day, time=full_date, user=user, team=team,
                             project=project, version=version, operate=text)
            new_bd.save()







