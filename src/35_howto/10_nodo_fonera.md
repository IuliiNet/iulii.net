### nodo su fonera 2.0g

In questa pagina si approfondisce la configurazione di un router fonera 2.0g (modello 2201) come nodo generico della rete IuliiNet.

#### specifications

* wifi
    * ap0 access point;
    * adhoc0 adhoc per le mesh;
* ethernet
    * eth0.1 accesso client;
    * eth0.2 mesh;
* batman-adv gw_mode client;
* nessun servizio attivo (no dhcp, no gateway, ecc.);

#### links utili:

* [wiki.openwrt.org/toh/fon/fonera](http://wiki.openwrt.org/toh/fon/fonera) wiki openwrt fonera 2.0g;
* [wiki.openwrt.org/doc/howto/build](http://wiki.openwrt.org/doc/howto/build "building openwrt") informazioni compilazione sorgenti openwrt.
* [github.com/iuliinet/devices/tree/master/fonera2.0g](https://github.com/iuliinet/devices/tree/master/fonera2.0g) file di configurazione;

#### files di configurazione:

/etc/config/wireless

    config wifi-device  radio0
       option type      mac80211
       option channel   11
       option hwmode	11g
       option path	'platform/ar231x-wmac.0'`
       
    config wifi-iface              
       option device   radio0
       option network  lan
       option mode     ap
       option ssid     IuliiNet-ap
       option encryption none

    config wifi-iface
       option device   radio0
       option network  mesh0
       option ifname   adhoc0
       option mode     adhoc
       option ssid     IuliiNet-mesh

/etc/config/batman-adv

    config 'mesh' 'bat0'
        option 'interfaces' 'mesh0 mesh1'
        option 'aggregated_ogms'
        option 'ap_isolation'
        option 'bonding'
        option 'fragmentation'
        option 'gw_bandwidth'
        option 'gw_mode'
       	option 'gw_sel_class'
       	option 'log_level'
       	option 'orig_interval'
       	option 'vis_mode'
       	option 'bridge_loop_avoidance'

/etc/config/network

    config interface 'loopback'
        option ifname 'lo'
    	option proto 'static'
    	option ipaddr '127.0.0.1'
     	option netmask '255.0.0.0'

    config interface 'lan'
     	option type 'bridge'
    	option proto 'static'
    	option ipaddr '192.168.1.1'
    	option netmask '255.255.255.0'
    	option ifname 'eth0.1 bat0'
       	option ip6addr '2001:470:7023:1::0018:84d0:80bc/64'

    config interface 'mesh0'
    	option ifname 'adhoc0'
    	option mtu '1528'
    	option proto 'none'
   
    config interface 'mesh1'
    	option ifname 'eth0.2'
      	option proto 'none' 

/etc/rc.local

    #!/bin/sh

    IPV6PREFIX="2001:470:7023:1" # ipv6 /64 prefix
    PUBKEY=""  #ssh pubkey
    HOSTNAME="fonera"   #hostname

    uci set system.@system[0].hostname=$HOSTNAME
    uci commit system
                                 
    /etc/init.d/dnsmasq disable
    /etc/init.d/nodogsplash disable
    /etc/init.d/radvd disable      
    /etc/init.d/firewall disable
                                    
    IPV6="$IPV6PREFIX::$(cat /sys/class/net/eth0/address |awk -F: '{print $1$2":"$3$4":"$5$6}')/64"
    uci set network.lan.ip6addr=$IPV6                                                              
    uci commit network
  
    echo $PUBKEY > /etc/dropbear/authorized_keys
    
    exit 0
