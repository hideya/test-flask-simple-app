let saveTimeout;
const saveStatus = document.getElementById('save-status');
const memoContent = document.getElementById('memo-content');

function updateSaveStatus(message, isError = false) {
    saveStatus.textContent = message;
    saveStatus.className = isError ? 'text-danger' : 'text-muted';
}

function saveMemo() {
    updateSaveStatus('Saving...');
    
    fetch('/api/save-memo', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            content: memoContent.value
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            updateSaveStatus('All changes saved');
        } else {
            updateSaveStatus('Error saving changes', true);
        }
    })
    .catch(() => {
        updateSaveStatus('Error saving changes', true);
    });
}

memoContent.addEventListener('input', () => {
    updateSaveStatus('Unsaved changes...');
    clearTimeout(saveTimeout);
    saveTimeout = setTimeout(saveMemo, 1000);
});

// Initial focus
memoContent.focus();
