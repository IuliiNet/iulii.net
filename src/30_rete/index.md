### La rete

Questa sezione si prefigge l'obiettivo di descrivere, anche entrando in dettagli piuttosto tecnici, la struttura della rete iulii.net e delle [reti mesh](http://it.wikipedia.org/wiki/Wireless_mesh_network "wireless mesh network su wikipedia") basate su [batmnad-adv](http://www.open-mesh.org/wiki/batman-adv/ "batman-adv homepage") in generale.

#### la struttura della rete

La rete del progetto iulii.net basa il collegamento dei nodi sul protocollo su layer2 [batman-adv](http://www.open-mesh.org/wiki/batman-adv/ "homepage del progetto batmnad-adv"). E' disponibile un'[introduzione a batman-adv](batman-adv.html "introduzione a batman-adv"). Al momento attuale è supportata la versione 2012.1 e compatibili di batman-adv.

Si è scelto l'utilizzo sul layer3 per protocollo ipv6 data la semplicità di assegnazione degli indirizzi e la facilitazione nell'evitare conflitti ip. Ai nodi della rete può essere assegnata la sottorete ipv6 2001:470:7023:1::/64. Normalmente gli indirizzi ipv6 dei nodi sono assegnati staticamente in base al macaddress.

I nodi della rete possono comunicare tra loro su una rete wireless configurata in adhoc mode sull'essid **www.ninux.org-www.iulii.net-mesh**.

Sui nodi della rete è installata una distribuzione linux, nel caso più comune si tratta di [openwrt](http://openwrt.org "homepage di openwrt"). Ma possono essere utilizzate qualsiasi tipo di distribuzione.

I client si possono collegare ai nodi utilizzando interfaccie wifi, ethernet o vpn.

#### collegarsi alla rete

Tra le vie possibili per entrare nella rete del progetto iulii.net gli accessi più comuni sono :

* **wireless** se il dispositivo (pc, smartphone, tablet, ...) è sotto la copertura di una rete wireless in modalità access point (ap), normalmente è necessario selezionare l'essid **www.ninux.org-www.iulii.net-ap** ed attendere l'assegnazione dell'indirizzo ipv6;
* **ethernet** se il dispositivo è dotato di una porta ethernet e si trova nei pressi di un nodo è possibile connettersi via rete anche utilizzando il cavo;
* **vpn** è altresì possibile collegarsi alla rete utilizzando un [tunnel vpn](http://wiki.ninux.org/TincVPN "collegarsi a ninux con una vpn"). Questo metodo è anche utilizzato per collegare tra loro delle isole della rete.

Il dispositivo deve avere il supporto al router advertisement. Infatti, su alcuni nodi della rete è presente un router advertisement daemon (come ad esempio [radvd](http://www.litech.org/radvd/ "homepage di radvd") o [dnsmasq](http://www.thekelleys.org.uk/dnsmasq/doc.html "homepage di dnsmasq")) per gestire in maniera automatica l'assegnazione degli indirizzi e del routing ipv6 nella sottorete dei clients evitanti i conflitti, come ad esempio 2001:470:7023:2::/64.

Non è escluso che su alcuni nodi sia presente un server dhcp per la gestione degli indirizzi ipv4.

#### configurazione dei nodi 

Sono presenti approfondimenti sulla [configurazione dei nodi](nodi/ "configurazione dei nodi").
 
#### servizi 

E' disponibile un elenco (incompleto) dei [servizi accessibili](servizi.html "servizi") dalla rete del progetto.
