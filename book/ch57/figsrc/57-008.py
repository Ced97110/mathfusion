import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
box(ax, 44, 26, 42, 36, 'fixe', fill=False, dash=True)
text(ax, 84, 59, 'ℤ²', 'sujet', 'l', ha='right', weight='bold')
box(ax, 2, 31, 18, 12, 'sujet', label='(2, 1)')
rows = [(48, '× 3', '(6, 3)', 'resultat'), (32, '× (−2)', '(−4, −2)', 'resultat'), (6, '× ½', '(1 ; ½)', 'limite')]
for y, op, lab, role in rows:
    cy = y + 4
    arrow(ax, (21, 37), (46, cy), 'varie', lw=1.0)
    box(ax, 48, y, 24 if role != 'limite' else 24, 8, role, label=lab, size='s')
    text(ax, 36, cy + (3.2 if cy > 37 else -3.2), op, 'varie', 's')
text(ax, 80, 16, 'hors de la boîte', 'limite', 's', ha='right')
save(fig, '57-008')
