import os
import json
import firebase_admin
from firebase_admin import credentials, firestore

# GitHub Secret'tan Firebase anahtarını al
firebase_keys = os.environ.get("FIREBASE_CREDENTIALS")

if not firebase_keys:
    raise ValueError("FIREBASE_CREDENTIALS secret'ı bulunamadı!")

# Firebase'i başlat
cred_dict = json.loads(firebase_keys)
cred = credentials.Certificate(cred_dict)
firebase_admin.initialize_app(cred)

db = firestore.client()

# Botun veritabanına ekleyeceği fırsatlar
yeni_firsatlar = [
    {
        "urun_adi": "🤖 Robot Süpürge %30 İndirim",
        "fiyat": "4899",
        "link": "https://www.google.com"
    },
    {
        "urun_adi": "🎮 Oyun Konsolu Fırsatı",
        "fiyat": "12500",
        "link": "https://www.google.com"
    }
]

# Firestore 'firsatlar' koleksiyonuna verileri yaz
for firsat in yeni_firsatlar:
    db.collection("firsatlar").add(firsat)
    print(f"Eklendi: {firsat['urun_adi']}")

print("Tüm fırsatlar başarıyla veritabanına aktarıldı!")
