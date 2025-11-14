# tp1_primalite_dataset.py

import random
import sympy

def save_list_to_file(numbers, filename):
    """Sauvegarde une liste de nombres dans un fichier texte."""
    with open(filename, "w") as f:
        for n in numbers:
            f.write(str(n) + "\n")

def prime_pool_up_to(max_n):
    """Renvoie une liste de tous les nombres premiers jusqu’à max_n."""
    return list(sympy.primerange(2, max_n))

def sample_primes_from_pool(pool, k):
    """Sélectionne aléatoirement k nombres premiers distincts depuis le pool."""
    if k > len(pool):
        raise ValueError("k est plus grand que la taille du pool")
    return random.sample(pool, k)
def is_prime(n):
    """Vérifie si un nombre est premier."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_pool_between(start, end):
    """Renvoie une liste de nombres premiers entre start et end."""
    primes = []
    for n in range(start, end + 1):
        if is_prime(n):
            primes.append(n)
    return primes


if __name__ == "__main__":
    # 1.Créer la grande liste de premiers
    #pool = prime_pool_up_to(2_000_000)  # plus grand pool
    #print("Nombre total de nombres premiers disponibles :", len(pool))

     #2.Sélectionner 100 nombres aléatoires parmi eux
    #random100 = sample_primes_from_pool(pool, 100)

    # 3.Sauvegarder dans un fichier
    #save_list_to_file(random100, "Random100.txt")
    #print("Fichier Random100.txt créé avec", len(random100), "nombres premiers.")
    # 4.Créer le jeu Random1000
    #pool_large = prime_pool_up_to(2_000_000)
    #random1000 = sample_primes_from_pool(pool_large, 1000)
    #save_list_to_file(random1000, "Random1000.txt")
    #print("Fichier Random1000.txt créé avec", len(random1000), "nombres premiers.")
    # 5.Créer le jeu Test-1
    #test1_pool = prime_pool_between(1000, 1_000_000)
    #random_test1 = sample_primes_from_pool(test1_pool, 100)
    #save_list_to_file(random_test1, "Test-1.txt")
    #print("Fichier Test-1.txt créé avec", len(random_test1), "nombres premiers entre 1000 et 1 000 000.")
    # =======================
#  Jeu de données : Test-2
# =======================



      #test2_primes = []  # liste principale qui contiendra tous les nombres premiers sélectionnés

      #for digits in range(3, 7):  # de 3 à 12 chiffres inclus
      #   start = 10 ** (digits - 1)
       #  end = (10 ** digits) - 1

        # print(f"Génération de nombres premiers à {digits} chiffres...")

    #     # Générer une liste de nombres premiers dans cet intervalle
         #prime_candidates = prime_pool_between(start, end)

    #     # Si la liste est vide ou trop courte, on évite les erreurs
         #if len(prime_candidates) < 10:
          #   print(f"Pas assez de nombres premiers à {digits} chiffres ({len(prime_candidates)} trouvés).")
           #  primes_sample = prime_candidates
         #else:
          #   primes_sample = random.sample(prime_candidates, 10)

    #     # Ajouter à la liste principale
         #test2_primes.extend(primes_sample)

    #     # Écriture du fichier Test-2.txt
         #with open("Test-2.txt", "w") as f:
          #   for p in test2_primes:
           #      f.write(str(p) + "\n")

         #print("Fichier Test-2.txt créé avec succès !")

    # =======================
#  Jeu de données : Test-3
# =======================

    test3_primes = []  # on stockera tous les nombres premiers ici
    digits_list = [3, 6, 9, 12]  # tailles demandées

    for digits in digits_list:
        start = 10 ** (digits - 1)
        end = (10 ** digits) - 1

        print(f"Génération de nombres premiers à {digits} chiffres...")

        prime_candidates = prime_pool_between(start, end)

        if len(prime_candidates) == 0:
            print(f"Aucun nombre premier trouvé à {digits} chiffres.")
            continue

        # On prend 10 nombres premiers au hasard (ou tous s’il y en a moins)
        sample_size = min(10, len(prime_candidates))
        primes_sample = random.sample(prime_candidates, sample_size)

        # On les ajoute à la liste principale
        test3_primes.extend(primes_sample)

    # Écriture du fichier Test-3.txt
    with open("Test-3.txt", "w") as f:
        for p in test3_primes:
            f.write(str(p) + "\n")

    print("Fichier Test-3.txt créé avec succès !")
