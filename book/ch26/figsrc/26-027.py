import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(98)
text(ax, 44, 92, "sin(90° − A) = cos A", "resultat", "l", weight="bold")
steps = (("sujet", "1. prendre A = 40°"), ("varie", "2. calculer 90° − 40° = 50°"),
         ("sujet", "3. sin 50° ≈ 0,7660"), ("autre", "4. cos 40° ≈ 0,7660"), ("resultat", "égaux : 0,7660"))
for i, (role, lab) in enumerate(steps):
    y = 70 - i * 16
    box(ax, 14, y, 60, 11, role, label=lab, size="m")
    if i < 4: arrow(ax, (44, y), (44, y - 5), "fixe")
save(fig, "26-027")
