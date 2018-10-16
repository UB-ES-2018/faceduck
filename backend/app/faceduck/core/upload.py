from werkzeug.utils import secure_filename
import uuid
import os


def upload_media(file, save_path, host_url):
    filename = str(uuid.uuid4()) + "-" + secure_filename(file.filename)
    file.save(os.path.join(save_path, filename))

    return_url = host_url + "media/" + filename

    return {
        "media-url": return_url
    }

