from app import create_app
from models import db, Organization, User, Template, Campaign, Target
from utils.tokens import generate_tracking_token

app = create_app()

with app.app_context():
    # Create the provider organization (Pwn & Patch)
    provider = Organization(name='Pwn & Patch', domain='pwnandpatch.com', type='provider')
    db.session.add(provider)
    db.session.commit()

    # Create a test client organization
    client = Organization(name='Test Bank', domain='testbank.tn', type='client')
    db.session.add(client)
    db.session.commit()

    # Create a consultant user under Pwn & Patch
    consultant = User(
        username='consultant1',
        email='consultant@pwnandpatch.com',
        password_hash='placeholder_will_hash_later',
        role='consultant',
        organization_id=provider.id
    )
    db.session.add(consultant)
    db.session.commit()

    # Create a simple test template
    template = Template(
        name='CNSS Test',
        institution='CNSS',
        language='fr',
        subject='Votre déclaration est en attente',
        html_content='<p>Cliquez ici pour régulariser votre déclaration.</p>',
        landing_page='cnss_login'
    )
    db.session.add(template)
    db.session.commit()

    # Create a campaign for the test client
    campaign = Campaign(
        name='Test Campaign',
        organization_id=client.id,
        template_id=template.id,
        created_by=consultant.id,
        status='draft',
        authorized=True
    )
    db.session.add(campaign)
    db.session.commit()

    # Create one test target with a secure tracking token
    target = Target(
        campaign_id=campaign.id,
        organization_id=client.id,
        first_name='Ahmed',
        last_name='Ben Ali',
        email='ahmed@testbank.tn',
        department='Finance',
        tracking_token=generate_tracking_token()
    )
    db.session.add(target)
    db.session.commit()

    print('Seed data created successfully.')
    print(f'Target created: {target.first_name} {target.last_name}')
    print(f'Tracking token: {target.tracking_token}')