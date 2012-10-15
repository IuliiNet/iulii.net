### elementi della rete

Di seguito un'introduzione agli elementi della rete.

#### i nodi

I nodi sono dei dispositivi (comunemente router wireless radio con openwrt) che comunicano tra loro e *sorreggono la comunicazioni all'interno della rete*.

I nodi della rete si possono interfacciare via:

* **wireless**, essid: **iulii.net-mesh** in modalità adhoc;
* **ethernet**, via cavo;
* **vpn**, connessione via [tunnel vpn](http://wiki.ninux.org/TincVPN "collegarsi a ninux con una vpn"). Questo metodo è utilizzato anche per collegare diverse isole della rete.

La configurazione del layer3 è gestita dal protocollo ipv6. 

Ai **nodi può essere assegnata la sottorete ipv6 2001:470:7023:2::/64**. Normalmente gli indirizzi ipv6 dei nodi sono assegnati staticamente in base al macaddress. 

Su alcuni nodi della rete è presente un router advertisement (ra) daemon (come ad esempio [radvd](http://www.litech.org/radvd/ "homepage di radvd") o [dnsmasq](http://www.thekelleys.org.uk/dnsmasq/doc.html "homepage di dnsmasq")) per gestire in maniera automatica l'assegnazione degli indirizzi e del routing ipv6 nella sottorete dei clients.

Non è escluso che su alcuni nodi sia presente un server dhcp per la gestione degli indirizzi sia ipv6 che ipv4.

Esempi di configurazione di nodi sono disponibili all'indirizzo [https://github.com/iuliinet/configs](https://github.com/iuliinet/configs "esempi di configurazione")

#### i clients

Sono i dispositivi personali (pc, notebook, smartphone, tablet, router, ...), per questi gli accessi possibili per entrare nella rete del progetto iulii.net sono:

* **wireless**, essid: **www.iulii.net-ap** in modalità ap;
* **ethernet**, collegamento via cavo;
* **vpn**, connessione via [tunnel vpn](http://wiki.ninux.org/TincVPN "collegarsi a ninux con una vpn").

Per la gestione automatica degli indirizzi ipv6 si consiglia:

* [ndisc](http://www.remlab.net/ndisc6/ "ndisc") per SO unix like;
* Microsoft Windows Vista+;

Ad esempio, **la sottorete ipv6 2001:470:7023:2::/64 può essere assegnata ai clients**, diversa da quella dei nodi.
