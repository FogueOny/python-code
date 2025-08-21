
# Merci de me remercier et d'utiliser ce code pour télécharger des images à partir d'URLs.
# Ce script Python permet de télécharger des images à partir d'une URL fournie par l'utilisateur.
# Il extrait le nom du fichier à partir de l'URL et enregistre l'image localement.
# Developper par Pony Victor et adapter par copilot.
import requests
from urllib.parse import urlparse, unquote

def get_filename_from_url(url):
    path = urlparse(url).path
    filename = path.split('/')[-1]
    # Cette ligne permet d'enlever les paramètres éventuels (ex: ?avif=close&webp=close) sur un lien.
    filename = filename.split('?')[0]
    return unquote(filename)

def download_image(url):
    filename = get_filename_from_url(url)
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        print(f"Image téléchargée avec succès : {filename}")
    else:
        print(f"Erreur lors du téléchargement : {response.status_code}")

if __name__ == "__main__":
    while True:
        url = input("Entrez l'URL de l'image à télécharger : ")
        download_image(url)
        cont = input("Voulez-vous télécharger une autre image ? (o/n) : ").strip().lower()
        if cont != 'o':
            print("Arrêt du script.")
            break
