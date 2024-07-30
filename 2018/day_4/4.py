import re 

class LogEntry():
    def __init__(self,line):

        #[1518-11-05 00:03] Guard #99 begins shift
        #[1518-11-05 00:45] falls asleep
        #[1518-11-05 00:55] wakes up        
        x = re.match("\[(\d{4})-(\d{2})-(\d{2}) (\d{2})\:(\d{2})\] (.+)$",line)
        self.year = int(x.groups()[0])
        self.month = int(x.groups()[1])
        self.day = int(x.groups()[2])
        self.hour = int(x.groups()[3])
        self.min = int(x.groups()[4])
        self.event = x.groups()[5]
        if "Guard" in self.event:
            x = re.match("Guard \#(\d+) ",self.event)
            self.guard_number = int(x.groups()[0])
        else:
            self.guard_number = -1


def calc_sleep_minutes(entries):
    g = {}
    asleep_minutes = {}
    current_guard = 0
    start_time = 0
    end_time = 0
    for e in entries:
        if e.guard_number > 0:
            current_guard = e.guard_number
            if current_guard not in asleep_minutes.keys():
                asleep_minutes[current_guard] = {}
        elif "asleep" in e.event:
            start_time = e.min
        else:
            end_time = e.min
            if current_guard in g.keys():
                g[current_guard] += (end_time - start_time)
            else:
                g[current_guard] = (end_time - start_time)
            for min in range(start_time,end_time):
                if min in asleep_minutes[current_guard].keys():
                    asleep_minutes[current_guard][min] += 1
                else:
                    asleep_minutes[current_guard][min] = 1

    return g,asleep_minutes

def get_max_key_from_dict(d):
    max_val = 0
    max_key = 0
    for k,v in d.items():
        if v > max_val:
            max_val = v
            max_key = k
    return max_key

def get_max_val_from_double(d):
    max_parent_key = 0
    max_sub_key = 0
    max_val = 0
    for k,v in d.items():
        for kk,vv in v.items():
            if vv > max_val:
                max_val = vv 
                max_sub_key = kk 
                max_parent_key = k 
    return max_parent_key, max_sub_key, max_val

if __name__ == "__main__":
    log = []
    f = open("input-4.txt", "r")
    entries = f.read().splitlines()
    for e in entries:
        log.append(LogEntry(e))
    sorted_log = sorted(log,key=lambda x:(x.year, x.month, x.day, x.hour, x.min))

    sleep_totals, sleep_minutes = calc_sleep_minutes(sorted_log)
    max_guard_id = get_max_key_from_dict(sleep_totals)
    max_guard_worst_min = get_max_key_from_dict(sleep_minutes[max_guard_id])
    p1_result = max_guard_id * max_guard_worst_min
    print(p1_result)

    worst_guard, worst_min, num_minutes = get_max_val_from_double(sleep_minutes)
    p2_result = worst_guard * worst_min 
    print(p2_result)