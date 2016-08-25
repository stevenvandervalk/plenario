from collections import defaultdict
from flask import redirect, render_template
from flask_admin import Admin, AdminIndexView, expose
from flask_admin.menu import MenuLink, url_for
from flask_login import current_user

from plenario.database import session
from plenario.sensor_network.sensor_models import FeatureOfInterest
from plenario.sensor_network.sensor_models import NetworkMeta, NodeMeta, Sensor

from admin_view import admin_views
from views import blueprint, redis


class ApiaryIndexView(AdminIndexView):

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("auth.login"))
    
    @expose("/")
    def index(self):
        errors = defaultdict(list)
        for key in redis.scan_iter(match="AOTMapper_*"):
            errors[key].append(redis.get(key))
        return self.render("apiary/index.html", errors=errors)


admin = Admin(
    index_view=ApiaryIndexView(url="/apiary"),  
    name="Plenario",
    template_mode="bootstrap3",
    url="/apiary",
)

admin.add_view(admin_views["FOI"](FeatureOfInterest, session))
admin.add_view(admin_views["Sensor"](Sensor, session))
admin.add_view(admin_views["Network"](NetworkMeta, session))
admin.add_view(admin_views["Node"](NodeMeta, session))

apiary = admin  
apiary_bp = blueprint
