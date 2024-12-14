from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from ..forms import TrackerForm, TrackerEntryForm
from ..models import Tracker, TrackerEntry
from ..extensions import db

bp = Blueprint('tracker', __name__)

@bp.route('/dashboard')
@login_required
def dashboard():
    trackers = current_user.trackers.all()
    return render_template('tracker/dashboard.html', trackers=trackers)

@bp.route('/tracker/create', methods=['GET', 'POST'])
@login_required
def create_tracker():
    form = TrackerForm()
    if form.validate_on_submit():
        tracker = Tracker(name=form.name.data, 
                          description=form.description.data, 
                          user_id=current_user.id)
        db.session.add(tracker)
        db.session.commit()
        flash('Tracker created successfully!', 'success')
        return redirect(url_for('tracker.dashboard'))
    return render_template('tracker/create_tracker.html', form=form)

@bp.route('/tracker/<int:tracker_id>/add_entry', methods=['GET', 'POST'])
@login_required
def add_entry(tracker_id):
    tracker = Tracker.query.get_or_404(tracker_id)
    
    # Ensure the current user owns the tracker
    if tracker.owner != current_user:
        flash('You do not have permission to add entries to this tracker.', 'danger')
        return redirect(url_for('tracker.dashboard'))

    form = TrackerEntryForm()
    if form.validate_on_submit():
        entry = TrackerEntry(
            tracker_id=tracker.id, 
            value=form.value.data, 
            note=form.note.data
        )
        db.session.add(entry)
        db.session.commit()
        flash('Entry added successfully!', 'success')
        return redirect(url_for('tracker.view_tracker', tracker_id=tracker.id))
    
    return render_template('tracker/add_entry.html', form=form, tracker=tracker)

@bp.route('/tracker/<int:tracker_id>')
@login_required
def view_tracker(tracker_id):
    tracker = Tracker.query.get_or_404(tracker_id)
    
    # Ensure the current user owns the tracker
    if tracker.owner != current_user:
        flash('You do not have permission to view this tracker.', 'danger')
        return redirect(url_for('tracker.dashboard'))

    entries = tracker.entries.order_by(TrackerEntry.timestamp.desc()).all()
    return render_template('tracker/view_tracker.html', tracker=tracker, entries=entries)
