// Copyright: Your Name. Apache 2.0
// GLSL sources of the CARTE scene (shots 4-9). Two full-frame quads:
//   carteSol    — the designed polder map (static, analytically anti-aliased, dark and desaturated);
//   carteDessin — every vector element (arrows, aeroplanes, balloon, rings, arc, cross, scale, text),
//                 drawn as signed distance fields: edges are filtered with fwidth, so the image is
//                 crisp at any resolution without MSAA. Output is premultiplied alpha.
// Units: world x, z in km (+x east, -z north). Colours are display-ready sRGB (no tone mapping).

const COMMUN = /* glsl */ `
#extension GL_OES_standard_derivatives : enable
precision highp float;
varying vec2 vP;
float hash12(vec2 p) { vec3 p3 = fract(vec3(p.xyx) * .1031); p3 += dot(p3, p3.yzx + 33.33); return fract((p3.x + p3.y) * p3.z); }
// Exact 1D box-filtered coverage of a band of half width hw, at distance d from its centre, pixel footprint fw.
float couv(float d, float hw, float fw) { return clamp((min(d + .5 * fw, hw) - max(d - .5 * fw, -hw)) / fw, 0., 1.); }
`;

export const VERTEX = /* glsl */ `
precision highp float;
attribute vec3 position;
uniform mat4 world;
uniform mat4 viewProjection;
varying vec2 vP;
void main() {
  vec4 w = world * vec4(position, 1.);
  vP = w.xz;
  gl_Position = viewProjection * w;
}
`;

