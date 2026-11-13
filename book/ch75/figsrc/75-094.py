import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 60, r'3 vecteurs non nuls sur $F_2$', 'encre', 'm')
pts = [(24, 24, r'$(1,0)$'), (56 - 6, 24, r'$(0,1)$'), (37, 44, r'$(1,1)$')]
pts = [(14, 22, r'$(1,0)$'), (46, 22, r'$(0,1)$'), (30, 46, r'$(1,1)$')]
for x, y, l in pts: disc(ax, x, y, 3, 'sujet')
text(ax, 14, 15.5, pts[0][2], 'sujet', 's'); text(ax, 46, 15.5, pts[1][2], 'sujet', 's'); text(ax, 30, 53, pts[2][2], 'sujet', 's')
arrow(ax, (18, 24), (42, 24), 'varie', lw=0.9, both=True)
arrow(ax, (44, 26), (32, 43), 'varie', lw=0.9, both=True)
arrow(ax, (28, 43), (16, 26), 'varie', lw=0.9, both=True)
text(ax, 64, 42, '3 choix', 'encre', 's'); text(ax, 64, 34, '× 2 choix', 'encre', 's'); text(ax, 64, 26, '× 1 choix', 'encre', 's')
text(ax, 64, 17, '= 6', 'resultat', 'l')
text(ax, 44, 5, 'dont 3 rotations : sous-groupe → non simple', 'limite', 's')
save(fig, '75-094')
