# app/routes/api.py
from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from ..models import Tracker, TrackerEntry
from ..extensions import db

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/trackers', methods=['GET'])
@login_required
def get_trackers():
    trackers = current_user.trackers.all()
    return jsonify([
        {
            'id': tracker.id, 
            'name': tracker.name, 
            'description': tracker.description
        } for tracker in trackers
    ])

@bp.route('/tracker/<int:tracker_id>/entries', methods=['GET'])
@login_required
def get_tracker_entries(tracker_id):
    tracker = Tracker.query.get_or_404(tracker_id)
    
    # Ensure the current user owns the tracker
    if tracker.owner != current_user:
        return jsonify({'error': 'Unauthorized'}), 403

    entries = tracker.entries.order_by(TrackerEntry.timestamp.desc()).all()
    return jsonify([
        {
            'id': entry.id,
            'value': entry.value,
            'note': entry.note,
            'timestamp': entry.timestamp.isoformat()
        } for entry in entries
    ])
