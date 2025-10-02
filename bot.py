import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
    MessageHandler,
    filters
)

# --- MENU CONTENTS ---
menus = {
    "step1": """📘 STEP 1 — WHAT IS PLAYOPS?
Welcome to PlayOps.
We know some of you are just joining — and ARG might be a new term.

🔹 What is an ARG?
A typical ARG (Alternate Reality Game) is an interactive, story-driven experience that uses the real world as its platform.
Instead of living only inside a video game or movie, an ARG unfolds across websites, videos, social media, and even real-world actions.

🔹 But PlayOps isn’t typical
PlayOps is also a documentary.
That means every mission, every fragment, every Twin unlocked becomes part of the record.
Proof, not résumé.
Right now, in Preseason, we are exposing the Feed (broken systems shaping our generation).
At the end of the year, the PlayOps Simulator launches.
That’s when the community shifts from mapping the problem → to building the Grid together, proving solutions through skill, collaboration, and brand partnerships.
Weekly episodes will continue — but now as a living archive of Gen Z building what’s next.

🔹 The Three Layers of PlayOps
The Community ARG (what you’re in now)
 – Daily missions inside Telegram
 – Everything you post is real, not roleplay
 – Your actions become part of the Documentary Lore
The Simulation Game (launching Winter 2025)
 – A structured game world built on the proof we’re collecting now
 – Players who rise on the leaderboard here will unlock access to the next stage
The Cinematic Layer (AI Twin)
 – Your real actions power a digital version of you
 – That twin appears in short films, trailers, and on Roku
 – Film + game blur together: the documentary is the lore, the lore is the documentary

🔹 Think of it like this
Every great game has lore.
Every great film has a story.
In PlayOps, they are the same thing.
“We’re building the story world of the game in real life.
The missions you complete today are both real actions and the lore of the game tomorrow.”

🔹 Your Mission Right Now
⚡ Help rebuild the Grid for Gen Z — a real movement — inside a gamified environment.
""",
    "step2": """🗣 STEP 2 — COMMUNITY ENTRY
Why this step matters
This is how you show up as a real person, not a username.

Connecting LinkedIn lets the system auto-build your proof trail in #Social Log (so teammates can find & boost you).

We don’t care about follower count — we care about proof.

1) Post your intro in #General
Copy + paste this template and fill it in:
Name / Handle:
Location / Time zone:
Role(s) I’m drawn to: [Decoder, Lorekeeper, Feed Watcher, Signal Booster, UX/UI Architect, Interface Architect, System Builder]
One cultural signal I’ve noticed lately:
(1–2 sentences on why I joined PlayOps):

Examples of a good “cultural signal”:
“Friends use AI to draft everything at school; grades feel less meaningful than projects.”
“Job posts ask for ‘entry-level’ but want 3–5 yrs experience. Feels like a broken filter.”
“People trust creators more than ads; comments > billboards.”

Tip: keep it honest and specific — your signal may become a discovery we feature.

2) Connect LinkedIn in the Terminal App
Open @PlayOpsARGTerminalBot → Settings → Socials → Add LinkedIn (required).

Optional: add 1–2 more platforms you’ll actually use for missions.

After linking, your handle will auto-appear in #Social Log (give it a minute).

Troubleshooting
Not showing in #Social Log after a few minutes?

Reopen the app and double-check Socials.

If still missing → Ask AI Bot @TapSphere_SupportBot on the support topic or open a ticket @TapSphere_SupportBot by privately messaging /start.

Privacy note
Share only what you’re comfortable with in your intro.

LinkedIn is required because it’s the most verifiable proof channel for our mission.
""",
    "step3": """🗺 STEP 3 — GROUP MAP (HOW PLAYOPS IS ORGANIZED)
Why this step matters
Telegram can feel messy if you’re new. We split the group into topics (like threads) so you know exactly where to go.
Each topic has a purpose — use the right one, and nothing gets lost.

🔹 Topics You’ll Use
📢 Announcements - Official mission drops, lore fragments, gear, trailers. Read-only. Keep notifications ON.
🗣 General - Intros, casual chat, quick questions. First stop for newcomers.
🎯 Roles (7 topics) - Each role has its own topic — post your proofs there.
🔑 Decoder
📚 Lorekeeper
🕵️ Feed Watcher
📣 Signal Booster
🎨 UX/UI Architect (includes UX/UI Designer)
🧩 Interface Architect (includes Front-End Developer)
🛠 System Builder (includes Back-End Developer)
🧩 Characters - Reflections + AI Twin applications. This is where members’ stories feed into the cinematic layer.
📱 Social Log - Auto-sync of everyone’s connected LinkedIn/other handles. Use it to boost each other’s posts.
🛠 Support - You’re here now. Onboarding menu, FAQ bot, ticket system. Always come here first if stuck.

🔑 Rules to Remember
Post proofs only in the correct Role topic.
Don’t post missions in General or Announcements.
If the app/bot “routes” you to a topic → you’re in the right place.
If in doubt: ask in Support, not General.
""",
    "step4": """📘 STEP 4 — ROLES & HOW THEY WORK
Why this step matters
Roles are how we divide the work of rebuilding the Grid. They give structure so every action counts, and every player has a lane. You can stick with one role or rotate — either way, your proofs power the community documentary and future game.

🔹 The 7 Core Roles (with skill tracks)
🔑 Decoder - Solve puzzles, uncover hidden patterns, lead clue hunts. Good for critical thinkers, code-breakers, puzzle lovers.
📚 Lorekeeper - Summarize missions, write transcripts, keep timelines. Good for writers, organizers, archivists.
🕵️ Feed Watcher - Spot real-world “glitches” in culture, media, or news that connect to the ARG. Good for researchers, current-events trackers, culture nerds.
📣 Signal Booster - Amplify missions on LinkedIn (+1 other platform when required). Share memes, reels, reflections. Good for social-savvy players, creatives, connectors.
🎨 UX/UI Architect - Imagine how the Grid should look/feel. Create mockups, flows, visuals, and experience designs. Good for designers, product minds, Figma lovers.
🧩 Interface Architect - Prototype creative systems, dashboards, or interfaces that expand the ARG. Good for front-end coders, web/game hackers, systems thinkers.
🛠 System Builder - Test mechanics, stabilize the simulation, connect dots behind the scenes. Good for engineers, database thinkers, troubleshooters.

🔑 How Roles Work in Practice
Each role has its own topic in Telegram. Post proofs there — not in General.
You can switch roles anytime.
Minimum = 1 proof per day (mission + LinkedIn if required).
Some missions encourage cross-role collab → that’s how we unlock bigger discoveries.
""",
    "step5": """🕹 STEP 5 — MISSIONS & APP BASICS
Why this step matters
Missions are the heartbeat of PlayOps. They drop daily in the app — your proofs fuel the community story, the documentary, and the future game.

🔹 1) Starting a Mission
Open the Terminal App → Mission Page.
Select your mission.
You’ll be redirected to the PlayOps Telegram Bot mission post.
Always reply in that mission post — not in General or Announcements.
Open the app every day to refresh your timer.

🔹 2) Timer Logic (Survival Time)
Everyone starts with 23h daily survival time.
Completing a task correctly = +1 extra hour added to your clock.
Time carries over:
Example: End Day 1 with +2h → start Day 2 with 25h.
If your timer hits 0 → it’s game over (you’re out of the Grid).

🔹 3) XP Rules (Proof Formats)
XP depends on the format of your proof:
📝 Text only → +1 XP
🖼 Image only → +2 XP
📝🖼 Text + Image → +3 XP
🎥 Video only → +3 XP
📝🎥 Text + Video → +4 XP
⏱ Late response → Half XP + half time

🔹 4) Common Mistakes to Avoid
❌ Reading but not replying = no XP/time earned.
❌ Replying in the wrong format = looks “completed,” but no credit.
✅ Always double-check that your reply matches the required format.

🔹 Quick Recap
Missions = daily proof.
Timer = lifeline.
XP = progress.
Proof format matters.
Open the app every day.
""",
    "step6": """📰 STEP 6 — FEED FILES / DISCOVERY
Why this step matters
The Feed Files are our daily archive of Documentary Lore — a hybrid of story + real record.
They’re posted daily on LinkedIn, and each one captures a discovery made by members.

🔹 What is Lore?
Every great game has a story world — the lore.
It’s the backstory, the hidden code, the fragments that explain why the game exists and how it unfolds.
In PlayOps, the lore isn’t fiction. It’s documentary lore — built from real actions, cultural signals, and the truths you uncover.
So when you read a Feed File, you’re not just reading story — you’re reading our real record of Gen Z exposing the Feed and building the Grid.

🔹 What is a Discovery?
A discovery is when someone in the community notices a pattern or truth in the world that reveals how the Feed (broken system) works or how the Grid (our proof system) should be built.
Examples:
Fake followers don’t equal trust → proof matters more than hype.
Job posts ask for “entry-level” but want 3–5 years of experience → broken filter.
Everyone trusts comments more than ads → signals come from people, not billboards.
Each day, one member’s discovery is featured in the Feed File.

🔹 Ongoing Program (12 Weeks)
The PlayOps Preseason is a 12-week cycle, but it runs continuously — new people start every week.
There’s no “behind” or “midway.” Whenever you join, you’re stepping into the ongoing flow of Documentary Lore.
Your starting point is simply the day you arrive. From there, you catch up on Feed Files to see what’s already been uncovered, then continue adding your own discoveries.
Think of it like an open series: the story doesn’t reset, it keeps unfolding. When you join, you enter the arc-in-progress and start leaving your mark on it.

🔹 Your Task
Go to the PlayOps LinkedIn Page → https://www.linkedin.com/company/tapsphere
Start from Feed File – Entry 1.
Read + comment on each entry until today’s post.
Comments = proof you’ve read and understood.
We award XP on the backend for this catch-up.
Once caught up, continue daily: read + comment on the new Feed File.

🔹 Why This Matters
Feed Files = Documentary Lore → the story + record of this generation’s proof.
Your comments = proof you’re part of the mission.
The discoveries you contribute may become part of the film + future Simulation game lore.
""",
    "step7": """🎬 STEP 7 — AI TWIN / CINEMATIC LAYER (OPTIONAL)
Why this step matters
Every great game has characters.
In PlayOps, you are the character — not an avatar, not a script.
The new wave of gaming is the blur between game and film.
Think Squid Game on Netflix — except here, it’s not fiction.
PlayOps lives in that blur: what happens in the ARG becomes part of the documentary lore, and your AI Twin carries it into the cinematic story we release on Roku.

🔹 How It Works
Think of PlayOps like a film set — except the script isn’t written ahead of time. It’s written by what you say and do every day.
Application (Audition Stage)
Submit the AI Twin form.
You need 42 XP to qualify (qualifying = eligible, not yet accepted).

Acceptance (Cast Member)
If accepted, you receive:
- An AI Twin built from your likeness (≈85–90% accuracy).
- A short intro video in the PlayOps Characters series.
This is like being added to the cast list of the PlayOps saga.

Episodes (Landing a Role)
Not every cast member is in every scene.
Which voices/twins appear depends on the missions you complete and the truths you share.

How Your Voice Becomes Story
With a twin → your twin performs your chosen words.
Without a twin (yet) → your words appear as holograms, voiced by another twin.

🔹 Why It Matters
Application = audition
Acceptance = cast member
Missions = your daily lines
Episodes = the film we create together
Your actions are both proof and story — part of the Documentary Lore that blurs into the PlayOps cinematic experience on Roku.

Apply here: https://docs.google.com/forms/d/e/1FAIpQLSdHF8163dD2lyvHGYXdRvwcV-A9dAZoK8sXxKuctoiQGC7stQ/viewform?usp=dialog
See more / discuss: Check the #Characters topic.
""",
    "step8": """🛠 STEP 8 — SUPPORT & HELP
Why this step matters
Support is your safety net. Whenever you’re confused, this is where you go — not General chat.

🔹 Inside the Support Topic, you’ll find 2 Menus:
Onboarding Menu (you’re in it now) - Guides you step by step through the PlayOps setup.
Important Links Menu (always available)
- 📲 Terminal App
- 📰 AI Twin Application
- 🤝 Referral Link
- 🎬 Preseason Trailer / Roku link
- 📱 PlayOps LinkedIn & YouTube
- 🛠 Support Ticket
- 🤖 AI Bot

🔹 Getting Help
AI Bot 🤖 - Ask the bot in Support for quick answers to FAQs, rules, or troubleshooting.
Ticket System 🛠 - If the bot can’t solve your issue, open a ticket in Support. A moderator will respond.
Onboarding Buddy 👥 - Each new member is paired with a community buddy who will guide you through your first mission.
Admins (if needed)
- Lian — @lian_pham
- Neha (App/Tech) — @Nehapatil03
- Migleisy (Onboarding) — @M_Mighty1
- Hamza (Stickers) — @okhamzi

Bottom line: If you ever feel stuck → Support is the only place you need to go.
""",
    "step9": """✅ STEP 9 — FINISH / NEXT STEPS
Why this step matters
You’ve completed onboarding — you’re ready to play.
Now lock in a few final steps so you never miss a mission.

🔹 What to Do Now
📢 Turn ON Notifications in Announcements
📱 Follow PlayOps on LinkedIn → https://www.linkedin.com/company/tapsphere
▶️ Subscribe to PlayOps YouTube → https://www.youtube.com/@PlayOpsTV
🤝 Connect with Lian Pham on LinkedIn → https://www.linkedin.com/in/lian-pham/

🔹 Program Start
The Program runs in 12-week cycles, but it’s ongoing.
New members start every week.
Your personal Day 1 = today — and the missions begin from here.

🔹 What to Expect
Daily mission drops → App + Role Topic
Role proofs → post in your role topic.
LinkedIn → comment daily on the Feed File to stay in the flow of the Documentary Lore.
XP + Timer → your lifeline inside the Grid.

Welcome to the Grid.
You
...
""",
    "step10": """ 📍 STEP 10 — 🧩 TRY A TEST MISSION
              ✅ Why this step matters:\nBefore your first live mission, you’ll do a practice run.
              This shows you exactly how the app → bot → proof flow works.
              🔹 How to Do It:
              1. Open the Terminal App → select the Signal Booster task (the easiest starting role).
              2. Or, if you want a challenge, choose a harder role or even a late task from previous days.
              3. Post your proof in the correct role topic (e.g. #Signal Booster).
              4. Check that your timer + XP updated correctly ✅
""",
    "menu2": """🗂 MENU 2 — IMPORTANT LINKS
Once you’re onboarded, you don’t need to repeat the tutorial. But you will need quick access to core links that keep the Grid running.

📲 Terminal App: @PlayOpsARGTerminalBot
📰 AI Twin Application: https://docs.google.com/forms/d/e/1FAIpQLSdHF8163dD2lyvHGYXdRvwcV-A9dAZoK8sXxKuctoiQGC7stQ/viewform?usp=dialog
🤝 Referral Link: @TapSphereRefBot
🎬 Preseason Trailer: https://youtu.be/TC1wLyibwWs
📱 PlayOps LinkedIn Page: https://www.linkedin.com/company/tapsphere
▶️ PlayOps YouTube: https://www.youtube.com/@PlayOpsTV
🛠 Support Ticket System: @TapSphere_SupportBot
🤖 Ask the AI Bot: @TapSphere_SupportBot - mention the bot and ask queries in support topic
"""
}

