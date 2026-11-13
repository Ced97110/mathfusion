import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
text(ax, 44, 95, r'$a+bi \;\rightarrow\; (a-bi)/(a^2+b^2)$', 'encre', 'm')
rows = [('sujet', r'$3+4i$', 'le nombre de départ'),
        ('varie', r'$3-4i$', r'on change le signe de $b$'),
        ('fixe', r'$(3+4i)(3-4i)=9+16=25$', r'produit : $a^2+b^2$'),
        ('resultat', r'$(3-4i)/25$', r'l’inverse de $3+4i$')]
for k, (role, ex, note) in enumerate(rows):
    y = 70 - k * 22
    text(ax, 11, y + 8.5, f'étape {k + 1}', role, 's')
    box(ax, 22, y, 64, 17, role)
    text(ax, 54, y + 11, ex, role, 'm')
    text(ax, 54, y + 4.5, note, 'encre', 's')
    if k < 3: arrow(ax, (54, y - 0.3), (54, y - 4.7), 'fixe')
save(fig, '44-196')
