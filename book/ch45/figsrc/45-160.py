import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
bw, g = 13, 3.5
xs = [6 + i * (bw + g) for i in range(5)]
lab = [r'$G$', r'$G$', r'$G$', r'$\cdots$', r'$G$']
sub = [r'$g_1$', r'$g_2$', r'$g_3$', r'$\cdots$', r'$g_n$']
for i, x in enumerate(xs):
    if i == 3:
        text(ax, x + bw / 2, 42, lab[i], 'fixe', 'l'); text(ax, x + bw / 2, 22, sub[i], 'fixe', 'l'); continue
    box(ax, x, 36, bw, 12, 'sujet', label=lab[i], size='l')
    arrow(ax, (x + bw / 2, 35), (x + bw / 2, 30), 'varie')
    box(ax, x, 17, bw, 12, 'resultat', label=sub[i], size='l')
brace(ax, xs[0], xs[4] + bw, 50, 'sujet', label=r'$n$ copies de $G$ : $G^n$', down=False, size='m')
text(ax, 44, 8, 'un élément : une liste de $n$ cases', 'resultat', 's')
save(fig, '45-160')
