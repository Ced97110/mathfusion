import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
f = numberline(ax, 8, 74, 44, 0, 45, 15, arrow_right=False)
text(ax, 44, 60, 'droite–plan : le plus petit', 'sujet', 's')
for v, r, t in ((21.80, 'resultat', '21,80°'), (42.03, 'fixe', '42,03°')):
    disc(ax, f(v), 44, 1.8, r); text(ax, f(v), 51, t, r, 's')
f2 = numberline(ax, 8, 74, 14, 0, 45, 15, arrow_right=False)
text(ax, 44, 30, 'plan–plan : le plus grand', 'autre', 's')
for v, r, t in ((0, 'fixe', '0°'), (12.70, 'fixe', '12,70°'), (20, 'resultat', '20°')):
    disc(ax, f2(v), 14, 1.8, r); text(ax, f2(v), 21, t, r, 's')
save(fig, '27-120')
