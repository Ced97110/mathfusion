// Épreuve 1, partie approfondie : exemple publié par la FAA, propriétés sur des milliers
// de cas tirés au hasard (fast-check), tolérance d'arrivée réelle, et preuve que le cap
// doit être bloqué en vol.
import fc from "fast-check";
import { describe, expect, it } from "vitest";
import data from "../data/vent_travers.json";
import { capPourRoute, ecartAuSeuilM, vecteurSol } from "./vent.js";

const TOL = 1e-6;
const ecartAngle = (a, b) => Math.abs(((a - b + 540) % 360) - 180);

describe("exemple résolu publié par la FAA (PHAK, fig. 16-21 à 16-23)", () => {
  const ex = data.exemple_faa;
  const r = capPourRoute(ex.vitesse_air_kt, { vientDuDeg: ex.vent_vient_du_deg, vitesseKt: ex.vent_kt }, ex.route_deg);
  // La FAA trace au rapporteur et arrondit au degré et au nœud : la tolérance ne peut pas être plus fine.
  it("cap 076°, correction 14° à gauche, vitesse sol 88 kt (à ±0,5 près)", () => {
    expect(Math.abs(r.capDeg - ex.resultat_cap_deg)).toBeLessThanOrEqual(0.5);
    expect(Math.abs(r.correctionDeg - ex.resultat_correction_deg)).toBeLessThanOrEqual(0.5);
    expect(Math.abs(r.vitesseSolKt - ex.resultat_vitesse_sol_kt)).toBeLessThanOrEqual(0.5);
  });
});

describe("propriétés sur 10 000 cas tirés au hasard", () => {
  const cas = fc.record({
    tas: fc.double({ min: 40, max: 300, noNaN: true }),
    ratio: fc.double({ min: 0, max: 0.95, noNaN: true }),
    vientDu: fc.double({ min: 0, max: 360, noNaN: true }),
    route: fc.double({ min: 0, max: 360, noNaN: true }),
  });

  it("avec le cap calculé, la somme des vecteurs suit exactement la route voulue", () => {
    fc.assert(
      fc.property(cas, ({ tas, ratio, vientDu, route }) => {
        const vent = { vientDuDeg: vientDu, vitesseKt: tas * ratio };
        const r = capPourRoute(tas, vent, route);
        const s = vecteurSol(tas, r.capDeg, vent);
        return ecartAngle(s.routeDeg, route) < TOL && Math.abs(s.vitesseSolKt - r.vitesseSolKt) < TOL;
      }),
      { numRuns: 10000 },
    );
  });

  it("la longueur de la somme suit la loi des cosinus", () => {
    fc.assert(
      fc.property(cas, fc.double({ min: 0, max: 360, noNaN: true }), ({ tas, ratio, vientDu }, cap) => {
        const w = tas * ratio;
        const s = vecteurSol(tas, cap, { vientDuDeg: vientDu, vitesseKt: w });
        const angle = ((vientDu + 180 - cap) * Math.PI) / 180;
        const attendu = Math.sqrt(tas ** 2 + w ** 2 + 2 * tas * w * Math.cos(angle));
        return Math.abs(s.vitesseSolKt - attendu) < TOL;
      }),
      { numRuns: 10000 },
    );
  });

  it("sans vent, le cap égale la route et la vitesse sol égale la vitesse air", () => {
    fc.assert(
      fc.property(cas, ({ tas, route }) => {
        const r = capPourRoute(tas, { vientDuDeg: 0, vitesseKt: 0 }, route);
        return ecartAngle(r.capDeg, route) < TOL && Math.abs(r.vitesseSolKt - tas) < TOL;
      }),
      { numRuns: 10000 },
    );
  });
});

describe("tolérance d'arrivée réelle : 700 ft de large au seuil (AIM)", () => {
  const demiLargeurM = (data.tolerance_arrivee.largeur_totale_ft / 2) * 0.3048;
  const vent = { vientDuDeg: data.vent.vient_du_deg, vitesseKt: (data.vent.vitesse_m_s * 3600) / 1852 };
  const tas = data.avion.vitesse_air_kt;
  const route = data.mission.route_voulue_deg;
  // Distance d'essai : une heure de vol avec le bon cap (choix de conception, à fixer).
  const distanceNm = capPourRoute(tas, vent, route).vitesseSolKt;
  const gagne = (cap) => Math.abs(ecartAuSeuilM(vecteurSol(tas, cap, vent).routeDeg, route, distanceNm)) <= demiLargeurM;

  it("au dixième de degré, seul le cap 083,6° gagne", () => {
    expect(gagne(83.6)).toBe(true);
    expect(gagne(83.5)).toBe(false);
    expect(gagne(83.7)).toBe(false);
  });
  it("le cap de la fausse idée (pointer la piste, 090°) rate de plusieurs kilomètres", () => {
    expect(Math.abs(ecartAuSeuilM(vecteurSol(tas, 90, vent).routeDeg, route, distanceNm))).toBeGreaterThan(20000);
  });
});

describe("pourquoi le cap doit être bloqué en vol", () => {
  it("si le joueur vise sans cesse la piste, il arrive sans avoir additionné les vecteurs", () => {
    const vent = { vientDuDeg: data.vent.vient_du_deg, vitesseKt: (data.vent.vitesse_m_s * 3600) / 1852 };
    const tas = data.avion.vitesse_air_kt;
    // Poursuite : départ à 131 NM à l'ouest de la piste, cap recalculé vers la piste toutes les 0,36 s.
    let x = -131;
    let y = 0;
    const dt = 1e-4; // heures
    for (let i = 0; i < 20000 && Math.hypot(x, y) > 0.05; i += 1) {
      const capVersPiste = ((Math.atan2(-x, -y) * 180) / Math.PI + 360) % 360;
      const s = vecteurSol(tas, capVersPiste, vent);
      x += s.estKt * dt;
      y += s.nordKt * dt;
    }
    expect(Math.hypot(x, y)).toBeLessThan(0.05); // à moins de 93 m de la piste
  });
});
