import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)

def bits(ax, x, y, s, roles, cw, ch=5.5, size='m'):
    for i, c in enumerate(s):
        box(ax, x + i * cw, y, cw, ch, roles if isinstance(roles, str) else roles[i], label=c, size=size, r=0.5)

def flip(s, i):
    return s[:i] + ('1' if s[i] == '0' else '0') + s[i + 1:]

cw = 4.6
A = '01000001'
w = 8 * cw
text(ax, 44, 70, r'$A$ : deux 1, nombre pair', 'sujet', 'm', weight='bold')
bits(ax, 44 - w / 2, 58, A, ['sujet' if c == '1' else 'fixe' for c in A], cw)
for xl, i, label, role in [(5, 0, '0 devient 1 : +1', 'varie'), (88 - 5 - w, 1, '1 devient 0 : −1', 'varie')]:
    B = flip(A, i)
    bits(ax, xl, 26, B, ['varie' if j == i else ('sujet' if c == '1' else 'fixe') for j, c in enumerate(B)], cw)
    arrow(ax, (xl + i * cw + cw / 2, 56.5), (xl + i * cw + cw / 2, 33), 'varie')
    text(ax, xl + w / 2, 40, label, role, 's')
    n = B.count('1')
    text(ax, xl + w / 2, 18, f'{"trois" if n == 3 else "un seul"} 1 : impair', 'limite', 's')
text(ax, 44, 5, 'un bit inversé : le nombre de 1 change de 1', 'encre', 'm', weight='bold')
save(fig, '68-043')
