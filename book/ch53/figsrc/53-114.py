import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
assert 16 + 8 + 2 + 1 == 27
bits = '11011'
for i, (w, b) in enumerate(zip((16, 8, 4, 2, 1), bits)):
    used = b == '1'
    text(ax, 11 + i * 16, 44, str(w), 'resultat' if used else 'fixe', 'm')
    box(ax, 4 + i * 16, 24, 14, 12, 'resultat' if used else 'fixe', label=b, size='l', dash=not used)
text(ax, 44, 12, '16 + 8 + 2 + 1 = 27', 'resultat', 'm')
text(ax, 11 + 2 * 16, 19, 'non utilisée', 'fixe', 's')
save(fig, '53-114')
