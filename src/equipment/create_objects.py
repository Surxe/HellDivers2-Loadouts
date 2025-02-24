# Import parent path
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append(parent_dir)

# Import local libraries
from src.equipment.Weapon import Weapon
from src.equipment.Stratagem import Stratagem
from src.equipment.Boost import Boost

weapons = [
    #(id, name, slot, category)
    # Primary
    # Assault Rifle
    Weapon("ar23-liberator", "AR-23 Liberator", "Primary", "Assault Rifle"),
    Weapon("ar23p-liberator-penetrator", "AR-23P Liberator Penetrator", "Primary", "Assault Rifle"),
    Weapon("ar23c-liberator-concussive", "AR-23C Liberator Concussive", "Primary", "Assault Rifle"),
    Weapon("sta-52-assault-rifle", "StA-52 Assault Rifle", "Primary", "Assault Rifle"),
    Weapon("ar23a-liberator-carbine", "AR-23A Liberator Carbine", "Primary", "Assault Rifle"),
    Weapon("ar61-tenderizer", "AR-61 Tenderizer", "Primary", "Assault Rifle"),
    Weapon("br14-adjudicator", "BR-14 Adjudicator", "Primary", "Assault Rifle"),
    # Marksman Rifle
    Weapon("r2124-constitution", "R-2124 Constitution", "Primary", "Marksman Rifle"),
    Weapon("r63-diligence", "R-63 Diligence", "Primary", "Marksman Rifle"),
    Weapon("r63cs-diligence-counter-sniper", "R-63CS Diligence Counter Sniper", "Primary", "Marksman Rifle"),
    # Sniper Rifle
    Weapon("plas39-accelerator-rifle", "PLAS-39 Accelerator Rifle", "Primary", "Sniper Rifle"),
    # Submachine Gun
    Weapon("mp98-knight", "MP-98 Knight", "Primary", "Submachine Gun"),
    Weapon("sta-11-smg", "StA-11 SMG", "Primary", "Submachine Gun"),
    Weapon("smg32-reprimand", "SMG-32 Reprimand", "Primary", "Submachine Gun"),
    Weapon("smg37-defender", "SMG-37 Defender", "Primary", "Submachine Gun"),
    Weapon("smg72-pummeler", "SMG-72 Pummeler", "Primary", "Submachine Gun"),
    # Shotgun
    Weapon("sg8-punisher", "SG-8 Punisher", "Primary", "Shotgun"),
    Weapon("sg8s-slugger", "SG-8S Slugger", "Primary", "Shotgun"),
    Weapon("sg20-halt", "SG-20 Halt", "Primary", "Shotgun"),
    Weapon("sg451-cookout", "SG-451 Cookout", "Primary", "Shotgun"),
    Weapon("sg225-breaker", "SG-225 Breaker", "Primary", "Shotgun"),
    Weapon("sg225sp-breaker-spray-pray", "SG-225SP Breaker Spray&Pray", "Primary", "Shotgun"),
    Weapon("sg225ie-breaker-incendiary", "SG-225IE Breaker Incendiary", "Primary", "Shotgun"),
    # Explosive
    Weapon("cb9-exploding-crossbow", "CB-9 Exploding Crossbow", "Primary", "Explosive"),
    Weapon("r36-eruptor", "R-36 Eruptor", "Primary", "Explosive"),
    # Energy-Based
    Weapon("sg8p-punisher-plasma", "SG-8P Punisher Plasma", "Primary", "Energy-Based"),
    Weapon("arc12-blitzer", "ARC-12 Blitzer", "Primary", "Energy-Based"),
    Weapon("las5-scythe", "LAS-5 Scythe", "Primary", "Energy-Based"),
    Weapon("las16-sickle", "LAS-16 Sickle", "Primary", "Energy-Based"),
    Weapon("las17-double-edge-sickle", "LAS-17 Double-Edge Sickle", "Primary", "Energy-Based"),
    Weapon("plas1-scorcher", "PLAS-1 Scorcher", "Primary", "Energy-Based"),
    Weapon("plas101-purifier", "PLAS-101 Purifier", "Primary", "Energy-Based"),
    # Special
    Weapon("flam66-torcher", "FLAM-66 Torcher", "Primary", "Special"),
    Weapon("jar5-dominator", "JAR-5 Dominator", "Primary", "Special"),

    # Secondary
    # Pistol
    Weapon("p2-peacemaker", "P-2 Peacemaker", "Secondary", "Pistol"),
    Weapon("p19-redeemer", "P-19 Redeemer", "Secondary", "Pistol"),
    Weapon("p113-verdict", "P-113 Verdict", "Secondary", "Pistol"),
    Weapon("p4-senator", "P-4 Senator", "Secondary", "Pistol"),
    # Melee
    Weapon("cqc19-stun-lance", "CQC-19 Stun Lance", "Secondary", "Melee"),
    Weapon("cqc30-stun-baton", "CQC-30 Stun Baton", "Secondary", "Melee"),
    Weapon("cqc5-combat-hatchet", "CQC-5 Combat Hatchet", "Secondary", "Melee"),
    # Special
    Weapon("p11-stim-pistol", "P-11 Stim Pistol", "Secondary", "Special"),
    Weapon("sg22-bushwhacker", "SG-22 Bushwhacker", "Secondary", "Special"),
    Weapon("p72-crisper", "P-72 Crisper", "Secondary", "Special"),
    Weapon("gp31-grenade-pistol", "GP-31 Grenade Pistol", "Secondary", "Special"),
    Weapon("las7-dagger", "LAS-7 Dagger", "Secondary", "Special"),
    Weapon("gp31-ultimatum", "GP-31 Ultimatum", "Secondary", "Special"),
    Weapon("plas15-loyalist", "PLAS-15 Loyalist", "Secondary", "Special"),

    # Throwable
    # Standard
    Weapon("g6-frag", "G-6 Frag", "Throwable", "Standard"),
    Weapon("g12-high-explosive", "G-12 High Explosive", "Throwable", "Standard"),
    Weapon("g10-incendiary", "G-10 Incendiary", "Throwable", "Standard"),
    # Special
    Weapon("g16-impact", "G-16 Impact", "Throwable", "Special"),
    Weapon("g13-incendiary-impact", "G-13 Incendiary Impact", "Throwable", "Special"),
    Weapon("g23-stun", "G-23 Stun", "Throwable", "Special"),
    Weapon("g4-gas", "G-4 Gas", "Throwable", "Special"),
    Weapon("g50-seeker", "G-50 Seeker", "Throwable", "Special"),
    Weapon("g3-smoke", "G-3 Smoke", "Throwable", "Special"),
    Weapon("g123-thermite", "G-123 Thermite", "Throwable", "Special"),
    Weapon("k2-throwing-knife", "K-2 Throwing Knife", "Throwable", "Special")
]

