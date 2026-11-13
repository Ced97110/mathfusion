import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cx, cy, R = 24, 31, 20
def P(k): a = math.radians(90 - 360 * k / 7); return (cx + R * math.cos(a), cy + R * math.sin(a))
disc(ax, cx, cy, R, 'fixe', fill=False, lw=0.5)
for k in range(7):
    x, y = P(k); disc(ax, x, y, 3.4, 'varie' if k == 0 else 'sujet', label=str(k))
text(ax, 66, 54, 'diviseurs de 7', 'encre', 's')
text(ax, 66, 48, '1 et 7 seulement', 'encre', 's')
text(ax, 55, 36, '1', 'sujet', 'm'); box(ax, 62, 31, 22, 9, 'varie', label='{0}')
text(ax, 55, 20, '7', 'sujet', 'm'); box(ax, 62, 15, 22, 9, 'sujet', label='0 à 6', size='s')
text(ax, 66, 8, 'deux sous-groupes', 'resultat', 's')
save(fig, '46-263')
