"""
F1 2026 Season Predictor — Powered by Claude AI
================================================
Run in VS Code terminal:
  python f1_predictor_2026.py

Requirements:
  pip install anthropic

You'll need an Anthropic API key: https://console.anthropic.com
Set it as an environment variable:
  Windows:  set ANTHROPIC_API_KEY=your_key_here
  Mac/Linux: export ANTHROPIC_API_KEY=your_key_here
Or the script will prompt you to enter it.
"""

import os
import sys
import textwrap

try:
    import anthropic
except ImportError:
    print("\n  ❌  Missing dependency. Run:  pip install anthropic\n")
    sys.exit(1)

# ─────────────────────────────────────────────
#  ANSI COLOUR CODES
# ─────────────────────────────────────────────
class C:
    RED     = "\033[91m"
    YELLOW  = "\033[93m"
    CYAN    = "\033[96m"
    GREEN   = "\033[92m"
    WHITE   = "\033[97m"
    GREY    = "\033[90m"
    BOLD    = "\033[1m"
    RESET   = "\033[0m"

# ─────────────────────────────────────────────
#  2026 SEASON DATA
# ─────────────────────────────────────────────
TEAMS = {
    "1":  ("McLaren",       ["Lando Norris (4)",    "Oscar Piastri (81)"],  "Mercedes"),
    "2":  ("Mercedes",      ["George Russell (63)", "Kimi Antonelli (12)"], "Mercedes"),
    "3":  ("Red Bull",      ["Max Verstappen (1)",  "Isack Hadjar (6)"],    "Ford/Honda"),
    "4":  ("Ferrari",       ["Charles Leclerc (16)","Lewis Hamilton (44)"], "Ferrari"),
    "5":  ("Williams",      ["Carlos Sainz (55)",   "Alex Albon (23)"],     "Mercedes"),
    "6":  ("Racing Bulls",  ["Liam Lawson (30)",    "Arvid Lindblad (43)"], "Honda"),
    "7":  ("Aston Martin",  ["Fernando Alonso (14)","Lance Stroll (18)"],   "Mercedes"),
    "8":  ("Haas",          ["Esteban Ocon (31)",   "Oliver Bearman (87)"], "Ferrari"),
    "9":  ("Audi",          ["Nico Hülkenberg (27)","Gabriel Bortoleto (5)"],"Audi"),
    "10": ("Alpine",        ["Pierre Gasly (10)",   "Jack Doohan (7)"],     "Mercedes"),
    "11": ("Cadillac",      ["Sergio Pérez (11)",   "Valtteri Bottas (77)"],"Ferrari"),
}

CALENDAR = [
    ("R1",  "Australia"),   ("R2",  "China"),         ("R3",  "Japan"),
    ("R4",  "Bahrain"),     ("R5",  "Saudi Arabia"),  ("R6",  "Miami"),
    ("R7",  "Canada"),      ("R8",  "Monaco"),        ("R9",  "Spain"),
    ("R10", "Austria"),     ("R11", "Britain"),       ("R12", "Belgium"),
    ("R13", "Hungary"),     ("R14", "Netherlands"),   ("R15", "Italy"),
    ("R16", "Azerbaijan"),  ("R17", "Singapore"),     ("R18", "USA (Austin)"),
    ("R19", "Mexico"),      ("R20", "Brazil"),        ("R21", "Las Vegas"),
    ("R22", "Qatar"),       ("R23", "Madrid"),        ("R24", "Abu Dhabi"),
]

QUICK_QUESTIONS = [
    ("Q1", "Who wins the 2026 Drivers' Championship and why?"),
    ("Q2", "Which team wins the Constructors' title?"),
    ("Q3", "How will Lewis Hamilton perform at Ferrari in his debut season?"),
    ("Q4", "Can Verstappen bounce back after losing his title in 2025?"),
    ("Q5", "How does the active aero regulation change racing strategy?"),
    ("Q6", "Will Adrian Newey transform Aston Martin into title contenders?"),
    ("Q7", "How will Cadillac fare as the new 11th team on the grid?"),
    ("Q8", "Who is the standout rookie — Hadjar, Antonelli, or Lindblad?"),
]

