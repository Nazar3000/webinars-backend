import subprocess

from Project_W.celery import app


@app.task(track_started=True)
def start_stream_file(video_path, stream_name, user_id):
    command = 'ffmpeg -re -i {file_path} ' \
              '-acodec copy -vcodec copy -f flv rtmp://stream.foxery.io/stream/{stream_name}?user_id={user_id}' \
        .format(file_path=video_path, stream_name=stream_name, user_id=user_id)
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    print(output, error)
