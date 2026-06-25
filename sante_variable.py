# === SECTION A : CONSTANTES NATIONALES ET NORMES OMS ===

TAUX_EUR_FCFA = 655.957
TAUX_USD_FCFA = 600.0

SEUIL_OMS_DENSITE_MEDICALE = 2.3   # medecins pour 1000 habitants
SEUIL_OMS_COUVERTURE_VACCIN = 95.0 # %
SEUIL_MORTALITE_ALERTE = 2.0       # % deces / hospitalisations
SEUIL_RUPTURE_STOCK_JOURS = 30     # jours minimum de stock

DEPARTEMENTS_CONGO = [
    "Brazzaville", "Pointe-Noire", "Bouenza", "Cuvette",
    "Cuvette-Ouest", "Kouilou", "Lekoumou", "Likouala",
    "Niari", "Plateaux", "Pool", "Sangha"
]

# === SECTION B : VARIABLES DES 5 HOPITAUX ===

# Hopital 1 - CHU de Brazzaville
h1_nom = "CHU de Brazzaville"
h1_ville = "Brazzaville"
h1_departement = "Brazzaville"
h1_type = "CHU"
h1_nb_lits = 320
h1_nb_lits_occupes = 284
h1_nb_medecins = 47
h1_nb_infirmiers = 123
h1_population_zone = 1_800_000

# Hopital 2 - Hopital General Pointe-Noire
h2_nom = "Hopital General Pointe-Noire"
h2_ville = "Pointe-Noire"
h2_departement = "Kouilou"
h2_type = "General"
h2_nb_lits = 180
h2_nb_lits_occupes = 143
h2_nb_medecins = 22
h2_nb_infirmiers = 58
h2_population_zone = 128_000

# Hopital 3 - Hopital de Dolisie
h3_nom = "Hopital de Dolisie"
h3_ville = "Dolisie"
h3_departement = "Niari"
h3_type = "General"
h3_nb_lits = 150
h3_nb_lits_occupes = 120
h3_nb_medecins = 15
h3_nb_infirmiers = 45
h3_population_zone = 95_000

# Hopital 4 - Hopital de district Owando
h4_nom = "Hopital de district Owando"
h4_ville = "Owando"
h4_departement = "Cuvette"
h4_type = "District"
h4_nb_lits = 90
h4_nb_lits_occupes = 70
h4_nb_medecins = 8
h4_nb_infirmiers = 25
h4_population_zone = 60_000

# Hopital 5 - Centre de sante Impfondo
h5_nom = "Centre de sante Impfondo"
h5_ville = "Impfondo"
h5_departement = "Likouala"
h5_type = "Centre"
h5_nb_lits = 60
h5_nb_lits_occupes = 45
h5_nb_medecins = 5
h5_nb_infirmiers = 18
h5_population_zone = 40_000

# SECTION C : VARIABLES DES 5 MEDICAMENTS 

med1_nom = "Artemether-Lumefantrine"
med1_quantite = 500
med1_seuil_rupture = 50
med1_cout_unitaire = 1500.0

med2_nom = "Amoxicilline"
med2_quantite = 800
med2_seuil_rupture = 100
med2_cout_unitaire = 500.0

med3_nom = "Paracetamol"
med3_quantite = 1200
med3_seuil_rupture = 200
med3_cout_unitaire = 100.0

med4_nom = "SRO"
med4_quantite = 600
med4_seuil_rupture = 80
med4_cout_unitaire = 200.0

med5_nom = "Vaccin antipaludeen"
med5_quantite = 300
med5_seuil_rupture = 30
med5_cout_unitaire = 2500.0

#  SECTION D : CALCULS D'INITIALISATION 

# Densité médicale nationale (somme des medecins / somme population * 1000)
total_medecins = h1_nb_medecins + h2_nb_medecins + h3_nb_medecins + h4_nb_medecins + h5_nb_medecins
total_population = h1_population_zone + h2_population_zone + h3_population_zone + h4_population_zone + h5_population_zone
densite_medicale_nationale = round((total_medecins / total_population) * 1000, 2)

# Taux d’occupation moyen
total_lits = h1_nb_lits + h2_nb_lits + h3_nb_lits + h4_nb_lits + h5_nb_lits
total_lits_occupes = h1_nb_lits_occupes + h2_nb_lits_occupes + h3_nb_lits_occupes + h4_nb_lits_occupes + h5_nb_lits_occupes
taux_occupation_moyen = round(total_lits_occupes / total_lits * 100, 1)

# Valeur totale du stock de médicaments
valeur_stock_medicaments = (
    med1_quantite * med1_cout_unitaire +
    med2_quantite * med2_cout_unitaire +
    med3_quantite * med3_cout_unitaire +
    med4_quantite * med4_cout_unitaire +
    med5_quantite * med5_cout_unitaire
)



# === SECTION E : RAPPORT D'INVENTAIRE ===
print(" RAPPORT INITIAL DU SYSTEME DE SANTE ")
print(f"Densite medicale nationale : {densite_medicale_nationale} medecins / 1000 hab [Norme OMS >= {SEUIL_OMS_DENSITE_MEDICALE}]")
print(f"Taux d'occupation moyen    : {taux_occupation_moyen}%")
print(f"Valeur stock medicaments   : {valeur_stock_medicaments:,} FCFA")
print("\nInventaire des medicaments essentiels :")
print(f"- {med1_nom} : {med1_quantite} unités (seuil {med1_seuil_rupture})")
print(f"- {med2_nom} : {med2_quantite} unités (seuil {med2_seuil_rupture})")
print(f"- {med3_nom} : {med3_quantite} unités (seuil {med3_seuil_rupture})")
print(f"- {med4_nom} : {med4_quantite} unités (seuil {med4_seuil_rupture})")
print(f"- {med5_nom} : {med5_quantite} unités (seuil {med5_seuil_rupture})")
