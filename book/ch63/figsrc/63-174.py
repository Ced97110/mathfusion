import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
bw, bh = 26, 17
xs = [4, 31, 58]
ym, yt, yb = 50, 78, 22
box(ax, 31, yt, bw, 11, 'sujet', label=r'$\mathbb{Q}(\sqrt{3},\sqrt{5})$', size='s')
box(ax, 31, yb, bw, 11, 'fixe', label=r'$\mathbb{Q}$')
mid = [(r'$\mathbb{Q}(\sqrt{5})$', 'varie', r'fixé par $\sigma$'), (r'$\mathbb{Q}(\sqrt{3})$', 'autre', r'fixé par $\tau$'),
       (r'$\mathbb{Q}(\sqrt{15})$', 'resultat', r'fixé par $\mu$')]
for x, (lab, role, fx) in zip(xs, mid):
    box(ax, x, ym, bw, bh, role)
    text(ax, x + bw / 2, ym + 11.5, lab, role, 's')
    text(ax, x + bw / 2, ym + 5, fx, role, 's')
    line(ax, [(x + bw / 2, ym + bh), (44, yt)], role)
    line(ax, [(x + bw / 2, ym), (44, yb + 11)], role)
legend = [(r'$\sigma$ : $\sqrt{3} \mapsto -\sqrt{3}$, $\sqrt{5}$ fixe', 'varie'),
          (r'$\tau$ : $\sqrt{5} \mapsto -\sqrt{5}$, $\sqrt{3}$ fixe', 'autre'),
          (r'$\mu = \sigma\tau$ : change les deux signes', 'resultat')]
for i, (s, role) in enumerate(legend):
    text(ax, 10, 14 - 6 * i + 0, s, role, 's', ha='left')
text(ax, 44, 96, '3 corps intermédiaires, 4 automorphismes', 'fixe', 's')
save(fig, '63-174')
