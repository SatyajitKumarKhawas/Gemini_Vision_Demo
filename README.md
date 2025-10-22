## 🖼️ Gemini Image + Text Demo

An interactive **Streamlit app** that uses **Google Gemini 2.5 Flash** to analyze images and answer text prompts.
Users can upload an image, optionally add a question, and get a smart AI-generated response.

---

### 🚀 Features

* Accepts **image uploads** (`.jpg`, `.jpeg`, `.png`)
* Optional **text input** for context-based responses
* Uses **Gemini 2.5 Flash** for multimodal (image + text) generation
* Simple and responsive Streamlit interface

---

### ⚙️ Setup Instructions

#### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/Gemini_Vision_Demo.git

```

#### 2️⃣ Install dependencies

```bash
pip install streamlit google-generativeai python-dotenv
```

#### 3️⃣ Create a `.env` file

```
GOOGLE_API_KEY=your_api_key_here
```

#### 4️⃣ Run the app

```bash
streamlit run app.py
```

---

### 💡 How It Works

1. Upload an image (e.g., a photo, chart, object, etc.).
2. Optionally enter a text query like *“Describe this image”* or *“What object is shown?”*.
3. Click **Ask Gemini** — the model will respond with insights.

---

### 🧠 Example Use Cases

* Image description or captioning
* Object or scene understanding
* Visual question answering

---

### 📁 Project Structure

```
app.py
.env
requirements.txt
README.md
```

---

### 👨‍💻 Author

**Satyajit Kumar Khawas**

