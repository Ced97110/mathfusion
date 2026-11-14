import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 56, '5 groupes transitifs possibles', 'sujet', 'm')
groups = [(r'$A_4$', 12, 'carré'), (r'$V$', 4, 'carré'), (r'$S_4$', 24, 'non'), (r'$D$', 8, 'non'), (r'$C$', 4, 'non')]
w, gap, x0 = 13.0, 2.0, 3.0
cx = []
for i, (nm, n, kind) in enumerate(groups):
    x = x0 + i * (w + gap) + (3 if i >= 2 else 0)
    box(ax, x, 34, w, 14, 'sujet', label=nm + '\n' + str(n), size='s')
    cx.append(x + w / 2)
box(ax, 4, 8, 30, 12, 'varie', label=r'$d$ est un carré', size='s')
box(ax, 38, 8, 46, 12, 'fixe', label=r'$d$ n’est pas un carré', size='s')
for i, (nm, n, kind) in enumerate(groups):
    if kind == 'carré':
        arrow(ax, (cx[i], 33), (4 + 8 + i * 14, 21), 'varie')
    else:
        arrow(ax, (cx[i], 33), (38 + 8 + (i - 2) * 15, 21), 'fixe')
text(ax, 44, 1.5, '2 réponses seulement', 'varie', 's')
save(fig, '65-081')
