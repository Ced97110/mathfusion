import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import itertools

CODE = ['00000', '01101', '10011', '11110']
def add(a, b):
    return ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))
def syn(w):
    x = [int(c) for c in w]
    return f'{x[1] ^ x[2]}{x[0] ^ x[3]}{x[0] ^ x[1] ^ x[4]}'
classes = {}
for t in itertools.product('01', repeat=5):
    w = ''.join(t); classes.setdefault(syn(w), []).append(w)
fig, ax = canvas(80)
cw, ch, x0 = 16, 6.2, 16
text(ax, 9, 74, 'syndrome', 'resultat', 's')
text(ax, 48, 74, 'mots de la classe', 'encre', 's')
for i, s in enumerate(sorted(classes)):
    ws = classes[s]
    low = min(x.count('1') for x in ws)
    mins = sorted(x for x in ws if x.count('1') == low)
    chef = mins[0]
    y = 66 - i * ch - 3
    text(ax, 9, y + ch / 2, s, 'resultat', 's')
    for k, c in enumerate(CODE):
        wd = add(chef, c)
        assert syn(wd) == s
        role = 'sujet' if wd == chef else ('varie' if wd in mins else 'fixe')
        box(ax, x0 + k * cw, y, cw, ch, role, label=wd, size='s')
ax.add_patch(Rectangle((x0 + 2, 2.5), 3, 3, ec=COL['sujet'], fc=FILL['sujet'], lw=0.6))
text(ax, x0 + 7, 4, 'chef de classe', 'encre', 's', ha='left')
ax.add_patch(Rectangle((x0 + 38, 2.5), 3, 3, ec=COL['varie'], fc=FILL['varie'], lw=0.6))
text(ax, x0 + 43, 4, 'même poids', 'encre', 's', ha='left')
save(fig, '68-169')
