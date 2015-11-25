generate:
	./minimalsite.py -t templates/default_template.py

github:
	git add .
	git commit -am fix
	git push

vultr:	
	./minimalsite.py -t templates/default_template.py
	rsync -avr -e ssh ./dst/* vultr:www/iulii.ninux.org/

sun:
	./minimalsite.py -t templates/default_template.py
	rsync -avr -e ssh ./dst/* sun:/mnt/disk4t/www/iulii.lii/

clean:
	find . -type f -name "*.html" -exec rm -f {} \;
	find . -type d -empty -exec rm -rf {} \ ;
