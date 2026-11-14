import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
u = 3.6
for (L, l, y, cap) in [(7, 3, 38, r'$3\times7=21$ m²'), (8, 4, 14, r'$4\times8=32$ m²')]:
    box(ax, 14, y, L * u, l * u, 'varie', True, r=0.3)
    text(ax, 14 + L * u / 2, y + l * u + 2.6, f'{L} m', 'varie', 's')
    text(ax, 10, y + l * u / 2, f'{l} m', 'varie', 's')
    text(ax, 14 + L * u + 4, y + l * u / 2, cap, 'encre', 'm', ha='left')
text(ax, 44, 5, '30 m² : largeur entre 3 et 4', 'sujet', 'm')
save(fig, '23-001')
