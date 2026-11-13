import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
f = numberline(ax, 22, 70, 50, 0, 2, step=0.5)
h = lambda a: 22 + a / 90 * 48
numberline(ax, 22, 70, 14, 0, 90, step=30, labels=False)
for v in (0, 30, 60, 90): text(ax, h(v), 9.8, f'{v}°', 'fixe', 's')
text(ax, 22, 58, 'tangente', 'sujet', 's', ha='left')
line(ax, [(f(0.12), 55), (f(2), 55)], 'resultat', lw=1.4); text(ax, 78, 58, 'tout nombre > 0', 'resultat', 's', ha='right')
text(ax, 22, 5, 'angle aigu', 'sujet', 's', ha='left')
for v in (0.5, 0.75, 1, 1.5, 2):
    a = math.degrees(math.atan(v))
    arrow(ax, (f(v), 43), (h(a), 17), 'varie')
    disc(ax, f(v), 50, 1.3, 'resultat'); disc(ax, h(a), 14, 1.3, 'resultat')
line(ax, [(f(0), 32), (f(0), 47)], 'limite', dash=True); text(ax, f(0), 33, '×', 'limite', 'l')
text(ax, 11, 32, 'aucun angle', 'limite', 's')
disc(ax, f(0), 50, 1.6, 'limite'); disc(ax, h(0), 14, 1.6, 'limite')
save(fig, '25-130')
