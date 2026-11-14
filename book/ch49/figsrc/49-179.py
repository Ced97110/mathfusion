import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
sizes = [1, 4, 4, 2, 4, 1]; bw = 10.5; gap = 2.6
x0 = (W - (6 * bw + 5 * gap)) / 2
for i, n in enumerate(sizes):
    x = x0 + i * (bw + gap)
    box(ax, x, 26, bw, 9, 'sujet', label=str(n), size='l', weight='bold')
    arrow(ax, (x + bw / 2, 15), (x + bw / 2, 25), 'varie', lw=0.8)
    text(ax, x + bw / 2, 12, str(i + 1), 'varie', 'm')
brace(ax, x0, W - x0, 37, 'resultat', None, down=False, depth=2.4)
text(ax, W / 2, 45, r'$\sum_i$ : on additionne, une fois par orbite', 'resultat', 'm')
text(ax, W / 2, 5, 'le numéro i parcourt les orbites', 'varie', 's')
save(fig, '49-179')
