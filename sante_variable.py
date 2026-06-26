# === MINI PROJET SANTE PUBLIQUE ===
# Semaine 2 + Semaine 3
# Fichier : sante_variables.py

# === SECTION A : CONSTANTES NATIONALES ET NORMES OMS ===
TAUX_EUR_FCFA = 655.957
TAUX_USD_FCFA = 600.0

SEUIL_OMS_DENSITE_MEDICALE = 2.3   # médecins pour 1000 habitants
SEUIL_OMS_COUVERTURE_VACCIN = 95.0 # %
SEUIL_MORTALITE_ALERTE = 2.0       # % décès / hospitalisations
SEUIL_RUPTURE_STOCK_JOURS = 30     # jours minimum de stock

DEPARTEMENTS_CONGO = [
    "Brazzaville", "Pointe-Noire", "Bouenza", "Cuvette",
    "Cuvette-Ouest", "Kouilou", "Lekoumou", "Likouala",
    "Niari", "Plateaux", "Pool", "Sangha"
]

# === SECTION B : VARIABLES DES 5 HOPITAUX ===
h1_nom, h1_nb_lits, h1_nb_lits_occupes, h1_nb_medecins, h1_population_zone = "CHU de Brazzaville", 320, 284, 47, 1_800_000
h2_nom, h2_nb_lits, h2_nb_lits_occupes, h2_nb_medecins, h2_population_zone = "Hopital General Pointe-Noire", 180, 143, 22, 128_000
h3_nom, h3_nb_lits, h3_nb_lits_occupes, h3_nb_medecins, h3_population_zone = "Hopital de Dolisie", 150, 120, 15, 95_000
h4_nom, h4_nb_lits, h4_nb_lits_occupes, h4_nb_medecins, h4_population_zone = "Hopital de district Owando", 90, 70, 8, 60_000
h5_nom, h5_nb_lits, h5_nb_lits_occupes, h5_nb_medecins, h5_population_zone = "Centre de santé Impfondo", 60, 45, 5, 40_000

# === SECTION C : VARIABLES DES 5 MEDICAMENTS ===
med1_nom, med1_quantite, med1_seuil_rupture, med1_cout_unitaire = "Artemether-Lumefantrine", 500, 50, 1500.0
med2_nom, med2_quantite, med2_seuil_rupture, med2_cout_unitaire = "Amoxicilline", 800, 100, 500.0
med3_nom, med3_quantite, med3_seuil_rupture, med3_cout_unitaire = "Paracetamol", 1200, 200, 100.0
med4_nom, med4_quantite, med4_seuil_rupture, med4_cout_unitaire = "SRO", 600, 80, 200.0
med5_nom, med5_quantite, med5_seuil_rupture, med5_cout_unitaire = "Vaccin antipaludeen", 300, 30, 2500.0

# === SECTION D : CALCULS D'INITIALISATION ===
total_medecins = h1_nb_medecins + h2_nb_medecins + h3_nb_medecins + h4_nb_medecins + h5_nb_medecins
total_population = h1_population_zone + h2_population_zone + h3_population_zone + h4_population_zone + h5_population_zone
densite_medicale_nationale = round((total_medecins / total_population) * 1000, 2)

total_lits = h1_nb_lits + h2_nb_lits + h3_nb_lits + h4_nb_lits + h5_nb_lits
total_lits_occupes = h1_nb_lits_occupes + h2_nb_lits_occupes + h3_nb_lits_occupes + h4_nb_lits_occupes + h5_nb_lits_occupes
taux_occupation_moyen = round(total_lits_occupes / total_lits * 100, 1)

valeur_stock_medicaments = (
    med1_quantite * med1_cout_unitaire +
    med2_quantite * med2_cout_unitaire +
    med3_quantite * med3_cout_unitaire +
    med4_quantite * med4_cout_unitaire +
    med5_quantite * med5_cout_unitaire
)

# === SECTION E : CONDITIONS & BRANCHEMENTS (Semaine 3) ===
def classification_stock(nom, stock, seuil):
    if stock <= seuil:
        return nom, "RUPTURE CRITIQUE", "[ROUGE]", "Alerte immédiate PNA - commande express sous 24h"
    elif stock <= seuil * 1.5:
        return nom, "ALERTE STOCK", "[ORANGE]", "Commande urgente à déclencher sous 72h"
    elif stock <= seuil * 2:
        return nom, "STOCK LIMITE", "[JAUNE]", "Surveillance renforcée - planifier commande"
    else:
        return nom, "STOCK NORMAL", "[VERT]", "Situation normale - suivi standard"

# Application aux médicaments
medicaments = [
    classification_stock(med1_nom, med1_quantite, med1_seuil_rupture),
    classification_stock(med2_nom, med2_quantite, med2_seuil_rupture),
    classification_stock(med3_nom, med3_quantite, med3_seuil_rupture),
    classification_stock(med4_nom, med4_quantite, med4_seuil_rupture),
    classification_stock(med5_nom, med5_quantite, med5_seuil_rupture)
]

# Compteurs
nb_ruptures = sum(1 for m in medicaments if m[1] == "RUPTURE CRITIQUE")
nb_alertes = sum(1 for m in medicaments if m[1] == "ALERTE STOCK")
nb_normaux = sum(1 for m in medicaments if m[1] == "STOCK NORMAL")

# === SECTION F : RAPPORT FINAL ===
print("=== RAPPORT DU SYSTEME DE SANTE ===")
print(f"Densité médicale nationale : {densite_medicale_nationale} médecins / 1000 hab [Norme OMS >= {SEUIL_OMS_DENSITE_MEDICALE}]")
print(f"Taux d'occupation moyen    : {taux_occupation_moyen}%")
print(f"Valeur stock médicaments   : {valeur_stock_medicaments:,} FCFA")

print("\n=== INVENTAIRE DES MEDICAMENTS ===")
for nom, statut, couleur, action in medicaments:
    print(f"{couleur} {nom}")
    print(f"Statut : {statut}")
    print(f"Action : {action}")
    print("-"*60)

print("\n=== BILAN FINAL ===")
print(f"Ruptures critiques : {nb_ruptures}")
print(f"Alertes stock      : {nb_alertes}")
print(f"Stocks normaux     : {nb_normaux}")

if nb_ruptures > 0:
    print(f"!! ALERTE PRIORITAIRE : {nb_ruptures} médicaments en RUPTURE CRITIQUE !!")
