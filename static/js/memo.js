let saveTimeout;
const saveStatus = document.getElementById('save-status');
const memoContent = document.getElementById('memo-content');
const previewContent = document.getElementById('preview-content');
const previewTab = document.getElementById('preview-tab');

function updateSaveStatus(message, isError = false) {
    saveStatus.textContent = message;
    saveStatus.className = isError ? 'text-danger' : 'text-muted';
}

function updatePreview() {
    if (previewContent) {
        previewContent.innerHTML = marked.parse(memoContent.value);
    }
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
    updatePreview();
    clearTimeout(saveTimeout);
    saveTimeout = setTimeout(saveMemo, 1000);
});

// Update preview when switching to preview tab
previewTab.addEventListener('shown.bs.tab', updatePreview);

// Initial preview update and focus
updatePreview();
memoContent.focus();
