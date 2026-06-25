from flask import Blueprint, request
from datetime import datetime
from models import db, Target, Event

# A Blueprint groups related routes into one module
tracking_bp = Blueprint('tracking', __name__)


@tracking_bp.route('/track/click/<token>')
def track_click(token):
    # Find the target by their unique tracking token
    target = Target.query.filter_by(tracking_token=token).first()

    # If the token matches no one, reveal nothing useful
    if not target:
        return 'Not found', 404

    # Record the click event
    event = Event(
        target_id=target.id,
        campaign_id=target.campaign_id,
        organization_id=target.organization_id,
        event_type='clicked',
        ip_address=request.remote_addr,
        user_agent=request.headers.get('User-Agent'),
        timestamp=datetime.utcnow()
    )
    db.session.add(event)
    db.session.commit()

    # For now, confirm it worked (later this redirects to the fake landing page)
    return f'Click recorded for {target.first_name} {target.last_name}.'