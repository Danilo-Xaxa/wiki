from django.shortcuts import render

from . import util
from markdown2 import Markdown


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entrada(request, title):
    content = util.get_entry(title)
    if content:
        markdowner = Markdown()
        html = markdowner.convert(content)
        return render(request, html)
    else:
        return render(request, "encyclopedia/error.html", {
            "error_msg": f"There is not a page called {title}. Make one..."
        })
