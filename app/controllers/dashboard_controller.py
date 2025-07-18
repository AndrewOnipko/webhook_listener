from flask import Blueprint, render_template
from app.models.push_event import PushEvent
from app.logger import simple_logger

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/dashboard")
@simple_logger
def dashboard():
    commits = PushEvent.get_all_desc()
    return render_template("dashboard.html", commits=commits)