from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def mypage():
    return render_template("homepage.html")


@app.route("/contact")
def contact():
    return """
        <ul>
        <li>e-mail : +48-123456789</li>
        <li>telefon : jan.kowalski@gmail.pl</li>
    </ul>
    
    <form action="...">
        <textarea name="" id="" cols="10" rows="10"></textarea>
        <input type="submit" value="przeslij">
    </form>

    """
