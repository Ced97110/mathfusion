import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(94)
ROLES = ['sujet', 'varie', 'resultat']; N = [4, 5, 3]; L = ['A', 'B', 'C']
def panel(y0, dy, const, title, trole):
    text(ax, 44, y0 + 3 * dy + 1.5, title, trole, 'm', weight='bold')
    for i in range(3):
        y = y0 + (2 - i) * dy
        box(ax, 4, y - 4, 4 + N[i] * 5.4 + 1, 8, 'fixe', dash=True)
        for k in range(N[i]): disc(ax, 8.2 + k * 5.4, y, 2.1, 'fixe')
        box(ax, 62, y - 4, 22, 8, ROLES[i], label=L[i], weight='bold')
        tgt = 0 if const else i
        yt = y0 + (2 - tgt) * dy
        a = (4 + N[i] * 5.4 + 2.2, y); b = (61, yt)
        arrow(ax, a, b, trole, lw=1.0)
panel(58, 10, False, r'$\nu$ canonique : pion $\to$ sa boîte', 'sujet')
panel(14, 10, True, 'pas canonique : tout vers A', 'limite')
text(ax, 44, 3, 'les groupes B et C sont ignorés', 'limite', 's')
text(ax, 10, 89, r'$S$', 'fixe', 'm'); text(ax, 73, 89, r'$S/E$', 'fixe', 'm')
save(fig, '43-081')
