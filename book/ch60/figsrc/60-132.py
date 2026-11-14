import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
bx, bw, bh = 22, 64, 11
ys = [86, 68, 50, 32, 14]
steps = [(r'$h$ : plus petit ordre hors de $\langle g\rangle$', 'sujet', 'départ'),
         (r'$p\,h$ est dans $\langle g\rangle$ : $p\,h = r\,g$', 'sujet', ''),
         (r'$p$ divise $r$ : $r = p\,s$', 'varie', 'décisive'),
         (r'$a = h - s\,g$, d’ordre $p$, hors de $\langle g\rangle$'.replace('\\u2019', '’'), 'resultat', ''),
         (r'donc $|h| = p$', 'resultat', 'arrivée')]
for y, (s, role, tag) in zip(ys, steps):
    box(ax, bx, y, bw, bh, role, label=s, size='s')
    if tag:
        text(ax, 11, y + bh / 2, tag, role, 's', weight='bold')
for y in ys[:-1]:
    arrow(ax, (bx + bw / 2, y - 0.4), (bx + bw / 2, y - 6.6), 'varie')
text(ax, 44, 6, 'grille : h = (0, 1), |h| = 2 = p', 'fixe', 's')
save(fig, '60-132')