SYSTEM_PROMPT = """You are an expert Formula 1 analyst providing predictions for the 2026 F1 season.
You have deep knowledge of:

2026 SEASON CONTEXT:
- Massive regulation reset: new power units (~50/50 ICE/electric), active aerodynamics, no DRS replaced by
  "Overtake Mode" (within 1 second of car ahead), Active Aero on front/rear wings
- 24 races, starts Australia March 8, ends Abu Dhabi December 6
- New Madrid street circuit added, Imola dropped. 6 Sprint weekends: China, Miami, Canada, GB, Netherlands, Singapore
- Cost cap raised to $215M. Three pre-season tests held

2026 DRIVER LINEUPS:
- McLaren: Lando Norris (reigning WDC #4), Oscar Piastri (#81) — Mercedes power
- Mercedes: George Russell (#63), Kimi Antonelli (#12) — bookies favourite Russell
- Red Bull: Max Verstappen (#1), Isack Hadjar (#6, promoted rookie) — Ford/Honda power
- Ferrari: Charles Leclerc (#16), Lewis Hamilton (#44) — strong preseason pace
- Williams: Carlos Sainz (#55), Alex Albon (#23) — Mercedes power
- Racing Bulls: Liam Lawson (#30), Arvid Lindblad (#43, only true rookie, 18yo) — Honda power
- Aston Martin: Fernando Alonso (#14), Lance Stroll (#18) — Adrian Newey first season, Mercedes power
- Haas: Esteban Ocon (#31), Oliver Bearman (#87) — Ferrari power
- Audi: Nico Hülkenberg (#27), Gabriel Bortoleto (#5) — Audi power unit debut
- Alpine: Pierre Gasly (#10), Jack Doohan (#7) — Mercedes customer power
- Cadillac: Sergio Pérez (#11), Valtteri Bottas (#77) — brand new team, Ferrari power

PRESEASON TESTING:
- Lewis Hamilton set fastest time at Barcelona private test (Jan 26-30)
- Kimi Antonelli set fastest time at Bahrain Test 1 (Feb 11-13)
- Mercedes and Ferrari stood out for engine power
- Reg changes mean 2025 competitiveness does NOT predict 2026 performance reliably

KEY STORYLINES:
- Norris defending his first WDC title, Piastri hungry after near-miss in 2025
- Hamilton's blockbuster Ferrari move — can he win an 8th world title?
- Verstappen must prove himself post-Red Bull dominance era
- Newey at Aston Martin: could be the biggest wildcard of the season
- Cadillac debut: first new F1 team since Haas in 2016
- Audi power unit completely unproven in race conditions
- Active Aero could create unpredictable overtaking patterns

Provide detailed, analytical predictions with clear reasoning. Be specific about performance expectations,
reliability risks, and strategic factors. Use F1 terminology. Acknowledge genuine uncertainty where it exists.
Keep responses focused and readable in a terminal (avoid excessive markdown, prefer plain text with occasional
dashes for structure). Aim for 200-350 words per response unless asked for more detail."""


# ─────────────────────────────────────────────
#  HELPERS
# ─────────────────────────────────────────────
def clear_line():
    print("\r" + " " * 60 + "\r", end="", flush=True)

def wrap_print(text: str, indent: int = 4, width: int = 80):
    """Word-wrap and print text with indent."""
    prefix = " " * indent
    for paragraph in text.split("\n"):
        if paragraph.strip() == "":
            print()
            continue
        # Bold/header-like lines (all caps or starting with --)
        if paragraph.strip().startswith("--") or paragraph.strip().isupper():
            print(f"{C.YELLOW}{prefix}{paragraph.strip()}{C.RESET}")
        elif paragraph.strip().startswith("-"):
            print(f"{C.GREY}{prefix}  {paragraph.strip()}{C.RESET}")
        else:
            wrapped = textwrap.fill(paragraph, width=width - indent,
                                    initial_indent=prefix,
                                    subsequent_indent=prefix)
            print(f"{C.WHITE}{wrapped}{C.RESET}")

