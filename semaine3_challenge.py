# === CHALLENGE ENTREPRISE - RAPPORT COMPARATIF HOPITAUX DU POOL ===
# Date : 15 janvier 2026

# --- Données des hôpitaux ---
h1_nom = "Hopital District Kinkala"
h1_budget = 12_500_000
h1_consultations = 1847
h1_hospitalisations = 312
h1_deces = 8
h1_lits_total = 45
h1_lits_occupes = 41
h1_medecins = 3
h1_population = 85_000

h2_nom = "CMS de Vindza"
h2_budget = 6_800_000
h2_consultations = 923
h2_hospitalisations = 87
h2_deces = 2
h2_lits_total = 20
h2_lits_occupes = 14
h2_medecins = 1
h2_population = 42_000

h3_nom = "Hopital de Kindamba"
h3_budget = 9_200_000
h3_consultations = 1234
h3_hospitalisations = 201
h3_deces = 11
h3_lits_total = 35
h3_lits_occupes = 33
h3_medecins = 2
h3_population = 67_000

# --- Fonction de calcul des indicateurs ---
def indicateurs(nom, budget, consultations, hospitalisations, deces, lits_total, lits_occupes, medecins, population):
    cout_moyen = round(budget / (consultations + hospitalisations), 2)
    taux_occupation = round(lits_occupes / lits_total * 100, 1)
    densite_medicale = round((medecins / population) * 1000, 3)
    taux_mortalite = round((deces / hospitalisations) * 100, 1)

    critique = (taux_mortalite > 2.0 or densite_medicale < 0.05)

    return {
        "nom": nom,
        "cout_moyen": cout_moyen,
        "taux_occupation": taux_occupation,
        "densite_medicale": densite_medicale,
        "taux_mortalite": taux_mortalite,
        "critique": critique
    }

# --- Calcul pour chaque hôpital ---
hopitaux = [
    indicateurs(h1_nom, h1_budget, h1_consultations, h1_hospitalisations, h1_deces, h1_lits_total, h1_lits_occupes, h1_medecins, h1_population),
    indicateurs(h2_nom, h2_budget, h2_consultations, h2_hospitalisations, h2_deces, h2_lits_total, h2_lits_occupes, h2_medecins, h2_population),
    indicateurs(h3_nom, h3_budget, h3_consultations, h3_hospitalisations, h3_deces, h3_lits_total, h3_lits_occupes, h3_medecins, h3_population)
]

# --- Rapport comparatif ---
print("="*75)
print(" RAPPORT COMPARATIF - HOPITAUX DU POOL ")
print(" Date : 15 janvier 2026")
print("="*75)

for h in hopitaux:
    print(f"{h['nom']}")
    print(f" - Coût moyen par patient : {h['cout_moyen']} FCFA")
    print(f" - Taux d'occupation      : {h['taux_occupation']}%")
    print(f" - Densité médicale       : {h['densite_medicale']} médecins / 1000 hab")
    print(f" - Taux de mortalité      : {h['taux_mortalite']}%")
    if h["critique"]:
        print(" !! SITUATION CRITIQUE !!")
    print("-"*75)

# --- Vérification budget pour recruter 5 médecins par hôpital ---
cout_medecin = 1_200_000
budget_total = h1_budget + h2_budget + h3_budget
cout_medecins_requis = 3 * 5 * cout_medecin

print("\n=== BILAN BUDGET ===")
if budget_total >= cout_medecins_requis:
    print(f"Le budget total ({budget_total:,} FCFA) suffit pour recruter 5 médecins par hôpital.")
else:
    print(f"Le budget total ({budget_total:,} FCFA) est insuffisant pour recruter 5 médecins par hôpital.")
