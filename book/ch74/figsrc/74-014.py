import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 44, 46, r'$2\cos\theta$ doit être entier', 'sujet', 'l')
f = numberline(ax, 12, 68, 14, -2, 2, 1)
disc(ax, f(-2), 14, 1.6, 'resultat'); disc(ax, f(0.618), 14, 1.6, 'limite')
text(ax, f(-2) + 8, 31, '180° : −2\nentier', 'resultat', 's'); arrow(ax, (f(-2), 25), (f(-2), 17), 'resultat', lw=0.9)
text(ax, f(0.618), 31, '72° : ≈ 0,618\npas entier', 'limite', 's'); arrow(ax, (f(0.618), 25), (f(0.618), 17), 'limite', lw=0.9)
save(fig, '74-014')
