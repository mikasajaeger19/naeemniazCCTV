#!/bin/bash

# Activate Python virtual environment if you have one
# source venv/bin/activate

# Function to run the camera learning script
run_camera_learning() {
    echo "Starting camera learning script..."
    python3 cameralearning.py &
    CAMERA_PID=$!
    echo "Camera learning script is running with PID: $CAMERA_PID"
}

# Function to run the Flask gallery API
run_gallery_api() {
    echo "Starting Flask gallery API..."
    python3 app.py &
    FLASK_PID=$!
    echo "Flask gallery API is running with PID: $FLASK_PID"
}

# Function to clean up processes on exit
cleanup() {
    echo "Stopping camera learning script..."
    kill $CAMERA_PID
    echo "Stopping Flask gallery API..."
    kill $FLASK_PID
    echo "All processes stopped."
}

# Run both functions in the background
run_camera_learning
run_gallery_api

# Wait for any process to exit
wait $CAMERA_PID $FLASK_PID

# Perform cleanup if any process exits
cleanup
