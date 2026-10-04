"""First-load intro screen for app.py: pure HTML/CSS, no scripts, fonts or network requests.

A fixed overlay shows the heat chain (server rack -> pipe -> salt battery -> pipe -> apartments) in the
dashboard's chart colors while the first load imports libraries and trains the forecast. app.py clears it
as soon as that work is done. The CSS failsafe hides it after 90 s even if the script errors first.
"""

DC, STORE, WARM, LINE, IDLE, MUTED = "#2b6cb0", "#e8871e", "#f5b94f", "#334155", "#e2e8f0", "#5b6472"

STATUS = ["Capturing server heat…", "Charging the salt battery…", "Training the demand forecast…",
          "Delivering hot water to Fulton Houses…"]

_CSS = f"""
.ch-intro {{position: fixed; inset: 0; z-index: 1000001; background: #ffffff; display: flex; flex-direction: column;
  align-items: center; justify-content: center; gap: 1.1rem; padding: 16px;
  animation: ch-in .25s ease-out, ch-failsafe .3s 90s forwards;}}
.ch-intro .ch-brand {{font-size: 1.25rem; font-weight: 700; color: #1f2937; letter-spacing: .01em;}}
.ch-intro svg {{width: min(560px, 100%); height: auto; overflow: visible;}}
.ch-intro text {{font-size: 11px; fill: {MUTED}; font-family: inherit;}}
.ch-wave {{animation: ch-rise 1.8s ease-in-out infinite; opacity: 0;}}
.ch-led {{animation: ch-blink 1.2s steps(2, jump-none) infinite;}}
.ch-flow {{stroke-dasharray: 0 16; stroke-linecap: round; animation: ch-flow .7s linear infinite;}}
.ch-fill {{transform-box: fill-box; transform-origin: 50% 100%; animation: ch-charge 3.6s ease-in-out infinite;}}
.ch-salt {{animation: ch-melt 3.6s ease-in-out infinite;}}
.ch-win {{fill: {IDLE}; animation: ch-light 3.6s ease-out infinite;}}
.ch-status {{position: relative; height: 1.5em; width: min(560px, 100%); text-align: center; color: {MUTED};
  font-size: .95rem;}}
.ch-status span {{position: absolute; inset: 0; opacity: 0; animation: ch-status 8s infinite;}}
.ch-status .ch-static {{display: none;}}
@keyframes ch-in {{from {{opacity: 0;}} to {{opacity: 1;}}}}
@keyframes ch-failsafe {{to {{opacity: 0; visibility: hidden;}}}}
@keyframes ch-rise {{0% {{opacity: 0; transform: translateY(4px);}} 40% {{opacity: .9;}}
  100% {{opacity: 0; transform: translateY(-10px);}}}}
@keyframes ch-blink {{0% {{opacity: 1;}} 100% {{opacity: .25;}}}}
@keyframes ch-flow {{to {{stroke-dashoffset: -16;}}}}
@keyframes ch-charge {{0% {{transform: scaleY(.06);}} 70%, 100% {{transform: scaleY(1);}}}}
@keyframes ch-melt {{0%, 15% {{opacity: 1;}} 60%, 100% {{opacity: 0;}}}}
@keyframes ch-light {{0%, 20% {{fill: {IDLE};}} 45%, 100% {{fill: {WARM};}}}}
@keyframes ch-status {{0% {{opacity: 0; transform: translateY(4px);}} 4%, 22% {{opacity: 1; transform: none;}}
  26%, 100% {{opacity: 0;}}}}
@media (prefers-reduced-motion: reduce) {{
  .ch-intro {{animation: ch-failsafe .3s 90s forwards;}}
  .ch-intro * {{animation: none !important;}}
  .ch-wave {{opacity: .7;}}
  .ch-win {{fill: {WARM};}}
  .ch-salt {{opacity: 0;}}
  .ch-status span {{display: none;}}
  .ch-status .ch-static {{display: inline; position: static; opacity: 1;}}
}}
"""

