# 🚀 DevOps İzleme ve Uyarı Sistemi – Flask, Prometheus, Alertmanager

Bu proje, bir Flask uygulamasının hata oranını izleyen ve belirli bir eşik aşıldığında otomatik olarak uyarı üreten bir **Monitoring & Alerting** altyapısı sunar. Prometheus, Alertmanager ve özel bir webhook ile uyarılar konsola iletilir.

## 📌 Amaç

- Prometheus ile Flask uygulamasından metrik toplamak
- Belirli bir hata oranında uyarı oluşturmak
- Alertmanager ile webhook üzerinden uyarıyı dış servise (Flask tabanlı `alert_receiver.py`) iletmek
- Gerçek zamanlı log takibiyle sistem sağlığını analiz etmek

---

## 🧱 Proje Bileşenleri

- `app.py` → Flask uygulaması (hata üretir ve `/metrics` endpoint'i sunar)
- `alert_receiver.py` → Prometheus Alertmanager'dan gelen uyarıları alır ve loglar
- `prometheus.yml` → Prometheus yapılandırma dosyası (scrape ayarları, uyarı kuralları dahil)
- `alertmanager.yml` → Alertmanager yapılandırması (webhook ayarı)
- `alert_rules.yml` → Uyarı kurallarını tanımlar (örneğin: 1 dakikada 1’den fazla hata)
- `docker-compose.yml` → Tüm bileşenleri Docker ile ayağa kaldırır
