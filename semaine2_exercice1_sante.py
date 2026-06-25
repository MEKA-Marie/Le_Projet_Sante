#  VARIABLES PATIENT 

nom_patient = "MAVOUNGOU Celestine"
age_patient = 42
sexe_patient = "F"
departement_patient = "Brazzaville"
couverture_sociale = "CNSS"

#  VARIABLES CONSULTATION 

type_consultation = "Urgences"
cout_consultation_fcfa = 15000.0
nb_consultations = 1
remise_cnss_pct = 30.0
diagnostic_principal = "Paludisme grave"

#  VARIABLES HOPITAL 

nom_hopital = "CHU de Brazzaville"
ville_hopital = "Brazzaville"
nb_lits_total = 320
nb_lits_occupes = 284
nb_medecins_actifs = 47

#   CALCULS 

# Coût total après remise CNSS
cout_total_fcfa = cout_consultation_fcfa * nb_consultations * (1 - remise_cnss_pct / 100)

# Taux d’occupation des lits
taux_occupation_pct = round(nb_lits_occupes / nb_lits_total * 100, 1)

# Ratio consultations par médecin (hypothèse : 120 consultations ce matin)
nb_consultations_hopital = 120
ratio_consultations_medecin = round(nb_consultations_hopital / nb_medecins_actifs, 1)


#  AFFICHAGE 
print("="*60)
print(f" FICHE PATIENT - {nom_patient}")
print("="*60)
print(f"Age           : {age_patient} ans")
print(f"Sexe          : {sexe_patient}")
print(f"Departement   : {departement_patient}")
print(f"Couverture    : {couverture_sociale}")
print("\nCONSULTATION")
print(f"Type          : {type_consultation}")
print(f"Diagnostic    : {diagnostic_principal}")
print(f"Cout unitaire : {cout_consultation_fcfa:,.0f} FCFA")
print(f"Remise CNSS   : {remise_cnss_pct}%")
print(f"COUT TOTAL    : {cout_total_fcfa} FCFA")
print("\nHOPITAL :", nom_hopital)
print(f"Ville         : {ville_hopital}")
print(f"Lits occupés  : {nb_lits_occupes} / {nb_lits_total} ({taux_occupation_pct}%)")
print(f"Medecins actifs : {nb_medecins_actifs}")
print(f"Ratio consult. : {ratio_consultations_medecin} consultations / médecin ce matin")
print("\nSTATUT : Prise en charge validée")
