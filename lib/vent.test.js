// Épreuve 1 du niveau « Vent de travers » : chaque valeur que le niveau affichera
// est comparée à la formule du triangle des vents (1e-6), et la mesure réelle
// est recalculée par la méthode du Pilot's Handbook of Aeronautical Knowledge (FAA) à 0,1° près.
import { describe, expect, it } from "vitest";
import data from "../data/vent_travers.json";
import {
  capPourRoute,
  composantesVent,
  noeudsDepuisMs,
  sommeNaive,
  vecteurSol,
} from "./vent.js";

const TOL = 1e-6;
const rad = (d) => (d * Math.PI) / 180;
const deg = (r) => (r * 180) / Math.PI;

const TAS = data.avion.vitesse_air_kt;
const W = (data.vent.vitesse_m_s * 3600) / 1852; // 1 kt = 1852 m / 3600 s (définition)
const VENT = { vientDuDeg: data.vent.vient_du_deg, vitesseKt: W };
const ROUTE = data.mission.route_voulue_deg;

// Référence indépendante : méthode FAA (PHAK, ch. 16), résolue dans le triangle
// par la loi des sinus (correction de cap) et la loi des cosinus (vitesse sol),
// sans passer par les composantes est/nord utilisées dans lib/vent.js.
function referenceFAA(tas, vientDuDeg, w, route) {
  const angleVent = rad(vientDuDeg - route);
  const correction = deg(Math.asin((w * Math.sin(angleVent)) / tas));
  const cap = route + correction;
  const angleCapVers = rad(vientDuDeg + 180 - cap);
  const gs = Math.sqrt(tas ** 2 + w ** 2 + 2 * tas * w * Math.cos(angleCapVers));
  return { cap, gs };
}

describe("conversion", () => {
  it("9,5 m/s en nœuds avec 1 kt = 1852/3600 m/s", () => {
    expect(noeudsDepuisMs(9.5)).toBeCloseTo((9.5 * 3600) / 1852, 4);
    expect(Math.abs(noeudsDepuisMs(9.5) - (9.5 * 3600) / 1852)).toBeLessThan(TOL);
    // le facteur du JSON est l'arrondi à 6 décimales de la définition
    expect(Math.abs(data.conversion.metres_par_seconde_par_noeud - 1852 / 3600)).toBeLessThan(1e-6);
  });
});

describe("composantes du vent", () => {
  it("vent du 316° sur route 090° : travers vers le sud, vent arrière", () => {
    const c = composantesVent(VENT, ROUTE);
    expect(Math.abs(c.traversKt - W * Math.sin(rad(316 - 90)))).toBeLessThan(TOL);
    expect(Math.abs(c.faceKt - W * Math.cos(rad(316 - 90)))).toBeLessThan(TOL);
    expect(c.traversKt).toBeLessThan(0); // pousse vers la droite de la route : le sud
    expect(c.faceKt).toBeLessThan(0); // vent de face négatif = vent arrière
  });
});

describe("cap pour tenir la route 090°", () => {
  const r = capPourRoute(TAS, VENT, ROUTE);
  const ref = referenceFAA(TAS, VENT.vientDuDeg, W, ROUTE);

  it("égale la formule du triangle des vents à 1e-6", () => {
    const c = composantesVent(VENT, ROUTE);
    expect(Math.abs(r.capDeg - (ROUTE + deg(Math.asin(c.traversKt / TAS))))).toBeLessThan(TOL);
  });
  it("recalculée par la méthode FAA : cap à 0,1° près, vitesse sol à 1e-6", () => {
    expect(Math.abs(r.capDeg - ref.cap)).toBeLessThan(0.1);
    expect(Math.abs(r.vitesseSolKt - ref.gs)).toBeLessThan(TOL);
  });
  it("donne les valeurs du plan : 083,6° et 131,1 kt", () => {
    expect(r.capDeg).toBeCloseTo(83.59, 2);
    expect(r.vitesseSolKt).toBeCloseTo(131.08, 2);
  });
  it("avec ce cap, la somme des vecteurs suit bien la route 090°", () => {
    const s = vecteurSol(TAS, r.capDeg, VENT);
    expect(Math.abs(s.routeDeg - ROUTE)).toBeLessThan(TOL);
    expect(Math.abs(s.vitesseSolKt - r.vitesseSolKt)).toBeLessThan(TOL);
  });
  it("renvoie null si le vent de travers dépasse la vitesse air", () => {
    expect(capPourRoute(10, { vientDuDeg: 0, vitesseKt: 20 }, 90)).toBeNull();
  });
});

describe("le joueur pointe plein est (cap 090°)", () => {
  const s = vecteurSol(TAS, 90, VENT);
  it("somme des vecteurs avion + vent, composante par composante", () => {
    const vers = rad(VENT.vientDuDeg + 180);
    expect(Math.abs(s.estKt - (TAS + W * Math.sin(vers)))).toBeLessThan(TOL);
    expect(Math.abs(s.nordKt - W * Math.cos(vers))).toBeLessThan(TOL);
  });
  it("dérive 13,28 NM/h au sud, route 095,75°, vitesse sol 132,50 kt", () => {
    expect(s.nordKt).toBeCloseTo(-13.28, 2);
    expect(s.routeDeg).toBeCloseTo(95.75, 2);
    expect(s.vitesseSolKt).toBeCloseTo(132.5, 2);
  });
  it("la fausse idée (119 + 18,5) donne une autre vitesse que la vraie somme", () => {
    expect(Math.abs(sommeNaive(TAS, VENT) - (TAS + W))).toBeLessThan(TOL);
    expect(sommeNaive(TAS, VENT) - s.vitesseSolKt).toBeGreaterThan(4);
  });
});

describe("entrées invalides", () => {
  it("refuse une vitesse non finie ou négative", () => {
    expect(() => vecteurSol(Number.NaN, 90, VENT)).toThrow();
    expect(() => vecteurSol(119, 90, { vientDuDeg: 316, vitesseKt: -1 })).toThrow();
  });
});