export const SOL = COMMUN + /* glsl */ `
uniform vec4 uCadre; // frame centre (x, z) and half extents (km)

float vnoise(vec2 p) {
  vec2 i = floor(p), f = fract(p);
  vec2 u = f * f * f * (f * (f * 6. - 15.) + 10.); // C2 interpolation: no visible cells
  float a = hash12(i), b = hash12(i + vec2(1., 0.)), c = hash12(i + vec2(0., 1.)), d = hash12(i + vec2(1., 1.));
  return mix(mix(a, b, u.x), mix(c, d, u.x), u.y);
}
float relief(vec2 q) { return .6 * vnoise(q / 41.) + .28 * vnoise(q / 17.3 + 4.1) + .12 * vnoise(q / 6.9 - 2.7); }

const float RH = 6.2;  // polder row height, km
const float BW = 8.7;  // polder block width, km

// Colour of one polder block at local coordinates l (km), with its strips filtered for footprint fw.
vec3 bloc(vec2 id, vec2 l, float fw) {
  float hb = hash12(id + 7.13);
  float s = mix(.24, .62, hash12(id + 3.71));            // strip width
  float w = (hb < .58 ? l.x : l.y) / s;
  float fu = fw / s;
  float c = floor(w + .5);
  float dd = w - c;                                      // signed distance to the nearest strip edge
  float t = clamp(dd / max(fu, 1e-4) + .5, 0., 1.);
  float v = mix(hash12(id * 13.1 + vec2(c - 1., 1.7)), hash12(id * 13.1 + vec2(c, 1.7)), t);
  v = mix(v, .5, clamp(fu * 1.4 - .5, 0., 1.));          // strips finer than a pixel: their average
  float fosse = couv(abs(dd) * s, .016, fw);             // thin ditch between strips
  float k = hash12(id + 1.9);
  vec3 base = k < .45 ? vec3(.112, .126, .119) : (k < .8 ? vec3(.124, .126, .112) : vec3(.128, .118, .108));
  base *= .955 + .09 * hash12(id + 5.3);
  vec3 col = base * (.94 + .12 * v);
  return mix(col, vec3(.082, .092, .096), .7 * fosse);
}

vec3 rangee(float j, float x, float fw, out float dxBord) {
  float off = hash12(vec2(j, 2.31)) * BW;
  float xx = x + off;
  float i = floor(xx / BW);
  float lx = xx - i * BW;
  dxBord = lx < .5 * BW ? lx : lx - BW;
  return vec3(i, lx, off);
}

void main() {
  vec2 q = vec2(vP.x, -vP.y);                            // (east, north)
  vec2 fwv = fwidth(vP);
  float fw = max(max(fwv.x, fwv.y), 1e-4);
  const float A = .33;                                   // polders are not aligned with the route
  vec2 r = mat2(cos(A), sin(A), -sin(A), cos(A)) * q;

  // --- polder blocks, blended analytically across the nearest block and row edges
  float j = floor(r.y / RH);
  float ly = r.y - j * RH;
  float dyBord = ly < .5 * RH ? ly : ly - RH;
  float dx;
  vec3 g = rangee(j, r.x, fw, dx);
  vec3 cC = bloc(vec2(g.x, j), vec2(g.y, ly), fw);
  vec3 cX = dx < 0. ? bloc(vec2(g.x + 1., j), vec2(g.y - BW, ly), fw) : bloc(vec2(g.x - 1., j), vec2(g.y + BW, ly), fw);
  float jn = dyBord < 0. ? j + 1. : j - 1.;
  float dxn;
  vec3 gn = rangee(jn, r.x, fw, dxn);
  vec3 cY = bloc(vec2(gn.x, jn), vec2(gn.y, dyBord < 0. ? ly - RH : ly + RH), fw);
  vec3 col = mix(cY, mix(cX, cC, clamp(abs(dx) / fw + .5, 0., 1.)), clamp(abs(dyBord) / fw + .5, 0., 1.));

  // --- soft relief light from the north-west
  float e = .7;
  float h0 = relief(q);
  vec2 grad = vec2(relief(q + vec2(e, 0.)) - h0, relief(q + vec2(0., e)) - h0) / e;
  float lum = 1. + .28 * dot(grad * 30., normalize(vec2(-1., 1.)));
  col *= clamp(lum, .88, 1.1) * (.95 + .1 * h0);

  // --- roads (block edges) and ditches (row edges); every fifth row edge is a canal
  vec3 eau = vec3(.066, .082, .096);
  col = mix(col, vec3(.158, .162, .164), .55 * couv(abs(dx), .045, fw));
  float jb = floor(r.y / RH + .5);
  float large = mod(jb, 5.) == 0. ? .19 : .055;
  col = mix(col, eau, .85 * couv(abs(dyBord), large, fw));

  // --- a meandering river to the north and a group of lakes to the south-west
  float fr = 47. + 5.5 * sin(q.x / 31. + .5) + 2.4 * sin(q.x / 11.3 + 2.);
  float dfr = 5.5 / 31. * cos(q.x / 31. + .5) + 2.4 / 11.3 * cos(q.x / 11.3 + 2.);
  float dr = abs(q.y - fr) / sqrt(1. + dfr * dfr);
  col = mix(col, col * .86 + vec3(.0, .004, .006), couv(dr, 2.2, fw) * .6);   // flood plain
  col = mix(col, eau, couv(dr, .42, fw));
  float zone = exp(-dot((q - vec2(-38., -57.)) / vec2(26., 13.), (q - vec2(-38., -57.)) / vec2(26., 13.)));
  float f = vnoise(q / 7.5 + 9.) * .72 + vnoise(q / 2.9) * .28 + zone * .62 - .86;
  col = mix(col, eau * 1.05, .35 * clamp(f / max(fwidth(f), 1e-5) + .5, 0., 1.) * step(.02, zone)); // faint: never competes with arrows

  // --- vignette towards the frame edges, then dithering against banding
  vec2 dv = (vP - uCadre.xy) / uCadre.zw;
  col *= 1. - .32 * smoothstep(.62, 1.35, length(dv * vec2(.82, 1.)));
  col += (hash12(gl_FragCoord.xy) - .5) / 255.;
  gl_FragColor = vec4(col, 1.);
}
`;

