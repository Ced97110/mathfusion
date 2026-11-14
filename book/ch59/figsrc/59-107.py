import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
cw, h, x0 = 5.0, 7, 26
text(ax, 44, 76, 'diag(2, 10, 0)', 'encre', 'm', weight='bold')
def cells(y, n, role, hl=None):
    for i in range(n):
        box(ax, x0 + i * cw, y, cw, h, 'varie' if i == hl else role, r=0.3)
def retour(y, n, label, off):
    a = (x0 + n * cw - cw / 2, y - 0.5)
    b = (x0 + cw / 2, y - 0.5)
    arrow(ax, a, b, 'fixe', lw=0.9, curve=-0.25)
    text(ax, x0 + n * cw / 2, y - off, label, 'fixe', 's')
# ligne 1 : 2 éléments
text(ax, 4, 58 + h / 2, 'ann = (2)', 'fixe', 's', ha='left')
cells(58, 2, 'fixe'); retour(58, 2, 'retour à 0 après 2', 5.5)
# ligne 2 : 10 éléments
text(ax, 4, 38 + h / 2, 'ann = (10)', 'fixe', 's', ha='left')
cells(38, 10, 'fixe'); retour(38, 10, 'retour à 0 après 10', 10)
# ligne 3 : copie de l'anneau
text(ax, 4, 12 + h / 2, 'ann = (0)', 'sujet', 's', ha='left')
cells(12, 8, 'sujet', hl=5)
arrow(ax, (x0 + 8 * cw + 1, 12 + h / 2), (x0 + 8 * cw + 11, 12 + h / 2), 'sujet', lw=1.0)
text(ax, x0 + 5.5 * cw, 12 + h + 4, '5·z₃ ≠ 0', 'varie', 's')
text(ax, x0 + 4 * cw, 3, 'jamais de retour à 0 : libre', 'sujet', 's')
save(fig, '59-107')
