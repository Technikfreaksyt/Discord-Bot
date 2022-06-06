# Discord-Bot
Ich zeige dir, wie du deinen eigenen Discord Bot ganz einfach erstellen kannst. 
Als erstes musst du dir eine App unter : https://discord.com/developers/applications erstellen.
Danach gehst du auf den Punkt Bot und erstellst einen.
Dort wird etwas von einem Token stehen, den musst du unbedingt aufbeahren, erstelle dir dafür am besten eine Textdatei und sichere sie, du kannst den Token zwar zurrücksetzen, aber dann musst du den Token austauschen. 

Jetzt musst du dir Discord-py installieren: 

# Discord py:
MAC OS:
python3 -m pip install -U discord.py
Windows:
py -3 -m pip install -U discord.py

Jetzt musst du in den Benutzereinstellungen in Discord unter erweitert den Entwicklermodus aktivieren.

# Discord-Bot #2
Jetzt installierst du dir VS-Code: https://code.visualstudio.com/download mit dem Python Addon, welches du im VS-Code Addon Store findest.
Jetzt installierst du dir das Programm Python : https://code.visualstudio.com/download


# Einrichten vom Skript
Wenn du dir das Skript dann heruntergeladen und in VS-Code geöffnet hast, wirst in "Zeile 10" sehen "activity = discord.Game(name="KI", type=1)" 
Das KI kannst z.B durch den Namen des Bots, oder ein beliebiges Wort ersetzen.
In "Zeile 11" wirstdu das sehen "await client.change_presence(status=discord.Status.online, activity=activity)" , das online kannst du durch online,idle,do_not_disturb oder invisble ersetzen.

In "Zeile 23,24" kannst du sehen "if message.content.startswith('hello'): await message.channel.send('Hello!')" das erste Hello ist ein Befehl, den könnt ihr beliebig verändern, der Teil wo das zweite Hello ist das, was passiert wenn z.B hello geschrieben wird.

Auf dem Skript könnt ihr eueren Bot aufbauen.

# Wilkommensbildschirm
Als erstes muss man die Autoroles konfigurieren ( Skript ist im Ordner Funktionen mit dem namen welcome), Die ID vom Server ist nicht mit Klammern versehen.

Der Rest steht im Skript, die Kommentierungen bitte einfach mit den richtigen Daten austauschen. 

# Supportkanal
Das Skript findest du im Ordner Funktionen und heißt: support
Die Funtkion support kanal musst mit bei der Funktion vom "if message.content.startswith('hello')" einbauen, den den Blcok mit hello kopierst du eifach und guckst, ob eer richtig eingerückt ist.
Der Befehl kann z.B sein /help,//help,!help,?help,/support,.... , der Befehl kann so sein, wie du willst
Jetzt pass gut auf!!!
Unter dem Teil wos steht,das der Channel erstellt wird, ist einmal das :  await channel.set_permissions(message.author,send_messages=True,read_message_history=True,read_messages=True) und einmal das: 
await channel.set_permissions(discord.utils.get(message.author.guild.roles, id = #ID der Rolle ),send_messages=False,read_messages = False,read_message_history=False) 
Das erste muss unbedingt bleiben, sonst kann der Autor seinen eigenen Knal nicht sehen.
Das zweite sagt welche Rolle was darf, bei meinem Bot ist es so: dei Mitglied Rolle kann den Kanal nicht sehen, außer es ist ihr eigener Support Kanal.
Du kannst den Zweiten Teil beliebig einfügen, und für jede Rolle alles Passend konfigurieren.
False heißt dabei: Man darf es nicht , True heißt: man darf es.

# Sprachkanal
der Code ist im Ordnmer Funktionen mit dem Namen Voice.
Den Befehl kannst du so ändern , wie er für dich sein soll, z.B !voice, ?voice, /voice,.....
Der Code wird so wie das hello eingerückt, also das if , muss in der Spalte vom hello sein.




# Hosten vom Bot
Ihr könnt euern Bot z.B be replit hosten, wer den Bot aber bei sich Zuhause hosten möchte, kann ein Raspberry Pi mit dem Rapberry Pi Os nehmen, dann könnt ihr per VNC Connect einen Remote-Zugriff darauf einrichten , wo ihr auch den vollständigen Desktop vom Pi sehen könnt.
Alle Libarys die das Bot-Skript braucht, müsst ihr auch auf dem Pi installieren.
Discord-py müsst ihr auf dem Pi installieren, sonst geht gar nichts, die restlichen Liabrys die ihr euch nachinstalliert habt, welche auch vom Skript genutzt werden, müssen dann halt auch auf dem Pi installiert werden.



# Links
Discord Python bei GitHub: https://github.com/Rapptz/discord.py
                                  

