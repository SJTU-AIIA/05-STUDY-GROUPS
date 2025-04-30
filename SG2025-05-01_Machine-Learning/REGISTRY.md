# Project Registry

| Project | Authors | Version | Tags | Last Updated | Links |
|---------|---------|---------|------|--------------|-------|
| sunqisheng | @DysonFabienSun | 0.0.0 |  | 2025-05-01 | [Folder](/home/runner/work/05-STUDY-GROUPS/05-STUDY-GROUPS/SG2025-05-01_Machine-Learning/studyspace/sunqisheng) \| [Image]() |

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
