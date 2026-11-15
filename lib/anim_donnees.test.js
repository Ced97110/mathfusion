// The film's data file must agree with the tested wind-triangle code (lib/vent.js), to 1e-6.
import { describe, expect, it } from "vitest";
import d from "../public/anim/vent-de-travers/donnees.json";
import src from "../data/vent_travers.json";
import { capPourRoute, vecteurSol } from "./vent.js";

const TOL = 1e-6;
const KM = 1.852;
const vent = { vientDuDeg: src.vent.vient_du_deg, vitesseKt: (src.vent.vitesse_m_s * 3600) / 1852 };
const pres = (a, b) => expect(Math.abs(a - b)).toBeLessThan(TOL);

describe("donnees.json du film", () => {
  it("cap, vitesses et écart égalent lib/vent.js", () => {
    const bon = capPourRoute(src.avion.vitesse_air_kt, vent, 90);
    const faux = vecteurSol(src.avion.vitesse_air_kt, 90, vent);
    pres(d.bon.cap, bon.capDeg);
    pres(d.bon.gs, bon.vitesseSolKt);
    pres(d.faux.gs, faux.vitesseSolKt);
    pres(d.km.bon.vitesse_sol_kmh, bon.vitesseSolKt * KM);
    pres(d.km.faux.sol.est, faux.estKt * KM);
    pres(d.km.faux.sol.nord, faux.nordKt * KM);
    pres(d.km.faux.ecart_apres_1h, -faux.nordKt * KM);
  });
  it("en km : sol = air + vent, composante par composante, pour les deux caps", () => {
    for (const v of [d.km.faux, d.km.bon]) {
      pres(v.sol.est, v.air.est + d.km.vent.est);
      pres(v.sol.nord, v.air.nord + d.km.vent.nord);
    }
    pres(d.km.bon.sol.nord, 0); // the corrected flight ends exactly on the runway line
    pres(d.km.bon.sol.est, d.km.distance);
  });
  it("le vent en km/h vient de la mesure : 9,5 m/s × 3,6", () => {
    pres(d.km.vent_kmh, src.vent.vitesse_m_s * 3.6);
    pres(Math.hypot(d.km.vent.est, d.km.vent.nord), d.km.vent_kmh);
    pres(d.km.naif.longueur, d.km.avion_kmh + d.km.vent_kmh);
  });
  it("le sondage contient 342 niveaux et le niveau mesuré à 1222 m", () => {
    expect(d.niveaux.length).toBe(342);
    expect(d.niveaux.some(([h, dir, v]) => h === 1222 && dir === 316 && v === 9.5)).toBe(true);
  });
});
