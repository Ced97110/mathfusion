import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(67)
def ring(cx, cy, n, sub, R=10):
    for k in range(n):
        x = cx + R * math.sin(2 * math.pi * k / n); y = cy + R * math.cos(2 * math.pi * k / n)
        disc(ax, x, y, 2.0, 'varie' if k in sub else 'sujet')
ring(16, 34, 6, [0, 2, 4])
ring(44, 34, 7, [])
box(ax, 59, 24, 28, 20, 'autre', label='60\npas une\nhorloge', size='s')
for x, t in [(16, r'$\mathbb{Z}/6$'), (44, r'$\mathbb{Z}/7$'), (73, r'$A_5$')]:
    text(ax, x, 55, t, 'sujet', 'l')
text(ax, 16, 17, 'pas simple', 'fixe', 'm', weight='bold')
text(ax, 44, 17, 'simple', 'resultat', 'm', weight='bold')
text(ax, 73, 17, 'simple', 'autre', 'm', weight='bold')
text(ax, 16, 10, '6 : non premier', 'encre', 's')
text(ax, 44, 10, '7 : premier', 'encre', 's')
text(ax, 73, 10, '60 : non premier', 'encre', 's')
text(ax, 73, 3, 'non abélien', 'autre', 's')
text(ax, 16, 47.5, 'sous-groupe', 'varie', 's')
text(ax, 30, 63.5, r'abélien simple : $\mathbb{Z}/p$, $p$ premier', 'resultat', 's', weight='bold')
save(fig, '64-071')
