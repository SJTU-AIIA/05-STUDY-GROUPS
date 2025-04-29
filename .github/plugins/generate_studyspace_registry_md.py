import json
from pathlib import Path
import os
from baselib import ROOT_DIR

def generate_projects_markdown(registry_path):
    with open(registry_path) as f:
        data = json.load(f)
    
    md_content = """# Project Registry

| Project | Authors | Version | Tags | Last Updated | Links |
|---------|---------|---------|------|--------------|-------|
"""
    for project in data["projects"]:
        authors = ", ".join(f"@{a}" for a in project["authors"])
        tags = ", ".join(f"`{t}`" for t in project["tags"])
        md_content += f"| {project['name']} | {authors} | {project['version']} | {tags} | {project['last_updated'][:10]} | [Folder]({project['path']}) \| [Image]({project['image']}) |\n"

    # Add search functionality
    md_content += """
<script>
document.addEventListener('DOMContentLoaded', function() {
    const table = document.querySelector('table');
    const input = document.createElement('input');
    input.type = 'text';
    input.placeholder = 'Search projects...';
    input.style.marginBottom = '10px';
    input.style.width = '100%';
    input.style.padding = '8px';
    table.parentNode.insertBefore(input, table);

    input.addEventListener('keyup', function() {
        const filter = input.value.toLowerCase();
        const rows = table.querySelectorAll('tbody tr');
        
        rows.forEach(row => {
            const text = row.textContent.toLowerCase();
            row.style.display = text.includes(filter) ? '' : 'none';
        });
    });
});
</script>
"""
    return md_content

if __name__ == "__main__":
    for studygroup in [folder for folder in os.listdir(ROOT_DIR) if os.path.isdir(os.path.join(ROOT_DIR, folder)) and not folder.startswith(".")]:
        registry_path = Path(f"{studygroup}/_registry.json")
        md_path = Path(f"{studygroup}/REGISTRY.md")
        
        md_content = generate_projects_markdown(registry_path)
        md_path.write_text(md_content)
        print(f"Generated {md_path}")