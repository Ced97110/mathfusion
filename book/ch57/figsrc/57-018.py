import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
cx = [16, 44, 72]
text(ax, 2, 84, 'avant', 'fixe', 'm', ha='left', weight='bold')
for x, s, k in zip(cx, ['ℝ²', 'ℤ²', 'plan, T'], ['1', '2', '3']):
    box(ax, x - 12, 68, 24, 10, 'sujet', label=s)
    arrow(ax, (x, 68), (x, 59), 'varie', lw=1.0)
    box(ax, x - 12, 49, 24, 10, 'varie', label='preuve ' + k, size='s')
text(ax, 2, 40, 'après', 'fixe', 'm', ha='left', weight='bold')
box(ax, 24, 24, 40, 10, 'resultat', label='une seule preuve')
for x in cx:
    arrow(ax, (44, 24), (x, 14), 'resultat', lw=1.0)
    box(ax, x - 12, 3, 24, 10, 'sujet', label={16: 'ℝ²', 44: 'ℤ²', 72: 'plan, T'}[x])
save(fig, '57-018')
