### sviluppo della documentazione

Lo sviluppo di una buona documentazione, non solo questo sito internet, è un passo fondamentale per facilitare la diffusione della rete.

In particolare i sorgenti del progetto iulii.net, ed in particolare del sito internet, sono disponibili via repositories git agli indirizzi:

* [https://github.com/iuliinet/iulii.net](https://github.com/iuliinet/iulii.net "iulii.net su github");
* [git://git.iulii.net/iulii.net.git](git://git.iulii.net/iulii.net.git ""iulii.net su redo.iulii.net"").

La scelta di git per mantenere i sorgenti del progetto è dettata dal fatto che è un ottimo servizio, permette inoltre sia l'editing online (su github) che offline, oltre ad un backup decentralizzato.

#### organizzazione del repository

Le directory del repository del progetto sono così organizzate:

* [**configs**](https://github.com/iuliinet/iulii.net/tree/master/configs "iulii.net configs backup") backup delle configurazioni dei nodi;
* [**site**](https://github.com/iuliinet/iulii.net/tree/master/site "iulii.net sources site") questo sito internet;
	* **src** sorgenti [markdown](http://daringfireball.net/projects/markdown/syntax "homepage markdown");
	* **css** fogli di stile;
	* **img** immagini;

#### editing 

Per contribuire allo sviluppo della documentazione e dei firmware è consigliabile:

* installazione del client [git](http://git-scm.com "git client").
* iscrizione al sito [http://github.com](http://github.com "github");
* comunicazione all'indirizzo email [info@iulii.net](mailto:info.iulii.net "info") dell'intenzione, avendo cura di specificare il la chiave pubblica ssh ed il nickname registrato su github;
* attendere conferma da un amministratore;

##### offline

Per chi ha dimestichezza con git su ambiente unix questi sono i passi da seguire:

* git clone git://github.com/iuliinet/iulii.net.git;
* cd iulii.net;
* (editing);
* git add . ; git commit -a;
* git push

##### online

Gli utenti che hanno ottenuto l'autorizzazione alla modifica del repository nella versione online, dopo essersi loggati su github con le loro credenziali, possono semplicemente procedere all'editing direttamente dall'interfaccia di github.

#### editing del sito internet

Come indicato sopra, nella directory *site* è presente questo sito internet. In particolare nella directory *site/src* sono presenti i sorgenti [markdown](http://daringfireball.net/projects/markdown/ "makdown syntax"). 

Il linguaggio di markup markdown semplifica la scrittura di documenti in formato testo, permettendo di evidenziare titoli, sottotitoli, links, elenchi, ecc.

Lo script python [minimalsite.py](https://github.com/lavish/minimalsite "minimalsite by lavish") permette di generare, a partire da una struttura a directories e files markodwn, un sito internet statico.

Una volta apportate le opportune modifiche a questi sorgenti, per generare le pagine html aggiornate è sufficiente eseguire il comando *make* all'interno della directory *site*. 

Per poter visualizzare le modifiche effettuate in formato html è necessario configurare localmente un server http che come cartella radice punti a */path/to/iulii.net*.

Successivamente per caricare le modifiche online è possibile aggiornare il repository e caricare il tutto online (git commit -am "update" ; git push).
