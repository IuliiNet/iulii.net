github:
	git add .
	git commit -am fix
	git push

flarevm:	
	./minimalsite.py -t templates/default_template.py
	rsync -avr -e ssh ./dst/* flarevm:www/iulii.net/

kino:
	./minimalsite.py -t templates/nojs_template.py
	rsync -avr -e ssh ./dst/* lucapost@kino:repo/iulii.net/

clean:
	find . -type f -name "*.html" -exec rm -f {} \;
	find . -type d -empty -exec rm -rf {} \ ;
