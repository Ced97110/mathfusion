import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
# e1 = f1 - f2 et e2 = 2 f2 - f1, avec des kilos
q, g = 3.0, 0.9
def lot(x, y, nb, nv, role):
    w = 11.0
    box(ax, x, y, w, 9.5, role, r=0.6)
    for i in range(nb):
        box(ax, x + 1.4 + i * (q + g), y + 5.0, q, q, 'sujet', r=0.3, lw=0.6)
    for i in range(nv):
        box(ax, x + 1.4 + i * (q + g), y + 1.3, q, q, 'autre', r=0.3, lw=0.6)
    return x + w / 2
# ligne 1 : f1 - f2 = e1
y1 = 40
c = lot(4, y1, 2, 1, 'varie'); text(ax, c, y1 - 3.5, r'$f_1$', 'varie', 's')
text(ax, 21, y1 + 4.7, '−', 'encre', 'l')
c = lot(26, y1, 1, 1, 'varie'); text(ax, c, y1 - 3.5, r'$f_2$', 'varie', 's')
text(ax, 43, y1 + 4.7, '=', 'encre', 'l')
c = lot(48, y1, 1, 0, 'resultat'); text(ax, c, y1 - 3.5, r'$e_1$', 'resultat', 's')
text(ax, 75, y1 + 4.7, '(1, 0)', 'resultat', 's')
# ligne 2 : 2 f2 - f1 = e2
y2 = 12
lot(4, y2, 1, 1, 'varie'); c = lot(16, y2, 1, 1, 'varie'); text(ax, 15.5, y2 - 3.5, r'$2\,f_2$', 'varie', 's')
text(ax, 33, y2 + 4.7, '−', 'encre', 'l')
c = lot(38, y2, 2, 1, 'varie'); text(ax, c, y2 - 3.5, r'$f_1$', 'varie', 's')
text(ax, 55, y2 + 4.7, '=', 'encre', 'l')
c = lot(60, y2, 0, 1, 'resultat'); text(ax, c, y2 - 3.5, r'$e_2$', 'resultat', 's')
text(ax, 83, y2 + 4.7, '(0, 1)', 'resultat', 's', ha='right')
box(ax, 4, 59, 3.4, 3.4, 'sujet', r=0.3, lw=0.6); text(ax, 9, 60.7, 'riz', 'sujet', 's', ha='left')
box(ax, 22, 59, 3.4, 3.4, 'autre', r=0.3, lw=0.6); text(ax, 27, 60.7, 'lentilles', 'autre', 's', ha='left')
save(fig, '58-015')