def divider(char="─", colour=C.GREY):
    print(f"{colour}{char * 62}{C.RESET}")

def header(title: str):
    divider("═", C.RED)
    print(f"{C.RED}{C.BOLD}  {title}{C.RESET}")
    divider("═", C.RED)

def section(title: str):
    print()
    divider()
    print(f"{C.CYAN}{C.BOLD}  {title}{C.RESET}")
    divider()

def spinner_frames():
    return ["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"]


# ─────────────────────────────────────────────
#  API CALL WITH STREAMING
# ─────────────────────────────────────────────
def ask_claude(client: anthropic.Anthropic, conversation: list, question: str) -> str:
    """Send a message and stream the response."""
    conversation.append({"role": "user", "content": question})

    print(f"\n{C.GREY}  ◼ Analysing...{C.RESET}")
    print()

    full_response = ""
    print(f"  {C.GREEN}", end="", flush=True)

    with client.messages.stream(
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        system=SYSTEM_PROMPT,
        messages=conversation,
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)
            full_response += text

    print(C.RESET)
    conversation.append({"role": "assistant", "content": full_response})
    return full_response


# ─────────────────────────────────────────────
#  MENU SCREENS
# ─────────────────────────────────────────────
def show_teams_menu():
    section("2026 CONSTRUCTOR LINEUP")
    for key, (team, drivers, engine) in TEAMS.items():
        print(f"  {C.YELLOW}{key:>2}.{C.RESET} {C.BOLD}{C.WHITE}{team:<15}{C.RESET}  "
              f"{C.GREY}{engine:<12}{C.RESET}  "
              f"{C.CYAN}{' / '.join(d.split(' (')[0] for d in drivers)}{C.RESET}")

def show_calendar_menu():
    section("2026 RACE CALENDAR")
    cols = 3
    items = list(CALENDAR)
    for i in range(0, len(items), cols):
        row = items[i:i+cols]
        line = "  ".join(
            f"{C.RED}{r:<4}{C.RESET} {C.WHITE}{n:<18}{C.RESET}"
            for r, n in row
        )
        print(f"  {line}")

def show_quick_menu():
    section("QUICK PREDICTION TOPICS")
    for key, question in QUICK_QUESTIONS:
        short = question[:60] + ("..." if len(question) > 60 else "")
        print(f"  {C.YELLOW}{key}{C.RESET}  {C.GREY}{short}{C.RESET}")

def show_main_menu():
    print()
    divider("─", C.GREY)
    print(f"  {C.CYAN}[T]{C.RESET} Teams & Drivers    "
          f"{C.CYAN}[C]{C.RESET} Calendar    "
          f"{C.CYAN}[Q]{C.RESET} Quick Questions")
    print(f"  {C.CYAN}[A]{C.RESET} Ask anything       "
          f"{C.CYAN}[N]{C.RESET} New chat    "
          f"{C.CYAN}[X]{C.RESET} Exit")
    divider("─", C.GREY)


# ─────────────────────────────────────────────
#  TEAM / RACE PREDICTION SHORTCUTS
# ─────────────────────────────────────────────
def pick_team_prediction(client, conversation):
    show_teams_menu()
    print(f"\n  {C.GREY}Enter team number (or Enter to cancel): {C.RESET}", end="")
    choice = input().strip()
    if choice in TEAMS:
        team, drivers, engine = TEAMS[choice]
        q = (f"Give me a full 2026 season prediction for {team}. "
             f"Drivers: {drivers[0]} and {drivers[1]}, running {engine} power. "
             f"Include: expected championship position, likely points total, key races, "
             f"strengths, weaknesses, and whether they can challenge for titles.")
        print(f"\n  {C.YELLOW}▶ Predicting: {team}{C.RESET}")
        ask_claude(client, conversation, q)

