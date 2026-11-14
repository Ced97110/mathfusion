import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
def chain(y, items, role):
    x = 6; xs = []
    for k, it in enumerate(items):
        w = 8 if it == 'dots' else 10
        if it == 'dots': text(ax, x + w / 2, y + 4.5, r'$\cdots$', role, 'm')
        else: box(ax, x, y, w, 9, role, label=it, size='m')
        xs.append((x, x + w)); x += w
        if k < len(items) - 1:
            c = x + 3; line(ax, [(c - 1.3, y + 3.2), (c + 1.3, y + 5.8)], 'fixe'); line(ax, [(c - 1.3, y + 5.8), (c + 1.3, y + 3.2)], 'fixe'); x += 6
    return xs[0][0], xs[-1][1]
a, b = chain(62, [r'$A$', r'$A$', 'dots', r'$A$'], 'sujet')
brace(ax, a, b, 60, 'sujet', r'$n$ facteurs')
text(ax, 66, 66.5, r'$=A^{n}$', 'resultat', 'l', ha='left', weight='bold')
chain(36, [r'$\mathbb{R}$'] * 2, 'sujet'); text(ax, 66, 40.5, r'$=\mathbb{R}^{2}$ plan', 'resultat', 'm', ha='left')
chain(12, [r'$\mathbb{R}$'] * 3, 'sujet'); text(ax, 66, 16.5, r'$=\mathbb{R}^{3}$ espace', 'resultat', 'm', ha='left')
save(fig, '42-170')
