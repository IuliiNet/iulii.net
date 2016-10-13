generate:
	./minimalsite.py -t templates/default_template.py

github:
	git add .
	git commit -am fix
	git push

vultr:	
	rsync -avr -e ssh ./dst/* vultr2:www/iulii.ninux.org/

all: 
	make generate
	make github
	make vultr

clean:
	find . -type f -name "*.html" -exec rm -f {} \;
	find . -type d -empty -exec rm -rf {} \ ;
