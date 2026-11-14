import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
x0, k = 38.0, 14.0
terms = [1, 1, 1 / 2, 1 / 6, 1 / 24]
labs = [r'$1$', r'$1+1=2$', r'$+\frac{1}{2}=2{,}5$', r'$+\frac{1}{6}\approx 2{,}667$', r'$+\frac{1}{24}\approx 2{,}708$']
text(ax, 44, 61, r'$e^u$ pour $u=1$ : on ajoute les termes', 'sujet', 's')
s = 0.0
for i, t in enumerate(terms):
    y = 46 - i * 9
    if s > 0:
        box(ax, x0, y, s * k, 6, 'sujet', r=0.2, lw=0.6)
    box(ax, x0 + s * k, y, t * k, 6, 'varie', r=0.2, lw=0.6)
    s += t
    text(ax, x0 - 2, y + 3, labs[i], 'encre', 's', ha='right')
ex = x0 + 2.718 * k
line(ax, [(ex, 6), (ex, 54)], 'resultat', lw=1.0, dash=True)
text(ax, ex - 8, 2, r'$e\approx 2{,}718$', 'resultat', 's')
save(fig, '66-077')
