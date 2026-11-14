import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 66, 63, 'avant la virgule', 'fixe', 's')
rows = [(r'$248{,}0\times10^{1}$', '3 chiffres', 'fixe'), (r'$24{,}80\times10^{2}$', '2 chiffres', 'fixe'),
        (r'$2{,}480\times10^{3}$', '1 seul chiffre', 'sujet')]
for i, (lab, note, role) in enumerate(rows):
    y = 44 - i * 17
    box(ax, 4, y, 44, 11, role, label=lab, size='m')
    text(ax, 66, y + 5.5, note, role, 'm')
save(fig, '14-068')
