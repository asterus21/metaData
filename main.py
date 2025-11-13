import os
import cv2 as cv


PATH = r"D:/video/video/"


def get_video_duration(file_name: str) -> tuple:
    """Returns a number of frames and frames per second for a video file."""
    cap = cv.VideoCapture(file_name)
    frames_per_second = cap.get(cv.CAP_PROP_FPS)
    frames_count = int(cap.get(cv.CAP_PROP_FRAME_COUNT))

    return frames_count, frames_per_second


def main(folder):
    """Returns metadata for all video files in a folder."""
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
    data = []
    for file in files:
        frames_count, frames_per_second = get_video_duration(file)
        duration = frames_count / frames_per_second      
        data.append(
            ''.join(
                    [ 
                    file,
                    ', размер: ',
                    str(os.path.getsize(file) // (1024 ** 2)),
                    ' мб',
                    ', длительность: ',
                    str(int(duration / 60)), # minutes 
                    ':',
                    str(int(duration % 60)), # seconds
                    ]
                )
            )
    # print(data)
    # TODO: add Pandas to create a table of files data
    return data


if __name__ == '__main__':
    main(PATH)
