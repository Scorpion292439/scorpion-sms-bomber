# Scorpion SMS Bomber 🦂

![Scorpion Banner](https://via.placeholder.com/800x200/FF0000/FFFFFF?text=SCORPION+STRIKE)  
*(Not: Gerçek banner için bir GIF veya resim ekleyebilirsin, örneğin scorpion animasyonu.)*

## 🚀 Hızlı Başlangıç
**Scorpion SMS Bomber**, Termux'ta çalışan güçlü bir SMS test aracı. Kırmızı akrep gibi sessiz ve ölümcül vuruşlar yapar! ⚡  
Sadece **etik testler** ve **kendi cihazın** için kullan. Kötüye kullanım yasal sorunlar doğurur – **sorumlu ol!**

### Özellikler
- **Normal Mod**: Belirli sayıda SMS, aralıklı gönderim.
- **Turbo Mod**: Thread'lerle ultra hızlı bombardıman (Ctrl+C ile durdur).
- **Desteklenen Servisler**: 9+ API (Kahve Dünyası, BIM, Evidea, vb.).
- **Termux Optimizasyonu**: Renkli arayüz, banner ve emoji desteği.

## 📱 Termux Kurulumu (Android'de 5 Dakika!)
Termux'u Google Play'den indir ve aç. Sonra şu adımları izle:

1. **Paketleri Güncelle** (Temel hazırlık):
   pkg update && pkg upgrade -y
   
2. **Python ve Git Yükle**:
   pkg install python git -y
   
3. **Repoyu Klonla** (Bu repo'yu indir):
   git clone https://github.com/Scorpion292439/scorpion-sms-bomber.git
cd scorpion-sms-bomber

4. **Gerekli Kütüphaneleri Yükle**:
   pip install requests colorama
   
5. **Başlat ve Vur!** 🦂:
   python scorpion_sms.py
- Banner çıkacak, menü görünecek. 1 (Normal), 2 (Turbo) veya 3 (Çıkış) seç.

**İpucu**: İnternet bağlantın stabil olsun. İlk çalıştırmada izinleri ver (storage için `termux-setup-storage`).

## 🎮 Kullanım Kılavuzu
Program açılınca kırmızı SCORPION banner'ı göreceksin. Menü şöyle:

| Seçenek | Açıklama | Örnek Giriş |
|---------|----------|-------------|
| **1 - Normal Mod** | SMS'leri yavaşça gönder (dosya desteği var). | Numara: `5551234567`<br>SMS Adedi: `50`<br>Aralık: `2` saniye |
| **2 - Turbo Mod** | Hızlı thread'lerle saldırı! | Numara: `5551234567`<br>E-posta: Opsiyonel |
| **3 - Çıkış** | Güvenli ayrıl. | - |

- **Telefon Numarası**: +90 olmadan, 10 haneli (örn: 5551234567).
- **E-posta**: Bilmiyorsan boş bırak, rastgele oluşturulur.
- **Dosya Desteği**: Birden fazla numara için TXT dosya yükle (her satıra bir numara).

**Örnek Çıktı** (Başarılı vuruş):
🦂[STRIKE HIT] Target Down! 5551234567 --> api.kahvedunyasi.com

## ⚠️ Uyarılar ve Sorumluluk
- **Yasal Uyarı**: Bu araç **sadece kendi numaran** veya **izinli testler** için. Spam yasaları (örneğin KVKK, GDPR) ihlal eder – cezai sorumluluk sana ait!
- **Sorumlu Kullanım**: Rate limit'leri aşma, IP'n banlanmasın.
- **Sorun Giderme**:
  - Hata: `No module named 'requests'` → `pip install requests` tekrarla.
  - Renkler çıkmıyor: `export TERM=xterm-256color`.
  - Turbo donuyor: Ctrl+C bas.

## 🔧 Katkı ve Destek
- Yıldız ver ⭐, fork'la geliştir!
- Issue aç: Bug raporla veya yeni API ekle.
- Lisans: MIT (Serbest kullanım, ama kredi ver).

**Scorpion'un Zehriyle Vur!** 🦂💥  
*Powered by xAI's Grok – Hızlı, Akıllı, Tehlikeli.*  

---

*Son Güncelleme: 21 Kasım 2025*  
[GitHub Repo](https://github.com/Scorpion292439/scorpion-sms-bomber) | [Termux Docs](https://wiki.termux.com)
