import file_ops

def register(app):

    @app.route('/create/<file_name>', methods=["POST"])
    def create(file_name):
        file_ops.create_file(file_name)
        return "I created file {}".format(file_name)

    @app.route('/read/<file_name>', methods=["POST"])
    def read(file_name):
        return file_ops.read_file(file_name)

    @app.route('/update/<file_name>/<content>', methods=["POST"])
    def update(file_name, content):
        file_ops.update_file(file_name, content)
        return "file: {} content: {}".format(file_name, content)

    @app.route('/delete/<file_name>', methods=["POST"])
    def delete(file_name):
        file_ops.delete_file(file_name)
        return "file deleted {}".format(file_name)