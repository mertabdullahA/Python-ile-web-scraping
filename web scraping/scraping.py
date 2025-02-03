import requests
from bs4 import BeautifulSoup

def laptop_ozelliklerini_getir(url):
    try:
        response=requests.get(url)
        response.raise_for_status() 

        soup=BeautifulSoup(response.text, "html.parser")
        
        ozellikler=soup.find('div', class_='product-list__content product-detail-big-price')
        
        if not ozellikler:
            print("Laptop özellikleri bulunamadı. Farklı bir URL deneyin.")
            return
        
        print("Laptop Özellikleri:")
        for özellik in ozellikler:
            print(özellik.get_text(strip=True))
            
    except requests.exceptions.RequestException as e:
        print(f"Bir hata oluştu: {e}")
        

# Kullanıcıdan URL alma
kullanici_url =input("Laptop özelliklerini görmek istediğiniz URL'yi giriniz:")
laptop_ozelliklerini_getir(kullanici_url)
            
