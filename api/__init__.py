from app import app


## API Routes ##
from api.blueprints.users.views import users_api_blueprint
app.register_blueprint(users_api_blueprint, url_prefix='/api/v1/users')

from api.blueprints.login.views import login_api_blueprint
app.register_blueprint(login_api_blueprint, url_prefix='/api/v1/auth')

from api.blueprints.event.views import event_api_blueprint
app.register_blueprint(event_api_blueprint, url_prefix='/api/v1/event')

from api.blueprints.registration.views import registration_api_blueprint
app.register_blueprint(registration_api_blueprint, url_prefix='/api/v1/registration')

from api.blueprints.payment.views import payment_api_blueprint
app.register_blueprint(payment_api_blueprint, url_prefix='/api/v1/payment')



