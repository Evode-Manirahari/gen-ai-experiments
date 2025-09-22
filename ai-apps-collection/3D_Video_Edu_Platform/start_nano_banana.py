#!/usr/bin/env python3
"""
Script to start Nano Banana alongside the 3D Video Educational AI Platform
"""

import subprocess
import time
import os
import sys
import signal
import threading
from pathlib import Path

class NanoBananaManager:
    def __init__(self):
        self.nano_banana_process = None
        self.streamlit_process = None
        self.running = False
    
    def start_nano_banana(self):
        """Start Nano Banana development server"""
        try:
            nano_banana_path = Path(__file__).parent.parent / "nano-banana-image-workflow-nextjs"
            
            if not nano_banana_path.exists():
                print("❌ Nano Banana directory not found!")
                print(f"Expected path: {nano_banana_path}")
                return False
            
            print("🚀 Starting Nano Banana...")
            
            # Change to Nano Banana directory
            os.chdir(nano_banana_path)
            
            # Start Nano Banana
            self.nano_banana_process = subprocess.Popen(
                ["npm", "run", "dev"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            # Wait a moment for it to start
            time.sleep(3)
            
            if self.nano_banana_process.poll() is None:
                print("✅ Nano Banana started successfully!")
                print("🌐 Nano Banana running at: http://localhost:3000")
                return True
            else:
                print("❌ Failed to start Nano Banana")
                return False
                
        except Exception as e:
            print(f"❌ Error starting Nano Banana: {e}")
            return False
    
    def start_streamlit(self):
        """Start Streamlit app"""
        try:
            print("🚀 Starting 3D Video Educational AI Platform...")
            
            # Start Streamlit
            self.streamlit_process = subprocess.Popen(
                ["streamlit", "run", "enhanced_app.py", "--server.port=8501"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            # Wait a moment for it to start
            time.sleep(3)
            
            if self.streamlit_process.poll() is None:
                print("✅ Streamlit started successfully!")
                print("🌐 3D Video Edu Platform running at: http://localhost:8501")
                return True
            else:
                print("❌ Failed to start Streamlit")
                return False
                
        except Exception as e:
            print(f"❌ Error starting Streamlit: {e}")
            return False
    
    def stop_processes(self):
        """Stop all running processes"""
        print("\n🛑 Stopping processes...")
        
        if self.nano_banana_process:
            self.nano_banana_process.terminate()
            print("✅ Nano Banana stopped")
        
        if self.streamlit_process:
            self.streamlit_process.terminate()
            print("✅ Streamlit stopped")
        
        self.running = False
    
    def monitor_processes(self):
        """Monitor running processes"""
        while self.running:
            try:
                # Check Nano Banana
                if self.nano_banana_process and self.nano_banana_process.poll() is not None:
                    print("⚠️ Nano Banana stopped unexpectedly")
                    self.running = False
                    break
                
                # Check Streamlit
                if self.streamlit_process and self.streamlit_process.poll() is not None:
                    print("⚠️ Streamlit stopped unexpectedly")
                    self.running = False
                    break
                
                time.sleep(1)
                
            except KeyboardInterrupt:
                break
    
    def run(self):
        """Run both applications"""
        print("🎬 3D Video Educational AI Platform + Nano Banana")
        print("=" * 50)
        
        # Check if required tools are installed
        try:
            subprocess.run(["npm", "--version"], check=True, capture_output=True)
            subprocess.run(["streamlit", "--version"], check=True, capture_output=True)
        except subprocess.CalledProcessError:
            print("❌ Required tools not found!")
            print("Please install Node.js and Streamlit")
            return
        
        # Start Nano Banana
        if not self.start_nano_banana():
            print("❌ Cannot start without Nano Banana")
            return
        
        # Start Streamlit
        if not self.start_streamlit():
            print("❌ Cannot start without Streamlit")
            self.stop_processes()
            return
        
        self.running = True
        
        print("\n🎉 Both applications are running!")
        print("=" * 50)
        print("🌐 3D Video Edu Platform: http://localhost:8501")
        print("🎨 Nano Banana Workflow: http://localhost:3000")
        print("=" * 50)
        print("Press Ctrl+C to stop both applications")
        
        # Set up signal handler
        def signal_handler(sig, frame):
            self.stop_processes()
            sys.exit(0)
        
        signal.signal(signal.SIGINT, signal_handler)
        
        # Monitor processes
        try:
            self.monitor_processes()
        except KeyboardInterrupt:
            self.stop_processes()

def main():
    manager = NanoBananaManager()
    manager.run()

if __name__ == "__main__":
    main()
