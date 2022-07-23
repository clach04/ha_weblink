# ha_weblink

Home Assistant weblink extractor and generator

Home Assistant no longer supports weblink, https://www.home-assistant.io/lovelace/entities/#weblink should be used instead.

If looking for a simple launcher dashboard take a look at:

  * https://github.com/bastienwirtz/homer
  * https://github.com/jeroenpardon/sui (and forks, e.g. https://github.com/magikmw/sui)
  * https://github.com/Tenzinn3/Managethis
  * https://github.com/mescon/Muximux
  * or even hand edited html file like https://www.reddit.com/r/selfhosted/comments/hjk2qd/comment/fwqvcyy

This script will take an existing HA data yaml file and generate a quick-n-dirty html file, without the need to migrate existing data.

Sample, data.yaml:

	weblink:
	  entities:
		- name: Router
		  url: http://127.0.0.1/
		  icon: mdi:router-wireless

Usage:

    python ha_weblink.py > index.html

## Todo

Icons that specify a URL, extension to Home Assistant original implementation.
Currently attempts to use favicon in root directory of URL (also an extension not present in original).
