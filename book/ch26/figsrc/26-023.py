import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
for x0, role, t1, t2, t3, ct in ((2, "resultat", "26 m ÷ 30 m", "= 0,8666…", "mètres simplifiés", "30 m"),
                                 (46, "limite", "26 m ÷ 3000 cm", "≈ 0,0087", "pas de simplification", "3000 cm")):
    box(ax, x0, 2, 40, 60, role, fill=False, lw=0.8)
    text(ax, x0 + 20, 56, t1, role, "m")
    ax.add_patch(Rectangle((x0 + 5, 42), 26 * 0.9, 4, ec=COL["sujet"], fc=FILL["sujet"], lw=0.8, zorder=2))
    text(ax, x0 + 5 + 26 * 0.9 / 2, 44, "26 m", "sujet", "s")
    ax.add_patch(Rectangle((x0 + 5, 34), 30 * 0.9, 4, ec=COL["fixe"], fc=FILL["fixe"], lw=0.8, zorder=2))
    text(ax, x0 + 5 + 30 * 0.9 / 2, 36, ct, "fixe", "s")
    text(ax, x0 + 20, 24, t2, role, "l")
    text(ax, x0 + 20, 12, t3, role, "s")
save(fig, "26-023")
