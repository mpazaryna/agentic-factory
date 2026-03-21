// Drafts Action: Kairos Knote
//
// Captures the current draft as a knote in kairos/knotes/YYYY/MM/
//
// SETUP (one time):
// 1. In Drafts, create a new Action
// 2. Add a "Script" step and paste this code
// 3. Create a Bookmark named "kairos" pointing to your kairos/ folder
//    (Settings → Bookmarks → + → navigate to your kairos/ folder)
//
// USAGE:
// Type or dictate a thought, then run this action.
// The draft content becomes the knote body.

// Get the kairos bookmark
let fm = FileManager.createForLocalBookmark("kairos");

if (!fm) {
    alert("Bookmark 'kairos' not found. Create a bookmark pointing to your kairos/ folder in Drafts Settings → Bookmarks.");
    context.fail();
} else {
    // Build timestamp components
    let now = new Date();
    let year = now.getFullYear().toString();
    let month = String(now.getMonth() + 1).padStart(2, '0');
    let day = String(now.getDate()).padStart(2, '0');
    let hours = String(now.getHours()).padStart(2, '0');
    let minutes = String(now.getMinutes()).padStart(2, '0');
    let seconds = String(now.getSeconds()).padStart(2, '0');

    let dateStr = `${year}-${month}-${day}`;
    let timeStr = `${hours}:${minutes}`;
    let filename = `${year}-${month}-${day}-${hours}${minutes}${seconds}.md`;
    let dirPath = `/knotes/${year}/${month}`;
    let filePath = `${dirPath}/${filename}`;

    // Build knote content
    let content = `---
tags: [knote]
date: ${dateStr}
time: ${timeStr}
source: drafts
---

${draft.content}`;

    // Ensure directory exists
    fm.createDirectory(dirPath, true);

    // Write the knote
    if (fm.writeString(filePath, content)) {
        // Archive the draft after successful write
        draft.isArchived = true;
        draft.update();
        app.displaySuccessMessage(`Knote captured: ${filename}`);
    } else {
        alert("Failed to write knote. Check bookmark permissions.");
        context.fail();
    }
}
