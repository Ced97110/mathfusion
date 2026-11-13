import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
steps = [('1. la formule', r'$V=\frac{1}{3}\pi r^2 h$'),
         ('2. remplacer les lettres', r'$\frac{1}{3}\times 3{,}14\times 2^2\times 5$'),
         ('3. le carré d’abord', r'$2^2 = 4$'),
         ('4. l’aire de la base', r'$3{,}14\times 4 = 12{,}56$'),
         ('5. fois la hauteur', r'$12{,}56\times 5 = 62{,}8$'),
         ('6. le tiers', r'$62{,}8 \div 3 \approx 20{,}93$')]
hh, gap = 11.5, 3.6
top = 98
for i, (lab, ex) in enumerate(steps):
    y = top - (i + 1) * hh - i * gap
    last = i == len(steps) - 1
    role = 'resultat' if last else 'sujet'
    box(ax, 3, y, 38, hh, 'varie' if i == 2 else 'fixe', label=lab, size='s')
    box(ax, 46, y, 39, hh, role, label=ex, size='m')
    if not last:
        arrow(ax, (65, y), (65, y - gap + 0.2), 'fixe', lw=0.9)
save(fig, '11-149')
