import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 4, 64, 'ordre de 4 h : un nombre', 'sujet', 's', ha='left', weight='bold')
for x, t in [(14, '4 h'), (40, '8 h'), (66, '0')]:
    disc(ax, x, 50, 5, 'sujet' if t != '0' else 'resultat', label=t, size='s')
arrow(ax, (19.5, 50), (34.5, 50), 'varie', lw=1.0); arrow(ax, (45.5, 50), (60.5, 50), 'varie', lw=1.0)
text(ax, 27, 45, '+ 4 h', 'varie', 's'); text(ax, 53, 45, '+ 4 h', 'varie', 's')
text(ax, 80, 50, 'n = 3', 'sujet', 'l', weight='bold')
text(ax, 4, 31, 'annulateur : un ensemble', 'resultat', 's', ha='left', weight='bold')
f = numberline(ax, 6, 78, 18, 0, 12, labels=False, arrow_right=False)
for v in range(13):
    if v % 3 == 0:
        disc(ax, f(v), 18, 2.3 if v == 3 else 1.7, 'sujet' if v == 3 else 'resultat')
        text(ax, f(v), 11.5, str(v), 'sujet' if v == 3 else 'resultat', 's')
text(ax, 44, 3.5, 'n = 3 est le plus petit ; il y a aussi 6, 9, 12', 'resultat', 's')
save(fig, '57-170')
