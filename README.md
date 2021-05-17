# ha_weblink
Home Assistant weblink extractor and generator

Home Assistant no longer supports weblink, https://www.home-assistant.io/lovelace/entities/#weblink should be used instead.

This script will take an existing HA data yaml file and generate a quick-n-dirty html file.

Sample, data.yaml:

	weblink:
	  entities:
		- name: Router
		  url: http://127.0.0.1/
		  icon: mdi:router-wireless

Usage:

    python ha_weblink.py > index.html

