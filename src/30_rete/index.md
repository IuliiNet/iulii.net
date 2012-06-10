### La rete

Questa sezione si prefigge l'obiettivo di descrivere, anche entrando in dettagli piuttosto tecnici, la struttura della rete iulii.net e delle [reti mesh](http://it.wikipedia.org/wiki/Wireless_mesh_network "wireless mesh network su wikipedia") basate su [batman-adv](http://www.open-mesh.org/wiki/batman-adv/ "batman-adv homepage") in generale. 

Sono presenti inoltre esempi di configurazioni di nodi con [openwrt](http://openwrt.org "openwrt") e [gentoo](http://gentoo.org "gentoo homepage");

#### introduzione a batman-adv

Batman-adv è un protocollo di routing per reti mesh, ottimizzato per l’utilizzo su reti  wireless. Il tipico scenario in cui questo protocollo viene utilizzato è una rete wireless adhoc multi-hop.

E' un protocollo su layer2, cioè instaura comunicazione con gli altri nodi della rete senza utilizzare i comuni indirizzi ip (che sono sul layer3).

Quello che sarà necessario indicare a batman-adv sono i device da utilizzare per la mesh, e se il nodo in questione deve funzionare da nodo gateway per internet o da nodo clients. Fatto questo, batman-adv creerà una nuova interfaccia (nel caso bat0) sulla quale si potrà lavorare sul layer3.

Grazie a tutte le bat0 di ogni device viene quindi a crearsi una struttura di nodi simile ad "un grande switch". Quindi ad ogni bat0 (o al bridge al quale appartiene)sarà possibile assegnare i suoi ip. Quindi ogni device batman-adv riuscirà a vedere, attraverso i suoi vicini, tutti gli altri nodi della rete.

Un primo aspetto molto interessante di questo approccio alla rete (che tra l'altro forniscono anche altri protocolli di routing come oslr, ed è quindi una caratteristica intrinseca delle reti mesh) è la creazione di una struttura a maglia, nella quale ogni nodo riesce a comunicare direttamente (single-hop) con un alto numero di nodi vicini. Si capisce che in questo modo, la caduta di un singolo nodo non pregiudica il collegamento di altri nodi, che infatti saranno in grado di trovare la strada per le loro comunicazioni attraverso gli altri vicini attivi.

In maniera complementare, l'aggiunta di un altro nodo alla rete mesh sarà automaticamente riconosciuta da tutti i suoi vicini, e quindi da tutti i nodi della rete mesh, contribuendo in questo modo alla crescita della rete.

#### introduzione ai nodi

I nodi delle rete sono dei dispositivi (comumemente router wireless radio con installata la distribuzione openwrt) che comunicano tra loro e *sorreggono la comunicazioni all'interno della rete*.

Il progetto iulii.net basa il collegamento dei nodi sul layer2 sul protocollo batman-adv. Sul layer3 si utilizza il protocollo ipv6, scelto per la semplicità di assegnazione degli indirizzi e la facilitazione nell'evitare conflitti ip. 

Normalmente gli indirizzi ipv6 dei nodi sono assegnati staticamente in base al macaddress. Ai **nodi della rete può essere assegnata la sottorete ipv6 2001:470:7023:1::/64**.

I nodi della rete possono comunicare tra loro su una rete wireless configurata in adhoc mode sull'essid **www.ninux.org-www.iulii.net-mesh**, oltre che via ethernet e tunnel vpn.

Su alcuni nodi della rete è presente un router advertisement (ra) daemon (come ad esempio [radvd](http://www.litech.org/radvd/ "homepage di radvd") o [dnsmasq](http://www.thekelleys.org.uk/dnsmasq/doc.html "homepage di dnsmasq")) per gestire in maniera automatica l'assegnazione degli indirizzi e del routing ipv6 nella sottorete dei clients.

Sono disponibili degli esempi sulla [configurazione dei nodi](nodi/ "configurazione dei nodi").

#### introduzione ai clients

Per i clients, cioè i dispositivi personali (pc, notebook, smartphone, tablet, router, ...), gli accessi possibili per entrare nella rete del progetto iulii.net sono:

* **wireless**, essid: **www.ninux.org-www.iulii.net-ap** in modalità ap;
* **ethernet**, collegamento via cavo;
* **vpn**, connessione via [tunnel vpn](http://wiki.ninux.org/TincVPN "collegarsi a ninux con una vpn"), questo metodo è anche utilizzato per collegare tra loro delle isole della rete.

Sui clients deve essere attivo il supporto ipv6. Per la gestione automatica degli indirizzi ipv6 si consiglia:

* [ndisc](http://www.remlab.net/ndisc6/ "ndisc") per SO unix like;
* Microsoft Windows Vista+;

Ad esempio, **la sottorete ipv6 2001:470:7023:2::/64 può essere assegnata ai clients**.

Non è escluso che su alcuni nodi sia presente un server dhcp per la gestione degli indirizzi ipv4.

#### servizi 

E' disponibile un elenco (incompleto) dei [servizi accessibili](servizi.html "servizi") dalla rete del progetto.
