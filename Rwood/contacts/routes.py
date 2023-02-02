from flask import render_template, request, Blueprint, flash, abort, redirect, url_for




contacts = Blueprint('contacts', __name__)


@contacts.route("/contact")
def contacts_home():

    return render_template('contacts/home.html')