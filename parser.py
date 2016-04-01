import sys
import yaml

NAMES = {
    'Arsenal FC': 'arsenal',
    'Arsenal': 'arsenal',
    'AFC Bournemouth': 'bournemouth',
    'Watford FC': 'watford',
    'Sunderland AFC': 'sunder',
    'Sunderland': 'sunder',
    'Fulham FC': 'fulham',
    'Fulham': 'fulham',
    'Norwich City': 'norwich',
    'Norwich': 'norwich',
    'Queens Park Rangers': 'qpr',
    'QPR': 'qpr',
    'Swansea City': 'swansea',
    'Swansea': 'swansea',
    'Leicester City': 'leicester',
    'Burnley FC': 'burnley',
    'Reading FC': 'reading',
    'Reading': 'reading',
    'Stoke City': 'stoke',
    'Stoke': 'stoke',
    'FC Stoke City': 'stoke',
    'FC  Stoke City': 'stoke',
    'West Bromwich Albion': 'west brom',
    'West Brom': 'west brom',
    'West Bromwich': 'west brom',
    'Cardiff City': 'cardiff',
    'Crystal Palace': 'crystal palace',
    'Liverpool FC': 'liverpool',
    'Liverpool': 'liverpool',
    'Hull City': 'hull city',
    'West Ham United': 'west ham',
    'West Ham': 'west ham',
    'Aston Villa': 'aston villa',
    'Newcastle United': 'newcastle',
    'Newcastle': 'newcastle',
    'Tottenham Hotspur': 'tottenham',
    'Tottenham': 'tottenham',
    'Wigan Athletic': 'wigan',
    'Wigan': 'wigan',
    'Chelsea FC': 'chelsea',
    'FC Chelsea FC': 'chelsea',
    'Chelsea': 'chelsea',
    'Manchester City': 'manchester city',
    'Manchester C': 'manchester city',
    'Southampton FC': 'southampton',
    'Southampton': 'southampton',
    'Everton FC': 'everton',
    'Everton': 'everton',
    'Manchester United': 'manchester united',
    'Manchester U': 'manchester united'
}

def parse_premier(l):
    out = {}
    round = -1
    date = None, None
    for m in l:
        if m.startswith('Matchday'):
            round += 1
        if m.startswith('['):
            date = m[1:-1].split(' ')[-1]
        if m.startswith('  '):
            print(m)
            host_q, guest_q = m[2:].split('-')
            print(host_q)
            print(guest_q)
            print(m)
            host, _, host_goals = host_q.strip().rpartition(' ')
            guest_goals, _, guest = guest_q.strip().partition(' ')
            host_goals, guest_goals = int(host_goals), int(guest_goals)
            host, guest = NAMES[host.strip()], NAMES[guest.strip()]
            if host not in out:
                out[host] = []
            if guest not in out:
                out[guest] = []
            out[host].append({'role': 'H', 'other': guest, 'home': host_goals, 'away': guest_goals, 'date': date})
            out[guest].append({'role': 'A', 'other': host, 'home': host_goals, 'away': guest_goals, 'date': date})
    return out


def main():
    if len(sys.argv) < 3:
        print('pass an year and a premier filenames')
    else:
        year = sys.argv[1]
        filenames = sys.argv[2:]
        m = []
        for filename in filenames:
            with open(filename, 'r') as f:
                m += f.read().split('\n')[4:]

        yaml.Dumper.ignore_aliases = lambda *args : True
        with open('premier_league_%s.yaml' % year, 'w') as f:
            f.write(yaml.dump(parse_premier(m)))

if __name__ == '__main__':
    main()
