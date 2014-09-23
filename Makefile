generate: 
	./minimalsite.py -t templates/default_template.py
	./minimalsite.py -t templates/nojs_template.py
	git add .
	git commit -am fix

github:
	git push

flarevm:	
	rsync -avr -e ssh ./dst/* flarevm:www/iulii.net/

kino:
	rsync -avr -e ssh ./dst/* lucapost@kino:repo/iulii.net/

clean:
	find . -type f -name "*.html" -exec rm -f {} \;
	find . -type d -empty -exec rm -rf {} \ ;
