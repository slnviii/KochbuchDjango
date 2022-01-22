# KochbuchDjango
Kochbuch app für Python Kurs
https://miro.com/app/board/o9J_lmER22A=/  
Code Anleitung https://cloud.hs-augsburg.de/s/FSPxopKBnfXp3FS
Standardpasswort für alle User: !abcd1234

## "Wie kriege ich dieses Repository das erste mal in mein Pycharm?"  
-> Pycharm Clone Funktion  
How to clone:  
-Install Pycharm  
-VCS oben in Leiste -> Github installieren (Enable Version Control Integration dann siehe #1 auf Bild unten "Checkout from Version Control: Github) Git installation zulassen von pycharm (braucht windows admin zustimmung)  
-File -> Settings -> Version Control -> Add Account: github account(über Passwort auth)  
Jetzt sollte auch in der Menüleiste nicht mehr VCS stehen sondern Git  
-Git oben in Leiste -> Clone...(#2 auf bild) -> https://github.com/Mbl07/KochBuch.git Jetzt sollte eine lokale Kopie vom aktuellen Github Repo erstellt worden sein  
![alt text](https://cloud.hs-augsburg.de/s/8Z8YA9JSsJW9AC2/preview)  
  
  
  


_______________________________________________________________________________________________
# Github in Pycharm allgemein:  

## **!!!NIE AUF MASTER PUSHEN OHNE GRUPPENABSPRACHE!!!**
## **!!!NIE REMOTE/ORIGIN BRANCHES LÖSCHEN!!!** 
Repository/Repo = beinhaltet all unsere branches auf github  
Branch = Verzeichnis einfach gesagt   
Commit = branch änderungen lokal speichern  
Pull/Update = aktuelle branch code/dateien von github ziehen  
Push = branch änderungen auf github hochladen  

**Pycharm Allgemein**  
![alt text](https://cloud.hs-augsburg.de/s/i45c6Bxr7Cy9TDF/preview)  
#1 Git Konsole, hier mit rechtsklick auf lokale branches updaten/pushen/neuer branch etc  
#2 ganz rechts unten sieht man auf welchem branch man gerade arbeitet, direkt darüber kann man auch den Event-Log anschalten (sehr nützlich um zB gelöschte branches wiederherzustellen, Beispiele siehe unterstrichen)  
#3 zwischen Projektdateien und Commitfenster wechseln  
#4 Git-Log: was wurde wo/wann gepushed/geupdatet von unserem Github 
  
  
  
  

## Empfohlene Vorgehensweise für bearbeiten unseres Repos: 
![alt text](https://cloud.hs-augsburg.de/s/3YrWFNWbwt2qgME/preview)
**#0** Nie Remote updaten/löschen etc, immer in lokal arbeiten und dann pushen(s. später)  
**#1 CHECKOUT**  bei Lokalen Branches unseren dev branch auswählen mit "checkout" falls er noch nicht ausgewählt ist  
**#2 UPDATE**   dev branch updaten (entweder mit rechtsklick oder mit toolbar oben rechts) // Sichergehen rechts unten in pycharm, dass "dev" auch der aktuelle/ausgewählte branch ist  
Pycharm holt sich nun den aktuellen Code unseres "dev" Verzeichnis aus github und aktualisiert die offenen Fenster damit  
**#3 NEW TEST BRANCH**   optional aber empfohlen: dev rechtsklicken und neuen branch daraus erstellen, beliebig benennen. Dieser neue branch sollte jetzt das aktuelle verzeichnis sein  
"Warum erstellt man sich lokal einen test-branch?" es kann später zu einem Versionskonflikt kommen und so hat man einfach ein backup seines codes  

**#4 (kein Bild) Code/Dateien beliebig bearbeiten auf diesem branch, was eben gerade ansteht**  
**#5 COMMIT**  Fertig? Zeit für Commit entweder unter "Project" links oben oder rechts oben in Git toolbar  
**#6** Haken reinsetzen bei den Änderungen, dann eine Nachricht einfügen, was man geändert(optional aber hilfreich für andere), dann Commit klicken  
Nach dem Commit sind die änderungen nun lokal auf deinem branch gespeichert, aber noch nicht auf unserem Github oder deinen lokalen übergeordneten branches wie dev und master  
**#7 MERGE** Nun den "dev" branch auswählen als aktiv(rechtsklick checkout), und dann rechtsklick auf den branch den man gerade bearbeitet hat (test hier) und "merge selected branch into current"  
Dies fügt die Änderungen des temporären branches "test" auf den lokalen "dev" branch  
![alt text](https://cloud.hs-augsburg.de/s/CFngYP64dtEgcQC/preview)
Nun sollte eigentlich alles passen und man den lokalen dev branch mit seinen Änderungen auf unser github hochladen und den remote dev branch so aktualisieren  
Es kann jetzt jedoch vorkommen, dass jemand während ihr an einer Datei lokal gearbeitet habt, diese Datei auch bei sich bearbeitet hat  
Beispiel: ihr beide habt unseren Dev Branch Version 1.9 von unserem github geladen, und ihr beide habt die datei index.html bearbeitet  
Nun ist Person#1 vor dir fertig und lädt seine änderungen hoch und damit ist der dev branch nun eine Version weiter  
wenn du nun deine änderungen hochladen willst, akzeptiert github dies nicht, da die aktuelle github dev branch version nicht der vorgänger deiner Version ist  
es kommt also zu einem Konflikt  
**DESHALB -->**  
Nachdem man #7 gemacht hat sollte man seinen lokalen dev branch einfach nochmal updaten(rechtsklick)... wenn jemand ihn derweilen editiert hat online wird pycharm sich melden und dir mitteilen, dass es einen Konflikt gibt und fragt dich ob es 1) deine Änderungen behalten soll im lokalen dev branch oder 2) sie durch die neue version ersetzen soll  
lässt man seine Änderungen ersetzen ist nun der eigene Code offensichtlich weg auf lokalem dev branch, zum Glück hat man aber noch seinen "test"branch auf dem noch alles gespeichert ist  
**Was machen, wenn Konflikt besteht?**  
Entweder, man löst diesen Konflikt, indem man den neuen Code akzeptiert (Accept theirs) und dann wieder zurück zu #4 geht und dann seine Änderungen so einfügt(eigener Code ist ja noch im test branch, also einfach mit checkout zwischen beiden hin und herwechseln und copy pasten), dass sie die anderen Änderungen nicht zerstören **ODER**  

Ganz einfach, die anderen fragen, was wir machen bzgl. diesem Konflikt! Welche Änderungen wir übernehmen oder eventuell einfach beide Änderungen mit reinnehmen(die Option gibt es bei pycharm auch noch, nennt sich "merge")  
**Nicht machen:** Änderungen von anderen grundlos überschreiben ohne bescheid zu geben  

### Zu diesen Konflikten kommt es nur wenn 2 Personen denselben Code in derselben Datei im selben branch gleichzeitig bearbeiten  
es entstehen keine Konflikte wenn jetzt Person#1 zB index.html bearbeitet und hochlädt und den dev branch aktualisiert WÄHREND Person#2 im dev branch account.html bearbeitet und dann seine Änderungen hochläd, hier wird Github trotzdem einfach die änderungen von #2 in die neuere dev version von #1 mergen weil es keine Konflikte gibt bzw an unterschiedlichen Dateien gearbeitet wurde  

Und nun nach dem ganzen Text: wie lade ich überhaupt meine Änderungen hoch nachdem es nun keine Konflikte nach dem erneuten update gab?  

**#8 PUSH**: Rechtsklick auf den lokalen dev branch und "push", es öffnet sich ein Fenster wo man nochmal den commit sieht der hochgeladen wird --> auf PUSH klicken  
(pycharm zeigt auch einen kleinen grünen Pfeil neben branches an bei denen der PUSH noch nicht gemacht wurde)  
**der test branch muss nicht gepushed werden, das würde nur einen test branch in unserem github mit dieser version erstellen(nicht schlimm)  
nachdem man den lokalen dev branch erfolgreich gepushed hat kann man den lokalen test branch auch einfach wieder löschen (siehe letztes Bild), und für die nächsten Änderungen wieder neu erstellen mit der neusten Dev branch version, also einfach zurück zu #1**
