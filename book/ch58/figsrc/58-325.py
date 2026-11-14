import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
c = 5.4; x0 = 6.0; y = 24
text(ax, 44, 48, '14 divisé par 6', 'encre', 's')
for i in range(14):
    role = 'sujet' if i < 12 else 'varie'
    gap = 1.2 * (i // 6 if i < 12 else 2)
    box(ax, x0 + i * c + gap, y, c - 0.8, 7, role, r=0.3)
def xr(i):
    return x0 + i * c + 1.2 * (i // 6 if i < 12 else 2)
brace(ax, xr(0), xr(5) + c - 0.8, y + 7.5, 'sujet', label='6', down=False)
brace(ax, xr(6), xr(11) + c - 0.8, y + 7.5, 'sujet', label='6', down=False)
brace(ax, xr(12), xr(13) + c - 0.8, y + 7.5, 'varie', label='reste 2', down=False)
text(ax, (xr(0) + xr(11) + c) / 2, 14, 'quotient : 2 fois 6', 'sujet', 's')
text(ax, (xr(12) + xr(13) + c) / 2 - 2, 14, 'reste', 'varie', 's')
box(ax, 14, 1.5, 60, 8, 'resultat', label='14 = 2 × 6 + 2, et 2 < 6', size='m')
save(fig, '58-325')
