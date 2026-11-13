import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 69, r'lettre L : $p=11$, $a=5$, $b=3$', 'fixe', 'm', weight='bold')
bw, gap, x0 = 22.0, 6.0, 2.0
xs = [x0 + i * (bw + gap) for i in range(3)]
sym = [(r'$a\,p$', 'sujet'), (r'$+\,b$', 'varie'), ('mod 26', 'fixe')]
mean = ['5 × 11 = 55', '55 + 3 = 58', '58 : reste 6']
for i, (x, (s, r)) in enumerate(zip(xs, sym)):
    box(ax, x, 44, bw, 12, r, label=s, size='l', weight='bold')
    if i < 2: arrow(ax, (x + bw + 0.4, 50), (x + bw + gap - 0.4, 50), 'fixe')
    arrow(ax, (x + bw / 2, 44), (x + bw / 2, 33), r)
    box(ax, x, 20, bw, 12, r, label=mean[i], size='s')
text(ax, 44, 11, 'on lit de gauche à droite', 'fixe', 's')
save(fig, '53-047')