export const DESSIN = COMMUN + /* glsl */ `
uniform vec4 uFl0, uFl1, uFl2;     // arrows blue, violet, green: (tail.x, tail.z, tip.x, tip.z)
uniform vec4 uCo0, uCo1, uCo2;     // their colour and opacity
uniform vec4 uLigne;               // intended line: depart (x, z), runway (x, z)
uniform vec4 uDivers;              // line alpha, runway arrival glow, arrival pulse, aeroplanes above arrows (1/0)
uniform vec4 uRA, uRB, uRC;        // answer rings: (x, z, alpha, green amount)
uniform vec4 uLet;                 // letters alpha A, B, C, ring pulse of B
uniform vec4 uLien0, uLien1;       // dashed links ghost -> real, balloon -> real
uniform vec4 uDivers2;             // links alpha, trail alpha, offset marker alpha, unused
uniform vec4 uTrace;               // green trail: depart (x, z), real aeroplane (x, z)
uniform vec4 uEcart;               // offset marker segment
uniform vec4 uArc;                 // orange arc: centre (x, z), current angle (rad, east = 0, north positive), alpha
uniform vec4 uCroix;               // red cross: (x, z, progress, unused)
uniform vec4 uBallon;              // (x, z, alpha, unused)
uniform vec4 uFant, uAvion;        // ghost and real aeroplane: (x, z, nose angle from north clockwise, alpha)
uniform vec4 uNord, uEch;          // north mark and scale bar: (x, z, alpha, unused)
uniform vec4 uEp;                  // x: stroke width factor (1.4 on the phone frame), y: runway size 0 small .. 1 large (shot 9)
uniform vec3 uBleu, uViolet, uVert, uOrange, uRouge, uGris;
uniform sampler2D atlas;

vec4 acc = vec4(0.);
float FW = 1.;
void poser(vec3 c, float a) { a = clamp(a, 0., 1.); acc.rgb = c * a + acc.rgb * (1. - a); acc.a = a + acc.a * (1. - a); }
float remp(float d) { return clamp(.5 - d / FW, 0., 1.); }

float sdSeg(vec2 p, vec2 a, vec2 b) { vec2 pa = p - a, ba = b - a; float h = clamp(dot(pa, ba) / max(dot(ba, ba), 1e-6), 0., 1.); return length(pa - ba * h); }
float sdBox(vec2 p, vec2 b) { vec2 d = abs(p) - b; return length(max(d, 0.)) + min(max(d.x, d.y), 0.); }
float sdTri(vec2 p, vec2 p0, vec2 p1, vec2 p2) {
  vec2 e0 = p1 - p0, e1 = p2 - p1, e2 = p0 - p2;
  vec2 v0 = p - p0, v1 = p - p1, v2 = p - p2;
  vec2 pq0 = v0 - e0 * clamp(dot(v0, e0) / dot(e0, e0), 0., 1.);
  vec2 pq1 = v1 - e1 * clamp(dot(v1, e1) / dot(e1, e1), 0., 1.);
  vec2 pq2 = v2 - e2 * clamp(dot(v2, e2) / dot(e2, e2), 0., 1.);
  float s = sign(e0.x * e2.y - e0.y * e2.x);
  vec2 d = min(min(vec2(dot(pq0, pq0), s * (v0.x * e0.y - v0.y * e0.x)), vec2(dot(pq1, pq1), s * (v1.x * e1.y - v1.y * e1.x))), vec2(dot(pq2, pq2), s * (v2.x * e2.y - v2.y * e2.x)));
  return -sqrt(d.x) * sign(d.y);
}
float sdCaps(vec2 p, float r1, float r2, float h) { // uneven capsule along +y (iq)
  p.x = abs(p.x);
  float b = (r1 - r2) / h, a = sqrt(1. - b * b), k = dot(p, vec2(-b, a));
  if (k < 0.) return length(p) - r1;
  if (k > a * h) return length(p - vec2(0., h)) - r2;
  return dot(p, vec2(a, b)) - r1;
}

// Arrow from a to b: shaft half width .85 km, head 10 km long, 4.4 km half wide (shrinks for short arrows).
float sdFleche(vec2 p, vec4 ab) {
  vec2 d = ab.zw - ab.xy; float L = length(d);
  if (L < .05) return 1e4;
  vec2 u = d / L, v = vec2(-u.y, u.x);
  vec2 l = vec2(dot(p - ab.xy, u), dot(p - ab.xy, v));
  float k = uEp.x;
  float h = min(10. * k, .55 * L), hw = 4.4 * h / 10., sw = min(.85 * k, .42 * hw);
  float corps = sdBox(l - vec2(.5 * (L - h), 0.), vec2(max(.5 * (L - h), 0.), sw)) ;
  return min(corps, sdTri(l, vec2(L - h - .01, hw), vec2(L - h - .01, -hw), vec2(L, 0.)));
}
const vec2 OMBRE = vec2(.55, .75);   // arrows float a little above the map: light from the north-west
void fleche(vec2 p, vec4 ab, vec4 co) {
  if (co.a < .002) return;
  float ds = sdFleche(p - OMBRE, ab);
  poser(vec3(0.), .42 * co.a * (1. - smoothstep(-.9, 1.5, ds)));
  float d = sdFleche(p, ab);
  poser(co.rgb, co.a * .30 * exp(-max(d, 0.) / 2.4));                   // soft glow
  poser(co.rgb * (1. + .10 * smoothstep(-.9, 0., d)), co.a * remp(d));  // crisp body, lighter rim
}

// High-wing light aeroplane seen from above, in metres, nose along +u.
float sdAvion(vec2 l) {
  vec2 s = vec2(l.y, l.x);                                  // s.x across, s.y along (nose +)
  float fus = sdBox(s - vec2(0., .75), vec2(.5, 1.65)) - .18;
  fus = min(fus, sdCaps(vec2(s.x, -(s.y + .9)), .58, .17, 4.3));
  fus = min(fus, length(s - vec2(0., 2.55)) - .3);         // spinner
  float aile = sdBox(s - vec2(0., .05), vec2(5.5 - .25, .75 - .1)) - .12;
  float ta = sdBox(s - vec2(0., -4.75), vec2(1.7 - .2, .45)) - .14;
  return min(min(fus, aile), ta);
}
vec2 repere(vec2 p, vec2 c, float a) { // nose direction (sin a, -cos a) in world (x, z)
  vec2 f = vec2(sin(a), -cos(a)), r = vec2(cos(a), sin(a));
  return vec2(dot(p - c, f), dot(p - c, r));
}
void avion(vec2 p, vec4 st, bool fantome) {
  if (st.w < .002) return;
  const float SA = 1.35;                                   // drawn at 1.35 km per metre of aeroplane
  vec2 l = repere(p, st.xy, st.z) / SA;
  vec2 ls = repere(p - vec2(2.2, 3.), st.xy, st.z) / SA;
  poser(vec3(0.), st.w * (fantome ? .16 : .45) * (1. - smoothstep(-.8, 1.8, sdAvion(ls) * SA)));
  float d = sdAvion(l) * SA;
  if (fantome) {
    poser(uBleu, st.w * .28 * exp(-max(d, 0.) / 1.6));
    poser(uBleu, st.w * .5 * remp(d));
    poser(uBleu * 1.15, st.w * .9 * remp(abs(d + .09) - .09));          // bright outline
  } else {
    poser(vec3(.06, .07, .08), st.w * remp(d - .14));                     // dark keyline
    vec3 c = vec3(.95);
    float aile = abs(l.x - .05) < .85 && abs(l.y) < 5.6 ? 1. : 0.;
    c *= 1. - .07 * aile * smoothstep(.2, -.7, l.x);                       // flaps a shade darker
    c = mix(c, vec3(.32, .37, .42), remp((sdBox(vec2(l.y, l.x + 1.25), vec2(.3, .3)) - .05) * SA)); // rear window
    c = mix(c, vec3(.55), .8 * remp((abs(abs(l.y) - 2.6) - .03) * SA) * aile * step(abs(l.x - .05), .7)); // flap/aileron joint
    poser(c, st.w * remp(d));
  }
}

float glyphe(vec2 p, vec2 c, vec2 taille, vec4 cell) { // cell: x0, y0, w, h in atlas units (top-left origin)
  vec2 l = (p - c) / taille + .5;
  vec2 uv = vec2(cell.x + l.x * cell.z, 1. - (cell.y + l.y * cell.w));
  float a = texture2D(atlas, uv).a;
  return a * step(0., l.x) * step(l.x, 1.) * step(0., l.y) * step(l.y, 1.);
}

void anneau(vec2 p, vec4 r, float puls) {
  if (r.z < .002) return;
  vec3 c = mix(uGris, uVert, r.w);
  float R = 5.4 * (1. + .22 * puls);
  float d = length(p - r.xy);
  poser(c, r.z * .07 * (1. - smoothstep(R - FW, R, d)));
  poser(c, r.z * .35 * r.w * exp(-abs(d - R) / 1.6));
  poser(c, r.z * couv(abs(d - R), .32 + .12 * r.w, FW));
}

float tirets(vec2 p, vec2 a, vec2 b, float hw) {
  vec2 ab = b - a; float L = length(ab);
  if (L < .1) return 0.;
  vec2 u = ab / L;
  float s = dot(p - a, u), n = abs(dot(p - a, vec2(-u.y, u.x)));
  float per = 2.6, w = fract(s / per) - .5;
  float dash = couv(abs(w) * per, .3 * per, FW) * step(0., s) * step(s, L);
  return dash * couv(n, hw, FW);
}

void main() {
  vec2 p = vP;
  vec2 fwv = fwidth(vP);
  FW = max(max(fwv.x, fwv.y), 1e-4);

  // --- static furniture: intended line, departure point, runway, scale, north
  float la = uDivers.x;
  poser(uGris, la * .55 * couv(sdSeg(p, uLigne.xy, uLigne.zw), .2, FW));
  float dd = length(p - uLigne.xy);
  poser(uGris, la * .9 * couv(abs(dd - 1.6), .28, FW));
  poser(uGris, la * .9 * remp(dd - .55));
  vec2 e = uEch.xy;
  float ech = min(sdSeg(p, e, e + vec2(50., 0.)) - .28, min(sdSeg(p, e - vec2(0., 1.2), e + vec2(0., .4)), sdSeg(p, e + vec2(50., -1.2), e + vec2(50., .4))) - .22);
  ech = min(ech, sdSeg(p, e + vec2(25., -.8), e + vec2(25., 0.)) - .18);
  poser(uGris, uEch.z * .85 * remp(ech));
  poser(vec3(.9, .92, .95), uEch.z * glyphe(p, e + vec2(25., -5.4), vec2(19., 9.5), vec4(0., .5, .5, .5))); // >= 7:1 on the map
  vec2 nn = uNord.xy;
  float nd = min(sdTri(p, nn + vec2(0., -5.), nn + vec2(-1.7, .6), nn + vec2(0., -.6)), sdTri(p, nn + vec2(0., -5.), nn + vec2(0., -.6), nn + vec2(1.7, .6)));
  poser(uGris, uNord.z * .85 * remp(nd));
  poser(uGris, uNord.z * .35 * remp(abs(sdTri(p, nn + vec2(0., -5.), nn + vec2(0., -.6), nn + vec2(1.7, .6))) - .06));
  poser(vec3(.9, .92, .95), uNord.z * glyphe(p, nn + vec2(0., -9.5), vec2(8.5, 8.5), vec4(.75, 0., .25, .5)));

  // --- answer rings and letters
  anneau(p, uRA, 0.);
  anneau(p, uRB, uLet.w);
  anneau(p, uRC, 0.);
  poser(uGris, uLet.x * glyphe(p, uRA.xy + vec2(10.2, 0.), vec2(9., 9.), vec4(0., 0., .25, .5)));
  poser(mix(uGris, uVert, uRB.w), uLet.y * glyphe(p, uRB.xy + vec2(10.2, 0.), vec2(9., 9.), vec4(.25, 0., .25, .5)));
  poser(uGris, uLet.z * glyphe(p, uRC.xy + vec2(10.2, 0.), vec2(9., 9.), vec4(.5, 0., .25, .5)));

  // --- runway at the arrival: a light 20 x 3.5 km strip with its centreline and threshold bars, above
  // the rings so the green tip can be seen landing on it (shot 9); glows green on arrival
  // (small before shot 9, so the crossed point of shot 8 stays clearly beyond its far end)
  float kp = uEp.y;
  vec2 lp = p - uLigne.zw - vec2(mix(4.5, 6., kp), 0.);       // the arrival point lies on the runway, near its threshold
  float arr = uDivers.y;
  vec2 dimP = mix(vec2(4.5, .8), vec2(10., 1.75), kp);
  float rw = sdBox(lp, dimP);
  poser(uVert, arr * (.25 + .2 * uDivers.z) * exp(-max(rw, 0.) / 3.));
  poser(vec3(0.), la * .5 * (1. - smoothstep(-.4, .9, sdBox(lp - OMBRE * .5, dimP))));
  poser(mix(vec3(.58, .61, .65), mix(vec3(.58, .61, .65), uVert, .55), arr), la * remp(rw - .05));
  poser(vec3(.16, .17, .19), la * .7 * remp(abs(rw + .22) - .07));                 // dark edge line
  float tir = couv(abs(fract(lp.x / 1.5) - .5) * 1.5, .38, FW) * step(abs(lp.x), dimP.x - 1.6);
  poser(vec3(.97), la * .9 * tir * couv(abs(lp.y), .12, FW));
  poser(vec3(.97), la * .9 * couv(abs(abs(lp.x) - dimP.x + .6), .14, FW) * step(abs(lp.y), dimP.y - .35) * couv(abs(fract(lp.y / .45) - .5) * .45, .1, FW));

  // --- green trail, links of the parallelogram, offset marker, orange arc
  poser(uVert, uDivers2.y * .55 * couv(sdSeg(p, uTrace.xy, uTrace.zw), .5, FW));
  poser(uViolet, uDivers2.x * .85 * tirets(p, uLien0.xy, uLien0.zw, .2));
  poser(uBleu, uDivers2.x * .85 * tirets(p, uLien1.xy, uLien1.zw, .2));
  if (uDivers2.z > .002) {
    float m = tirets(p, uEcart.xy, uEcart.zw, .2);
    m = max(m, couv(sdSeg(p, uEcart.xy - vec2(1.6, 0.), uEcart.xy + vec2(1.6, 0.)), .2, FW));
    m = max(m, couv(sdSeg(p, uEcart.zw - vec2(1.6, 0.), uEcart.zw + vec2(1.6, 0.)), .2, FW));
    poser(uGris, uDivers2.z * .9 * m);
  }
  if (uArc.w > .002) {
    vec2 q = p - uArc.xy; q.y = -q.y;                                       // (east, north)
    float R = 100., an = clamp(atan(q.y, q.x), 0., uArc.z);
    float da = length(q - R * vec2(cos(an), sin(an)));
    vec2 b = R * vec2(cos(uArc.z), sin(uArc.z)), tg = vec2(-sin(uArc.z), cos(uArc.z)), rd = vec2(cos(uArc.z), sin(uArc.z));
    float dt = sdTri(q, b + tg * 4.2, b - tg * .5 + rd * 2.6, b - tg * .5 - rd * 2.6);
    float d = min(da - .62, uArc.z > .01 ? dt : 1e4);
    poser(uOrange, uArc.w * .3 * exp(-max(d, 0.) / 1.8));
    poser(uOrange, uArc.w * remp(d));
  }


  // --- balloon: lit disc, soft glow, short string
  if (uBallon.z > .002) {
    vec2 b = uBallon.xy, q = p - b;
    float R = 3.;
    float fil = sdSeg(q, vec2(.0, R - .1), vec2(.35, R + 1.3));
    fil = min(fil, sdSeg(q, vec2(.35, R + 1.3), vec2(-.1, R + 2.7))) - .1;
    poser(vec3(0.), uBallon.z * .35 * (1. - smoothstep(-.6, 1.3, length(q - vec2(1.4, 1.9)) - R)));
    poser(uViolet * .8, uBallon.z * remp(fil));
    float d = length(q) - R;
    poser(uViolet, uBallon.z * .38 * exp(-max(d, 0.) / 2.2));
    vec2 n = q / R;
    float z = sqrt(max(1. - dot(n, n), 0.));
    float lum = .62 + .5 * max(dot(vec3(n.x, -n.y, z), normalize(vec3(-.5, .55, .67))), 0.);
    vec3 c = uViolet * lum + vec3(1.) * .55 * pow(max(dot(vec3(n.x, -n.y, z), normalize(vec3(-.35, .4, .85))), 0.), 28.);
    poser(c, uBallon.z * remp(d));
  }

  // --- aeroplanes under the arrows once they rest on an arrow tip (shots 8-9)
  if (uDivers.w < .5) { avion(p, uFant, true); avion(p, uAvion, false); }

  // --- the three arrows (green under blue under violet: the sliding arrow stays on top)
  fleche(p, uFl2, uCo2);
  fleche(p, uFl0, uCo0);
  fleche(p, uFl1, uCo1);

  // --- aeroplanes above the arrows while they travel (shots 4-7)
  if (uDivers.w >= .5) { avion(p, uFant, true); avion(p, uAvion, false); }

  // --- red cross over the wrong point, drawn stroke by stroke
  if (uCroix.z > .002) {
    vec2 c = uCroix.xy;
    float k1 = clamp(uCroix.z * 2., 0., 1.), k2 = clamp(uCroix.z * 2. - 1., 0., 1.);
    float d = sdSeg(p, c + vec2(-6., -6.), c + vec2(-6., -6.) + vec2(12., 12.) * k1) - .75;
    if (k2 > 0.) d = min(d, sdSeg(p, c + vec2(6., -6.), c + vec2(6., -6.) + vec2(-12., 12.) * k2) - .75);
    poser(vec3(0.), .4 * (1. - smoothstep(-.8, 1.3, d - .9)));
    poser(uRouge, .35 * exp(-max(d, 0.) / 2.));
    poser(uRouge, remp(d));
  }

  gl_FragColor = acc;
}
`;
