from flask_restful import Api
from app import app
from app.resources.booking_resource import *
from app.resources.category_resource import *
from app.resources.role_resource import *
from app.resources.event_resource import *
from app.resources.user_resource import *
from app.resources.auth_resource import *

api = Api(app, prefix='/api/v1') 


api.add_resource(RoleResource, '/roles')
api.add_resource(ManageRoleResource, '/roles/<int:role_id>')

api.add_resource(UserResource, '/users')
api.add_resource(ManageUserResource, '/users/<int:user_id>')


api.add_resource(CategoryResource, '/categories')
api.add_resource(ManageCategoryResource, '/categories/<int:category_id>')

api.add_resource(EventResource, '/events')
api.add_resource(ManageEventResource, '/events/<int:event_id>')

api.add_resource(BookingResource, '/bookings')
api.add_resource(ManageBookingResource, '/bookings/<int:booking_id>')

api.add_resource(LoginResource, '/api/v1/auth/login')