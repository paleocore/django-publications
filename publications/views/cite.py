from django.shortcuts import render
from publications.models import Publication, CustomLink, CustomFile
from publications.utils import populate

def cite(request, citekey=None):
    citekeys = []
    publications = Publication.objects.all().order_by('citekey', '-year', '-month', '-id')

    for publication in publications:
        if publication.type.hidden:
            continue
        else:
            citekeys.append((publication.citekey, []))
        citekeys[-1][1].append(publication)

    if 'plain' in request.GET:
        return render(request, 'publications/publications.txt', {
            'publications': publications
        }, content_type='text/plain; charset=UTF-8')

    if 'bibtex' in request.GET:
        return render(request, 'publications/publications.bib', {
            'publications': publications
        }, content_type='text/x-bibtex; charset=UTF-8')

    if 'mods' in request.GET:
        return render(request, 'publications/publications.mods', {
            'publications': publications
        }, content_type='application/xml; charset=UTF-8')

    if 'ris' in request.GET:
        return render(request, 'publications/publications.ris', {
            'publications': publications
        }, content_type='application/x-research-info-systems; charset=UTF-8')

    if 'rss' in request.GET:
        return render(request, 'publications/publications.rss', {
            'url': 'http://' + request.get_host() + request.path,
            'publications': publications
        }, content_type='application/rss+xml; charset=UTF-8')

    #populate(publications)

    return render(request, 'publications/cite.html', {
        'citekeys': citekeys
    })
