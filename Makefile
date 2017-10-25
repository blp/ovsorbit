all:
	./generate.py
.PHONY: all

FILES = \
	episode-*.mp3 \
	abstract.html \
	favicon.png \
	feed-icon-*.png \
	index.html \
	rss.xml \
	app.js \
	jquery-1.11.3.min.js \
	orbit_*.png \
	style.css \
	count-popularity \
	update-stars \
	episode-22-slides.pdf
SRV = /srv/ovsorbit.benpfaff.org
install: all
	rsync -P $(FILES) benpfaff.org:'$(SRV)'
	ssh benpfaff.org 'cd $(SRV) && ./update-stars'
.PHONY: install

stats:

