from flask import render_template, request, Blueprint, flash, abort, redirect, url_for




accounts = Blueprint('accounts', __name__)


@accounts.route("/")
def accounts_home():

    return render_template('accounts/home.html')