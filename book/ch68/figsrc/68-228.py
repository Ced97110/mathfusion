import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 72, r'ligne $A$, équations $A$, $B$, $C$', 'encre', 'm', weight='bold')
A, B, C = '0001111', '0110011', '1010101'
x0, cw, sz = 24, 7.0, 6.2
for i in range(7):
    text(ax, x0 + i * cw + sz / 2, 63, str(i + 1), 'fixe', 's')
text(ax, 79, 63, 'communs', 'fixe', 's')
def row(y, s, mode):
    n = 0
    for i, c in enumerate(s):
        if c == '1' and mode == 'test': fc = COL['varie']
        elif c == '1' and A[i] == '1': fc = COL['resultat']; n += 1
        elif c == '1': fc = COL['sujet']
        else: fc = FILL['fixe']
        ax.add_patch(Rectangle((x0 + i * cw, y), sz, sz, fc=fc, ec=COL['fixe'], lw=0.5, zorder=2))
    return n
text(ax, 3, 55, 'mot testé', 'varie', 's', ha='left')
row(52, A, 'test')
line(ax, [(3, 47), (85, 47)], 'fixe', lw=0.6, dash=True)
for y, s, nm in ((38, A, 'A'), (29, B, 'B'), (20, C, 'C')):
    text(ax, 3, y + 3, f'éq. {nm}', 'sujet', 's', ha='left')
    n = row(y, s, 'eq')
    text(ax, 79, y + 3, str(n), 'resultat', 'l', weight='bold')
ax.add_patch(Rectangle((24, 8), 4.5, 4.5, fc=COL['resultat'], ec=COL['fixe'], lw=0.5, zorder=2))
text(ax, 31, 10.3, '1 en commun avec le mot testé', 'fixe', 's', ha='left')
text(ax, 44, 3, 'comptes pairs : mot du code', 'resultat', 's')
save(fig, '68-228')
