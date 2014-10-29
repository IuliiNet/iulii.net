import time
import datetime

SITE_NAME = "IuliiNet"
DESC = "rete wireless mesh libera e decentralizzata in friuli"
AUTHOR = "lucapost"
SRC = "/home/lucapost/repo/iuliinet/iulii.net/src"
DST = "/home/lucapost/repo/iuliinet/iulii.net/dst"
SITEMAP = "/home/lucapost/repo/iuliinet/iulii.net/dst/sitemap.xml"
URL = "http://iulii.net"
PREFIX = "/"
HOME = "home"
PATH_SEPARATOR = '/'
SRC_EXT = {"markdown": "md", "textile": "textile", "plain": "txt"}
DST_EXT = "html"
HIDDEN = set(["404.textile", "splash.textile"])
menu_code = ''
PAGES = {SRC + "/index.md": ("home page", "wireless mesh network libera e decentralizzata in friuli venezia giulia"),
	 SRC + "/30_rete/index.md": ("rete", "esempi di configurazione dei nodi della rete"),
	 SRC + "/30_rete/30_servizi.md": ("rete", "elenco dei servizi disponibili nelle rete"),
	 SRC + "/70_contatti.md": ("contatti", "contattare via email twitter facebook googleplus irc commenti"),
	 SRC + "/50_links.md": ("links", "collegamenti a siti amici")}

current_time = datetime.datetime.now()

def get_page_contents(node):
    """Return page title and description from the global variable pages if a
    match with current node page.src_file is found.
    """ 

    try:
        return (SITE_NAME + ' | ' + PAGES[node.page.src_pathname][0], \
            PAGES[node.page.src_pathname][1])
    except KeyError:
        return ('%%%TITLE%%%', '')

def menu(node):
    """Generate a hierarchical menu."""

    global menu_code

    menu_code = '\n'
    root = node
    while root.parent:
        root = root.parent
    menu_(root, node)
    return menu_code

def menu_(node, cur_node, node_prefix = PREFIX, indent = ''):
    """Auxiliary recursive function for menu generation."""

    global menu_code

    menu_code += indent + '<ul>\n'
    for child in sorted(node.children, key=lambda n: n.page.src_pathname):
        if child.page.dst_file.startswith("index.") or child.page.src_file in HIDDEN:
            continue
        menu_code += indent + '<li class="level-' + str(child.page.level) + '"><a '
        if(child == cur_node
        or (cur_node.page.dst_file.startswith("index.") and child == cur_node.parent)):
            menu_code += 'class="current" '
        menu_code += 'href="' + node_prefix + child.page.dst_file
        if child.children:
            menu_code += "/index." + DST_EXT + '">'    + child.page.name + '</a>\n'
            menu_(child, cur_node, node_prefix + child.page.dst_file + '/', indent + '\t')
            menu_code += indent + '</li>\n'
        else:
            menu_code += '">'   + child.page.name + '</a></li>\n'
    menu_code += indent + '</ul>\n'

def header(node):
    """Build the header and return it to a string."""

    (title, description) = get_page_contents(node)
    return '''<!DOCTYPE html>
	<!--[if lt IE 7]> <html class="no-js lt-ie9 lt-ie8 lt-ie7" lang="it"> <![endif]-->
	<!--[if IE 7]>    <html class="no-js lt-ie9 lt-ie8" lang="it"> <![endif]-->
	<!--[if IE 8]>    <html class="no-js lt-ie9" lang="it"> <![endif]-->
	<!--[if gt IE 8]><!--> <html class="no-js" lang="it"> <!--<![endif]-->
	<head>
        	<meta charset="utf-8" />
        	<meta name="author" content="''' + AUTHOR + '''" />
	        <meta name="description" content="''' + description + '''" />
        	<title>''' + title + '''</title>
		<meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1" />
		<link rel="icon" type="image/png" href="'''+ PREFIX +'''img/iuliinetlogo.png">
		<!--[if lt IE 9]>
  			<script src="'''+ PREFIX +'''assets/js/html5.js"></script>
		<![endif]-->
		<link rel="stylesheet" href="'''+ PREFIX +'''assets/css/demo.css" />
		<!--[if (gt IE 8) | (IEMobile)]><!-->
  			<link rel="stylesheet" href="'''+ PREFIX +'''assets/css/unsemantic-grid-responsive.css" />
		<!--<![endif]-->
		<!--[if (lt IE 9) & (!IEMobile)]>
  			<link rel="stylesheet" href="'''+ PREFIX +'''assets/css/ie.css" />
		<![endif]-->
		<link rel="stylesheet" type="text/css" media="all" href="'''+ PREFIX +'''assets/css/style.css" />
	</head>
	<body id="top">
		<div class="white">
		<div class="grid-container">
			<header>
				<hgroup class="grid-70 mobile-grid-100">
					<h1><a href="''' + PREFIX + '''">''' + SITE_NAME + '''</a></h1>
					<h2>''' + DESC + '''</h2>
				</hgroup>
				<figure>
					<img class="grid-30 hide-on-mobile" title="iuliinet logo" alt="iuliinet logo" src="'''+ PREFIX +'''img/iuliinetlogo.png">
				</figure>
			</header>
		</div>
		</div>
		<div class="blue">
		<div class="grid-container">
			<section class="grid-70 mobile-grid-100">
'''
def footer(node):
    """Build the footer and return it to a string."""

    return '''
			<p><a href="#top" title="back to top" class="backtotop">back to top</a></p>
    			</section>
			<div class="grid-30 mobile-grid-100">
				<div class="navigation">
					<div class="path">
						<b>path</b>: %%%PATH%%%
					</div>
					<nav>
						''' + menu(node) + '''
					</nav>
				</div>
				<div class="tt-widget">
                    			<a class="twitter-timeline" href="https://twitter.com/IuliiNet" data-border-color="#55a1d5" data-widget-id="349571026952269826">Tweets by @IuliiNet</a>
                    			<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+"://platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");</script>
				</div>
			</div>
		</div>
		</div>
		<footer class="grid-container">
			<div class="grid-100 mobile-grid-100">
				<div class="foot">
					<p>&copy; ''' + str(current_time.year) + ''' <a href="http://iulii.net" title="iulii.net website">iulii.net</a> | <a rel="license" href="http://creativecommons.org/licenses/by-nc/3.0/">license CC by-nc</a> | edit: ''' + time.strftime("%Y%m%d %I:%M:%S %p", node.page.last_edit) + '''</p>
				</div>
			</div>
			<div class="clear"></div>
		</footer>	
  		<script>
    			var _gaq=[['_setAccount','UA-6164762-12'],['_trackPageview']];
    			(function(d,t){var g=d.createElement(t),s=d.getElementsByTagName(t)[0];
    			g.src=('https:'==location.protocol?'//ssl':'//www')+'.google-analytics.com/ga.js';
    			s.parentNode.insertBefore(g,s)}(document,'script'));
  		</script>
</body>
</html>'''	
