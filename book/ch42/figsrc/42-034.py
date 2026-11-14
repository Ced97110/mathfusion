import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(36)
text(ax, 8, 14, r"$S=\{$", "encre", "l"); text(ax, 80, 14, r"$\}$", "encre", "l")
labs = [r"$a_1$", r"$a_2$", "…", r"$a_n$"]
for x, l in zip([16, 32, 48, 64], labs):
    box(ax, x, 8, 13, 12, "sujet" if l != "…" else "fixe", label=l, size="l")
brace(ax, 16, 77, 6, "sujet", "n éléments", depth=1.6)
arrow(ax, (38, 28), (38.2, 20.5), "varie")
text(ax, 38, 31.5, "indice = numéro de l’objet", "varie", "s")
save(fig, "42-034")
