from datetime import datetime
from flask import request
from flask_restful import Resource
from flasgger import swag_from
from core import Config
from core.bases import decorators
from .models import Nanny, db


class NannyResource(Resource):
    method_decorators = (decorators.exception_catcher_decorator, decorators.cors_decorator)

    @swag_from(Config.SWAGGER_FORMS + "nanny_get.yml")
    def get(self):
        query = db.session.query(Nanny)
        if "place" in request.args:
            query = query.filter(Nanny.place.ilike(f"%{request.args['place']}%"))
        if "animal" in request.args:
            query = query.filter(Nanny.animal == request.args['animal'])
        if "min_practice" in request.args:
            query = query.filter(Nanny.practice >= int(request.args['min_practice']))
        if "max_practice" in request.args:
            query = query.filter(Nanny.practice <= int(request.args['max_practice']))
        if "min_rate" in request.args:
            query = query.filter(Nanny.rate >= int(request.args['min_rate']))
        if "max_rate" in request.args:
            query = query.filter(Nanny.rate <= int(request.args['max_rate']))

        page = int(request.args.get("page", 1))
        page_size = int(request.args.get("page_size", 5))
        offset = (page - 1) * page_size

        query = query.offset(offset)
        query = query.limit(page_size)
        nannies = query.all()
        res = [nanny.serialize() for nanny in nannies]
        return res, 200

    @swag_from(Config.SWAGGER_FORMS + "nanny_post.yml")
    def post(self):
        file_res = request.files["photo"].filename.split(".")[-1]
        if file_res not in ("png", "jpg", "jpeg"):
            return "File must be an image.", 400

        nanny = Nanny(
            name=request.form["name"],
            animal=request.form["animal"],
            birthday=datetime.strptime(request.form["birthday"], "%Y-%m-%d").date(),
            place=request.form["place"],
            rate=int(request.form["rate"]),
            practice=int(request.form["practice"]),
            contact=request.form["contact"],
            about=request.form.get("about")
        )
        db.session.add(nanny)
        db.session.commit()

        request.files["photo"].save(Config.UPLOAD_FOLDER + f"nanny-photo-{nanny.id}.{file_res}")
        nanny.photo = f"{request.url_root}file/nanny-photo-{nanny.id}.{file_res}"
        db.session.add(nanny)
        db.session.commit()

        return nanny.serialize(), 201
