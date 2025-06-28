from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# HTML dosyasının yolu
project_dir = os.path.abspath(".")
auth_path = "file://" + os.path.join(project_dir, "auth.html")  # dosya adını HTML'e göre ayarla

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

driver = webdriver.Chrome(options=options)



def register_user(username, password):
    driver.get(auth_path)
    time.sleep(1)
    

    driver.find_element(By.ID, "signUp").click()
    time.sleep(1)


    driver.find_element(By.ID, "regUsername").clear()
    driver.find_element(By.ID, "regPassword").clear()
    driver.find_element(By.ID, "regUsername").send_keys(username)
    driver.find_element(By.ID, "regPassword").send_keys(password)

    driver.find_element(By.CSS_SELECTOR, "#registerForm button[type='submit']").click()
    time.sleep(1)

def login_user(username, password):
    driver.get(auth_path)
    time.sleep(1)


    driver.find_element(By.ID, "loginUsername").clear()
    driver.find_element(By.ID, "loginPassword").clear()
    driver.find_element(By.ID, "loginUsername").send_keys(username)
    driver.find_element(By.ID, "loginPassword").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "#loginForm button[type='submit']").click()
    time.sleep(1)

    try:
        return driver.find_element(By.ID, "loginMessage").text
    except:
        return "Giriş mesajı alınamadı"


# === 1. Başarılı Senaryo: Doğru Kayıt ===
print(">> Test 1: Kullanıcı ve şifre ile kayıt")
register_user("kullanici1", "12345")
print(">> Test 1 Başarılı!")


# === 2. Başarısız Senaryo: Kayıtlı Kullanıcı Hatası ===y
print(">> Test 2: Kayıtlı kullanıcı ve şifre ile giriş")
register_user("kullanici1", "12345")
print(">> Test 2 Başarılı!: Kayıtlı kullanıcı tespit edildi.")

# === 3. Başarılı Senaryo: Doğru Giriş ===
print(">> Test 3: Doğru kullanıcı, doğru şifre")
message = login_user("kullanici1", "12345")
assert "başarılı" in message.lower()
print(">> Test 3 Başarılı: Başarılı giriş yapıldı.")

# === 4. Başarısız Senaryo: Yanlış Şifre ===
print(">> Test 4: Doğru kullanıcı, yanlış şifre")
message = login_user("kullanici1", "yanlis")
assert "hatalı" in message.lower()
print(">> Test 4 Başarılı: Hatalı giriş tespit edildi.")


driver.quit()
