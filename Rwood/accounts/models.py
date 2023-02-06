from Rwood import db







class Account(db.Model):
    id=db.Column(db.Integer(), primary_key=True)
    account_name =db.Column(db.String(length=100), nullable=False)
    account_alias =db.Column(db.String(length=100), nullable=False)
    website =db.Column(db.String(length=100), nullable=False)
    account_owner =db.Column(db.String(length=100), nullable=False)
    parent_account =db.Column(db.String(length=100), nullable=False)
    account_number = db.Column(db.Integer(), nullable=False)
    account_record_type =db.Column(db.String(length=100), nullable=False)
    annual_revenue = db.Column(db.Integer(), nullable=False)
    no_of_employees= db.Column(db.Integer(), nullable=False)
    address = db.relationship('Address', backref='account')
    rwoodreference=db.relationship('Rwood', backref='account')
    industryinfo= db.relationship('IndustryInfo', backref='account')

   



class Address(db.Model):
    id=db.Column(db.Integer(), primary_key=True)
    region=db.Column(db.String(length=100), nullable=False)
    billing_address=db.Column(db.String(length=100), nullable=False)
    phone=db.Column(db.String(length=100), nullable=False)
    shipping_address=db.Column(db.String(length=100), nullable=False)
    fax=db.Column(db.String(length=100), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'))





class Rwood(db.Model):
    id=db.Column(db.Integer(), primary_key=True)
    KYC_docs=db.Column(db.String(length=100), nullable=False)
    KYC_doc_data=db.Column(db.String(length=100), nullable=False)
    refrence_check=db.Column(db.String(length=100), nullable=False)
    refrence_check_date=db.Column(db.String(length=100), nullable=False)
    commitment=db.Column(db.String(length=100), nullable=False)
    reliability=db.Column(db.String(length=100), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'))



class IndustryInfo(db.Model):
    id=db.Column(db.Integer(), primary_key=True)

    under_group=db.Column(db.String(length=100) )
    station_name=db.Column(db.String(length=100))
    expansion_setup=db.Column(db.String(length=100))
    industry=db.Column(db.String(length=100))
    sector=db.Column(db.String(length=100))
    market_impression_rating=db.Column(db.String(length=100))
    annual_coal_requirement=db.Column(db.String(length=100))
    imported_volume_PA=db.Column(db.String(length=100))
    imported_volume_from_indonesia_PA =db.Column(db.String(length=100))
    quantity_MT_monthly=db.Column(db.String(length=100))
    production_Unit=db.Column(db.String(length=100))
    originiaze_import_break_up=db.Column(db.String(length=100))
    port=db.Column(db.String(length=100))
    origin=db.Column(db.String(length=100))
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'))