"""
Simple deployment script for Bustan Al Reef website
Works without Git - just copies files to deployment folder
"""

import os
import shutil
from datetime import datetime

def deploy_website():
    """Deploy website to a deployment folder"""
    
    # Create deployment folder
    deploy_folder = r"C:\Users\97152\Desktop\bustan-alreef-deploy"
    
    if os.path.exists(deploy_folder):
        shutil.rmtree(deploy_folder)
    
    os.makedirs(deploy_folder)
    
    # Copy all website files
    source_folder = r"C:\Users\97152\Desktop\al reef"
    
    # Files to copy (HTML, CSS, JS, images)
    files_to_copy = []
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith(('.html', '.css', '.js', '.png', '.jpg', '.jpeg', '.gif', '.ico')):
                src_path = os.path.join(root, file)
                rel_path = os.path.relpath(src_path, source_folder)
                dst_path = os.path.join(deploy_folder, rel_path)
                
                # Create destination directory if needed
                os.makedirs(os.path.dirname(dst_path), exist_ok=True)
                shutil.copy2(src_path, dst_path)
                files_to_copy.append(rel_path)
    
    # Create deployment info
    with open(os.path.join(deploy_folder, 'deployment-info.txt'), 'w') as f:
        f.write(f"Bustan Al Reef Website Deployment\n")
        f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Files copied: {len(files_to_copy)}\n")
        f.write("\nFiles included:\n")
        for file in sorted(files_to_copy):
            f.write(f"- {file}\n")
    
    print(f"✅ Website deployed successfully!")
    print(f"📁 Deployment folder: {deploy_folder}")
    print(f"📄 Total files: {len(files_to_copy)}")
    print(f"\n🚀 Ready for deployment to any web server!")
    
    # Optional: Open deployment folder
    os.startfile(deploy_folder)

if __name__ == "__main__":
    deploy_website()
