# ha_weblink

Home Assistant weblink extractor and generator

Home Assistant no longer supports [weblink](https://github.com/home-assistant/core/pull/30834), https://www.home-assistant.io/lovelace/entities/#weblink should be used instead.

Old weblink:

  * code https://github.com/home-assistant/core/blob/0.106.6/homeassistant/components/weblink/__init__.py
  * documentation https://github.com/clach04/home-assistant.io/blob/patch-1/source/_components/weblink.markdown

If looking for a simple launcher dashboard take a look at:

  * https://github.com/bastienwirtz/homer
  * https://github.com/jeroenpardon/sui (and forks, e.g. https://github.com/magikmw/sui)
  * https://github.com/Tenzinn3/Managethis
  * https://github.com/mescon/Muximux
  * or even hand edited html file like https://www.reddit.com/r/selfhosted/comments/hjk2qd/comment/fwqvcyy

This is a clean room implementation of a script that will take an existing HA data yaml file and generate a quick-n-dirty html file, without the need to migrate existing data file/format/syntax.

Sample, data.yaml:

	weblink:
	  entities:
		- name: Router
		  url: http://127.0.0.1/
		  icon: mdi:router-wireless

Where icon names are Material Design Icons (MDI) come from https://fonts.google.com/icons or a directl URL to the image/icon.
If no icon is specified a favicon in default location (/favicon.ico) is assumed (an extension on the Home Assistant original implementation).

Usage:

    python ha_weblink.py > index.html

