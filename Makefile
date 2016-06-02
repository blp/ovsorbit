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
	style.css
install: all
	rsync -P $(FILES) benpfaff.org:/srv/ovsorbit.benpfaff.org
.PHONY: install

stats:

