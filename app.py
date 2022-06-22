from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_skill, get_candidates_by_name

app = Flask(__name__)

@app.route("/")
def page_all():
    users_data = load_candidates_from_json('candidates.json')
    return render_template('list.html', items=users_data)

@app.route('/candidate/<int:uid>')
def profile(uid):
    user_data = get_candidate(uid)
    return render_template("single.html", data=user_data)


@app.route('/search/<candidate_name>')
def that_name(candidate_name):
    user_data = get_candidates_by_name(candidate_name)
    return render_template("search.html", count=int(user_data[0]), liid = user_data[1], liname = user_data[2])

@app.route('/skill/<skill_name>')
def candidate_whith_skill(skill_name):
    user_data = get_candidates_by_skill(skill_name)
    return render_template('skill.html', count=int(user_data[0]), word=skill_name, liid = user_data[1], liname = user_data[2])

app.run()