# --- GENERATE INLINE KEYBOARD ---
def get_keyboard(current_step):
    step_keys = ["step1","step2","step3","step4","step5","step6","step7","step8","step9","step10","menu2"]
    if current_step in step_keys:
        idx = step_keys.index(current_step)
    else:
        idx = -1

    buttons = []
    # Back button
    if idx > 0:
        buttons.append(InlineKeyboardButton("⬅️ Back", callback_data=step_keys[idx-1]))
    # Next button
    if 0 <= idx < len(step_keys)-2:
        buttons.append(InlineKeyboardButton("➡️ Next", callback_data=step_keys[idx+1]))
    # Menu 2 button
    buttons.append(InlineKeyboardButton("🗂 Menu 2", callback_data="menu2"))
    return InlineKeyboardMarkup([buttons])

# --- START COMMAND ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = get_keyboard("step1")
    await update.message.reply_text(menus["step1"], reply_markup=keyboard, disable_web_page_preview=True)

# --- BUTTON CALLBACK ---
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data in menus:
        keyboard = get_keyboard(data)
        await query.message.reply_text(menus[data], reply_markup=keyboard, disable_web_page_preview=True)

# --- WELCOME MESSAGE WITH START BUTTON ---
async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    start_keyboard = ReplyKeyboardMarkup([["▶️ Start"]], resize_keyboard=True)
    await update.message.reply_text(
        "👋 Welcome! This is the **PlayOps Onboarding Bot**.\n\n"
        "It will guide you step by step through onboarding.\n"
        "Press ▶️ Start to begin 🚀",
        reply_markup=start_keyboard
    )

# --- HANDLE START BUTTON TAP ---
async def start_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await start(update, context)

# --- MAIN ---
if __name__ == "__main__":
    BOT_TOKEN = "8096484247:AAGKSCHyr1MqGe55UBSwYWIv2PQQ7xZUY6Q"  # <-- Replace with your bot token
    logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Handlers
    app.add_handler(CommandHandler("start", welcome))  # /start shows intro with Start button
    app.add_handler(MessageHandler(filters.Regex("^▶️ Start$"), start_button))  # Handle Start button
    app.add_handler(CallbackQueryHandler(button_handler))

    print("🤖 Bot is running...")
    app.run_polling()