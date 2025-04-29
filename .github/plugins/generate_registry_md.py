import json
from pathlib import Path

def generate_markdown(registry_path):
    with open(registry_path) as f:
        data = json.load(f)
    
    md_content = """# Project Registry

| Group | Teachers | Students | Version | Tags | Last Updated |
|---------|--------|----------|---------|------|--------------|
"""
    for studygroup in data["studygroups"]:
        teachers = ", ".join(f"@{a}" for a in studygroup["teachers"])
        students = ", ".join(f"@{a}" for a in studygroup["students"])
        tags = ", ".join(f"`{t}`" for t in studygroup["tags"])
        md_content += f"| {studygroup['name']} | {teachers} | {students} | {students['version']} | {tags} | {students['last_updated'][:10]} |\n"

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
    registry_path = Path("studygroups.json")
    md_path = Path("STUDYGROUPS.md")
    
    md_content = generate_markdown(registry_path)
    md_path.write_text(md_content)
    print(f"Generated {md_path}")