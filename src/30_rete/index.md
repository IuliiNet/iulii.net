### La rete

Questa sezione si prefigge l'obiettivo di descrivere, anche entrando in dettagli piuttosto tecnici, la struttura della rete iulii.net e delle [reti mesh](http://it.wikipedia.org/wiki/Wireless_mesh_network "wireless mesh network su wikipedia") basate su [batman-adv](http://www.open-mesh.org/wiki/batman-adv/ "batman-adv homepage") in generale. 

Sono presenti inoltre esempi di condifurazioni di nodi con distribuzione [openwrt](http://openwrt.org "openwrt").

Sono disponibili degli approfondimenti su  [batman-adv](batman-adv.html "approfondimento a batman-adv").

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
