import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
cx = [34, 54, 74]
heads = [r'dans $A$', r'dans $A$', r'dans $A \cap A$']
for x, h, role in zip(cx, heads, ['sujet', 'sujet', 'resultat']):
    text(ax, x, 65, h, role, 's')
def check(x, y, role):
    line(ax, [(x - 2.5, y), (x - 0.8, y - 2), (x + 2.8, y + 2.5)], role, lw=1.4)
def cross(x, y, role):
    line(ax, [(x - 2, y - 2), (x + 2, y + 2)], role, lw=1.4)
    line(ax, [(x - 2, y + 2), (x + 2, y - 2)], role, lw=1.4)
for y, n, ok in [(53, '2', True), (42, '4', True), (31, '6', True), (16, '5', False)]:
    text(ax, 12, y, n, 'encre' if ok else 'limite', 'l', weight='bold')
    role = 'resultat' if ok else 'limite'
    for x in cx:
        box(ax, x - 7, y - 4, 14, 8, role)
        (check if ok else cross)(x, y, role)
line(ax, [(5, 23.5), (83, 23.5)], 'fixe', lw=0.5, dash=True)
text(ax, 44, 5, r'$A \cap A = A$', 'resultat', 'l')
save(fig, '42-142')
