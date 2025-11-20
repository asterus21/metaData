import pandas
import os
import cv2


PATH = r"D:/video/video/"


def get_frames(file_name: str) -> float:
    """Returns a number of frames as the number of frames per second of the video."""
    video_capture = cv2.VideoCapture(file_name)
    frames_count = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
    frames_per_second = video_capture.get(cv2.CAP_PROP_FPS)
    duration = frames_count / frames_per_second

    return duration


def get_video_duration(duration: float) -> str:
    """Returns a video duration."""
    length = ':'.join([
        str(int(duration / 60)),  # minutes
        str(int(duration % 60))   # seconds
    ])

    return length


def get_files_list(folder: str) -> list:
    """Checks the files in hand, i.e. whether they exist and their type."""
    try:
        os.path.exists(folder)
        number_of_files = len(os.listdir(folder))
        if number_of_files == 0:
            raise Exception("Error: the folder is empty.")
    except FileNotFoundError:
        raise Exception("Error: the folder not found or empty.")
    files = [
        folder + os.listdir(folder)[i] for i in range(number_of_files)
    ]
    for file in files:
        if not file.endswith('.mov'):
            raise Exception('Error: the file(s) format is not supported. All files must be of the same format, e.g. "video.mov"')
    
    return files


def export_data(files: list) -> pandas.DataFrame:
    """Exports metadata for all video files into a CSV file."""    
    data = [file for file in files]
    size = [str(os.path.getsize(file) // (1024 ** 2)) + " мб." for file in files]
    length = [get_video_duration(get_frames(file)) for file in files]
    table = pandas.DataFrame({
        'File': data,
        'Size': size,
        'Duration': length
    })

    table.index += 1
    table.to_csv('video_metadata.csv', index=True, index_label='#')

    return table


def main(files: list) -> list:
    """Returns metadata for all video files in a folder."""    
    data = []
    for file in files:
        size = str(os.path.getsize(file) // (1024 ** 2))
        duration = get_video_duration(get_frames(file))
        data.append(
            ''.join(
                [
                    file,
                    ', размер: ',
                    size,
                    ' мб',
                    ', длительность: ',
                    duration
                ]
            )
        )    
    # print(data)
    return data


if __name__ == '__main__':    
    main(get_files_list(PATH))
    # export_data(get_files_list(PATH))
