all:
	./generate.py
.PHONY: all

FILES = \
	episode-*.mp3 \
	favicon.png \
	feed-icon-*.png \
	index.html \
	rss.xml \
	orbit_*.png \
	style.css \
	count-popularity \
	update-stars
SRV = /srv/ovsorbit.benpfaff.org
install: all
	rsync -P $(FILES) benpfaff.org:'$(SRV)'
	ssh benpfaff.org 'cd $(SRV) && ./update-stars'
.PHONY: install

stats:

