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
  		<meta name="viewport" content="width=device-width">
		<link rel="stylesheet" type="text/css" media="all" href="'''+ PREFIX +'''/assets/css/reset.css" />
		<link rel="stylesheet" type="text/css" media="all" href="'''+ PREFIX +'''/assetscss/text.css" />
		<link rel="stylesheet" type="text/css" media="all" href="'''+ PREFIX +'''/assetscss/960.css" />
		<link rel="stylesheet" type="text/css" media="all" href="'''+ PREFIX +'''/assetscss/hashgrid.css" />
		<link rel="stylesheet" type="text/css" media="all" href="'''+ PREFIX +'''/assetscss/style.css" />
		<link rel="icon" type="image/png" href="'''+ PREFIX +'''img/iuliinetlogo.png">
	</head>
	<body id="top">
		<header class="container_12 clearfix">
			<div class="grid_8">
				<hgroup>
					<h1><a href="''' + PREFIX + '''">''' + SITE_NAME + '''</a></h1>
					<h2><a href="''' + PREFIX + '''">''' + DESC + '''</a></h2>
				</hgroup>
			</div>
			<div class="grid_4">
				<a href="''' + PREFIX + '''">
					<img class="iuliinetlogo" title="iuliinet logo" alt="iuliinet logo" src="'''+ PREFIX +'''img/iuliinetlogo.png">
				</a>
			</div>
			<div class="clear"></div>
		</header>
		<section class="container_12 clearfix">
			<div class="grid_8">
'''
def footer(node):
    """Build the footer and return it to a string."""

    return '''
    		</div>
			<div class="grid_4 column">
				<div class="navigation">
					<div class="path">
						<b>path</b>: %%%PATH%%%
					</div>
					<nav>
						''' + menu(node) + '''
					</nav>
				</div>
			</div>
			<div class="clear"></div>
		</section>
		<footer class="container_12 clearfix">
			<div class="grid_12">
				<a href="#top" title="back to top" class="backtotop">back to top</a>
				<div class="foot">
					<p>&copy; ''' + str(current_time.year) + ''' <a href="http://iulii.net" title="iulii.net website">iulii.net</a> | <a rel="license" href="http://creativecommons.org/licenses/by-nc/3.0/">license CC by-nc</a> | edit: ''' + time.strftime("%Y%m%d %I:%M:%S %p", node.page.last_edit) + '''</p>
				</div>
			</div>
			<div class="clear"></div>
		</footer>	
<!--[if lt IE 7]><p class=chromeframe>Your browser is <em>ancient!</em> <a href="http://browsehappy.com/">Upgrade to a different browser</a> or <a href="http://www.google.com/chromeframe/?redirect=true">install Google Chrome Frame</a> to experience this site.</p><![endif]-->
	  	<script src="'''+ PREFIX +'''js/jquery.js"></script> 
  		<script src="'''+ PREFIX +'''js/plugins.js"></script>
  		<script src="'''+ PREFIX +'''js/main.js"></script>
  		<script src="'''+ PREFIX +'''js/hashgrid.js"></script>
</body>
</html>'''	
