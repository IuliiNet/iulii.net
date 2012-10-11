generate: 
	minimalsite.py -t custom_template.py

update:
	git commit -am fix
	git push

clean:
	find . -type f -name "*.html" -exec rm -f {} \;
	find . -type d -empty -exec rmdir {} \ ;