# Server rack, left
_RACK = (f'<rect x="20" y="30" width="70" height="110" rx="6" fill="#f8fafc" stroke="{LINE}" stroke-width="1.5"/>'
         + "".join(f'<rect x="30" y="{y}" width="50" height="16" rx="2" fill="{IDLE}"/>'
                   f'<circle class="ch-led" cx="72" cy="{y + 8}" r="2.5" fill="{DC}" style="animation-delay:{i * .3}s"/>'
                   for i, y in enumerate((42, 66, 90, 114)))
         + "".join(f'<path class="ch-wave" d="M{x} 24 q5 -5 0 -10 q-5 -5 0 -10" fill="none" stroke="{DC}" '
                   f'stroke-width="2" stroke-linecap="round" style="animation-delay:{i * .6}s"/>'
                   for i, x in enumerate((38, 55, 72)))
         + '<text x="55" y="160" text-anchor="middle">Data center</text>')


def _pipe(x1, x2, color):
    return (f'<line x1="{x1}" y1="110" x2="{x2}" y2="110" stroke="{IDLE}" stroke-width="10" stroke-linecap="round"/>'
            f'<line class="ch-flow" x1="{x1}" y1="110" x2="{x2}" y2="110" stroke="{color}" stroke-width="5"/>')


# Salt battery, middle: fills from the bottom while the solid salt crystals fade (melt)
_BATTERY = (f'<rect x="245" y="52" width="14" height="8" rx="2" fill="{LINE}"/>'
            f'<rect x="281" y="52" width="14" height="8" rx="2" fill="{LINE}"/>'
            f'<rect x="215" y="60" width="110" height="80" rx="10" fill="#ffffff" stroke="{LINE}" stroke-width="1.5"/>'
            f'<rect class="ch-fill" x="223" y="68" width="94" height="64" rx="5" fill="{STORE}" opacity=".85"/>'
            + "".join(f'<rect class="ch-salt" x="{x}" y="{y}" width="8" height="8" fill="#fff4e5" stroke="{STORE}" '
                      f'transform="rotate(45 {x + 4} {y + 4})"/>'
                      for x, y in ((240, 112), (262, 100), (288, 114), (300, 96)))
            + '<text x="270" y="160" text-anchor="middle">Salt battery</text>')

# Apartment building, right: windows light up warm one after another
_BUILDING = (f'<rect x="440" y="25" width="100" height="115" rx="4" fill="#f8fafc" stroke="{LINE}" stroke-width="1.5"/>'
             + "".join(f'<rect class="ch-win" x="{452 + c * 28}" y="{37 + r * 22}" width="18" height="13" rx="2" '
                       f'style="animation-delay:{(r * 3 + c) * .12:.2f}s"/>'
                       for r in range(4) for c in range(3)))
_BUILDING += (f'<rect x="481" y="124" width="18" height="16" rx="2" fill="{LINE}"/>'
              '<text x="490" y="160" text-anchor="middle">Fulton Houses</text>')

_PIPES = _pipe(92, 213, DC) + _pipe(327, 438, STORE)  # drawn first so they sit under the equipment

_HTML = f"""
<style>{_CSS}</style>
<div class="ch-intro" role="status" aria-live="polite">
<div class="ch-brand">ChelseaHeat</div>
<svg viewBox="0 0 560 170" aria-hidden="true">{_PIPES}{_RACK}{_BATTERY}{_BUILDING}</svg>
<div class="ch-status">{"".join(f'<span style="animation-delay:{i * 2}s">{t}</span>' for i, t in enumerate(STATUS))}<span class="ch-static">Loading the model…</span></div>
</div>
"""

# Streamlit's markdown treats indented lines as code and blank lines as block breaks, so send one line
INTRO_HTML = "".join(line.strip() for line in _HTML.splitlines())
