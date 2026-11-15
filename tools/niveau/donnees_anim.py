"""Build the data file of the « Vent de travers » animation from real measurements.

Usage: python3 tools/niveau/donnees_anim.py <sounding TEXT:LIST saved as text>
Reads data/vent_travers.json and the University of Wyoming sounding (De Bilt 06260,
2026-11-12 12 UTC). Writes data/sondage_debilt.json (levels up to 3200 m) and
public/anim/vent-de-travers/donnees.json. No value is invented: derived values use
the wind-triangle formulas also tested in lib/vent.js (see lib/anim_donnees.test.js).
"""

import json
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PLAFOND_M = 3200
ROW = re.compile(r"^\s*(\d+\.\d)\s+(\d+)\s+(-?\d+\.\d)\s+(-?\d+\.\d)\s+(\d+)\s+\S+\s+(\d+)\s+(\d+\.\d)")


def niveaux(texte: str) -> list[dict[str, float]]:
    out: list[dict[str, float]] = []
    for line in texte.splitlines():
        m = ROW.match(line)
        if m and int(m.group(2)) <= PLAFOND_M:
            out.append({"h": int(m.group(2)), "t": float(m.group(3)), "rh": int(m.group(5)),
                        "dir": int(m.group(6)), "v": float(m.group(7))})
    return out


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    d = json.loads((ROOT / "data/vent_travers.json").read_text(encoding="utf-8"))
    niv = niveaux(Path(sys.argv[1]).read_text(encoding="utf-8", errors="replace"))
    cible = d["vent"]["niveau"]["altitude_m"]
    hit = [n for n in niv if n["h"] == cible]
    if len(hit) != 1 or hit[0]["dir"] != d["vent"]["vient_du_deg"] or hit[0]["v"] != d["vent"]["vitesse_m_s"]:
        sys.exit("le sondage ne contient pas le niveau de data/vent_travers.json")

    sondage = {"station": d["vent"]["station"], "date_utc": d["vent"]["date_utc"], "source": d["vent"]["source"],
               "url": d["vent"]["url"], "consulte_le": "2026-11-14",
               "colonnes": "h = altitude (m), t = température (°C), rh = humidité (%), dir = le vent vient du (°), v = vitesse (m/s)",
               "niveaux": niv}
    (ROOT / "data/sondage_debilt.json").write_text(json.dumps(sondage, ensure_ascii=False) + "\n", encoding="utf-8")

    tas = d["avion"]["vitesse_air_kt"]
    w = d["vent"]["vitesse_m_s"] * 3600 / 1852
    frm, route = d["vent"]["vient_du_deg"], d["mission"]["route_voulue_deg"]
    vers = math.radians(frm + 180)
    vent = [w * math.sin(vers), w * math.cos(vers)]  # est, nord
    travers = w * math.sin(math.radians(frm - route))
    cap = route + math.degrees(math.asin(travers / tas))

    def sol(c: float) -> dict[str, float]:
        e = tas * math.sin(math.radians(c)) + vent[0]
        n = tas * math.cos(math.radians(c)) + vent[1]
        return {"cap": c, "est": e, "nord": n, "gs": math.hypot(e, n), "route": math.degrees(math.atan2(e, n)) % 360}

    bon, faux = sol(cap), sol(float(route))
    distance = bon["gs"]
    heures_faux = distance / faux["est"]
    out = {"tas": tas, "vent": {"vient_du": frm, "ms": d["vent"]["vitesse_m_s"], "kt": w, "est": vent[0], "nord": vent[1], "altitude_m": cible},
           "route": route, "distance_nm": distance, "bon": bon, "faux": faux,
           "ecart_faux_km": abs(faux["nord"] * heures_faux) * 1.852, "heures_faux": heures_faux,
           "naif_kt": tas + w, "niveaux": [[n["h"], n["dir"], n["v"], n["rh"]] for n in niv]}
    # Same case in km and km/h for a viewer with no aviation vocabulary (1 NM = 1.852 km exactly).
    km = 1.852
    vms = d["vent"]["vitesse_m_s"]
    out["km"] = {
        "avion_kmh": tas * km, "vent_kmh": vms * 3.6, "distance": distance * km,
        "vent": {"est": vent[0] * km, "nord": vent[1] * km},
        "faux": {"cap": faux["cap"], "air": {"est": tas * km, "nord": 0.0},
                 "sol": {"est": faux["est"] * km, "nord": faux["nord"] * km}, "vitesse_sol_kmh": faux["gs"] * km,
                 "ecart_apres_1h": abs(faux["nord"]) * km},
        "bon": {"cap": cap, "virage_deg": route - cap,
                "air": {"est": tas * km * math.sin(math.radians(cap)), "nord": tas * km * math.cos(math.radians(cap))},
                "sol": {"est": bon["est"] * km, "nord": bon["nord"] * km}, "vitesse_sol_kmh": bon["gs"] * km},
        "naif": {"longueur": (tas + w) * km, "est": (tas + w) * km, "nord": 0.0},
    }
    dest = ROOT / "public/anim/vent-de-travers/donnees.json"
    dest.write_text(json.dumps(out, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"{len(niv)} niveaux ; cap {cap:.2f}° ; gs {bon['gs']:.2f} kt ; écart {out['ecart_faux_km']:.2f} km")


if __name__ == "__main__":
    main()
