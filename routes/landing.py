from flask import Blueprint, request, render_template, redirect
from datetime import datetime
from models import db, Target, Event

landing_bp = Blueprint('landing', __name__, template_folder='../landing_pages')


@landing_bp.route('/landing/<token>')
def landing_page(token):
    # Find the target by their unique tracking token
    target = Target.query.filter_by(tracking_token=token).first()

    if not target:
        return 'Not found', 404

    return render_template('cnss_login.html', token=token)


@landing_bp.route('/landing/submit/<token>', methods=['POST'])
def landing_submit(token):
    # Find the target by their token
    target = Target.query.filter_by(tracking_token=token).first()

    if not target:
        return 'Not found', 404

    # SECURITY: We record that a submission happened.
    # We do NOT store the username or password the employee typed.
    event = Event(
        target_id=target.id,
        campaign_id=target.campaign_id,
        organization_id=target.organization_id,
        event_type='submitted',
        ip_address=request.remote_addr,
        user_agent=request.headers.get('User-Agent'),
        timestamp=datetime.utcnow()
    )
    db.session.add(event)
    db.session.commit()

    return redirect('/awareness')