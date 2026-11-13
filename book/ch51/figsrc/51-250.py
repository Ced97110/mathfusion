import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
GX, SY = 2.08, 1.78
def mat(ax, cx, cy, M, role='sujet'):
    t = text(ax, cx, cy, f'{M[0][0]}   {M[0][1]}\n{M[1][0]}   {M[1][1]}', role, 'm'); t.set_linespacing(1.5)
    for s in (-1, 1):
        x = cx + s * 4.6
        line(ax, [(x - s * 1.2, cy + 4.4), (x, cy + 4.4), (x, cy - 4.4), (x - s * 1.2, cy - 4.4)], role, lw=0.8)
def cell(cx, cy, r, c): return (cx + (c - 0.5) * 2 * GX, cy + (0.5 - r) * 2 * SY)
def hl(ax, x, y, w, h, role='varie'):
    ax.add_patch(Rectangle((x, y), w, h, fc=FILL[role], ec=COL[role], lw=0.6, zorder=1))
fig, ax = canvas(76)
def groupe(cx, labels, role):
    for k, lab in enumerate(labels):
        r, c = divmod(k, 2)
        box(ax, cx - 10.5 + 11 * c, 52 - 11 * r, 10, 10, role, label=lab)
text(ax, 22, 71, r'$F$ : 4 tableaux', 'sujet', 'm')
groupe(22, ['0', '$I$', '$A$', '$B$'], 'sujet')
text(ax, 22, 35, r'$A \times B = I$', 'resultat', 'm')
text(ax, 66, 71, 'ℤ/4 : 4 nombres', 'autre', 'm')
groupe(66, ['0', '1', '2', '3'], 'autre')
text(ax, 66, 35, r'$2 \times 2 = 0$', 'limite', 'm')
# signe « différent » dessiné : deux traits et une barre oblique
line(ax, [(41, 49), (47, 49)], 'limite', lw=1.2); line(ax, [(41, 46), (47, 46)], 'limite', lw=1.2)
line(ax, [(42, 44.5), (46, 50.5)], 'limite', lw=1.2)
text(ax, 44, 20, r'$F$ : le seul corps à 4 éléments', 'sujet', 'm')
text(ax, 44, 12.5, 'à nommer près (chapitre 67)', 'sujet', 'm')
save(fig, '51-250')
