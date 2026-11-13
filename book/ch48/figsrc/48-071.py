import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
text(ax, 44, 87, r"$\ker f=4$ℤ : 4 paquets, 4 positions", 'encre', 's')
labs = ["0, 4, 8", "1, 5, 9", "2, 6, 10", "3, 7, 11"]
for i in range(4):
    x = 3 + 21.5 * i
    box(ax, x, 66, 19, 10, 'sujet', label=labs[i], size='s')
    arrow(ax, (x + 9.5, 66), (x + 9.5, 60), 'fixe', both=True)
    disc(ax, x + 9.5, 55, 4, 'resultat', label=str(i), size='s')
text(ax, 44, 43, "paquet 1 + paquet 2 = paquet 3\n1 + 2 = 3", 'resultat', 's')
text(ax, 44, 33, r"$\ker f=2$ℤ : 2 paquets, 2 positions", 'encre', 's')
for x, lab in [(4, "pairs\nposition 0"), (46, "impairs\nposition 2")]:
    box(ax, x, 16, 38, 11, 'sujet', label=lab, size='s')
    arrow(ax, (x + 19, 16), (x + 19, 11), 'fixe', both=True) if False else None
text(ax, 44, 6, "impairs + impairs = pairs\n2 + 2 = 0", 'resultat', 's')
save(fig, '48-071')
