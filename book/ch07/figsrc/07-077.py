import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(106)
steps = [('1 · facteurs premiers', r'$6=2\cdot3,\ 8=2^3,\ 16=2^4$', 'sujet'),
         ('2 · plus petit commun multiple', r'$2^4 \times 3 = 48$', 'sujet'),
         ('3 · recouper', r'$\frac{5}{6}=\frac{40}{48},\ \frac{1}{8}=\frac{6}{48}$', 'sujet'),
         ('4 · numérateurs', r'$40,\ 6,\ 21$', 'sujet'),
         ('5 · opérer', r'$40-6+21=55$', 'sujet'),
         ('6 · réduire', r'$\frac{55}{48}$ : plus rien à simplifier', 'resultat')]
h, gap = 12, 5
for k, (name, ex, role) in enumerate(steps):
    y = 102 - h - k * (h + gap)
    box(ax, 2, y, 84, h, role)
    text(ax, 5, y + h / 2, name, role, 's', ha='left', weight='bold')
    text(ax, 66, y + h / 2, ex, role, 's')
    if k < 5: arrow(ax, (44, y), (44, y - gap), 'fixe')
save(fig, '07-077')
