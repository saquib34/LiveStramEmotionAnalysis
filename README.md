# 🎭 Live Stream Emotion Detection with face-api.js 📹

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![face-api.js](https://img.shields.io/badge/face--api.js-v0.22.2-blue)](https://github.com/justadudewhohacks/face-api.js)
[![hls.js](https://img.shields.io/badge/hls.js-v1.3.5-green)](https://github.com/video-dev/hls.js)

## 📝 Description

This project demonstrates real-time emotion detection in a live video stream using face-api.js and hls.js. It detects faces in an HLS video stream, identifies their emotions, and overlays the results on the video with bounding boxes and detailed emotion statistics displayed below.

![Project Demo](https://via.placeholder.com/800x400?text=Emotion+Detection+Demo)

## ✨ Features

- 🔍 **Real-Time Detection**: Detects faces and their emotions in a live video stream every 200ms
- 🎨 **Visual Feedback**: Draws colored bounding boxes around faces with the dominant emotion labeled
- 📊 **Emotion Stats**: Displays detailed probability bars for each emotion per detected face
- 🎛️ **User Controls**: Start/stop detection and toggle fullscreen mode
- 📱 **Responsive Design**: Adapts to different screen sizes and devices

## 🧠 Emotions Detected

- 😐 Neutral
- 😊 Happy
- 😢 Sad
- 😠 Angry
- 😨 Fearful
- 🤢 Disgusted
- 😲 Surprised

## 🛠️ Prerequisites

To run this project, ensure you have the following:

- A modern web browser (e.g., Chrome, Firefox, Edge) supporting HTML5 and JavaScript ES6+
- A web server to serve the HTML file and model files (e.g., http-server, live-server, or any local server)
- An internet connection to load the external libraries (face-api.js and hls.js) and the demo stream

## 📦 Setup

Before running the project, you need to set up the face-api.js models:

### 1️⃣ Download Models:
- Visit the [face-api.js models repository](https://github.com/justadudewhohacks/face-api.js-models)
- Download the pre-trained models (tiny_face_detector and face_expression_net)
- Extract the files into a `models` directory at the root of your web server (e.g., `/path/to/server/models/`)

### 2️⃣ Verify Directory Structure:
Your server should have:
```
/your-server-root/
  ├── index.html
  └── models/
      ├── tiny_face_detector_model-weights_manifest.json
      ├── tiny_face_detector_model-shard1
      ├── face_expression_net-weights_manifest.json
      └── face_expression_net-shard1
```

### 3️⃣ Serve the Files:
Ensure your web server serves both the index.html file and the models directory correctly.

## 🚀 Usage

Follow these steps to run the project:

### 1️⃣ Clone or Download:
Clone this repository or download the index.html file to your local machine:
```bash
git clone https://github.com/saquib34/LiveStramEmotionAnalysis
```

### 2️⃣ Serve the Project:
Use a local web server to serve the files. For example, with http-server:
```bash
npm install -g http-server
cd /path/to/your-server-root
http-server -p 8080
```

### 3️⃣ Access in Browser:
Open your browser and navigate to http://localhost:8080.

### 4️⃣ Interact with the Application:
- **Wait for Initialization**: A loading screen appears while libraries and models load
- **Start Detection**: Once the "Stream ready!" message appears, click "Start Detection" to begin
- **View Results**: Faces are boxed with their dominant emotion, and emotion stats appear below the video
- **Stop Detection**: Click "Stop Detection" to pause the process
- **Fullscreen**: Click "Fullscreen" to expand the video view

## 📚 Libraries Used

This project relies on the following libraries:

- **[face-api.js](https://github.com/justadudewhohacks/face-api.js)**: Provides face detection and emotion recognition capabilities
- **[hls.js](https://github.com/video-dev/hls.js/)**: Enables HLS (HTTP Live Streaming) video playback in the browser

## 🖥️ UI Components

The user interface is structured as follows:

- **Header**: Displays the title "Live Stream Emotion Detection with face-api.js"
- **Status**: A dynamic message showing the current state (e.g., "Initializing...", "Stream ready!", "Running emotion detection...")
- **Controls**:
  - Start Detection Button: Initiates the detection process
  - Stop Detection Button: Pauses the detection (disabled until detection starts)
  - Fullscreen Button: Toggles fullscreen mode for the video container
- **Video Container**:
  - Video Element: Plays the live HLS stream
  - Overlay Canvas: Renders bounding boxes and emotion labels over the video
- **Emotion Stats**: Shows detailed emotion probabilities for each detected face in card-like sections

### UI Diagram

```mermaid
graph TD
    A[Body] --> B[Header<br>Title]
    A --> C[Container]
    C --> D[Status<br>Message]
    C --> E[Controls]
    E --> F[Start Detection<br>Button]
    E --> G[Stop Detection<br>Button]
    E --> H[Fullscreen<br>Button]
    C --> I[Video Container]
    I --> J[Video Element]
    I --> K[Overlay Canvas]
    C --> L[Emotion Stats<br>Face Cards]
```

## ⚙️ How It Works

The application operates as follows:

### Initialization:
- Loads face-api.js models (TinyFaceDetector and FaceExpressionNet) from the `/models` directory
- Uses hls.js to initialize the HLS stream in the video element

### Detection Process:
- When "Start Detection" is clicked, a loop runs every 200ms:
  - Detects faces using TinyFaceDetector
  - Analyzes emotions with FaceExpressionNet
  - Draws bounding boxes on the overlay canvas, colored by the dominant emotion (e.g., yellow for "happy")
  - Labels each box with the dominant emotion and its probability
  - Updates the emotion stats section with probability bars for all emotions per face

### User Interaction:
- Stop detection clears the loop and overlay
- Fullscreen toggles the video container's size

## 🔧 Customization

You can modify the project to suit your needs:

### Change Stream URL:
Edit the streamUrl variable in the `<script>` section:
```javascript
const streamUrl = "https://your-custom-stream-url.m3u8";
```
Ensure the stream is an HLS-compatible .m3u8 file.

### Adjust Detection Settings:
Modify the TinyFaceDetectorOptions in the startDetection function:
```javascript
const options = new faceapi.TinyFaceDetectorOptions({
  inputSize: 416, // Adjust input size (e.g., 224, 512)
  scoreThreshold: 0.5 // Adjust confidence threshold (0.0 to 1.0)
});
```

### Detection Frequency:
Change the interval in setInterval:
```javascript
detectionInterval = setInterval(async () => { ... }, 200); // e.g., 500 for 500ms
```

### Emotion Colors:
Update the emotionColors object:
```javascript
const emotionColors = {
  neutral: '#A9A9A9',
  happy: '#FFD700',
  sad: '#6495ED',
  angry: '#FF6347',
  fearful: '#9932CC',
  disgusted: '#8FBC8F',
  surprised: '#FF69B4'
};
```

## 🔍 Performance Tips

- **Resolution Trade-offs**: Lower the input size for faster detection but potentially less accuracy
- **Detection Interval**: Increase the interval between detections (e.g., 500ms) to reduce CPU usage
- **Frame Rate**: Consider setting a maximum frame rate using requestAnimationFrame instead of setInterval
- **Mobile Devices**: On mobile, use a smaller input size (224) and a longer interval (500ms)

## 🐛 Troubleshooting

- **"Error loading models"**:
  - Ensure the models directory is correctly placed and accessible at `http://your-server/models/`
  - Check network tab in browser developer tools for 404 errors

- **"Stream error"**:
  - Verify the streamUrl is a valid, accessible HLS stream
  - Make sure your browser supports HLS or is properly falling back to hls.js

- **No detection**:
  - Check browser console for errors (Ctrl+Shift+J) and ensure the video is playing
  - Verify that face-api.js models are loading correctly
  - Try with a different stream or webcam input

- **Performance issues**:
  - Reduce detection frequency by increasing the interval
  - Lower the inputSize in TinyFaceDetectorOptions
  - Close other browser tabs and applications

## 🔮 Future Enhancements

- **Webcam Support**: Add option to use local camera instead of HLS stream
- **Multiple Model Support**: Add option to switch between different face detection models
- **Recording**: Save detection sessions as video files
- **Emotion Analytics**: Track and display emotion changes over time
- **Multiple Face Tracking**: Maintain identity across frames for consistent tracking
- **Custom Emotion Thresholds**: Allow users to set sensitivity for different emotions

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.

Note: The external libraries (face-api.js and hls.js) have their own licenses. Refer to their repositories for more information:

- [face-api.js License](https://github.com/justadudewhohacks/face-api.js/blob/master/LICENSE)
- [hls.js License](https://github.com/video-dev/hls.js/blob/master/LICENSE)

## 👨‍💻 Contributors

-*Saquib* - (https://github.com/sauib34)

## 🙏 Acknowledgments

- [Vincent Mühler](https://github.com/justadudewhohacks) for creating face-api.js
- [The hls.js team](https://github.com/video-dev/hls.js/graphs/contributors) for their excellent streaming library
- All contributors and testers who helped improve this project

---

📥 **Got questions or suggestions?** Open an issue or submit a pull request!

💖 **Enjoy detecting emotions in live streams!**
