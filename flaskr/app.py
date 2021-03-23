from config import app, api
from res.UserRes import UserResource as User
from res.UsersRes import UsersResource as Users


api.add_resource(Users,
                 '/users')
api.add_resource(User,
                 '/users/<int:id>')


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
