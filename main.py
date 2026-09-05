import os
import json
import base64
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, firestore

# Secret üzerinden yetki alma
cred_json = os.environ.get("FIREBASE_CREDENTIALS")

if cred_json:
    cred_dict = json.loads(cred_json)
    cred = credentials.Certificate(cred_dict)
    
    # Firebase uygulamasını tekil olarak başlat
    if not firebase_admin._apps:
        firebase_admin.initialize_app(cred)
        
    db = firestore.client()
    
    # Profesyonel Fırsat Veri Yapısı (Zenginleştirilmiş Test Verisi)
    firsatlar = [
        {
            "title": "Xiaomi Robot Süpürge S10+",
            "price": "12.499 TL",
            "old_price": "15.999 TL",
            "discount_rate": "%22",
            "image_url": "https://picsum.photos/200/200?random=1",
            "category": "Teknoloji",
            "store": "Trendyol",
            "url": "https://www.trendyol.com",
            "created_at": datetime.now()
        },
        {
            "title": "Sony PlayStation 5 Slim 1TB",
            "price": "18.999 TL",
            "old_price": "21.500 TL",
            "discount_rate": "%12",
            "image_url": "https://picsum.photos/200/200?random=2",
            "category": "Teknoloji",
            "store": "Amazon",
            "url": "https://www.amazon.com.tr",
            "created_at": datetime.now()
        },
        {
            "title": "Philips Airfryer XXL Fritöz",
            "price": "4.250 TL",
            "old_price": "5.999 TL",
            "discount_rate": "%29",
            "image_url": "https://picsum.photos/200/200?random=3",
            "category": "Ev & Yaşam",
            "store": "Hepsiburada",
            "url": "https://www.hepsiburada.com",
            "created_at": datetime.now()
        }
    ]
    
    # Firestore veri yazma işlemi
    collection_ref = db.collection("firsatlar")
    for item in firsatlar:
        collection_ref.add(item)
        
    print("Zenginleştirilmiş veri yapısı başarıyla eklendi!")
else:
    print("FIREBASE_CREDENTIALS bulunamadı!")
