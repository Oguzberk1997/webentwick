# Code Reminduz

Willkommen bei Code Reminduz!

Unser Fokus liegt auf der Konzeption und Planung von Musterveranstaltungen. Dazu gehören Hochzeiten, Verlobungsfeiern und Geburtstage, die über unsere Website geplant und durchgeführt werden können. Für diese drei Arten von Veranstaltungen haben wir zunächst Beispielvorlagen erstellt, die auf der Website angezeigt werden. Diese Vorlagen können dann entsprechend den individuellen Kundenpräferenzen angepasst werden. Es ist wichtig, die zentralen Aspekte der Feier zu berücksichtigen, und der Veranstaltungsort spielt eine entscheidende Rolle, da Elemente wie Catering, DJs, Fotografen und die Location eng damit verbunden sind. Wenn es sich zum Beispiel um die Planung einer Hochzeitsfeier handelt, werden die wesentlichen Anforderungen und Standards einer Hochzeit veranschaulicht.

Wir freuen uns darauf, dich bei der Gestaltung und Umsetzung deiner Traumveranstaltung zu unterstützen!

## Einrichtungshilfe

Um das Projekt auf deinem lokalen Rechner einzurichten, folge diesen Schritten:

1. Klone das Repository:

   ```bash
   git clone https://github.com/Oguzberk1997/webentwick
   ```

2. Installiere die erforderlichen Python-Pakete:

   ```bash
   pip install -r requirements.txt
   ```

3. Initialisiere die Datenbank:

   ```bash
   flask init-db
   ```

4. Füge Beispieldaten für Tests ein:

   ```bash
   flask insert-sample-data
   ```

5. Starte den Flask-Server:
   ```bash
   flask run
   ```

Wenn du während der Entwicklung die Live-Neuladung für die Frontend-Oberfläche aktivieren möchtest, befolge diese zusätzlichen Schritte:

1. Installiere die Node.js-Abhängigkeiten:

   ```bash
   npm install
   ```

2. Starte den Entwicklungsserver mit Live-Neuladung:
   ```bash
   npx run dev
   ```

## Test Login-Daten

Benutzer: `benutzer@example.com`
Passwort:`passwort123`

## Entwicklung

Implementierungsstatus:

- [x] Anmeldung
- [x] Registrierung
- [x] Veranstaltungen erstellen
- [x] Zugriff auf Veranstaltungen
- [x] Veranstaltung anzeigen
- [x] Veranstaltung löschen
- [x] Nachrichtenübermittlung über Toast (funktioniert prima)
- [x] Mini-JSON-API für die Abruf von Veranstaltungen in 1 Minute
- [ ] Veranstaltung bearbeiten
- [ ] Veranstaltung teilen
- [ ] Benachrichtigungen für bevorstehende Veranstaltungen

### Highlights des Frontend-Designs

Anstatt Bootstrap-Flask haben wir uns für die Verwendung von Tailwind CSS mit Flowbite entschieden. Diese Wahl wurde getroffen, um die modernen und anpassbaren Designkomponenten von Tailwind CSS zu nutzen. Flowbite erleichtert den Entwicklungsprozess, indem es vorgefertigte Komponenten bietet, die nahtlos in Tailwind CSS integriert werden und so zu einer noch polierteren Benutzeroberfläche führen.

### Highlights des Backend-Designs

Wir haben bcrypt zur Passworthash-Erstellung anstelle von Standard-Hashing-Methoden verwendet. Diese Entscheidung wurde getroffen, um die Sicherheit zu erhöhen, indem ein robustes Passworthashing-Verfahren integriert wird, das Salz und mehrere Hashing-Runden verwendet. Bcrypt ist allgemein anerkannt für seine Effektivität, Benutzerpasswörter vor verschiedenen Arten von Angriffen wie Brute-Force- und Regenbogentabellen-Angriffen zu schützen.

### Herausforderungen

- Die Integration der Live-Neuladefunktion für das Frontend bei gleichzeitiger Sicherstellung der Kompatibilität mit dem Backend stellte eine bedeutende Herausforderung dar. Dies erforderte eine sorgfältige Konfiguration und Koordination der Entwicklungsumgebungen.

- Die Implementierung der Funktion zur Bearbeitung von Veranstaltungen erwies sich aufgrund der Notwendigkeit, verschiedene Aspekte der Veranstaltung zu behandeln, wie Datumänderungen, Gästeliste-Modifikationen und mehr, als komplexer als erwartet.

## Zukünftige Erweiterungen

- **Veranstaltung bearbeiten**: Benutzern die Möglichkeit geben, Veranstaltungsdetails nach der Erstellung zu bearbeiten, um eine nahtlose Aktualisierung der Veranstaltungsinformationen zu ermöglichen.

- **Veranstaltung teilen**: Die Möglichkeit implementieren, Veranstaltungsdetails mit anderen zu teilen, um eine einfache Zusammenarbeit und Abstimmung unter den Veranstaltungsteilnehmern zu ermöglichen.

- **Benachrichtigungen**: Ein Benachrichtigungssystem entwickeln, das anstehende Veranstaltungen erinnert, um die Benutzerbindung und die Teilnahme an Veranstaltungen zu erhöhen.

## Kontaktinformation

- [Oguzberk Ökem](mailto:oguzberk-oekem@outlook.de)

## Lizenz

Dieses Projekt ist unter der [MIT-Lizenz](LICENSE) lizenziert.
