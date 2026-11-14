import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
box(ax, 4, 86, 80, 10, 'sujet', label='départ : r − s reste dans S', size='s')
steps = [(66, r'$r-r=0$', r'$6-6=0$', 'fixe'), (48, r'$0-s=-s$', r'$0-9=-9$', 'varie'), (30, r'$r-(-s)=r+s$', r'$6-(-9)=15$', 'fixe')]
for y, g, n, role in steps:
    box(ax, 4, y, 62, 12, role, label=None)
    text(ax, 22, y + 6, g, role if role == 'varie' else 'encre', 's')
    text(ax, 52, y + 6, n, role if role == 'varie' else 'encre', 's')
for y0, y1 in [(86, 78), (66, 60), (48, 42), (30, 22)]:
    arrow(ax, (35, y0), (35, y1), 'fixe')
text(ax, 76, 54, 'étape qui\nporte le poids', 'varie', 's')
box(ax, 4, 10, 80, 12, 'resultat', label=r'arrivée : $r+s$ = 6 + 9 = 15', size='s')
save(fig, '51-087')
