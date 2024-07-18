


if __name__ == "__main__":
    directory_path = "F:\\Video\\سریال\\Death note\\"
    file_list = os.listdir(directory_path)
    only_files = [f for f in file_list if isfile(join(directory_path, f))]
    full_paths = [os.path.join(directory_path, f) for f in only_files]
    for file in full_paths:
      
        video_path = file  # Replace with your video path
        print(video_path)
        combined_image = process_video(video_path)

        # Display the combined image (optional)
        # cv2.imshow("Dominant Colors", combined_image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        # Save the combined image (optional)
        cv2.imwrite(r"DeathNote/%s.jpg"%(Path(video_path).stem), combined_image)
        print()
import winsound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)
