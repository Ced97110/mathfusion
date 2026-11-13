import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def tri(ax, ox, oy, s, p=4, q=3, hl=None, arc=None):
    """Triangle rectangle en C ; A bas-gauche, C bas-droite, B haut-droite ; cotes p (AC) et q (BC)."""
    A = (ox, oy); C = (ox + p * s, oy); B = (ox + p * s, oy + q * s)
    poly(ax, [A, C, B], "fixe")
    for pts, k in (((A, C), "b"), ((C, B), "a"), ((A, B), "c")):
        line(ax, list(pts), (hl or {}).get(k, "fixe"), lw=2.2 if k in (hl or {}) else 0.9)
    line(ax, [(C[0] - 2.2, C[1]), (C[0] - 2.2, C[1] + 2.2), (C[0], C[1] + 2.2)], "fixe", lw=0.8)
    if arc:
        t1 = math.atan2(q, p)
        line(ax, [(ox + 7 * math.cos(t1 * i / 20), oy + 7 * math.sin(t1 * i / 20)) for i in range(21)], arc, lw=1.1)
    return A, B, C
fig, ax = canvas(100)
A, B, C = tri(ax, 30, 66, 7, hl={"b": "sujet"})
line(ax, [(A[0] + 6 * math.cos(0), A[1])] + [(A[0] + 6 * math.cos(t), A[1] + 6 * math.sin(t)) for t in [math.atan2(3, 4) * i / 20 for i in range(21)]], "varie", lw=1.1)
text(ax, A[0] - 3, A[1] - 2, "A", "varie", "l", weight="bold")
text(ax, B[0] + 3, B[1] + 2, "B", "autre", "l", weight="bold")
text(ax, 44, 61, "$b$ : touche A, face à B", "sujet", "s")
text(ax, 44, 92, "$c$ = hypoténuse", "fixe", "s") if False else None
box(ax, 4, 40, 80, 11, "sujet", label="départ : sin B = $b$/$c$", size="m")
box(ax, 4, 22, 80, 11, "varie", label="étape clé : $b$ est adjacent à A", size="m")
box(ax, 4, 4, 80, 11, "resultat", label="arrivée : sin B = cos A", size="m")
arrow(ax, (44, 40), (44, 33.5), "fixe"); arrow(ax, (44, 22), (44, 15.5), "fixe")
save(fig, "26-025")
