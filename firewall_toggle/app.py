from flask import Flask, render_template, url_for, redirect

from firewall_api import get_firewall_rules, toggle_firewall_rule


config={
    "DEBUG": True,
}


app = Flask(__name__)
app.config.from_mapping(config)


@app.route("/")
def index():
    firewall_rules = get_firewall_rules()
    return render_template("index.html", rules=firewall_rules['rows'])

@app.route("/toggle/<rule_uuid>")
def toggle_rule(rule_uuid):
    toggle_firewall_rule(rule_uuid)
    return redirect(url_for('index'))
    