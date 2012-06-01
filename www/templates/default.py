# Author:      Luca Postregna <luca.postregna@gmail.com>
# License:     MIT, see LICENSE for details

import os
import time, datetime

site_name = "iulii.net"
desc = "rete mesh libera e decentralizzata in friuli"
author = "lucapost"
src_dir = "src"
dst_dir = ""
prefix = "/"
home = "~"
path_separator = "/"
src_ext = {"markdown": "md", "textile": "tt", "plain": "txt"}
dst_ext = "html"
hidden = set(["404.md", "500.md", "search.md"])

current_time = datetime.datetime.now()
menu_code = ''

def menu(node):
	global menu_code

	menu_code = '\n'
	root = node
	while root.parent:
		root = root.parent
	menu_(root, node)
	return menu_code

def menu_(node, cur_node, node_prefix = prefix, indent = ''):
	global menu_code

	menu_code += indent + '<ul>\n'
	for child in sorted(node.children, key=lambda n: n.src_pathname):
		if child.dst_file.startswith("index.") or child.src_file in hidden:
			continue
		menu_code += indent + '<li class="level-' + str(child.level) + '"><a '
		if(child == cur_node
		or (cur_node.dst_file.startswith("index.") and child == cur_node.parent)):
			menu_code += 'class="current" '
		menu_code += 'href="' + node_prefix + child.dst_file
		if child.children:
			menu_code += "/index." + dst_ext + '">'	+ child.name + '</a>\n'
			menu_(child, cur_node, node_prefix + child.dst_file + '/', indent + '\t')
			menu_code += indent + '</li>\n'
		else:
			menu_code += '">'   + child.name + '</a></li>\n'
	menu_code += indent + '</ul>\n'

def header(node):
	"""Builds the header and returns it to a string."""
	
	return '''<!doctype html>
	<!--[if lt IE 7]> <html class="no-js lt-ie9 lt-ie8 lt-ie7" lang="it"> <![endif]-->
	<!--[if IE 7]>    <html class="no-js lt-ie9 lt-ie8" lang="it"> <![endif]-->
	<!--[if IE 8]>    <html class="no-js lt-ie9" lang="it"> <![endif]-->
	<!--[if gt IE 8]><!--> <html class="no-js" lang="it"> <!--<![endif]-->
	<head>
  		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
		<title>''' + site_name + ' | ' + node.name + '''</title>
  		<meta name="description" content="rete libera e decentralizzata in friuli">
  		<meta name="author" content="''' + author + '''" />
  		<meta name="viewport" content="width=device-width">
		<link rel="stylesheet" type="text/css" media="all" href="/css/reset.css" />
		<link rel="stylesheet" type="text/css" media="all" href="/css/text.css" />
		<link rel="stylesheet" type="text/css" media="all" href="/css/960.css" />
		<link rel="stylesheet" type="text/css" media="all" href="/css/hashgrid.css" />
		<link rel="stylesheet" type="text/css" media="all" href="/css/style.css" />
  		<script src="/js/vendor/modernizr-2.5.3.min.js"></script>
	</head>
	<body>
		<header class="container_12 clearfix">
			<hgroup class="grid_8">
				<h1><a href="''' + '../' * node.level + '''index.''' + dst_ext + '''">''' + site_name + '''</a></h1>
				<h2>''' + desc + '''</a></h2>
			</hgroup>
			<div class="grid_4 logo">
			</div>
			<div class="clear"></div>
		</header>
		<section class="container_12 clearfix">
			<article class="grid_8">
'''

def footer(node):
	"""Builds the footer and returns it to a string."""

	return '''
			</article>
			<div class="grid_4">
				<div class="path">
					path: %%%PATH%%%
				</div>
				<nav>
					''' + menu(node) + '''
				</nav>
			</div>
			<div class="clear"></div>
		</section>
		<footer class="container_12 clearfix">
			<p class="push_1 grid_10">
				&copy; ''' + str(current_time.year) + ' ' + author + '''
				| edit: ''' + time.strftime("%m/%d/%Y %I:%M:%S %p",time.localtime(os.path.getmtime(node.src_pathname))) + '''
				</p>
		</footer>
	  	<!--[if lt IE 7]><p class=chromeframe>Your browser is <em>ancient!</em> <a href="http://browsehappy.com/">Upgrade to a different browser</a> or <a href="http://www.google.com/chromeframe/?redirect=true">install Google Chrome Frame</a> to experience this site.</p><![endif]-->
	  	<script src="//ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
  		<script>window.jQuery || document.write('<script src="/js/vendor/jquery-1.7.2.min.js"><\/script>')</script>
  		<script src="/js/plugins.js"></script>
  		<script src="/js/main.js"></script>
  		<script src="/js/hashgrid.js"></script>
  		<script>
    			var _gaq=[['_setAccount','UA-XXXXX-X'],['_trackPageview']];
    			(function(d,t){var g=d.createElement(t),s=d.getElementsByTagName(t)[0];
    			g.src=('https:'==location.protocol?'//ssl':'//www')+'.google-analytics.com/ga.js';
    			s.parentNode.insertBefore(g,s)}(document,'script'));
  		</script>
</body>
</html>'''
