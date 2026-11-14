import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
cols = [(2, 20, r'$a,\ b$'), (24, 28, r'$a\vee b$'), (54, 32, r'$a+b$')]
roles = ['sujet', 'resultat', 'varie']
for (x, w_, h), r_ in zip(cols, roles):
    text(ax, x + w_ / 2, 66, h, r_, 'm')
data = [('0, 0', 0, 0), ('0, 1', 1, 1), ('1, 0', 1, 1), ('1, 1', 1, 0)]
for k, (ab, o, s) in enumerate(data):
    y = 46 - k * 11
    diff = (ab == '1, 1')
    box(ax, 2, y, 20, 9, 'fixe', label=ab, size='s')
    box(ax, 24, y, 28, 9, 'resultat' if o else 'fixe', label=str(o), size='m')
    box(ax, 54, y, 32, 9, ('limite' if diff else ('varie' if s else 'fixe')), label=str(s), size='m')
text(ax, 44, 6, 'seul cas différent : 1 et 1', 'limite', 'm')
save(fig, '80-206')
