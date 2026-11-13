import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 54, r'$\frac{4}{x-1}=\frac{2}{x+6}$', 'sujet', 'l')
f = numberline(ax, 6, 76, 26, -15, 3, step=3, arrow_right=False)
for v in (-6, 1):
    text(ax, f(v), 36, f'{v} interdit', 'limite', 's')
    line(ax, [(f(v), 28), (f(v), 34)], 'limite', dash=True)
disc(ax, f(-13), 26, 1.6, 'resultat')
text(ax, f(-13) + 2, 36, '-13 permis', 'resultat', 's', ha='left')
line(ax, [(f(-13), 28.5), (f(-13), 34)], 'resultat', dash=True)
box(ax, 14, 4, 60, 9, 'resultat', label='donc une solution')
save(fig, '21-131')
