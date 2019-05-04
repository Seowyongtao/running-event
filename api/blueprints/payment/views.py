from flask import Blueprint, request, jsonify
import os
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity
)

import braintree

payment_api_blueprint = Blueprint('payment_api',
                                  __name__,
                                  template_folder='templates')

def transact(options):
    return gateway.transaction.sale(options)

def find_transaction(id):
    return gateway.transaction.find(id)

# todo add your own id and keys
gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id=os.environ.get("MERCHANT_ID"),
        public_key=os.environ.get("PUBLIC_KEY"),
        private_key=os.environ.get("PRIVATE_KEY")
    )
)

@payment_api_blueprint.route('/new', methods=['GET'])
@jwt_required
def new_checkout():
    client_token = gateway.client_token.generate()
    return jsonify(client_token=client_token)


@payment_api_blueprint.route('/checkouts', methods=['POST'])
@jwt_required
def create_checkout():
    
    amount = request.json.get("amount")
    nonce = request.json.get("nonce")
    

    result = transact({
        'amount': amount,
        'payment_method_nonce': nonce,
        'options': {
            "submit_for_settlement": True
        }
    })

    if result.is_success or result.transaction:
       
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "failed"})
