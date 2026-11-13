import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
# lots f1 = (2, 1) et f2 = (1, 1) ; un f1 + trois f2 = (5, 4)
q, g = 3.4, 1.0
def lot(x, y, nb, nv, w, role):
    box(ax, x, y, w, 10.5, role, r=0.6)
    for i in range(nb):
        box(ax, x + 1.6 + i * (q + g), y + 5.4, q, q, 'sujet', r=0.3, lw=0.6)
    for i in range(nv):
        box(ax, x + 1.6 + i * (q + g), y + 1.5, q, q, 'autre', r=0.3, lw=0.6)
text(ax, 14, 50, r'$f_1 = (2,\ 1)$', 'varie', 's', weight='bold')
text(ax, 50, 50, r'$f_2 = (1,\ 1)$', 'varie', 's', weight='bold')
lot(6, 32, 2, 1, 12, 'varie')
text(ax, 25, 37, '+', 'encre', 'l')
for k in range(3):
    lot(32 + k * 12, 32, 1, 1, 8, 'varie')
text(ax, 50, 27, '3 lots', 'varie', 's')
box(ax, 2, 26, 3.4, 3.4, 'sujet', r=0.3, lw=0.6); text(ax, 7, 27.7, 'riz', 'sujet', 's', ha='left')
box(ax, 2, 20, 3.4, 3.4, 'autre', r=0.3, lw=0.6); text(ax, 7, 21.7, 'lentilles', 'autre', 's', ha='left')
arrow(ax, (44, 26), (44, 18.5), 'resultat', lw=1.3)
text(ax, 44, 12, r'5 kg de riz et 4 kg de lentilles : $(5,\ 4)$', 'resultat', 's', weight='bold')
text(ax, 44, 4, r'$f_1 + 3\,f_2 = (2,\ 1) + (3,\ 3) = (5,\ 4)$', 'encre', 's')
save(fig, '58-014')
