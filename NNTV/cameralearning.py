import torch
import cv2
import datetime
import os

# Create the 'images' folder if it doesn't exist
if not os.path.exists('images'):
    os.makedirs('images')

# Load the YOLOv5 model (you can replace 'yolov5s.pt' with 'yolov5m.pt', 'yolov5l.pt', or 'yolov5x.pt' for larger models)
model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5s.pt')  # Adjust the path if needed

# Initialize the video capture object
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Perform inference with YOLOv5
    results = model(frame)
    
    # Process the results
    for detection in results.xyxy[0]:
        x1, y1, x2, y2, conf, cls = detection  # Extract bounding box and confidence
        label = model.names[int(cls)]  # Get the class label
        
        if label == 'person':  # Only consider detections labeled as 'person'
            # Draw bounding box around detected person
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            
            # Log the event with a timestamp
            with open("log.txt", "a") as log:
                log.write(f"Human detected at {datetime.datetime.now()} with confidence {conf:.2f}\n")
            
            # Save the frame as an image file in the 'images' folder
            image_path = f"images/human_detected_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
            cv2.imwrite(image_path, frame)
    
    # Display the video feed with detected people highlighted
    cv2.imshow("Human Detection", frame)
    
    # Exit the loop if the user presses 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()
