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
	episode-*-slides.pdf \
	success-and-failure.pdf \
	ovsdb2*.txt
SRV = /srv/ovsorbit.benpfaff.org
install: all
	rsync -P $(FILES) benpfaff.org:'$(SRV)'
.PHONY: install

stats:

