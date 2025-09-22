# 🛠️ Setup Guide - Make It 100% Functional

## 🚨 **Current Status: 80-90% Functional**

The platform works well, but needs some setup to be 100% production-ready.

## 📋 **Quick Setup (15 minutes)**

### **Option 1: Minimal Setup (Works Immediately)**
```bash
# 1. Install Python dependencies
pip install -r requirements.txt

# 2. Run the app
streamlit run app.py

# 3. Enter API keys in the sidebar
# 4. Start generating videos!
```

**What works**: AI analysis, content generation, fallback video creation  
**What's limited**: 3D rendering (uses fallback videos)

### **Option 2: Full 3D Setup (30 minutes)**

#### **Step 1: Install Blender**
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install blender

# macOS
brew install blender

# Windows
# Download from https://www.blender.org/download/

# Verify installation
blender --version
```

#### **Step 2: Install FFmpeg**
```bash
# Ubuntu/Debian
sudo apt install ffmpeg

# macOS
brew install ffmpeg

# Windows
# Download from https://ffmpeg.org/download.html

# Verify installation
ffmpeg -version
```

#### **Step 3: Run Full App**
```bash
streamlit run app.py
```

## 🔧 **Troubleshooting Common Issues**

### **Issue 1: "Blender not found"**
**Solution**: Install Blender and add to PATH
```bash
# Check if Blender is in PATH
which blender

# If not found, add to PATH
export PATH="/path/to/blender:$PATH"
```

### **Issue 2: "FFmpeg not found"**
**Solution**: Install FFmpeg
```bash
# Install FFmpeg
sudo apt install ffmpeg  # Ubuntu
brew install ffmpeg      # macOS

# Verify
ffmpeg -version
```

### **Issue 3: "API key errors"**
**Solution**: Get API keys
1. **OpenAI**: https://platform.openai.com/api-keys
2. **Google**: https://makersuite.google.com/app/apikey

### **Issue 4: "Permission denied"**
**Solution**: Fix file permissions
```bash
chmod +x app.py
mkdir -p output
chmod 755 output
```

## 🚀 **Production Deployment**

### **Docker Setup (Recommended)**
```bash
# Build Docker image
docker build -t 3d-video-edu .

# Run container
docker run -p 8501:8501 \
  -e OPENAI_API_KEY=your-key \
  -e GOOGLE_API_KEY=your-key \
  3d-video-edu
```

### **Cloud Deployment**
```bash
# Deploy to Streamlit Cloud
streamlit run app.py

# Or use the provided Docker configuration
docker-compose up -d
```

## 📊 **Performance Optimization**

### **For Better 3D Rendering**
1. **Use GPU acceleration** (if available)
2. **Increase memory limits** for Blender
3. **Use lower resolution** for faster rendering
4. **Enable caching** for repeated generations

### **For Better Video Quality**
1. **Use FFmpeg** for video processing
2. **Enable hardware acceleration**
3. **Optimize compression settings**
4. **Use appropriate codecs**

## 🎯 **Testing the Platform**

### **Test 1: Basic Functionality**
1. Open the app
2. Enter API keys
3. Select a topic (e.g., "Photosynthesis")
4. Click "Generate 3D Video"
5. Check if video is created

### **Test 2: 3D Rendering**
1. Ensure Blender is installed
2. Try a physics topic (e.g., "Gravity")
3. Check if 3D scene is generated
4. Verify video output

### **Test 3: Error Handling**
1. Try without API keys
2. Try with invalid topic
3. Check error messages
4. Verify fallback behavior

## 🔍 **Monitoring and Debugging**

### **Check System Status**
The app includes a system status checker in the sidebar that shows:
- ✅ Python (always working)
- ✅/❌ Blender (depends on installation)
- ✅/❌ FFmpeg (depends on installation)
- ✅/❌ API Keys (depends on configuration)

### **Debug Mode**
```bash
# Run with debug logging
streamlit run app.py --logger.level=debug

# Check logs
tail -f logs/app.log
```

### **Common Error Messages**
- **"Blender not found"** → Install Blender
- **"API key required"** → Enter API keys
- **"Permission denied"** → Fix file permissions
- **"Out of memory"** → Increase container memory

## 🎉 **Success Indicators**

### **When Everything Works**
- ✅ System status shows all green
- ✅ Video generation completes without errors
- ✅ 3D scenes are rendered (if Blender installed)
- ✅ Videos are playable and educational
- ✅ No error messages in console

### **When Using Fallbacks**
- ⚠️ System status shows some red/yellow
- ⚠️ Fallback videos are generated instead of 3D
- ⚠️ Still functional but with limited features
- ⚠️ Can be improved by installing missing components

## 🚀 **Next Steps After Setup**

1. **Test with real topics** - Try different subjects and levels
2. **Customize templates** - Modify Blender templates for your needs
3. **Add your own 3D models** - Upload custom models for specific topics
4. **Optimize performance** - Tune settings for your hardware
5. **Deploy to production** - Use Docker or cloud deployment

## 💡 **Pro Tips**

### **For Development**
- Use `st.cache` for expensive operations
- Implement proper error handling
- Add progress bars for long operations
- Use async operations where possible

### **For Production**
- Set up monitoring and alerting
- Implement rate limiting
- Use CDN for video delivery
- Enable caching for better performance

---

**The platform is designed to work even with missing components - it gracefully falls back to alternative methods! 🎬✨**
