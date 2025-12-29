"""
ASDF X Post Generator - Configuration
=====================================
All templates, products, hashtags, and settings for post generation.
Easily modifiable to adapt to changing needs.
"""

from dataclasses import dataclass, field
from typing import List, Optional
from enum import Enum
import random

# =============================================================================
# ENUMS
# =============================================================================

class PostType(Enum):
    RAID = "raid"
    THREAD = "thread"
    REPLY = "reply"
    ANNOUNCEMENT = "announcement"
    CULT = "cult"
    FUD_RESPONSE = "fud_response"
    MILESTONE = "milestone"

class DayOfWeek(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

# =============================================================================
# PRODUCTS
# =============================================================================

@dataclass
class Product:
    name: str
    description: str
    url: str
    price: Optional[str] = None
    competitor: Optional[str] = None
    competitor_price: Optional[str] = None
    unique_feature: Optional[str] = None
    tags: List[str] = field(default_factory=list)

PRODUCTS = {
    "holdex": Product(
        name="HolDEX",
        description="DexScreener alternative with $20 listings",
        url="alonisthe.dev/holdex",
        price="$20",
        competitor="DexScreener",
        competitor_price="$300",
        unique_feature="K-Score (holder conviction metric)",
        tags=["#HolDEX", "#DexScreener", "#DEX"]
    ),
    "ignition": Product(
        name="Ignition",
        description="Launchpad where fees go to holders",
        url="alonisthe.dev/ignition",
        price="0.02 SOL",
        competitor="Traditional launchpads",
        competitor_price="Creator keeps fees",
        unique_feature="Fees airdrop to top holders",
        tags=["#Ignition", "#PumpFun", "#Launchpad", "#Airdrop"]
    ),
    "asdforecast": Product(
        name="ASDForecast",
        description="Prediction market for SOL price",
        url="alonisthe.dev/asdforecast",
        price="Fees burned",
        competitor="Polymarket",
        competitor_price="House wins",
        unique_feature="15-minute SOL/USD prediction frames",
        tags=["#ASDForecast", "#PredictionMarket"]
    ),
    "burn_engine": Product(
        name="ASDF Burn Engine",
        description="Auto buyback and burn every 5 minutes",
        url="github.com/zeyxx/asdf-burn-engine",
        unique_feature="Automated on-chain burns",
        tags=["#TokenBurn", "#Deflationary"]
    ),
    "burn_tracker": Product(
        name="ASDF Burn Tracker",
        description="Verify all burns on-chain",
        url="github.com/sollama58/ASDFBurnTracker",
        unique_feature="Transparent burn verification",
        tags=["#TokenBurn", "#Transparency"]
    )
}

# =============================================================================
# HASHTAGS
# =============================================================================

HASHTAGS = {
    "core": ["#ASDFASDFA", "#ASDF", "#Solana", "#SOL"],
    "products": ["#HolDEX", "#Ignition", "#ASDForecast"],
    "topics": {
        "dexscreener": ["#DexScreener", "#DEX"],
        "launchpad": ["#PumpFun", "#Launchpad", "#Airdrop"],
        "prediction": ["#PredictionMarket", "#Polymarket"],
        "memecoin": ["#Memecoin", "#Memecoins", "#MemeSeason"],
        "building": ["#BuildInPublic", "#OpenSource", "#Web3Dev"],
        "burns": ["#TokenBurn", "#Deflationary", "#Tokenomics"],
        "trading": ["#CryptoTwitter", "#CT", "#Alpha"],
        "solana": ["#SolanaSummer", "#SolanaEcosystem"]
    },
    "cashtags": ["$ASDF", "$ASDFASDFA", "$SOL", "$PUMP"]
}

def get_hashtags(post_type: PostType, product: str = None, topic: str = None, count: int = 3) -> str:
    """Generate appropriate hashtags for a post."""
    tags = []

    # Always include 1-2 core tags
    tags.extend(random.sample(HASHTAGS["core"][:2], min(2, len(HASHTAGS["core"][:2]))))

    # Add product tag if specified
    if product and product in PRODUCTS:
        product_tags = PRODUCTS[product].tags
        if product_tags:
            tags.append(random.choice(product_tags))

    # Add topic tag if specified
    if topic and topic in HASHTAGS["topics"]:
        tags.append(random.choice(HASHTAGS["topics"][topic]))

    # Limit to count
    tags = list(dict.fromkeys(tags))[:count]  # Remove duplicates and limit

    return " ".join(tags)

# =============================================================================
# POST TEMPLATES
# =============================================================================

# RAID TEMPLATES
RAID_TEMPLATES = {
    "imagine": {
        "template": """Imagine continuing to pay {competitor} {competitor_price} when a {price} solution exists.
{url}

Imagine being able to reward your own holders with $PUMP airdrops through Ignition.
alonisthe.dev/ignition

Imagine being able to bet on Solana price going up/down in the next 15 minutes.
alonisthe.dev/asdforecast

Few.

{hashtags}""",
        "products": ["holdex"],
        "style": "kovni"
    },

    "what_do_you_think": {
        "template": """what do you think about {problem}???

Let's stop this.
{product_name} lets you {solution}

{url}

{hashtags}""",
        "problems": {
            "holdex": "paying $300 just to add an image and social links",
            "ignition": "creator fees going straight to devs who dump on you",
            "asdforecast": "prediction markets where the house always wins"
        },
        "solutions": {
            "holdex": "do exactly what that DEX offers for just $20",
            "ignition": "airdrop fees to holders instead",
            "asdforecast": "burn every fee instead of extracting"
        },
        "style": "kovni"
    },

    "fuck_x": {
        "template": """fuck {target} and their {complaint}

{product_name} exists. {value_prop}

{url}

{hashtags}""",
        "targets": {
            "holdex": ("dexscreener", "$300 to update jpegs and $1000 to put lightning bolt emojis", "$20. burned."),
            "ignition": ("launchpads that reward dumpers", "creator fees going to devs who dump", "fees go to holders."),
            "asdforecast": ("prediction markets where the house wins", "extracting fees from users", "fees burn.")
        },
        "style": "jean_terre"
    },

    "comparison": {
        "template": """{competitor}: {competitor_price} → their pocket
{product_lower}: {price} → burned

same service. opposite model.

{url}

{hashtags}""",
        "style": "direct"
    },

    "provocation": {
        "template": """{competitor} made millions {action}.
we made {product_lower}.
{price}. burned.

cope.

{url}

{hashtags}""",
        "actions": {
            "holdex": "moving jpegs",
            "ignition": "from creator fees",
            "asdforecast": "from prediction fees"
        },
        "style": "provocative"
    }
}

# THREAD TEMPLATES
THREAD_TEMPLATES = {
    "holdex": [
        "dexscreener made $50M+ charging $300 to update token pages.\n\nwe built the alternative.\n\nhere's why HolDEX changes everything 🧵\n\n{hashtags}",
        "the problem:\n\n→ $300 to add an image\n→ $300 to add social links\n→ $1000+ for \"boost\" features\n→ all money goes to... dexscreener\n\nextractive infra became the norm.\nnobody questioned it.",
        "think about it:\n\nyou launch a token.\nyou build a community.\nyou want to update your page.\n\ndexscreener: \"that'll be $300\"\n\nfor moving jpegs.\nin 2024.",
        "so we built HolDEX.\n\nsame features.\n$20.\nfees burned, not extracted.\n\nalonisthe.dev/holdex",
        "what you get:\n\n→ token page updates for $20\n→ K-Score (holder conviction metric)\n→ automatic holder count tracking\n→ real-time price data\n→ fully functional API\n→ mobile-friendly UI\n\nopen source. verifiable.",
        "the K-Score is unique to HolDEX.\n\nit measures actual holder conviction.\nnot volume (can be faked).\nnot market cap (can be manipulated).\n\nreal holders. real conviction.",
        "where do the fees go?\n\n100% burned.\n\nnot to a team wallet.\nnot to \"development.\"\nburned. on-chain. verifiable.\n\nevery update = less $ASDF supply.",
        "the math:\n\ndexscreener: $300 → their pocket\nholdex: $20 → burned\n\nsame service.\n$280 difference.\nopposite model.",
        "fully open source.\n\ndon't trust us?\nread the code.\n\ngithub.com/sollama58/HolDex",
        "extractive infra had its run.\n\ntime for alternatives.\n\n→ check HolDEX: alonisthe.dev/holdex\n→ update your token for $20\n→ see your K-Score\n\nlet's flip dexscreener.\n\nthis is fine 🔥\n\n{hashtags}"
    ],

    "ignition": [
        "launchpads have a problem:\n\ncreator fees go to creators.\ncreators dump.\nyou hold the bag.\n\nwe fixed it.\n\nhere's Ignition 🧵\n\n{hashtags}",
        "the current launchpad model:\n\n1. creator launches token\n2. creator earns fees from volume\n3. creator accumulates bag\n4. creator dumps on holders\n5. holders lose\n6. creator moves to next token\n\nrepeat infinitely.",
        "the incentives are broken.\n\ncreators are rewarded for dumping.\nholders are rewarded for... holding bags.\n\nwhy would anyone hold long-term?",
        "Ignition flips the model.\n\ncreator fees → airdropped to top holders.\ndev allocation → auto-distributed to holders.\n\nyou hold, you earn.\nsimple.",
        "how it works:\n\n1. launch on pump.fun via Ignition (0.02 SOL)\n2. trading generates fees\n3. fees buy $PUMP\n4. $PUMP airdrops to top holders\n5. dev bags auto-distributed\n\nno dumping middlemen.",
        "now the incentives align:\n\ncreators want volume → holders get airdrops\nholders want to hold → they earn more\neveryone wins except dumpers\n\nimagine that.",
        "the dev allocation problem:\n\nmost launches: dev holds bag → dev dumps\n\nIgnition: dev holdings auto-airdropped.\n\ncan't dump what you don't hold.\nproblem solved.",
        "traditional launchpad:\n→ creator earns\n→ creator dumps\n→ you lose\n\nIgnition:\n→ you hold\n→ you earn\n→ creator can't dump\n\nwhich model makes more sense?",
        "Ignition is live.\n\nmultiple launches.\nairdrops distributed.\nworking as intended.\n\nalonisthe.dev/ignition",
        "tired of holding bags while creators dump?\n\ntry Ignition.\n\n→ launch: alonisthe.dev/ignition\n→ hold tokens, earn airdrops\n→ aligned incentives\n\nlaunchpads should reward holders, not dumpers.\n\nthis is fine 🔥\n\n{hashtags}"
    ],

    "asdforecast": [
        "prediction markets made billions.\n\npolymarket. drift. etc.\n\nwhere did the fees go?\n\nnot to you.\n\nhere's ASDForecast 🧵\n\n{hashtags}",
        "prediction market economics:\n\n→ you bet\n→ you win or lose\n→ platform takes fees\n→ fees go to... platform\n\nthe house always wins.\neven when you win.",
        "polymarket did $1B+ in volume.\n\nfees extracted: massive.\nfees shared with users: 0.\n\nyou're the product and the profit source.",
        "ASDForecast is different.\n\n→ bet on SOL price (15-min frames)\n→ platform takes fees\n→ fees burn $asdf\n\nthe house doesn't win.\nthe house burns.",
        "how it works:\n\n1. pick a 15-minute frame\n2. bet on SOL going up or down\n3. win = collect pot\n4. fees = burned\n\nno extraction.\npure prediction market.",
        "features:\n\n→ 15-minute SOL/USD frames\n→ real-time price tracking\n→ active wallet monitoring\n→ volume tracking in SOL\n→ live countdowns\n→ mobile friendly\n\nalonisthe.dev/asdforecast",
        "why burn fees instead of extract?\n\nextraction = platform gets rich, users stay same\nburning = supply decreases, holders benefit\n\nwe chose holders.",
        "perfect for degens:\n\n→ 15-minute frames = fast action\n→ SOL price = you already watch it\n→ fees burn = you're not enriching VCs\n\ndegen responsibly.",
        "fully transparent.\n\n→ bets on-chain\n→ burns verifiable\n→ no hidden fees\n\ndon't trust? verify.",
        "prediction markets don't need to extract.\n\nASDForecast proves it.\n\n→ try it: alonisthe.dev/asdforecast\n→ bet on SOL\n→ fees burn\n\nthe house doesn't win anymore.\n\nthis is fine 🔥\n\n{hashtags}"
    ],

    "ecosystem": [
        "no VC funding.\nno roadmap promises.\nno extraction.\n\njust 5 products shipped in months.\n\nhere's how a memecoin cult is replacing extractive infra 🧵\n\n{hashtags}",
        "crypto was supposed to remove middlemen.\n\ninstead we built new ones:\n→ dexscreener ($300 for page updates)\n→ launchpads (creators dump on holders)\n→ prediction markets (house always wins)\n\nextractors everywhere.",
        "$ASDFASDFA started as a memecoin.\n\nthen something happened:\n\ninstead of waiting for pumps, we started building.\n\nreplacements for every extractive tool in the trenches.",
        "product 1: HolDEX\n\ndexscreener alternative.\n$20 instead of $300.\nfees burned.\nK-Score for holder conviction.\n\nlive: alonisthe.dev/holdex",
        "product 2: Ignition\n\nlaunchpad where fees go to holders.\ndev bags auto-distributed.\nno more dumping creators.\n\nlive: alonisthe.dev/ignition",
        "product 3: ASDForecast\n\nprediction market for SOL price.\n15-minute frames.\nall fees burned.\n\nlive: alonisthe.dev/asdforecast",
        "product 4 & 5: burn infrastructure\n\n→ ASDF Burn Engine (auto buyback every 5 min)\n→ ASDF Burn Tracker (verify all burns)\n\nopen source:\ngithub.com/zeyxx/asdf-burn-engine\ngithub.com/sollama58/ASDFBurnTracker",
        "the model:\n\nevery product generates fees.\nevery fee burns $asdf.\nsupply decreases.\nholders benefit.\n\nno VC exits.\nno team dumps.\njust burn.",
        "why we build:\n\nextractive infra is a tax on the trenches.\nevery $300 listing is money leaving the ecosystem.\nevery creator dump is trust destroyed.\n\nwe're building the alternative.\none product at a time.",
        "the numbers:\n\n→ 5 products live\n→ 0 VC funding\n→ 7%+ supply burned\n→ 100% open source\n→ 4 devs building\n\nall from a \"memecoin.\"",
        "in a world where everyone PvPs on serial dev tokens, our cult builds.\n\n→ HolDEX: alonisthe.dev/holdex\n→ Ignition: alonisthe.dev/ignition\n→ ASDForecast: alonisthe.dev/asdforecast\n\njoin the cult. 💊\n\nthis is fine 🔥\n\n{hashtags}"
    ],

    "builder_story": [
        "4 devs.\n0 funding.\n5 months.\n5 products.\n\nhere's the story of building in the trenches without asking permission 🧵\n\n{hashtags}",
        "it started with a question:\n\nwhy do we accept paying $300 for a page update?\n\nno good answer.\n\nso we built HolDEX.",
        "HolDEX launched.\n\n$20 listings. fees burned. open source.\n\npeople said \"who cares?\"\nwe kept building.",
        "then we looked at launchpads.\n\ncreators earn fees. creators dump. holders lose.\n\nbroken incentives.\n\nso we built Ignition.\nfees to holders. problem solved.",
        "then prediction markets.\n\npolymarket proved demand.\nbut fees go to VCs.\n\nso we built ASDForecast.\nfees burn instead.",
        "the pattern:\n\n1. identify extraction\n2. build alternative\n3. burn fees instead of extract\n4. open source everything\n5. repeat\n\nsimple.",
        "we never raised.\n\nno VC calls.\nno token unlocks.\nno investors to satisfy.\n\njust building what the trenches need.",
        "$ASDFASDFA holders aren't waiting for pumps.\n\nthey're testing products.\nreporting bugs.\nspreading the word.\n\na cult that builds > a community that waits.",
        "what's next?\n\nmore extraction to replace.\nmore products to ship.\nmore fees to burn.\n\nwe don't do roadmaps.\nwe do shipping.",
        "the trenches deserve better infra.\n\nwe're building it.\n\n→ alonisthe.dev\n\nthis is fine 🔥\n\n{hashtags}"
    ]
}

# CULT/PHILOSOPHY TEMPLATES
CULT_TEMPLATES = [
    """$ASDFASDFA is a cult like none other.

It's no lie the chart looks choppy.
But we are not a chart. We are a cult.

Cults build. Cults hold.
Products ship regardless of price.

This is Fine 🔥

{hashtags}""",

    """Extractors made millions this cycle.
Dexscreener. Launchpads. Prediction markets.

We're building the alternatives.
Open source. Fees burned. No extraction.

The cult builds. The cult holds.
This is Fine 🔥

{hashtags}""",

    """crypto was supposed to remove middlemen.
then we built new ones.

dexscreener. launchpads. prediction platforms.
all extract.

we're building the alternatives.
open source. fees burned. no extraction.

alonisthe.dev

{hashtags}""",

    """everyone asks "when pump?"
nobody asks "what are we building?"

HolDEX replaces $300 listings with $20.
Ignition rewards holders, not dumpers.
ASDForecast burns fees instead of extracting.

We're not waiting for a pump. We're building the infra.

This is Fine 🔥

{hashtags}""",

    """In a world where everyone PvP on tokens created by serial developers, our cult innovates and builds to make things happen.

holdex. ignition. asdforecast.

See you in six months.

{hashtags}""",

    """no funding is a feature.
no one to satisfy but users.

{hashtags}"""
]

# FUD RESPONSE TEMPLATES
FUD_RESPONSES = {
    "scam": [
        """→ 5 products live
→ all open source
→ fees burned on-chain
→ verifiable anytime

but sure, "scam"

github.com/sollama58""",
        """scams extract.
we burn.

check the burn tracker yourself.""",
        """our code is open source.
our burns are on-chain.
our products are live.

what else do you need anon?"""
    ],

    "dead_chart": [
        """charts pump and dump.
products stay.

holdex. ignition. asdforecast.
still live. still building.""",
        """we're not here for the chart.
we're here to replace extractive infra.

the chart will follow the build.""",
        """you trade charts.
we build infra.

see you at the top.""",
        """It's no lie the chart looks choppy.
But we are not a chart. We are a cult.

Cults build. Cults hold.
Products ship regardless of price.

This is Fine 🔥"""
    ],

    "no_users": [
        """everyone tired of paying $300 for a page update.

you'll use it too. eventually.

alonisthe.dev/holdex""",
        """not yet mass adopted.
but neither was dexscreener at first.

difference: we don't extract $300.""",
        """early.

remind me in 6 months."""
    ],

    "how_money": [
        """we don't. fees burn.

that's the point.""",
        """"but how do you make money"

we hold $asdf.
every fee burns $asdf.
supply goes down.

you do the math.""",
        """we're not here to make money.
we're here to make extractors irrelevant."""
    ],

    "just_memecoin": [
        """"just a memecoin" with:
→ live dex alternative
→ live launchpad
→ live prediction market
→ open source everything

what does your "real project" have?""",
        """memecoin with more shipped products than most VC-backed projects.

but go off.""",
        """memecoins with no utility → gambling
memecoins with utility → asdf

we're not the same."""
    ],

    "why_not_dexscreener": [
        """$300 vs $20.
extraction vs burn.
closed vs open source.

any other questions?

alonisthe.dev/holdex""",
        """same features.
$280 cheaper.
fees burned instead of extracted.

why wouldn't you?"""
    ],

    "copy": [
        """yes. we copied the function.
no. we didn't copy the extraction.

$20 burned > $300 extracted.""",
        """open source alternatives aren't "copies."
they're improvements.

linux copied unix. firefox copied netscape.
holdex improves on dexscreener."""
    ],

    "universal": [
        """cool fud.

anyway, have you seen holdex? $20 vs dexscreener's $300.

alonisthe.dev/holdex""",
        """noted.

meanwhile we shipped holdex, ignition, asdforecast.
what did you ship?""",
        """you're fudding.
we're shipping.

we are not the same.""",
        """interesting take.

we're too busy building to argue.

alonisthe.dev"""
    ],

    "nuclear": [
        """5 products.
0 VC.
0 dumps.
100% open source.
all fees burned.

fud harder.""",
        """you'll use our infra eventually.
you just don't know it yet.

alonisthe.dev""",
        """the trenches need better infra.
we're building it.
you're welcome in advance."""
    ]
}

# REPLY/ENGAGEMENT TEMPLATES
REPLY_TEMPLATES = {
    "discovery_holdex": """Yooo, have you seen HolDEX?

No more paying $300 for Dexscreener. Now it's like $20 for updates, and you can even see the K-Score, which represents holder conviction, directly on HolDEX.

alonisthe.dev/holdex""",

    "discovery_ignition": """Have you tried Ignition yet?

Launch on Pump.fun, but fees go to your holders instead of you dumping on them. Aligned incentives.

alonisthe.dev/ignition""",

    "ecosystem": """The ASDF ecosystem, a cult created to build and to reward holders.

→ Ignition: alonisthe.dev/ignition
→ HolDEX: alonisthe.dev/holdex
→ ASDForecast: alonisthe.dev/asdforecast

Our system is built on belief, and in our own way, we're trying to move things forward and change the game.

Join us. 💊""",

    "challenge_holdex": """try holdex.
if you still prefer paying $300 after, I'll shut up.

alonisthe.dev/holdex""",

    "challenge_ignition": """use ignition once.
watch your holders get airdrops.
then tell me launchpads shouldn't change.

alonisthe.dev/ignition""",

    "high_fees": """this is why we built holdex.

$20 instead of $300.
fees burned, not extracted.

alonisthe.dev/holdex""",

    "launchpad_dump": """exactly why ignition exists.

fees go to holders, not creators.
can't dump what you don't hold.

alonisthe.dev/ignition""",

    "solana_projects": """check out the ASDF ecosystem:

→ HolDEX: dexscreener alternative, $20
→ Ignition: launchpad that rewards holders
→ ASDForecast: prediction market, fees burn

all live. all open source.

alonisthe.dev""",

    "building": """respect the build.

we shipped 5 products with 0 funding.
holdex. ignition. asdforecast. burn engine. validator.

all open source.

alonisthe.dev"""
}

# ANNOUNCEMENT TEMPLATES
ANNOUNCEMENT_TEMPLATES = {
    "product_launch": """{product_name} is now live 🔥

{description}

👉 {feature_1}
👉 {feature_2}
👉 {feature_3}
👉 {feature_4}

Check it out: {url}

{hashtags}""",

    "update": """Major upgrades to {product_name} 🔥

👉 {update_1}
👉 {update_2}
👉 {update_3}
👉 {update_4}

{url}

{hashtags}""",

    "milestone": """week {week_num} stats:

→ holdex: {holdex_stat}
→ ignition: {ignition_stat}
→ asdforecast: {forecast_stat}
→ burns: {burn_stat}

no VC. no hype. just shipping.

alonisthe.dev

this is fine 🔥

{hashtags}"""
}

# VIRAL/MEME TEMPLATES
VIRAL_TEMPLATES = [
    """them: fud
us: ship

them: $300
us: $20

them: extract
us: burn

we are not the same.

alonisthe.dev

{hashtags}""",

    """fud: free
building: mass time
products shipped: 5
fucks given: 0

alonisthe.dev

{hashtags}""",

    """you: typing fud
us: shipping products

see you at the top anon.

this is fine 🔥

{hashtags}"""
]

# =============================================================================
# WEEKLY SCHEDULE
# =============================================================================

WEEKLY_SCHEDULE = {
    DayOfWeek.MONDAY: {
        "theme": "Education",
        "posts": [
            {"time": "16:00", "type": PostType.THREAD, "template": "holdex"},
            {"time": "21:00", "type": PostType.RAID, "template": "what_do_you_think", "product": "holdex"}
        ]
    },
    DayOfWeek.TUESDAY: {
        "theme": "Raid Day",
        "posts": [
            {"time": "10:00", "type": PostType.RAID, "template": "imagine", "product": "holdex"},
            {"time": "16:00", "type": PostType.RAID, "template": "comparison", "product": "holdex"},
            {"time": "20:00", "type": PostType.RAID, "template": "what_do_you_think", "product": "ignition"}
        ]
    },
    DayOfWeek.WEDNESDAY: {
        "theme": "Engagement",
        "posts": [
            {"time": "17:00", "type": PostType.RAID, "template": "fuck_x", "product": "holdex"}
        ]
    },
    DayOfWeek.THURSDAY: {
        "theme": "Narrative",
        "posts": [
            {"time": "16:00", "type": PostType.THREAD, "template": "ecosystem"},
            {"time": "22:00", "type": PostType.CULT, "template": None}
        ]
    },
    DayOfWeek.FRIDAY: {
        "theme": "Degen",
        "posts": [
            {"time": "17:00", "type": PostType.RAID, "template": "fuck_x", "product": "ignition"},
            {"time": "20:00", "type": PostType.RAID, "template": "viral"},
            {"time": "23:00", "type": PostType.RAID, "template": "what_do_you_think", "product": "asdforecast"}
        ]
    },
    DayOfWeek.SATURDAY: {
        "theme": "Social Proof",
        "posts": [
            {"time": "18:00", "type": PostType.MILESTONE, "template": "milestone"},
            {"time": "20:00", "type": PostType.CULT, "template": None}
        ]
    },
    DayOfWeek.SUNDAY: {
        "theme": "Cult",
        "posts": [
            {"time": "15:00", "type": PostType.CULT, "template": None},
            {"time": "18:00", "type": PostType.CULT, "template": None}
        ]
    }
}

# =============================================================================
# STATS (Update these for milestone posts)
# =============================================================================

CURRENT_STATS = {
    "products_live": 5,
    "vc_funding": 0,
    "supply_burned_percent": "7%+",
    "devs": 4,
    "holdex_listings": "processing listings",
    "ignition_airdrops": "airdrops distributed",
    "forecast_status": "predictions running",
    "burn_status": "continuing every 5 min"
}
