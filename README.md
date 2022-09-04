# Busylight
Ein Dienst zum Setzen und Anpassen der Farbe des Kuando Busylight Omega-Modell

## Funktionen
- Setzen der Farbe des Kuando Busylight
- Anpassen der Farbe des Kuando Busylight

## Abhänigkeiten
- `python3`
- `python3-hid`

## Installation
#### Debian 11
```sh
echo 'deb http://download.opensuse.org/repositories/home:/it-und-entwicklung-fg:/busylight/Debian_11/ /' | sudo tee /etc/apt/sources.list.d/home:it-und-entwicklung-fg:busylight.list
curl -fsSL https://download.opensuse.org/repositories/home:it-und-entwicklung-fg:busylight/Debian_11/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/home_it-und-entwicklung-fg_busylight.gpg > /dev/null
sudo apt update
sudo apt install busylight
```
#### Debian 10
```sh
echo 'deb http://download.opensuse.org/repositories/home:/it-und-entwicklung-fg:/busylight/Debian_10/ /' | sudo tee /etc/apt/sources.list.d/home:it-und-entwicklung-fg:busylight.list
curl -fsSL https://download.opensuse.org/repositories/home:it-und-entwicklung-fg:busylight/Debian_10/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/home_it-und-entwicklung-fg_busylight.gpg > /dev/null
sudo apt update
sudo apt install busylight
```
#### Ubuntu 22.4
```sh
echo 'deb http://download.opensuse.org/repositories/home:/it-und-entwicklung-fg:/busylight/xUbuntu_22.04/ /' | sudo tee /etc/apt/sources.list.d/home:it-und-entwicklung-fg:busylight.list
curl -fsSL https://download.opensuse.org/repositories/home:it-und-entwicklung-fg:busylight/xUbuntu_22.04/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/home_it-und-entwicklung-fg_busylight.gpg > /dev/null
sudo apt update
sudo apt install busylight
```
#### Ubuntu 20.4
```sh
echo 'deb http://download.opensuse.org/repositories/home:/it-und-entwicklung-fg:/busylight/xUbuntu_20.04/ /' | sudo tee /etc/apt/sources.list.d/home:it-und-entwicklung-fg:busylight.list
curl -fsSL https://download.opensuse.org/repositories/home:it-und-entwicklung-fg:busylight/xUbuntu_20.04/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/home_it-und-entwicklung-fg_busylight.gpg > /dev/null
sudo apt update
sudo apt install busylight
```

## Verwendung
Die gewünschte Farbe kann in der Config-Datei (unter `/var/local/busylight/color.conf`)eingetragen werden

## Weiterentwicklung
Gerne kann dieses Projekt weiterentwicklelt werden oder auch Vorschläge für zusätzliche Funktionen an mich gesendet werden.

## Lizenz und Verwendung
Diese Projekt wird unter GPLv3 bereitgestellt.
