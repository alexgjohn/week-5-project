from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.skater import Skater
import repositories.lesson_repository as lesson_repo
import repositories.skater_repository as skater_repo
import repositories.level_repository as level_repo

skaters_blueprint = Blueprint("skaters", __name__)


@skaters_blueprint.route('/skaters')
def skaters():
    skaters = skater_repo.select_all()
    premium_skaters = skater_repo.get_premium_skaters()
    return render_template('skaters/index.jinja', skaters = skaters, premium_skaters = premium_skaters, title = "Meet Our Skaters!")

@skaters_blueprint.route('/skaters/<id>')
def show(id):
    skater = skater_repo.select(id)
    title = skater.full_name
    return render_template('skaters/show.jinja', skater = skater, title = title)