from imageai.Detection import VideoObjectDetection
import os

execution_path = "C:\\Users\\Rafos\Downloads"

detector = VideoObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "retinanet_resnet50_fpn_coco-eeacb38b.pth"))
detector.loadModel()

video_path = detector.detectObjectsFromVideo(input_file_path=os.path.join(execution_path, "TheaterSquare_1920x1080.mp4"),
                                output_file_path=os.path.join(execution_path, "Result_TheaterSquare_1920x1080")
                                , frames_per_second=20, log_progress=True)
print(video_path)