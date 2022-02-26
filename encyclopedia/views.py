from django.shortcuts import redirect, render
from . import util
from markdown2 import Markdown
from random import randint


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    content = util.get_entry(title)

    if content:
        markdowner = Markdown()
        html = markdowner.convert(content)
        return render(request, "encyclopedia/result.html", {
            "title": title,
            "content": html
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "error_msg": f"There is not a page called {title}. Make one..."
        })


def random_page(request):
    list_entries = util.list_entries()
    title = list_entries[randint(0, len(list_entries) - 1)]
    return redirect(f"/wiki/{title}")


