from Rwood.accounts.models import Account,Address,Rwood, IndustryInfo
from flask_marshmallow import Marshmallow


ma= Marshmallow()
class AccountSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Account

   


class AddressSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Address
        include_fk = True


class RwoodSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Rwood
        include_fk = True



class IndustrySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = IndustryInfo
        include_fk = True

account_schema= AccountSchema()
accounts_schema=AccountSchema(many=True)

address_schema= AddressSchema()
addresses_schema=AddressSchema(many=True)

rwood_schema= RwoodSchema()
rwoods_schema=RwoodSchema(many=True)



industry_schema= IndustrySchema()
industrys_schema= IndustrySchema(many=True)