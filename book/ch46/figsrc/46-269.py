import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
f = numberline(ax, 8, 70, 16, -2, 7, step=1, arrow_right=True)
for v in range(-2, 8):
    disc(ax, f(v), 16, 1.7, 'sujet' if v == 1 else ('limite' if v == 0 else 'fixe'), fill=(v != 0))
for v in range(0, 5):
    arrow(ax, (f(v), 19), (f(v + 1), 19), 'varie', curve=-0.7)
text(ax, f(2.5), 31, '1, 2, 3, 4, … ne retombent', 'varie', 's')
text(ax, f(2.5), 26.5, 'jamais sur 0', 'limite', 's')
text(ax, 44, 46, '⟨1⟩ = tous les entiers : infini', 'sujet', 'm')
text(ax, 44, 5, '$o(1) = \\infty$', 'sujet', 'l')
save(fig, '46-269')
