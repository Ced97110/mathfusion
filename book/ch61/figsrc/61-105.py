import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
ys = [78, 56, 34, 12]
txts = [(r'$z=2+\sqrt{2}+5\sqrt{3}+3\sqrt{6}$', 'sujet'),
        (r'$(2+\sqrt{2})\,1+(5+3\sqrt{2})\sqrt{3}$', 'fixe'),
        (r'$2+\sqrt{2}=2\cdot1+1\cdot\sqrt{2}$', 'varie'),
        (r'$z=2\cdot1+1\cdot\sqrt{2}+5\cdot\sqrt{3}+3\cdot\sqrt{6}$', 'resultat')]
for y, (s, r) in zip(ys, txts):
    box(ax, 4, y, 80, 11, r, label=s, size='s')
labs = [(r'regrouper : coefficients dans $K$', 'fixe'),
        (r'chaque coefficient en briques de $K$', 'varie'),
        (r'coefficients dans $F$ : 2, 1, 5, 3', 'resultat')]
for y, (s, r) in zip(ys[:-1], labs):
    arrow(ax, (10, y), (10, y - 11), r)
    text(ax, 14, y - 5.5, s, r, 's', ha='left')
save(fig, '61-105')
