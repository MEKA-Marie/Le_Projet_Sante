# Données des médicaments (S2 réutilisées)
m1_nom, m1_stock, m1_seuil_rupture = "Artemether-Lumefantrine", 3200, 2000
m2_nom, m2_stock, m2_seuil_rupture = "Amoxicilline 500mg", 950, 800
m3_nom, m3_stock, m3_seuil_rupture = "Paracetamol 500mg", 12400, 3000
m4_nom, m4_stock, m4_seuil_rupture = "SRO (sachets)", 4200, 5000
m5_nom, m5_stock, m5_seuil_rupture = "Vaccin DTP-HepB-Hib", 820, 1000

# Fonction de classification
def classification(stock, seuil):
    if stock <= seuil:
        return "RUPTURE CRITIQUE", "[ROUGE]", "Alerte immédiate PNA - commande express sous 24h"
    elif stock <= seuil * 1.5:
        return "ALERTE STOCK", "[ORANGE]", "Commande urgente à déclencher sous 72h"
    elif stock <= seuil * 2:
        return "STOCK LIMITE", "[JAUNE]", "Surveillance renforcée - planifier commande"
    else:
        return "STOCK NORMAL", "[VERT]", "Situation normale - suivi standard"

# Application aux 5 médicaments
m1_statut, m1_couleur, m1_action = classification(m1_stock, m1_seuil_rupture)
m2_statut, m2_couleur, m2_action = classification(m2_stock, m2_seuil_rupture)
m3_statut, m3_couleur, m3_action = classification(m3_stock, m3_seuil_rupture)
m4_statut, m4_couleur, m4_action = classification(m4_stock, m4_seuil_rupture)
m5_statut, m5_couleur, m5_action = classification(m5_stock, m5_seuil_rupture)

# Compteurs
nb_ruptures_critiques = 0
nb_alertes_stock = 0

for statut in [m1_statut, m2_statut, m3_statut, m4_statut, m5_statut]:
    if statut == "RUPTURE CRITIQUE":
        nb_ruptures_critiques += 1
    elif statut == "ALERTE STOCK":
        nb_alertes_stock += 1

# Rapport
print("="*65)
print(" RAPPORT DE STOCK - PHARMACIE NATIONALE D'APPROVISIONNEMENT")
print(" Date : 15 janvier 2026")
print("="*65)

for nom, stock, seuil, statut, couleur, action in [
    (m1_nom, m1_stock, m1_seuil_rupture, m1_statut, m1_couleur, m1_action),
    (m2_nom, m2_stock, m2_seuil_rupture, m2_statut, m2_couleur, m2_action),
    (m3_nom, m3_stock, m3_seuil_rupture, m3_statut, m3_couleur, m3_action),
    (m4_nom, m4_stock, m4_seuil_rupture, m4_statut, m4_couleur, m4_action),
    (m5_nom, m5_stock, m5_seuil_rupture, m5_statut, m5_couleur, m5_action),
]:
    print(f"{couleur} {nom}")
    print(f"Stock : {stock} unités | Seuil rupture : {seuil}")
    print(f"Statut : {statut}")
    print(f"Action : {action}")
    print("-"*65)

print("\nBILAN STOCK - PNA CONGO")
print(f"Ruptures critiques : {nb_ruptures_critiques}")
print(f"Alertes stock      : {nb_alertes_stock}")
print(f"Stocks normaux     : {5 - nb_ruptures_critiques - nb_alertes_stock}")

if nb_ruptures_critiques > 0:
    print(f"!! ALERTE PRIORITAIRE : {nb_ruptures_critiques} médicaments en RUPTURE CRITIQUE !!")
