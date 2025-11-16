from datetime import datetime

def saisir_articles():
    articles = []
    while True:
        nom = input("Nom du produit (ou 'fin' pour terminer): ")
        if nom.lower() == 'fin':
            break
        try:
            prix = float(input(f"Prix unitaire de '{nom}' (€): "))
            quantite = int(input(f"Quantité de '{nom}': "))
            articles.append((nom, prix, quantite))
        except ValueError:
            print("Erreur de saisie. Veuillez entrer des nombres valides.")
    return articles

def afficher_facture(client, articles):
    date = datetime.now().strftime("%d/%m/%Y %H:%M")
    total = sum(prix * quantite for _, prix, quantite in articles)

    print("\n" + "=" * 40)
    print(f"Facture pour: {client}")
    print(f"Date: {date}")
    print("-" * 40)
    print(f"{'Produit':20} {'Qté':>5} {'Prix':>10} {'Total':>10}")
    for nom, prix, quantite in articles:
        total_article = prix * quantite
        print(f"{nom:20} {quantite:>5} {prix:>10.2f} {total_article:>10.2f}")
    print("-" * 40)
    print(f"{'Montant total':>35}: {total:.2f} €")
    print("=" * 40)

# Programme principal
client = input("Nom du client: ")
articles = saisir_articles()
afficher_facture(client, articles)
