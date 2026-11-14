import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import itertools

def syn(w):
    x = [int(c) for c in w]
    return f'{x[1] ^ x[2]}{x[0] ^ x[3]}{x[0] ^ x[1] ^ x[4]}'
classes = {}
for t in itertools.product('01', repeat=5):
    w = ''.join(t); classes.setdefault(syn(w), []).append(w)
fig, ax = canvas(76)
text(ax, 26, 70, 'syndrome', 'resultat', 's')
text(ax, 64, 70, 'chef de classe', 'sujet', 's')
for i, s in enumerate(sorted(classes)):
    ws = classes[s]
    low = min(x.count('1') for x in ws)
    chef = sorted(x for x in ws if x.count('1') == low)[0]
    y = 56 - i * 7.5
    box(ax, 14, y, 24, 6.5, 'resultat', label=s, size='s')
    arrow(ax, (39, y + 3.25), (45, y + 3.25), 'fixe')
    box(ax, 46, y, 36, 6.5, 'sujet', label=chef, size='s')
save(fig, '68-173')
