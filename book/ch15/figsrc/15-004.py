import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
box(ax, 6, 66, 24, 7, 'sujet', label=r'$6n+40$'); box(ax, 36, 66, 24, 7, 'autre', label=r'$4n+70$')
y0 = 17
line(ax, [(5, y0), (83, y0)], 'fixe')
s = 0.28
for cx, n, a, b, w in ((22, 10, 100, 110, 'bleu moins cher'), (48, 15, 130, 130, 'prix égaux'), (74, 20, 160, 150, 'violet moins cher')):
    box(ax, cx - 9, y0, 8, a * s, 'sujet'); box(ax, cx + 1, y0, 8, b * s, 'autre')
    text(ax, cx - 5, y0 + a * s + 2.5, str(a), 'sujet', 's'); text(ax, cx + 5, y0 + b * s + 2.5, str(b), 'autre', 's')
    text(ax, cx, y0 - 4.5, f'n = {n}', 'encre', 's', weight='bold')
    text(ax, cx, y0 - 10, w, 'resultat', 's')
save(fig, '15-004')
