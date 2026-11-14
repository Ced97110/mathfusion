import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
text(ax, 44, 63, r'$h\in H=\{0,2,4\}$,  $k\in K=\{0,3\}$', 'encre', 's')
box(ax, 4, 40, 38, 10, 'sujet', label=r'$2+3=5$', size='m')
box(ax, 46, 40, 38, 10, 'autre', label=r'$3+2=5$', size='m')
text(ax, 23, 54, r'$hk$', 'sujet', 's'); text(ax, 65, 54, r'$kh$', 'autre', 's')
text(ax, 44, 45, r'$=$', 'resultat', 'xl')
text(ax, 44, 32, 'on refait pour les 6 couples', 'encre', 's')
hs = [0, 2, 4]; ks = [0, 3]
x0, y0, cw, ch = 40, 6, 14, 10
for i, h in enumerate(hs):
    text(ax, x0 + i * cw + cw / 2, y0 + 2 * ch + 3, str(h), 'sujet', 's')
for j, k in enumerate(ks):
    text(ax, x0 - 4, y0 + (1 - j) * ch + ch / 2, str(k), 'autre', 's')
    for i, h in enumerate(hs):
        box(ax, x0 + i * cw, y0 + (1 - j) * ch, cw - 1, ch - 1, 'resultat', label=str((h + k) % 6), size='s')
text(ax, 18, 24, r'$h$ en haut', 'sujet', 's'); text(ax, 18, 17, r'$k$ à gauche', 'autre', 's')
text(ax, 18, 10, r'$hk=kh$', 'resultat', 's'); text(ax, 18, 5, 'dans les 6 cases', 'resultat', 's')
save(fig, '45-210')