def pick_race_prediction(client, conversation):
    show_calendar_menu()
    print(f"\n  {C.GREY}Enter race code e.g. R1, R8 (or Enter to cancel): {C.RESET}", end="")
    choice = input().strip().upper()
    match = next(((r, n) for r, n in CALENDAR if r == choice), None)
    if match:
        _, name = match
        q = (f"Predict the {name} Grand Prix 2026. Cover: pole position, race winner, "
             f"full podium, key strategic battles, likely safety car scenarios, and "
             f"any potential upsets or dark horse performers.")
        print(f"\n  {C.YELLOW}▶ Predicting: {name} GP{C.RESET}")
        ask_claude(client, conversation, q)

def pick_quick_question(client, conversation):
    show_quick_menu()
    print(f"\n  {C.GREY}Enter question code e.g. Q1 (or Enter to cancel): {C.RESET}", end="")
    choice = input().strip().upper()
    match = next((q for k, q in QUICK_QUESTIONS if k == choice), None)
    if match:
        print(f"\n  {C.YELLOW}▶ {match}{C.RESET}")
        ask_claude(client, conversation, match)


# ─────────────────────────────────────────────
#  MAIN
# ─────────────────────────────────────────────
def main():
    # ── API key ──────────────────────────────
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print(f"\n{C.YELLOW}  No ANTHROPIC_API_KEY environment variable found.{C.RESET}")
        print(f"  {C.GREY}Get your key at: https://console.anthropic.com{C.RESET}")
        print(f"  Enter API key: ", end="")
        api_key = input().strip()
        if not api_key:
            print(f"{C.RED}  No key provided. Exiting.{C.RESET}\n")
            sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)
    conversation = []

    # ── Welcome banner ───────────────────────
    print()
    header("  🏎  F1 2026 SEASON PREDICTOR  ·  Powered by Claude AI")
    print(f"""
  {C.WHITE}The 2026 Formula 1 season marks a new era with completely
  overhauled technical regulations — new power units, active
  aerodynamics, no DRS, two new teams (Audi & Cadillac), and
  a reshuffled pecking order. Ask anything about it.{C.RESET}

  {C.YELLOW}Reigning Champion:{C.RESET} {C.WHITE}Lando Norris (McLaren){C.RESET}
  {C.YELLOW}Season Start:{C.RESET}      {C.WHITE}Australia, March 8 2026{C.RESET}
  {C.YELLOW}Rounds:{C.RESET}            {C.WHITE}24 Grands Prix{C.RESET}
""")

    # ── Main loop ────────────────────────────
    while True:
        show_main_menu()
        print(f"  {C.WHITE}Choice: {C.RESET}", end="")
        cmd = input().strip().upper()

        if cmd == "X":
            print(f"\n  {C.GREY}Lights out. Goodbye. 🏁{C.RESET}\n")
            break

        elif cmd == "N":
            conversation.clear()
            print(f"\n  {C.GREEN}✓ Conversation cleared — fresh start.{C.RESET}")

        elif cmd == "T":
            pick_team_prediction(client, conversation)

        elif cmd == "C":
            pick_race_prediction(client, conversation)

        elif cmd == "Q":
            pick_quick_question(client, conversation)

        elif cmd == "A":
            print(f"\n  {C.CYAN}Ask anything about the 2026 F1 season.{C.RESET}")
            print(f"  {C.GREY}(You can ask follow-up questions — context is remembered.){C.RESET}")
            print(f"  {C.WHITE}▶ {C.RESET}", end="")
            question = input().strip()
            if question:
                ask_claude(client, conversation, question)

        else:
            print(f"  {C.GREY}Unknown command. Try T, C, Q, A, N, or X.{C.RESET}")


if __name__ == "__main__":
    main()
