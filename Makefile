generate: 
	python2 ./minimalsite.py
	python2 ./gensitemap-xsl.py > sitemap.xml

clean:
	find . -type f -name "*.html" -exec rm -f {} \;
	find . -type d -empty -exec rmdir {} \;

