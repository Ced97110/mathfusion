import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 23, 68, 'restes par 12, groupés', 'fixe', 's'); text(ax, 73, 68, 'restes par 4', 'fixe', 's')
labs = ['0 · 4 · 8', '1 · 5 · 9', '2 · 6 · 10', '3 · 7 · 11']
for r, s in enumerate(labs):
    y = 50 - r * 14
    box(ax, 3, y, 40, 9, 'varie' if r == 0 else 'sujet', label=s)
    arrow(ax, (43, y + 4.5), (66, y + 4.5), 'fixe')
    box(ax, 66, y, 14, 9, 'resultat', label=str(r))
text(ax, 54, 59, 'noyau', 'varie', 's')
save(fig, '52-268')
