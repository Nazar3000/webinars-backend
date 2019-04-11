import subprocess

from Project_W.celery import app


@app.task(track_started=True)
def start_stream_file(video_path, stream_name, user_id):
    dest_path = video_path.split('.')[0] + '.flv'
    convert_to_mp4_command = 'ffmpeg -y -i {file_path} -c:v libx264 -ar 22050 -crf 19 {dest_path}'.format(
        file_path=video_path,
        dest_path=dest_path
    )

    convert_process = subprocess.Popen(convert_to_mp4_command.split(), stdout=subprocess.PIPE)
    convert_process.wait()

    command = 'ffmpeg -re -i {file_path} ' \
              '-acodec copy -vcodec copy -f flv rtmp://stream.foxery.io/stream/{stream_name}?user_id={user_id}' \
        .format(file_path=dest_path, stream_name=stream_name, user_id=user_id)
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    print(output, error)
