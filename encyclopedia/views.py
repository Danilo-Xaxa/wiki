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
    entries = util.list_entries()
    title = entries[randint(0, len(entries) - 1)]
    return redirect(f"/wiki/{title}")


def search(request):
    query = request.GET.get("q")

    if query.lower() in [entry.lower() for entry in util.list_entries()]:
        return redirect(f"/wiki/{query}")
    else:
        matches = []
        for entry in util.list_entries():
            if query in entry:
                matches.append(entry)
        if matches:
            return render(request, "encyclopedia/index.html", {
                "entries": matches
            })
        else:
            return render(request, "encyclopedia/error.html", {
                "error_msg": "There are no matches for your search :("
            })


def create_page(request):
    return render(request, "encyclopedia/create.html")


def save_page(request):
    title = request.POST.get('title')
    if title.lower() in [entry.lower() for entry in util.list_entries()]:
        return render(request, "encyclopedia/error.html", {
                    "error_msg": f"There is a page called {title} already :("
                })

    content = request.POST.get('content')
    util.save_entry(title, content)
    return redirect(f"/wiki/{title}")