stratagems = [
    #(id, name, department)
    # Patriotic Administration Center
    Stratagem("mg43-machine-gun", "MG-43 Machine Gun", "Patriotic Administration Center", "Machine Gun"),
    Stratagem("apw1-anti-materiel-rifle", "APW-1 Anti-Materiel Rifle", "Patriotic Administration Center", "Anti-Materiel Rifle"),
    Stratagem("m105-stalwart", "M-105 Stalwart", "Patriotic Administration Center", "Stalwart"),
    Stratagem("eat17-expendable-anti-tank", "EAT-17 Expendable Anti-Tank", "Patriotic Administration Center", "Expendable Anti-Tank"),
    Stratagem("gr8-recoilless-rifle", "GR-8 Recoilless Rifle", "Patriotic Administration Center", "Recoilless Rifle"),
    Stratagem("flam40-flamethrower", "FLAM-40 Flamethrower", "Patriotic Administration Center", "Flamethrower"),
    Stratagem("ac8-autocannon", "AC-8 Autocannon", "Patriotic Administration Center", "Autocannon"),
    Stratagem("mg206-heavy-machine-gun", "MG-206 Heavy Machine Gun", "Patriotic Administration Center", "Heavy Machine Gun"),
    Stratagem("rl77-airburst-rocket-launcher", "RL-77 Airburst Rocket Launcher", "Patriotic Administration Center", "RL-77 Airburst Rocket Launcher"),
    Stratagem("mls4x-commando", "MLS-4X Commando", "Patriotic Administration Center", "Commando"),
    Stratagem("rs422-railgun", "RS-422 Railgun", "Patriotic Administration Center", "Railgun"),
    Stratagem("faf14-spear", "FAF-14 Spear", "Patriotic Administration Center", "Spear"),
    Stratagem("stax3-wasp", "StA-X3 W.A.S.P. Launcher", "Patriotic Administration Center", "StA-X3 W.A.S.P. Launcher"),

    # Orbital Cannons
    Stratagem("orbital-gatling-barrage", "Orbital Gatling Barrage", "Orbital Cannons"),
    Stratagem("orbital-airburst-strike", "Orbital Airburst Strike", "Orbital Cannons"),
    Stratagem("orbital-120mm-he-barrage", "Orbital 120mm HE Barrage", "Orbital Cannons"),
    Stratagem("orbital-380mm-he-barrage", "Orbital 380mm HE Barrage", "Orbital Cannons"),
    Stratagem("orbital-walking-barrage", "Orbital Walking Barrage", "Orbital Cannons"),
    Stratagem("orbital-laser", "Orbital Laser", "Orbital Cannons"),
    Stratagem("orbital-napalm-barrage", "Orbital Napalm Barrage", "Orbital Cannons"),
    Stratagem("orbital-railcannon-strike", "Orbital Railcannon Strike", "Orbital Cannons"),

    # Hangar
    Stratagem("eagle-strafing-run", "Eagle Strafing Run", "Hangar"),
    Stratagem("eagle-airstrike", "Eagle Airstrike", "Hangar"),
    Stratagem("eagle-cluster-bomb", "Eagle Cluster Bomb", "Hangar"),
    Stratagem("eagle-napalm-airstrike", "Eagle Napalm Airstrike", "Hangar"),
    Stratagem("lift850-jump-pack", "LIFT-850 Jump Pack", "Hangar", "Jump Pack"),
    Stratagem("eagle-smoke-strike", "Eagle Smoke Strike", "Hangar"),
    Stratagem("eagle-110mm-rocket-pods", "Eagle 110mm Rocket Pods", "Hangar"),
    Stratagem("eagle-500kg-bomb", "Eagle 500kg Bomb", "Hangar"),
    Stratagem("m102-fast-recon-vehicle", "M-102 Fast Recon Vehicle", "Hangar", "M-102 Fast Recon Vehicle"),

    # Bridge
    Stratagem("orbital-precision-strike", "Orbital Precision Strike", "Bridge"),
    Stratagem("orbital-gas-strike", "Orbital Gas Strike", "Bridge"),
    Stratagem("orbital-ems-strike", "Orbital EMS Strike", "Bridge"),
    Stratagem("orbital-ems-strike", "Orbital EMS Strike", "Bridge"),
    Stratagem("orbital-smoke-strike", "Orbital Smoke Strike", "Bridge"),
    Stratagem("emg101-hmg-emplacement", "E/MG-101 HMG Emplacement", "Bridge", "HMG Emplacement"),
    Stratagem("fx12-sheild-generator-relay", "FX-12 Sheild Generator Relay", "Bridge", "Shield Generator Relay"),
    Stratagem("aarc3-tesla-tower", "A/ARC-3 Tesla Tower", "Bridge", "Tesla Tower"),

    # Engineering Bay
    Stratagem("md6-anti-personnel-minefield", "MD-6 Anti-Personnel Minefield", "Engineering Bay", "Anti-Personnel Minefield"),
    Stratagem("b1-supply-pack", "B-1 Supply Pack", "Engineering Bay", "Supply Pack"),
    Stratagem("gl21-grenade-launcher", "GL-21 Grenade Launcher", "Engineering Bay", "Grenade Launcher"),
    Stratagem("las98-laser-cannon", "LAS-98 Laser Cannon", "Engineering Bay", "Laser Cannon"),
    Stratagem("md14-incendiary-mines", "MD-14 Incendiary Mines", "Engineering Bay", "Incendiary Mines"),
    Stratagem("axlas5-guard-dog-rover", "AX/LAS-5 \"Guard Dog\" Rover", "Engineering Bay", "Guard Dog Rover"),
    Stratagem("sh20-ballistic-shield-backpack", "SH-20 Ballistic Shield Backpack", "Engineering Bay", "Ballistic Shield Backpack"),
    Stratagem("arc3-arc-thrower", "ARC-3 Arc Thrower", "Engineering Bay", "Arc Thrower"),
    Stratagem("md17-anti-tank-mines", "MD-17 Anti-Tank Mines", "Engineering Bay", "MD-17 Anti-Tank Mines"),
    Stratagem("las99-quasar-cannon", "LAS-99 Quasar Cannon", "Engineering Bay", "Quasar Cannon"),
    Stratagem("sh32-shield-generator-pack", "SH-32 Shield Generator Pack", "Engineering Bay", "Shield Generator Pack"),

    # Robotics Workshop
    Stratagem("amg43-machine-gun-sentry", "A/MG-43 Machine Gun Sentry", "Robotics Workshop", "Machine Gun Sentry"),
    Stratagem("ag16-gatling-sentry", "A/G-16 Gatling Sentry", "Robotics Workshop", "Gatling Sentry"),
    Stratagem("am12-mortar-sentry", "A/M-12 Mortar Sentry", "Robotics Workshop", "Mortar Sentry"),
    Stratagem("axar23-guard-dog", "AX/AR-23 \"Guard Dog\"", "Robotics Workshop", "Guard Dog"),
    Stratagem("aac8-autocannon-sentry", "A/AC-8 Autocannon Sentry", "Robotics Workshop", "Autocannon Sentry"),
    Stratagem("amls4x-rocket-sentry", "A/MLS-4x Rocket Sentry", "Robotics Workshop", "Rocket Sentry"),
    Stratagem("exo45-patriot-exosuit", "EXO-45 Patriot Exosuit", "Robotics Workshop", "EXO-45 Patriot Exosuit"),
    Stratagem("exo49-emancipator-exosuit", "EXO-49 Emancipator Exosuit", "Robotics Workshop", "EXO-49 Emancipator Exosuit"),

    # Warbonds
    Stratagem("tx41-sterilizer", "TX-41 Sterilizer", "Warbonds", "Sterilizer"),
    Stratagem("axtx13-guard-dog-dog-breath", "AX/TX-13 \"Guard Dog\" Dog Breath", "Warbonds", "Guard Dog Dog Breath"),
    Stratagem("sh51-directional-shield", "SH-51 Directional Shield", "Warbonds", "SH-51 Directional Shield"),
    Stratagem("eat12-anti-tank-emplacement", "E/AT-12 Anti-Tank Emplacement", "Warbonds", "E AT-12 Anti-Tank Emplacement"),
    Stratagem("aflam40-flame-sentry", "A/FLAm-40 Flame Sentry", "Warbonds", "A FLAM-40 Flame Sentry"),
    Stratagem("b100-portable-hellbomb", "B-100 Portable Hellbomb", "Warbonds", "Portable Hellbomb"),
]

boosts = [
    #(id, name)
    Boost("hellpod-space-optimization", "Hellpod Space Optimization"),
    Boost("vitality-enhancement", "Vitality Enhancement"),
    Boost("uav-recon-booster", "UAV Recon Booster"),
    Boost("stamina-enhancement", "Stamina Enhancement"),
    Boost("muscle-enhancement", "Muscle Enhancement"),
    Boost("increased-reinforcement-budget", "Increased Reinforcement Budget"),
    Boost("flexible-reinforcement-budget", "Flexible Reinforcement Budget"),
    Boost("localization-confusion", "Localization Confusion"),
    Boost("expert-extraction-pilot", "Expert Extraction Pilot"),
    Boost("motivational-shocks", "Motivational Shocks"),
    Boost("experimental-infusion", "Experimental Infusion"),
    Boost("firebomb-hellpods", "Firebomb Hellpods"),
    Boost("dead-sprint", "Dead Sprint"),
    Boost("armed-resupply-pods", "Armed Resupply Pods")
]

equipments = weapons + stratagems + boosts

if __name__ == "__main__":
    Weapon.save()
    Stratagem.save()
    Boost.save()
    print("Equipment objects created and saved to json files.")