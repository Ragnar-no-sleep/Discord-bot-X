# 🤖 ASDF X Post Generator - User Guide

Bot Discord pour générer des posts X (Twitter) pour l'écosystème ASDF.

---

## 📋 Commandes Rapides

| Commande | Description |
|----------|-------------|
| `/week` | Générer tous les posts d'une semaine |
| `/raid` | Générer un post raid |
| `/thread` | Générer un thread complet |
| `/cult` | Générer un post cult/philosophie |
| `/fud` | Générer une réponse anti-FUD |
| `/reply` | Générer une reply d'engagement |

---

## 📅 Générer une Semaine Complète

```
/week [numéro]
```

**Exemple:** `/week 1` → Génère tous les posts de la semaine 1

**Contenu généré:**
- Lundi: Thread HolDEX + 1 raid
- Mardi: 3 raids (matin/après-midi/soir)
- Mercredi: 1 raid + templates de reply
- Jeudi: Thread Ecosystem + post cult
- Vendredi: 3 posts degen
- Samedi: Milestone + communauté
- Dimanche: 2 posts philosophiques

---

## 🔥 Générer un Raid

```
/raid [produit] [style]
```

### Produits disponibles:
| Produit | Description |
|---------|-------------|
| `holdex` | Alternative DexScreener à $20 |
| `ignition` | Launchpad avec rewards holders |
| `asdforecast` | Prediction market SOL |

### Styles disponibles:
| Style | Description | Exemple |
|-------|-------------|---------|
| `imagine` | Style Kovni | "Imagine paying $300..." |
| `what_do_you_think` | Style Kovni | "what do you think about..." |
| `fuck_x` | Style Jean Terre | "fuck dexscreener..." |
| `comparison` | Comparaison directe | "$300 vs $20" |
| `provocation` | Provocateur | "cope." |
| `viral` | Format meme | "them: X / us: Y" |

**Exemples:**
```
/raid holdex comparison
/raid ignition what_do_you_think
/raid asdforecast fuck_x
```

---

## 🧵 Générer un Thread

```
/thread [type]
```

### Types disponibles:
| Type | Tweets | Description |
|------|--------|-------------|
| `holdex` | 10 | Thread produit HolDEX |
| `ignition` | 10 | Thread produit Ignition |
| `asdforecast` | 10 | Thread produit ASDForecast |
| `ecosystem` | 11 | Thread écosystème complet |
| `builder_story` | 10 | Histoire des builders |

**Exemple:** `/thread ecosystem`

Le bot envoie chaque tweet séparément, prêt à copier-coller.

---

## 💊 Générer un Post Cult

```
/cult
```

Génère un post philosophique/conviction aléatoire.

**Exemples de contenu:**
- "We are not a chart. We are a cult."
- "everyone asks 'when pump?' nobody asks 'what are we building?'"
- "no funding is a feature."

---

## 🛡️ Réponses Anti-FUD

### Une réponse aléatoire:
```
/fud [type]
```

### Toutes les réponses d'un type:
```
/fudall [type]
```

### Types de FUD:
| Type | Quand utiliser |
|------|----------------|
| `scam` | "C'est un scam/rugpull" |
| `dead_chart` | "Le chart est mort" |
| `no_users` | "Personne utilise ça" |
| `how_money` | "Comment vous faites de l'argent?" |
| `just_memecoin` | "C'est juste un memecoin" |
| `why_not_dexscreener` | "Pourquoi pas DexScreener?" |
| `copy` | "C'est juste une copie" |
| `universal` | Réponse passe-partout |
| `nuclear` | FUD intense |

**Exemples:**
```
/fud scam          → 1 réponse aléatoire
/fudall dead_chart → Toutes les réponses "dead chart"
```

---

## 💬 Replies d'Engagement

```
/reply [type]
```

### Types disponibles:
| Type | Utilisation |
|------|-------------|
| `discovery_holdex` | Présenter HolDEX |
| `discovery_ignition` | Présenter Ignition |
| `ecosystem` | Pitch écosystème complet |
| `challenge_holdex` | "try holdex, then talk" |
| `challenge_ignition` | "use ignition once" |
| `high_fees` | Quand quelqu'un parle de fees élevés |
| `launchpad_dump` | Quand quelqu'un se plaint des dumps |
| `solana_projects` | Quand on demande des projets Solana |
| `building` | Discussions sur le building |

**Exemple:** `/reply ecosystem`

---

## 📊 Post Milestone

```
/milestone [semaine]
```

Génère un post de stats/milestone pour la semaine spécifiée.

**Exemple:** `/milestone 2`

---

## 📁 Exporter les Posts

```
/export [type] [semaine]
```

### Types d'export:
| Type | Contenu |
|------|---------|
| `weekly` | Tous les posts d'une semaine |
| `fud` | Toutes les réponses FUD |
| `replies` | Tous les templates de reply |

**Exemple:** `/export weekly 1` → Fichier .txt avec tous les posts semaine 1

---

## 📚 Autres Commandes

| Commande | Description |
|----------|-------------|
| `/templates` | Voir tous les templates disponibles |
| `/schedule` | Voir le planning hebdomadaire |
| `/help_posts` | Aide complète |

---

## 🎯 Workflow Recommandé

### Chaque Lundi:
1. `/week [numéro]` → Générer la semaine
2. Copier les posts dans un doc
3. Programmer ou poster manuellement

### Pendant la semaine:
1. `/fud [type]` → Répondre au FUD rapidement
2. `/reply [type]` → Engager sous les posts d'influenceurs
3. `/raid [produit] [style]` → Posts supplémentaires si besoin

### Pour les threads:
1. `/thread [type]` → Générer le thread
2. Poster tweet par tweet sur X
3. Espacer les tweets de 1-2 minutes

---

## 💡 Tips

- **Tous les posts incluent les hashtags** automatiquement
- **Les threads sont numérotés** (Tweet 1/10, 2/10, etc.)
- **Format copier-coller** entre les balises ``` ```
- **Varier les styles** pour ne pas être répétitif
- **Adapter légèrement** les posts si nécessaire

---

## 🔗 Liens Utiles

- **HolDEX:** alonisthe.dev/holdex
- **Ignition:** alonisthe.dev/ignition
- **ASDForecast:** alonisthe.dev/asdforecast
- **GitHub:** github.com/sollama58

---

**this is fine 🔥**
