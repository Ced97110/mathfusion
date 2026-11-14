import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 58, 'ℤ, module sur lui-même', 'encre', 'm', weight='bold')
text(ax, 44, 51, 'idéal 6ℤ = sous-module de ℤ', 'sujet', 'm')
text(ax, 44, 43, 'addition : 6 + 12 = 18', 'resultat', 's')
text(ax, 44, 37, 'multiplication : 4 × 6 = 24', 'resultat', 's')
f = numberline(ax, 6, 70, 22, 0, 24, 6, role='fixe', arrow_right=True)
for n in range(25):
    if n % 6 == 0:
        disc(ax, f(n), 22, 1.8, 'sujet')
    else:
        disc(ax, f(n), 22, 0.5, 'fixe')
for n in (18, 24):
    disc(ax, f(n), 22, 2.6, 'resultat', fill=False, lw=1.1)
brace(ax, f(0), f(6), 15.5, 'fixe', label='ℤ/6ℤ : restes 0 à 5', size='s')
save(fig, '57-224')
