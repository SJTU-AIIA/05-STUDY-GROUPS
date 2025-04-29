# All Studygroups

| Group | Teachers | Students | Tags | Created | Last Updated |
|---------|--------|----------|------|---------|--------------|
| testgroup6 | @DysonFabienSun |  |  | 2025-04-30 | 2025-04-30 |
| testgroup8 | @DysonFabienSun |  |  | 2025-04-30 | 2025-04-30 |
| testgroup5 | @DysonFabienSun |  |  | 2025-04-30 | 2025-04-30 |
| testgroup7 | @DysonFabienSun |  |  | 2025-04-30 | 2025-04-30 |
| testgroup9 | @DysonFabienSun |  |  | 2025-04-30 | 2025-04-30 |

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
