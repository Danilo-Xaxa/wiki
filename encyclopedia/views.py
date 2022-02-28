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


def random(request):
    entries = util.list_entries()
    title = entries[randint(0, len(entries) - 1)]
    return redirect(f"/wiki/{title}")


def search(request):
    query = request.GET.get("q")

    for entry in util.list_entries():
        if query.casefold() == entry.casefold():
            return redirect(f"/wiki/{entry}")
    else:
        matches = []
        for entry in util.list_entries():
            if query.casefold() in entry.casefold():
                matches.append(entry)
        if matches:
            return render(request, "encyclopedia/index.html", {
                "entries": matches
            })
        else:
            return render(request, "encyclopedia/error.html", {
                "error_msg": "There are no matches for your search :("
            })


def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        for entry in util.list_entries():
            if title.casefold() == entry.casefold():
                return render(request, "encyclopedia/error.html", {
                    "error_msg": f"There is a page called {entry} already :("
                })

        content = request.POST.get('content')
        util.save_entry(title, content)
        return redirect(f"/wiki/{title}")

    return render(request, "encyclopedia/create.html")


def edit(request):
    if request.method == "POST":	
        title = request.POST.get('title')
        content = request.POST.get('content')
        util.save_entry(title, content)
        return redirect(f"/wiki/{title}")

    title = request.GET.get('title')
    content = util.get_entry(title)
    return render(request, "encyclopedia/edit.html", {
        "title": title,
        "content": content
        })
