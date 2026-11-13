import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
ys = [70, 58, 46, 34, 22]
text(ax, 14, 84, r'$S$ : 5 lettres', 'sujet', 's')
text(ax, 60, 84, r'$T$ : 3 tiroirs', 'autre', 's')
box(ax, 47, 40, 26, 36, 'autre', fill=False)
for i, y in enumerate(ys):
    disc(ax, 14, y, 3.5, 'sujet')
    ok = i < 3
    box(ax, 51, y - 4, 18, 8, 'autre' if ok else 'limite', dash=not ok, fill=ok)
    arrow(ax, (18, y), (50.5, y), 'varie' if ok else 'limite')
text(ax, 80, 28, 'pas de place', 'limite', 's', ha='center')
text(ax, 38, 8, '5 images, toutes différentes', 'varie', 's')
save(fig, '43-112')
