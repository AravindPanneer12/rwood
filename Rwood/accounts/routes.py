from flask import render_template, request, Blueprint, flash, abort, redirect, url_for,jsonify

from Rwood.accounts.models import Account,Address,Rwood,IndustryInfo
from Rwood.accounts.schema import account_schema,accounts_schema, address_schema,addresses_schema, rwood_schema,rwoods_schema, industry_schema,industrys_schema
from Rwood import db
accounts = Blueprint('accounts', __name__)

@accounts.route("/")
def alldatas():
    item = Account.query.all()
    address= Address.query.all()
    rwood= Rwood.query.all()
    industryInfo= IndustryInfo.query.all()
    
    return render_template('accounts/home.html', items=item, address= address,rwood= rwood, industryInfo= industryInfo)





@accounts.route("/account", methods=["POST"])
def add_author():
    account_name =request.json["account_name"]
    account_alias =request.json["account_alias"]
    website =request.json["website"]
    account_owner =request.json["account_owner"]
    parent_account =request.json["parent_account"]
    account_number = request.json["account_number"]
    account_record_type =request.json["account_record_type"]
    annual_revenue = request.json["annual_revenue"]
    no_of_employees= request.json["no_of_employees"]
   

    account = Account.query.filter_by(account_name=account_name).first()
    if not account:
        

        new_account = Account(account_name=account_name,account_alias=account_alias, website=website,account_owner=account_owner,parent_account=parent_account, account_number=account_number, account_record_type=account_record_type, annual_revenue=annual_revenue, no_of_employees=no_of_employees)
        db.session.add(new_account)
        db.session.commit()
    else:
        return f"account_name with {account_name} is already present"

    return account_schema.jsonify(new_account)






@accounts.route("/address", methods=["POST"])
def add_address():
   
    region= request.json["region"]
    billing_address= request.json["billing_address"]
    phone= request.json["phone"]
    shipping_address= request.json["shipping_address"]
    fax= request.json["fax"]
    
    account_name = request.json["account_name"]

    account = Account.query.filter_by(account_name=account_name).first()
    if not account:
        flash('there is no account in the name')
   
    address_check= Address.query.filter_by(region=region,billing_address=billing_address,phone=phone,shipping_address=shipping_address,fax=fax)
    
    if address_check:
        return "values are already Present"

    new_address = Address(region=region,billing_address=billing_address,phone=phone,shipping_address=shipping_address,fax=fax, account_id=account.id)
    db.session.add(new_address)
    db.session.commit()

    return address_schema.jsonify(new_address)





@accounts.route("/rwood", methods=["POST"])
def add_rwood():
   
    KYC_docs= request.json["KYC_docs"]
    KYC_doc_data= request.json["KYC_doc_data"]
    refrence_check= request.json["refrence_check"]
    refrence_check_date= request.json["refrence_check_date"]
    commitment= request.json["commitment"]
    reliability= request.json["reliability"]

    
    account_name = request.json["account_name"]



    account = Account.query.filter_by(account_name=account_name).first()
    if not account:
        return f"No account name with {account_name} "

    

    rwood= Rwood.query.filter_by(KYC_docs=KYC_docs,KYC_doc_data=KYC_doc_data,refrence_check=refrence_check,refrence_check_date=refrence_check_date,commitment=commitment,reliability=reliability).first()

   
    
    if  rwood:
       return 'Values are already present'
    
    new_rwood = Rwood(KYC_docs=KYC_docs,KYC_doc_data=KYC_doc_data,refrence_check=refrence_check,refrence_check_date=refrence_check_date,commitment=commitment,reliability=reliability, account_id=account.id)
    db.session.add(new_rwood)
    db.session.commit()


    return rwood_schema.jsonify(new_rwood)







@accounts.route("/industry/add", methods=["POST"])
def add_industryinfo():

    under_group = request.json['under_group'],
    station_name = request.json['station_name'],
    expansion_setup= request.json['expansion_setup'],
    industry=request.json['industry'] ,
    sector= request.json['sector'],
    market_impression_rating=request.json['market_impression_rating'] ,
    annual_coal_requirement= request.json['annual_coal_requirement'] ,
    imported_volume_PA= request.json['imported_volume_PA'],
    imported_volume_from_indonesia_PA=request.json['imported_volume_from_indonesia_PA'] ,
    quantity_MT_monthly= request.json['quantity_MT_monthly'],
    production_Unit=request.json['production_Unit'] ,
    originiaze_import_break_up=request.json['originiaze_import_break_up'],
    port=request.json['port'] ,
    origin= request.json['origin'],
    account_name= request.json['account_name']
    account = Account.query.filter_by(account_name=account_name).first()
    if not account:
        return f"No account name with {account_name} "

    
   

    industry_info= IndustryInfo(under_group=under_group, station_name=station_name, expansion_setup=expansion_setup, industry=industry,sector=sector,market_impression_rating=market_impression_rating, annual_coal_requirement=annual_coal_requirement, imported_volume_PA=imported_volume_PA, imported_volume_from_indonesia_PA=imported_volume_from_indonesia_PA, quantity_MT_monthly=quantity_MT_monthly, production_Unit=production_Unit, originiaze_import_break_up=originiaze_import_break_up, port=port, origin=origin, account_id=account.id )

    db.session.add(industry_info)
    db.session.commit()

    return industry_schema.jsonify(industry_info)




#delte method
@accounts.route("/account/delete/<id>", methods=["DELETE"])
def delete_account(id):
    account= Account.query.get(id)
    db.session.delete(account)
    db.session.commit()

    return f"account id-{id} is deleted"



@accounts.route("/address/delete/<id>", methods=["DELETE"])
def delete_address(id):
    address= Address.query.get(id)
    db.session.delete(address)
    db.session.commit()

    return f"address id-{id} is deleted"



@accounts.route("/rwood/delete/<id>", methods=["DELETE"])
def delete_rwood(id):
    rwood= Rwood.query.get(id)
    db.session.delete(rwood)
    db.session.commit()

    return f"rwood id-{id} is deleted"


@accounts.route("/industry/delete/<id>", methods=["DELETE"])
def delete_industryInfo(id):
    industry= IndustryInfo.query.get(id)
    db.session.delete(industry)
    db.session.commit()

    return f"industry id-{id} is deleted"





@accounts.route("/rwood/<id>", methods=["PUT"])
def update_wood(id):
    update_wood = Rwood.query.get(id)
    if not update_wood:
        return jsonify({"message": "Book not found"}), 404

    KYC_docs= request.json["KYC_docs"]
    KYC_doc_data= request.json["KYC_doc_data"]
    refrence_check= request.json["refrence_check"]
    refrence_check_date= request.json["refrence_check_date"]
    commitment= request.json["commitment"]
    reliability= request.json["reliability"]

    
    account_name = request.json["account_name"]

    account = Account.query.filter_by(account_name=account_name).first()
    if not account:
        return f'account name with {account_name} is not present '


    KYC_docs= request.json["KYC_docs"]
    KYC_doc_data= request.json["KYC_doc_data"]
    refrence_check= request.json["refrence_check"]
    refrence_check_date= request.json["refrence_check_date"]
    commitment= request.json["commitment"]
    reliability= request.json["reliability"]


    update_wood.KYC_docs = KYC_docs
    update_wood.KYC_doc_data = KYC_doc_data
    update_wood.refrence_check = refrence_check
    update_wood.refrence_check_date = refrence_check_date
    update_wood.commitment = commitment
    update_wood.reliability = reliability
    update_wood.account_id= account.id
    db.session.commit()

    return rwood_schema.jsonify(update_wood)