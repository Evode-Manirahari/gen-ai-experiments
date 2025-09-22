import streamlit as st
import asyncio
import json
import base64
from pathlib import Path
from typing import Dict, List, Optional
import tempfile
import os
from datetime import datetime
import subprocess
import shutil

# Import Nano Banana integration
from nano_banana_integration import integrate_with_main_app, NanoBananaVideoEduPlatform

# --- App Configuration ---
st.set_page_config(
    page_title="3D Video Educational AI Platform + Nano Banana",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

class EnhancedVideoEduPlatform:
    def __init__(self):
        self.setup_agents()
        self.setup_nano_banana()
    
    def setup_agents(self):
        """Initialize AI agents for different tasks"""
        
        # Content Analyzer Agent
        self.content_analyzer = {
            "name": "Content Analyzer",
            "instructions": """
            You are an expert educational content analyzer. Your job is to:
            1. Break down any educational topic into key visual concepts
            2. Identify what 3D objects, animations, and scenes would best demonstrate the concept
            3. Create a detailed storyboard with camera movements and object interactions
            4. Suggest appropriate 3D models and materials needed
            
            Always think in terms of 3D visualization and educational effectiveness.
            """,
            "tools": []
        }
        
        # 3D Scene Designer Agent
        self.scene_designer = {
            "name": "3D Scene Designer",
            "instructions": """
            You are a 3D scene design expert. Your job is to:
            1. Convert educational concepts into Blender Python API code
            2. Create 3D scenes with appropriate lighting, materials, and camera angles
            3. Design smooth animations that demonstrate the concept clearly
            4. Optimize scenes for educational video production
            
            Generate complete Blender Python scripts that can be executed directly.
            """,
            "tools": []
        }
        
        # Video Generator Agent
        self.video_generator = {
            "name": "Video Generator",
            "instructions": """
            You are a video production expert. Your job is to:
            1. Take 3D rendered frames and create compelling educational videos
            2. Add appropriate transitions, text overlays, and educational annotations
            3. Ensure videos are optimized for different platforms and devices
            4. Create engaging thumbnails and previews
            
            Focus on educational effectiveness and visual appeal.
            """,
            "tools": []
        }
    
    def setup_nano_banana(self):
        """Setup Nano Banana integration"""
        self.nano_banana_platform = NanoBananaVideoEduPlatform()
    
    async def analyze_topic(self, topic: str, subject: str, level: str) -> Dict:
        """Analyze educational topic and create visualization plan"""
        
        prompt = f"""
        Analyze this educational topic for 3D video creation:
        
        Topic: {topic}
        Subject: {subject}
        Level: {level}
        
        Provide a detailed analysis including:
        1. Key concepts to visualize
        2. 3D objects and scenes needed
        3. Animation sequences required
        4. Camera movements and angles
        5. Educational annotations and labels
        6. Estimated video duration
        
        Return as structured JSON.
        """
        
        # For now, return a mock analysis
        # In production, this would use OpenAI or another LLM
        analysis = {
            "topic": topic,
            "subject": subject,
            "level": level,
            "concepts": [
                {
                    "name": "Main Concept",
                    "description": f"Visual representation of {topic}",
                    "3d_objects": ["Sphere", "Cube", "Cylinder"],
                    "animations": ["Rotation", "Scale", "Movement"],
                    "camera_angles": ["Front", "Side", "Top"],
                    "annotations": ["Key terms", "Important relationships", "Process steps"]
                }
            ],
            "workflow_steps": [
                "Generate main concept visualization",
                "Add educational annotations",
                "Create animation frames",
                "Combine into educational sequence"
            ],
            "animation_frames": 3,
            "estimated_duration": 120
        }
        
        return analysis
    
    async def create_3d_scene(self, analysis: Dict) -> str:
        """Generate Blender Python script for 3D scene"""
        
        prompt = f"""
        Create a Blender Python script based on this analysis:
        
        {json.dumps(analysis, indent=2)}
        
        The script should:
        1. Set up the 3D scene with appropriate lighting
        2. Create all necessary 3D objects
        3. Add materials and textures
        4. Set up camera movements
        5. Create smooth animations
        6. Render frames for video production
        
        Return only the complete Python script that can be executed in Blender.
        """
        
        # For now, return a mock script
        script = f"""
import bpy
import bmesh
from mathutils import Vector
import math

# Clear existing mesh objects
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Set up scene
scene = bpy.context.scene
scene.frame_start = 1
scene.frame_end = 300

# Set up camera
bpy.ops.object.camera_add(location=(0, -10, 5))
camera = bpy.context.object
camera.rotation_euler = (math.radians(60), 0, 0)
scene.camera = camera

# Set up lighting
bpy.ops.object.light_add(type='SUN', location=(5, 5, 10))
sun = bpy.context.object
sun.data.energy = 3

# Create educational objects for: {analysis['topic']}
# This would be customized based on the analysis
bpy.ops.mesh.primitive_uv_sphere_add(location=(0, 0, 0), radius=2)
sphere = bpy.context.object
sphere.name = "Main_Concept"

# Add material
mat = bpy.data.materials.new(name="Concept_Material")
mat.use_nodes = True
mat.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.0, 0.5, 1.0, 1.0)
sphere.data.materials.append(mat)

# Set up rendering
scene.render.engine = 'CYCLES'
scene.render.resolution_x = 1920
scene.render.resolution_y = 1080
scene.render.fps = 30
scene.render.filepath = "/tmp/3d_edu_video/"

# Render animation
bpy.ops.render.render(animation=True)
"""
        
        return script
    
    async def generate_video(self, topic: str, script: str) -> str:
        """Generate final educational video"""
        
        # Check if Blender is available
        try:
            result = subprocess.run(['blender', '--version'], 
                                  capture_output=True, text=True, timeout=10)
            blender_available = result.returncode == 0
        except:
            blender_available = False
        
        if not blender_available:
            st.warning("⚠️ Blender not found. Using Nano Banana for visual generation...")
            return await self.nano_banana_platform.generate_educational_video(
                topic, "Physics", "High School"
            )
        
        # Execute Blender script and generate video
        video_path = await self.execute_blender_script(script, topic)
        return video_path
    
    async def execute_blender_script(self, script: str, topic: str) -> str:
        """Execute Blender script and generate video"""
        
        # Save script to temporary file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write(script)
            script_path = f.name
        
        try:
            # Execute Blender script
            output_dir = f"output/{topic.replace(' ', '_')}"
            os.makedirs(output_dir, exist_ok=True)
            
            cmd = [
                "blender",
                "--background",
                "--python", script_path,
                "--", output_dir
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                return f"{output_dir}/final_video.mp4"
            else:
                st.error(f"Blender execution failed: {result.stderr}")
                return None
                
        finally:
            os.unlink(script_path)

# Initialize platform
@st.cache_resource
def get_platform():
    return EnhancedVideoEduPlatform()

# --- UI Components ---
def render_sidebar():
    st.sidebar.title("🎬 3D Video Edu + Nano Banana")
    st.sidebar.markdown("Create immersive 3D educational videos with AI!")
    
    # API Keys
    openai_key = st.sidebar.text_input("OpenAI API Key:", type="password")
    google_key = st.sidebar.text_input("Google API Key:", type="password")
    
    # Topic Input
    st.sidebar.markdown("---")
    subject = st.sidebar.selectbox(
        "Subject:",
        ["Physics", "Chemistry", "Biology", "Mathematics", "History", "Geography", "Computer Science"]
    )
    
    level = st.sidebar.selectbox(
        "Level:",
        ["Elementary", "Middle School", "High School", "College", "Professional"]
    )
    
    topic = st.sidebar.text_area(
        "Educational Topic:",
        placeholder="e.g., Photosynthesis process, Water cycle, DNA replication..."
    )
    
    # Video Settings
    st.sidebar.markdown("---")
    duration = st.sidebar.slider("Video Duration (seconds):", 30, 300, 120)
    quality = st.sidebar.selectbox("Video Quality:", ["720p", "1080p", "4K"])
    language = st.sidebar.selectbox("Language:", ["English", "Spanish", "French", "German", "Hindi"])
    
    # Generation Method
    st.sidebar.markdown("---")
    generation_method = st.sidebar.radio(
        "Generation Method:",
        ["3D Blender (Full 3D)", "Nano Banana (Visual Workflow)", "Hybrid (Both)"]
    )
    
    return {
        "openai_key": openai_key,
        "google_key": google_key,
        "subject": subject,
        "level": level,
        "topic": topic,
        "duration": duration,
        "quality": quality,
        "language": language,
        "generation_method": generation_method
    }

def render_main_content(settings):
    st.title("🎬 3D Video Educational AI Platform + Nano Banana")
    st.markdown("Transform any topic into immersive 3D educational videos with AI!")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        if st.button("🚀 Generate Educational Video", type="primary", use_container_width=True):
            if not settings["topic"]:
                st.error("Please enter a topic to generate video.")
                return
            
            if not settings["openai_key"] or not settings["google_key"]:
                st.error("Please enter both API keys.")
                return
            
            # Generate video based on method
            with st.spinner("Creating your educational video..."):
                platform = get_platform()
                
                if settings["generation_method"] == "3D Blender (Full 3D)":
                    # Use 3D Blender method
                    st.info("🔍 Analyzing topic and creating 3D visualization plan...")
                    analysis = asyncio.run(platform.analyze_topic(
                        settings["topic"],
                        settings["subject"],
                        settings["level"]
                    ))
                    
                    with st.expander("📋 3D Visualization Plan", expanded=True):
                        st.json(analysis)
                    
                    st.info("🎨 Designing 3D scene and animations...")
                    script = asyncio.run(platform.create_3d_scene(analysis))
                    
                    with st.expander("🐍 Blender Script", expanded=False):
                        st.code(script, language="python")
                    
                    st.info("🎬 Rendering 3D video...")
                    video_path = asyncio.run(platform.generate_video(settings["topic"], script))
                
                elif settings["generation_method"] == "Nano Banana (Visual Workflow)":
                    # Use Nano Banana method
                    st.info("🎨 Using Nano Banana visual workflow...")
                    video_path = asyncio.run(platform.nano_banana_platform.generate_educational_video(
                        settings["topic"],
                        settings["subject"],
                        settings["level"]
                    ))
                
                else:  # Hybrid
                    # Use both methods
                    st.info("🔄 Using hybrid approach with both 3D and visual workflow...")
                    
                    # Try 3D first
                    try:
                        analysis = asyncio.run(platform.analyze_topic(
                            settings["topic"],
                            settings["subject"],
                            settings["level"]
                        ))
                        script = asyncio.run(platform.create_3d_scene(analysis))
                        video_path = asyncio.run(platform.generate_video(settings["topic"], script))
                    except:
                        # Fallback to Nano Banana
                        st.warning("3D generation failed, using Nano Banana...")
                        video_path = asyncio.run(platform.nano_banana_platform.generate_educational_video(
                            settings["topic"],
                            settings["subject"],
                            settings["level"]
                        ))
                
                if video_path:
                    st.success("✅ Educational video generated successfully!")
                    
                    # Display video
                    if video_path.endswith('.mp4'):
                        st.video(video_path)
                    else:
                        st.info(f"Video generated at: {video_path}")
                    
                    # Download button
                    if os.path.exists(video_path):
                        with open(video_path, "rb") as file:
                            st.download_button(
                                label="📥 Download Video",
                                data=file.read(),
                                file_name=f"{settings['topic'].replace(' ', '_')}_educational_video.mp4",
                                mime="video/mp4"
                            )
                else:
                    st.error("❌ Failed to generate video. Please try again.")
    
    with col2:
        st.markdown("### 🎯 Features")
        st.markdown("""
        - **🤖 AI-Powered Analysis**: Automatically breaks down topics into visual concepts
        - **🎨 3D Scene Generation**: Creates detailed 3D scenes with Blender
        - **🖼️ Visual Workflow**: Nano Banana integration for image generation
        - **🎬 Smart Video Production**: Generates smooth, educational animations
        - **🌍 Multi-Language**: Supports multiple languages
        - **⚡ Hybrid Approach**: Combines 3D and visual workflow methods
        """)
        
        st.markdown("### 📚 Example Topics")
        st.markdown("""
        - **Physics**: Gravity, Electromagnetic fields, Wave propagation
        - **Chemistry**: Molecular structures, Chemical reactions
        - **Biology**: Cell division, Ecosystem interactions
        - **Math**: Geometric proofs, Calculus concepts
        - **History**: Ancient civilizations, Historical events
        """)

def render_nano_banana_integration():
    """Render Nano Banana integration section"""
    
    st.markdown("---")
    st.subheader("🎨 Nano Banana Visual Workflow Integration")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        **Enhanced with Nano Banana Visual Workflow Builder!**
        
        - 🎨 **Visual Workflow Design**: Drag-and-drop interface for creating educational content
        - 🖼️ **AI Image Generation**: Generate educational illustrations with Google Gemini
        - ✏️ **Image Editing**: Add annotations, labels, and educational elements
        - 🎬 **Animation Frames**: Create step-by-step visual sequences
        - 🔄 **Workflow Automation**: Execute complex visual workflows automatically
        """)
        
        if st.button("🚀 Launch Nano Banana Workflow", type="secondary"):
            st.info("🔄 Opening Nano Banana workflow builder...")
            
            # Launch Nano Banana in new tab
            nano_banana_url = st.session_state.get('nano_banana_url', 'http://localhost:3000')
            st.markdown(f"""
            <script>
                window.open('{nano_banana_url}', '_blank');
            </script>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 🎯 Workflow Features")
        st.markdown("""
        - **Physics**: Molecular structures, force diagrams
        - **Chemistry**: Reaction mechanisms, molecular models
        - **Biology**: Cell processes, anatomical diagrams
        - **Math**: Geometric proofs, function visualizations
        - **History**: Timeline visualizations, historical scenes
        """)
        
        # Nano Banana status
        nano_banana_running = st.checkbox("Nano Banana Running", value=False)
        if nano_banana_running:
            st.success("✅ Nano Banana is running")
        else:
            st.warning("⚠️ Start Nano Banana first")

def render_advanced_features():
    st.markdown("---")
    st.subheader("🔧 Advanced Features")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🎨 Customization")
        st.markdown("""
        - Custom 3D models
        - Brand colors and themes
        - Interactive elements
        - Voice narration
        """)
    
    with col2:
        st.markdown("### 📊 Analytics")
        st.markdown("""
        - Learning effectiveness metrics
        - Engagement tracking
        - Performance analytics
        - A/B testing
        """)
    
    with col3:
        st.markdown("### 🌐 Integration")
        st.markdown("""
        - LMS integration
        - API access
        - Bulk generation
        - White-label solutions
        """)

# --- Main App ---
def main():
    settings = render_sidebar()
    render_main_content(settings)
    render_nano_banana_integration()
    render_advanced_features()

if __name__ == "__main__":
    main()
