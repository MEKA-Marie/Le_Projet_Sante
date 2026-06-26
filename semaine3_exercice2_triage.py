print("=== SYSTEME DE TRIAGE - URGENCES CHU BRAZZAVILLE ===")
print("Protocole Manchester adapté - DSS Congo 2026")
print()

# --- SAISIE DES DONNEES PATIENT ---
nom_patient = input("Nom du patient : ")
age_patient = int(input("Age (années) : "))
temperature = float(input("Température (°C) : "))
spo2 = float(input("Saturation O2 (%) : "))
tension_syst = int(input("Tension systolique (mmHg) : "))
douleur = int(input("Douleur /10 : "))

# --- VALIDATION DES PLAGES ---
if temperature < 35.0 or temperature > 43.0:
    print("ERREUR : Valeur de température impossible - vérifier la saisie")
if spo2 < 50.0 or spo2 > 100.0:
    print("ERREUR : SpO2 hors plage - vérifier le capteur")
if tension_syst < 50 or tension_syst > 250:
    print("ERREUR : Tension hors plage - vérifier le brassard")
if douleur < 0 or douleur > 10:
    print("ERREUR : Douleur doit être entre 0 et 10")
if age_patient < 0 or age_patient > 120:
    print("ERREUR : Age invalide - vérifier la saisie")

# --- TRIAGE ---
if temperature > 39.5 or spo2 < 90 or tension_syst > 180:
    niveau_triage = "1 - IMMEDIAT"
    couleur_triage = "[ROUGE]"
    delai_pec = "0 minute"
    action_triage = "Médecin présent immédiatement - code ROUGE activé"

elif temperature > 38.5 or spo2 < 94 or tension_syst > 140:
    niveau_triage = "2 - URGENT"
    couleur_triage = "[ORANGE]"
    delai_pec = "< 10 minutes"
    action_triage = "Appel médecin senior"

elif temperature > 37.5 or douleur > 6:
    niveau_triage = "3 - URGENT DIFFERE"
    couleur_triage = "[JAUNE]"
    delai_pec = "< 30 minutes"
    action_triage = "Infirmier - surveillance"

else:
    niveau_triage = "4 - MOINS URGENT"
    couleur_triage = "[VERT]"
    delai_pec = "< 120 minutes"
    action_triage = "File d'attente standard"

# --- AFFICHAGE ---
print()
print("="*55)
print(f"RESULTAT TRIAGE - {nom_patient.upper()}")
print("="*55)
print(f"Niveau : {niveau_triage} {couleur_triage}")
print(f"Température : {temperature} °C | SpO2 : {spo2}% | Tension : {tension_syst} mmHg | Douleur : {douleur}/10")
print(f"Prise en charge : {delai_pec}")
print(f"Action : {action_triage}")
