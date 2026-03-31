async function loadIncidents() {
    const response = await fetch('/api/incidents');
    const incidents = await response.json();
    const tbody = document.getElementById('incidents-body');
    tbody.innerHTML = '';
    incidents.forEach(incident => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${incident.id}</td>
            <td>${incident.title}</td>
            <td>${incident.description}</td>
            <td class="severity-${incident.severity}">${incident.severity}</td>
            <td class="status-${incident.status}">${incident.status}</td>
            <td>${incident.site_name}</td>
            <td>${incident.created_at}</td>
        `;
        tbody.appendChild(tr);
    });
}

document.addEventListener("DOMContentLoaded", () => {
    loadIncidents();
});

async function createIncident() {
    const title = document.getElementById('title').value;
    const description = document.getElementById('description').value;
    const severity = document.getElementById('severity').value;
    const status = document.getElementById('status').value;
    const siteId = document.getElementById('site_id').value;

    const response = await fetch('/api/incidents', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            title: title,
            description: description,
            severity: severity,
            status: status,
            site_id: siteId
        })
    });
    const result = await response.json();
    
    if (response.ok) {
        // Clear form and reload incidents
        document.getElementById('incident-form').reset();
        loadIncidents();
    } else {
        console.error('Error creating incident:', result);
    }
}


async function updateStatus(id, newStatus) {
const response = await fetch(`/api/incidents/${id}/status`, {
    method: 'PUT',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({status: newStatus})
});
const result = await response.json();
}

