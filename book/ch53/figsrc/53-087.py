import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
for cx, (p, q, n) in [(22, (5, 11, 55)), (66, (23, 29, 667))]:
    phi = (p - 1) * (q - 1)
    for dx, v, v2 in [(-17, p, p - 1), (1, q, q - 1)]:
        box(ax, cx + dx, 60, 16, 10, 'sujet', label=str(v))
        box(ax, cx + dx, 36, 16, 10, 'varie', label=str(v2))
        arrow(ax, (cx + dx + 8, 59.5), (cx + dx + 8, 46.5), 'varie')
        arrow(ax, (cx + dx + 8, 35.5), (cx + dx + 8, 22.5), 'varie')
    text(ax, cx, 53, '−1', 'varie', 'm')
    text(ax, cx, 29, r'$\times$', 'varie', 'l')
    box(ax, cx - 17, 12, 34, 10, 'resultat', label=rf'$\varphi({n}) = {phi}$')
save(fig, '53-087')
