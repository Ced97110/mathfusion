import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 68, 'ℤ/4 ⊕ ℤ/3', 'sujet', 'l')
text(ax, 44, 57, 'ℤ/3 →', 'sujet', 's')
text(ax, 8, 28, 'ℤ/4 ↓', 'sujet', 's')
special = {(2, 1): 'varie', (3, 2): 'varie', (1, 0): 'resultat'}
for a in range(4):
    text(ax, 21, 41 - 9 * a, str(a), 'fixe', 's')
    for b in range(3):
        role = special.get((a, b), 'fixe')
        box(ax, 26 + 12 * b, 37 - 9 * a, 11, 8, role, label=f'({a},{b})' if (a, b) in special else None, size='s', r=0.4)
for b in range(3):
    text(ax, 31.5 + 12 * b, 50, str(b), 'fixe', 's')
text(ax, 78, 38, 'mod 4 : 2+3=1', 'varie', 's')
text(ax, 78, 28, 'mod 3 : 1+2=0', 'varie', 's')
save(fig, '60-081')
