from flask import Flask, Response
from github import get_github_data

app = Flask(__name__)

with open("./templates/badge.svg", "r", encoding="utf-8") as f:
    TEMPLATE = f.read()



def render_svg(data):
    svg = TEMPLATE

    # whitelist keys your SVG expects
    keys = [
        "username",
        "handle",
        "avatar_url",
        "followers",
        "stars",
        "repos",
        "commits",
        "prs",
        "streak",
        "grade",
        "extra",
    ]

    for key in keys:
        value = data.get(key, "") 
        svg = svg.replace(f"{{{{{key}}}}}", str(value))

    return svg


@app.route("/card/<username>")
def card(username):
    try:
        data = get_github_data(username)

       
        data.setdefault("handle", data.get("username", ""))
        data.setdefault("repos", 0)
        data.setdefault("prs", 0)
        data.setdefault("extra", "Active")

        svg = render_svg(data)

        return Response(svg, mimetype="image/svg+xml")

    except Exception as e:
        return Response(f"<h1>Error: {str(e)}</h1>", status=500)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
