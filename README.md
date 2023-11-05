# ha_weblink

Home Assistant weblink extractor and static generator for a simple link dashboard.

This is a clean room implementation of a Python script that will take an existing HA data yaml file and generate a quick-n-dirty html file, without the need to migrate existing data file/format/syntax.

Home Assistant no longer supports [weblink](https://github.com/home-assistant/core/pull/30834), https://www.home-assistant.io/lovelace/entities/#weblink should be used instead.

Old weblink:

  * code https://github.com/home-assistant/core/blob/0.106.6/homeassistant/components/weblink/__init__.py
  * documentation https://github.com/clach04/home-assistant.io/blob/patch-1/source/_components/weblink.markdown

## Alternatives

If looking for a simple launcher dashboard take a look at:

  * https://github.com/clach04/ha_weblink/issues/8
  * https://github.com/pawelmalak/flame
  * https://github.com/bastienwirtz/homer
  * https://github.com/jeroenpardon/sui (and forks, e.g. https://github.com/magikmw/sui)
  * https://github.com/Tenzinn3/Managethis
  * https://github.com/mescon/Muximux
  * or even hand edited html file like https://www.reddit.com/r/selfhosted/comments/hjk2qd/comment/fwqvcyy

## Setup

    python -m pip install pyyaml

## Usage

    python ha_weblink.py sample.yaml > sample.html

If filename is not specified, `data.yaml` is assumed.

Sample, data.yaml:

	weblink:
	  entities:
		- name: Router
		  url: http://127.0.0.1/
		  icon: mdi:router-wireless

Where icon names are:

  1. Material Design Icons (MDI) come from https://fonts.google.com/icons, E.g. `mdi:...` or without mdi prefix - just like Home Assistant (used to support)
  2. direct URL to the image/icon, `http....` - NOT supported by HA
  3. `text:any text or emjoi` - NOT supported by HA

If no icon is specified a favicon in default location (/favicon.ico) is assumed, similar to #2 (an extension on the Home Assistant original implementation).
Can easily pull icons straight from google with the following URL - `https://www.google.com/s2/favicons?domain=``{Serivce URL}&sz={PIXEL SIZE}`, for example https://www.google.com/s2/favicons?domain=https://www.portainer.io/&sz=256

Usage:

    python ha_weblink.py > index.html

