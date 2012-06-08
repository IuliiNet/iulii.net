# README

sorgenti e script generatrici del sito internet [iulii.net](http://iulii.net)

## dipendenze

* git
* python2+
* markdown

#### editing del sito internet

Il linguaggio di markup [markdown](http://daringfireball.net/projects/markdown/ "makdown syntax") semplifica la scrittura di documenti in formato testo, permettendo di evidenziare titoli, sottotitoli, links, elenchi, ecc.

Lo script python [minimalsite.py](https://github.com/lavish/minimalsite "minimalsite by lavish") permette di generare, a partire da una struttura a directories e files markodwn, un sito internet statico.

Una volta apportate le opportune modifiche a questi sorgenti, per generare le pagine html aggiornate è sufficiente eseguire il comando *make* all'interno della directory *iulii.net*. 

Per poter visualizzare le modifiche effettuate in formato html è necessario configurare localmente un server http che come cartella radice punti a */path/to/iulii.net*.

Successivamente per caricare le modifiche online è possibile aggiornare il repository e caricare il tutto online (git commit -am "update" ; git push).
