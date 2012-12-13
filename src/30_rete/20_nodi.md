### elementi della rete

Di seguito un'introduzione agli elementi della rete.

#### nodi

I nodi sono dei dispositivi (comunemente router wireless radio con openwrt) che comunicano tra loro e *sorreggono la comunicazioni all'interno della rete*.

I nodi della rete si possono interfacciare via:

* **wireless**, essid: **IuliiNet-mesh** in modalità adhoc;
* **ethernet**, via cavo;
* **vpn**, connessione via [tunnel vpn](http://wiki.ninux.org/TincVPN "collegarsi a ninux con una vpn"). Questo metodo è utilizzato anche per collegare diverse isole della rete.

Esempi di configurazione di nodi sono disponibili nel repository [https://github.com/iuliinet/devices](https://github.com/iuliinet/devices).

##### tipi di nodi

Una suddivisione dei tipi di nodi che è possibile installare e configurare è la seguente:

* **hotspot** è questo il tipo di nodo probabilmente più semplice da installare e configurare. Prevede un accesspoint aperto con il nome della rete iulii.net-ap, dove ognuno ha la possibilità di accedere ai servizi che il propietario del nodo decide di rendere disponibili;
* **foglia** questo è un tipo di nodo normalmente connesso direttamente ad un solo altro nodo di tipo foglia, o più comunemente ad un nodo di backbone. Generalmente questo è anche un nodo hotspot;
* **backbone** questo genere di nodi è fondamentale per l'infrastruttura della rete in quanto generalmente mette in comunicazione diretta, oltre che diversi nodi foglia, almeno un altro nodo backbone; molto spesso questo tipo di nodi è fondamentale per il collegamento di segmenti della rete.
 
#### clients
   
Sono i dispositivi personali (pc, notebook, smartphone, tablet, router, ...), per questi gli accessi possibili per entrare nella rete del progetto iulii.net sono:

* **wireless**, essid: **IuliiNet-ap** in modalità ap;
* **ethernet**, collegamento via cavo;
* **vpn**, connessione via [tunnel vpn](http://wiki.ninux.org/TincVPN "collegarsi a ninux con una vpn").

#### isole

L'insieme dei nodi e dei client che possono comunicare tra loro forma un'isola di rete. Usualmente ad un'isola di rete è assegnata la stessa classe di indirizzi ip.

Diverse isole di rete possono interfacciarsi tra loro con connessioni vpn.
