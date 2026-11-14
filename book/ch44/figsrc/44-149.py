import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def grp(ax, x, y, u, n, role, label=None, h=8):
    box(ax, x, y, n * u, h, role, label=label)
    for i in range(1, n):
        xx = x + i * u
        line(ax, [(xx, y), (xx, y + 1.6)], role, lw=0.6); line(ax, [(xx, y + h - 1.6), (xx, y + h)], role, lw=0.6)

fig, ax = canvas(50)
u, x0, y = 6.2, 6.8, 22
text(ax, 44, 42, '3 × 4 : 4 groupes de 3', 'sujet', 'l')
for g in range(4):
    grp(ax, x0 + g * 3 * u + 0.3, y, u, 3, 'sujet', label='3', h=8)
brace(ax, x0, x0 + 12 * u, y - 0.5, 'varie', label='12 cases = 1 tour entier')
text(ax, 44, 8, '3 × 4 ≡ 0 (mod 12)', 'limite', 'l')
text(ax, 44, 32, '3 ≠ 0 et 4 ≠ 0', 'limite', 'm')
save(fig, '44-149')
