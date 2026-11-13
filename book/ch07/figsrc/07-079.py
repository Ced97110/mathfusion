import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
text(ax, 44, 86, r'$\frac{3}{5} + \frac{9}{44} \times (\frac{5}{9} - \frac{1}{4})$', 'sujet', 'm')
rows = [('1 · parenthèse', r'$\frac{5}{9} - \frac{1}{4} = \frac{11}{36}$', 'varie'),
        ('2 · multiplication', r'$\frac{9}{44} \times \frac{11}{36} = \frac{1}{16}$', 'varie'),
        ('3 · addition', r'$\frac{3}{5} + \frac{1}{16} = \frac{53}{80}$', 'resultat')]
for k, (lab, ex, role) in enumerate(rows):
    y = 64 - k * 22
    text(ax, 3, y, lab, role, 's', ha='left', weight='bold')
    text(ax, 62, y, ex, role, 'm')
    arrow(ax, (10, y + (14 if k == 0 else 7) if False else y + 13), (10, y + 7), 'fixe') if k > 0 else None
arrow(ax, (10, 78), (10, 70), 'fixe')
save(fig, '07-079')
