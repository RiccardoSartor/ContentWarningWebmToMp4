from moviepy.editor import VideoFileClip

def convert_webm_to_mp4(input_file, output_file):
    clip = VideoFileClip(input_file)
    clip.write_videofile(output_file)

#convert_webm_to_mp4("input.webm", "output.mp4")