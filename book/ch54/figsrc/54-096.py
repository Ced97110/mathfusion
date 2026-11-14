import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
# A = B = C = (1, 1)
AB = [1, 2, 1]
ABC = [1, 3, 3, 1]
assert [sum(AB[i - l] * 1 for l in (0, 1) if 0 <= i - l < 3) for i in range(4)] == ABC
trip = [(j, k, l) for j in range(2) for k in range(2) for l in range(2) if j + k + l == 2]
assert len(trip) == 3 and ABC[2] == 3
text(ax, 44, 67, r'$A=B=C=(1,1)$', 'encre', 'm')
for y, lab, role, first in [(52, r'$(AB)C$', 'sujet', r'$AB=(1,2,1)$'), (36, r'$A(BC)$', 'autre', r'$BC=(1,2,1)$')]:
    text(ax, 8, y + 4.5, lab, role, 'm')
    box(ax, 18, y, 26, 9, role, label=first, size='s')
    arrow(ax, (44, y + 4.5), (58, y + 4.5), role)
    text(ax, 51, y + 8, r'$\times$ le 3e', role, 's')
    box(ax, 58, y, 26, 9, 'resultat', label=r'$(1,3,3,1)$', size='s')
text(ax, 71, 31.5, '=', 'resultat', 'xl')
text(ax, 44, 24, r'rang 2 : $j+k+l=2$', 'varie', 'm')
for i, t in enumerate(trip):
    x = 6 + i * 28
    box(ax, x, 8, 24, 9, 'varie', label='(' + ', '.join(map(str, t)) + ')', size='s')
text(ax, 44, 3.5, r'$1+1+1=3$', 'resultat', 's')
save(fig, '54-096')
