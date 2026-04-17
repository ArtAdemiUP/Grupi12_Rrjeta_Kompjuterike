# Grupi12_Rrjeta_Kompjuterike
# 📡 Rrjeta Kompjuterike – Projekt: Client-Server System (Python)

## 📌 Përshkrimi i projektit
Ky projekt implementon një sistem Client-Server duke përdorur Python sockets. Sistemi mundëson komunikim mes disa klientëve dhe një serveri qendror, ku serveri menaxhon kërkesat dhe kontrollon privilegjet e qasjes në file dhe foldera.

---

## ⚙️ Teknologjitë e përdorura
- Python 3
- Socket Programming
- Threading
- OS Module (File Handling)

---


## 🚀 Si të ekzekutohet projekti

### 1. Starto serverin
python server.py

Serveri fillon dhe dëgjon lidhjet nga klientët.

---

### 2. Starto klientin
python client.py

Klienti lidhet me serverin përmes IP dhe portit të caktuar.

---

## 🔐 Sistemi i privilegjeve

Serveri përdor username për të caktuar privilegjet:

- admin → READ, WRITE, EXEC (qasje e plotë)
- user1 → READ only
- user2 → READ only

---

## 💬 Komandat e klientit

### READ
Shfaq listën e file-ve në server.
READ

---

### WRITE
Krijon ose ndryshon file në server (vetëm admin).
WRITE filename.txt teksti

---

### EXEC
Ekzekuton komandë në server (vetëm admin).
EXEC dir   (Windows)
EXEC ls    (Linux)

---

### EXIT
Shkëput klientin nga serveri.
EXIT

---

## 🔄 Funksionaliteti i serverit

- Pranon shumë klientë (multi-client)
- Përdor threading për lidhje paralele
- Lexon dhe shfaq mesazhet nga klientët
- Kontrollon privilegjet e përdoruesve
- Menaxhon qasjen në file system

---

## 📂 File system
Të gjitha file-t ruhen në:
server_files/

Vetëm admin ka qasje të plotë në këtë folder.

---

## 🧪 Shembull përdorimi

### Admin:
READ
WRITE test.txt Hello
EXEC dir

### User:
READ
WRITE → nuk lejohet
EXEC → nuk lejohet

---

## 📌 Përfundim
Ky projekt demonstron komunikimin Client-Server në rrjeta kompjuterike, përdorimin e socket-eve, multi-client connection dhe sistemin e privilegjeve për qasje në resurse të serverit.
