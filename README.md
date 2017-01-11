# D3-Django integration

Sample project to help who want to integrate D3 getting data from Django.

Forked from https://github.com/fgmacedo/django-d3-example

Companion repository of the StackOverflow answer: [Passing data from Django to D3](http://stackoverflow.com/a/26455798/585592).


## Quickstart for Geonode sites

Clone this repository.

Configure settings and URLs.
    cd cd ~geonode/geonode/geonode
    vi local_settings_gaz.py: add play and d3ex to INSTALLED_APPS
    vi urls.py: add code to import play.urls and d3ex.urls

Install.

    cd ~geonode/geonode
    sudo -H pip install --upgrade ../django-d3-example
    sudo service apache2 restart

Log into admin and add some Play instances (sample data).

    http://cfdev.intersect.org.au/admin/play/play/

See your chart at url:

    http://cfdev.intersect.org.au/play