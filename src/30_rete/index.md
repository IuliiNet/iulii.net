### La rete

Questa sezione si prefigge l'obiettivo di descrivere, anche entrando in dettagli piuttosto tecnici, la struttura della rete iulii.net e delle [reti mesh](http://it.wikipedia.org/wiki/Wireless_mesh_network "wireless mesh network su wikipedia") basate su [batmnad-adv](http://www.open-mesh.org/wiki/batman-adv/ "batman-adv homepage") in generale.

Per accedere ai [servizi](servizi.html "servizi del progetto iulii.net") è necessario collegarsi ad un nodo della rete. E' possibile ottenere questo utilizando un collegamento ethernet o molto più comunemente accedendo alla rete wireless con essid **www.ninux.org-www.iulii.net-ap**. Normalmente questa rete in modalità ap è accessibile da chiunque sensa bisogno di alcuna autenticazione. E' altresì possibile collegarsi alla rete utilizzando un [tunnel vpn](http://wiki.ninux.org/TincVPN "collegarsi a ninux con una vpn").

#### batmand-adv

La rete mesh del progetto iulii.net è basata sul protocollo su layer2 [batman-adv](http://www.open-mesh.org/wiki/batman-adv/ "homepage del progetto batmnad-adv"). E' disponibile un'[introduzione a batman-adv](batman-adv.html "introduzione a batman-adv"). 

#### wifi

Generalmente un nodo della progetto iulii.net mette a disposizione due essid:

* **www.ninux.org-www.iulii.net-mesh**: in modalità adhoc, è l'interfaccia gestita da batman-adv e permette il routing tra i nodi di tutta la rete;
* **www.ninux.org-www.iulii.net-ap**: in modalità ap, è adatto per accettare connessione dai client.
 
#### routing

Ai nodi della rete può essere assegnata la sottorete ipv6 2001:470:7023:1::/64.

Su alcuni nodi della rete è presente un router advertisement daemon (come ad esempio [radvd](http://www.litech.org/radvd/ "homepage di radvd") o [dnsmasq](http://www.thekelleys.org.uk/dnsmasq/doc.html "homepage di dnsmasq")) per gestire in maniera automatica l'assegnazione degli indirizzi e del routing ipv6 nella sottorete dei client, come ad esempio 2001:470:7023:2::/64.

I client devono quindi supportare il protocollo ipv6, ed allo stesso tempo poter inviare le richieste di router advertisement. Sui client unix sono disponibilie ad esempio [ndisc6](http://www.remlab.net/ndisc6/ "Recursive DNS Servers discovery Daemon for IPv6") o [networkmanager](http://www.gnome.org/projects/NetworkManager/ "homepage del progetto networkmanager"), tools analoghi sono disponibili su sistemi operativi microsoft windows vista+.

Non è escluso che su alcuni nodi sia presente un server dhcp per la gestione degli indirizzi ipv4.

#### configurazione dei nodi 

Sono presenti approfondimenti sulla [configurazione dei nodi](nodi/ "configurazione dei nodi").

#### servizi 

E' disponibile un elenco (incompleto) dei [servizi accessibili](servizi.html "servizi") dalla rete del progetto.
