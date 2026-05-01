# 1. Crearea dictionarului sales 
sales = {
    "Laptop": 15,
    "Mouse": 150,
    "Keyboards": 85,
    "Monitor": 30,
    "USB cables": 200
}

# 2. Functie pentru validarea datelor
def validate_sales_data(sales_dict):
    """Verifica daca exista produse cu cantitati negative"""
    for product, quantity in sales_dict.items():
        if quantity < 0:
            print(f"Atentie! Produsul '{product}' are o cantitate negativa: {quantity}")
            return False
    return True

# 3. Afisarea dictionarului initial
print("Dictionarul sales initial:")
for product, quantity in sales.items():
    print(f"  {product}: {quantity}")
print()

# 4. a) Cantitatea totala de produse vandute
total_sales = sum(sales.values())
print(f"a) Cantitatea totala de produse vandute: {total_sales}")

# 4. b) Produsul care s a vandut cel mai mult
best_selling = max(sales, key=sales.get)
print(f"b) Produsul care s a vandut cel mai mult: {best_selling} ({sales[best_selling]} unitati)")

# 4. c) Cel mai putin vandut produs
worst_selling = min(sales, key=sales.get)
print(f"c) Cel mai putin vândut produs: {worst_selling} ({sales[worst_selling]} unitati)")

# 4. d) Verificare si adaugare "Web camera"
if "Web camera" not in sales:
    sales["Web camera"] = 0
    print("d) Produsul 'Web camera' nu a fost gasit. A fost adaugat cu valoarea 0.")
else:
    print(f"d) Produsul 'Web camera' exista deja cu {sales['Web camera']} unitati.")

# 4. e) Cresterea unitatilor pentru "Monitor" cu 5
sales["Monitor"] += 5
print(f"e) Numărul de unitati pentru 'Monitor' a fost crescut cu 5. Noua valoare: {sales['Monitor']}")
print()

# 5. Afisarea dictionarului actualizat
print("Dictionarul sales actualizat:")
for product, quantity in sales.items():
    print(f"  {product}: {quantity}")
print()

# 6. Functie care creeaza o lista cu produsele cu vanzari critice 
def get_critical_products(sales_dict, threshold=50):
    """Returneaza o lista cu produsele care au vanzari sub pragul specificat"""
    critical_products = []
    for product, quantity in sales_dict.items():
        if quantity < threshold:
            critical_products.append(product)
    return critical_products

# Afisarea produselor critice
critical_products = get_critical_products(sales)
print(f"Produse cu vânzări critice (sub 50 unitati): {critical_products}")
print()

# 7. Validarea datelor din dictionar
print("Validarea datelor:")
if validate_sales_data(sales):
    print("Toate cantitatile sunt valide (niciuna negativa).")
print()