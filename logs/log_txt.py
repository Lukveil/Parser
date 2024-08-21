import re
from datetime import datetime
import bd


def log_pars(list_log):

    count_day = 1
    version = 0
    project = 0
    test = 0
    time_ob = 1
    time_day = 'PM'
    new_time_day = 'PM'
    text = ' '
    team = 0
    user = 0
    for id_list in list_log:
        if id_list not in ['Cloud bot', '']:

            if re.search(r"\s+(\d{1,2}:\d{2}\s+(PM|AM))", id_list) or re.search(r"APP\s+(\d{1,2}:\d{2}\s+(PM|AM))", id_list):
                name_time = id_list.split(' ')
                time_ob = datetime.strptime(f"{name_time[2]} {name_time[3]}", "%I:%M %p").time()
                time_day = name_time[3]

                continue

            elif re.search(r"\d{1,2}:\d{2}", id_list):
                time_ob = datetime.strptime(id_list, "%H:%M").time()
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
                        text = ' '.join(new_list[new_list.index('user') + 2:])
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
                            if text[0] == ' ':
                                text = text[0:]

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

                if 'запустил' in new_list and 'test' in new_list:
                    text = 'запустил тест'

                if 'стартовал' in new_list and 'grafana' in new_list:
                    text = 'стартовал grafana'

                if text[0] == ' ':
                    text = text[1:]

                full_date = datetime.strptime(f"{count_day} {time_ob}", "%d %H:%M:%S").isoformat()
                new_bd = bd.User(day=count_day, time=full_date, user=user, team=team,
                             project=project, version=version, operate=text)
                new_bd.save()


if __name__ == "__main__":
    with open('3monthslo.txt', 'r', encoding='UTF-8') as f:
        list_log = f.read().split("\n")

    log_pars(list_log)




